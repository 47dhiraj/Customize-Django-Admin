from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField



# Create your models here.

CATEGORY = (('Techno' , 'Techno') , ('Sports' , 'Sports') , ('Movie' , 'Movie') , ('Life' , 'Life'))

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    categories = models.CharField(choices= CATEGORY, max_length=10, default='Techno')
    description = RichTextField(blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='images')
    

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):                                    
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


    @property                                                           # yesari @property decorator rakhyo vani yo image_preview vanni method lai callable garako
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="110" height="60" />'.format(self.image.url))
        return ""


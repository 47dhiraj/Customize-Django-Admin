from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    # fields = ['author', 'title', 'slug', 'image', 'description', 'published']             # Admin panel particular blog page ma, specific field matra dekhios vanna ko lagi yesari fields attribute ma lekhna sakincha .. for eg: created_at  field dekhauna mildaina so tei vayera nalekheko
    
    list_display = ['image_preview', 'title', 'author', 'short_description', 'published', 'created_at', 'view_detail_button']                       
    prepopulated_fields = {'slug': ('title',)}                                              
    date_hierarchy = 'created_at'
    list_display_links = ['title']                                                          
    list_filter = ['published', 'created_at', 'categories', ['description', admin.EmptyFieldListFilter]]  
    # radio_fields = {'categories': admin.HORIZONTAL}                                         # by default ma choices haru select option jasari aauchan but yedi radio button jasari display garna cha vani yesari garna sakincha
    search_fields = ['categories']                                                          
    exclude = []                                                                            
    #save_on_top = True                                                                     # yedi save and delete button lai top tira lyauna cha vani yo garne,, yedi blog detail page tala samma dherai cha vani yesle edit garera save garna sajilo parcha i.e scroll down gari rakhnu parena
    readonly_fields = ('image_preview', )                                                  
    list_per_page = 4                                                                       
    actions = ['make_published', 'make_unpublished']
    ordering = ['-created_at']                                                             


    def short_description(self, obj):                                                       
        return obj.description[:20] + ' ...'


    def view_detail_button(self, obj):
        return format_html(f'<button style="background-color: #47d147; border-color: black; border-radius: 7px; padding: 4px 4px 4px 4px;"><a href="/admin/admin_app/blog/{obj.id}/change/" style="color: white;"> View Detail </a></button>')


    def make_published(self, request, queryset):
        queryset.update(published=True)
    make_published.short_description = 'Make this blog Published'
    

    def make_unpublished(self, request, queryset):
        queryset.update(published=False)
    make_unpublished.short_description = 'Make this blog Unpublished'


    def image_preview(self, obj):
        return obj.image_preview
    image_preview.short_description = 'Current Image Preview'
    image_preview.allow_tags = True


admin.site.register(Blog, BlogAdmin)




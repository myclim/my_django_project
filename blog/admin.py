from django.contrib import admin
from blog.models import BlogModel


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('blog_title',)}
    list_display = ['pk', 'blog_title']
    search_fields = ['blog_title', 'description']
    fields = [
        'blog_title',
        'slug',
        'description',
        ('create_at', 'update_at'),
        'watched',
        'image'
    ]
    readonly_fields = ('watched', 'create_at', 'update_at')




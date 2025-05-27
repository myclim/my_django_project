from django.db import models
from django.utils.text import slugify



class BlogModel(models.Model):
    blog_title = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL', blank=True)
    description = models.TextField(verbose_name='Описание')

    image = models.ImageField(upload_to='blog_image', blank=True, null=True, verbose_name='Изображение')
    watched = models.IntegerField(default=0, verbose_name='Просмотры')

    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'blog'
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        ordering = ['-create_at']
    
    def __str__(self):
        return self.blog_title




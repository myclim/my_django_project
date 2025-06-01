from django.db import models
from django.contrib.auth.models import AbstractUser



class UserModel(AbstractUser):
    image = models.ImageField(upload_to='user_image', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=10, blank=True, null=True, unique=True, verbose_name='Телефон')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.username

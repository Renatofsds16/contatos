#type:ignore

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorys'
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name}'


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=2024, blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, 
        blank=True, null=True
    )
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, 
        null=True
    )
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#type:ignore

from django.contrib import admin
from .models import Contact, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'show')
    list_display_links = ('first_name', 'last_name', 'phone',)
    list_editable = ('show',)
    ordering = ('-id',)
    search_fields = ('id', 'first_name', 'last_name',)
    list_per_page = 10
    list_max_show_all = 100

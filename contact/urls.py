from django.urls import path
from . import views

app_name = 'contact'


urlpatterns = [

    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    path('contact/<int:contact_id>/', views.contact, name='contact'),

    path('contact/<int:contact_id>/update/', views.user_update, name='update'),

    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update', views.update, name='update'),
    path('user/create/', views.register, name='register'),

    path('user/loguin/', views.loguin_views, name='loguin_views'),
    path('user/logout/', views.logout, name='logout'),
    path('user/update/', views.user_update, name='user_update'),

]

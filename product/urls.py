from django.conf.urls import url
from django.contrib import admin
from .views import get_list,create_new,update,delete
from django.urls import path


urlpatterns = [
    path('',get_list,name='get_list'),
    path('create',create_new,name='create'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>',delete,name='delete')

]
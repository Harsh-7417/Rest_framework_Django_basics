from django.conf.urls import url
from django.contrib import admin
#from .views import get_list,create_new,update,delete
from django.urls import path
from .view import productApiview,productlistApiview


urlpatterns = [
    path('<int:pk>/', productApiview.as_view(), name='apiview'),
    path('', productlistApiview.as_view(), name='apilistview')


]
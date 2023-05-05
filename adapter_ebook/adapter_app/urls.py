from django.urls import path
from . import views

urlpatterns = [
    path('adapter-ebook/', views.adapter_ebook, name='adapter_ebook'),
]

from . import views
from django.urls import path

urlpatterns = [


    path('',views.demo,name='demo'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('add/',views.addition,name='addition')
    path('abou/',views.about,name='aboutus'),


    path('contact/',views.contact,name='contact'),
    path('news/',views.news,name='blog'),
    path('element/',views.elements,name='blogdetails'),
    path('destiny/',views.destination,name='destinations'),



]
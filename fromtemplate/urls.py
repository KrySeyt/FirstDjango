from django.http import HttpResponseRedirect
from django.urls import path

from . import views


urlpatterns = [
    path('', lambda request: HttpResponseRedirect('main/'), name='blank'),
    path('main/', views.show_main_page, name='main-page'),
    path('contacts/', views.show_contacts, name='contacts'),
    path('about-us/', views.show_about_us, name='about-us'),
    path('index/', views.show_index, name='index'),
]

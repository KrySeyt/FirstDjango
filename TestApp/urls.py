from django.urls import path

from . import views


urlpatterns = [
    path('', views.show_main_page, name='main-page'),
    path('request/', views.request_response, name='request'),
]

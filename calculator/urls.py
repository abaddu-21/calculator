from django.conf.urls import url
from django.contrib import admin
from calculator import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view()),
]
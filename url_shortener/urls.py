from django.urls import path

from . import views


urlpatterns = [
    path('', views.URLShortener.as_view(), name='index'),
]
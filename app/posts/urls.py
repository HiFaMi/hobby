from django.contrib import admin
from django.urls import path, include

from .views import test_view, post_create

app_name = 'post'

urlpatterns = [
    path('test/', test_view),
    path('create/', post_create, name='post-create')
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', submit_comment, name='submit_comment'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('article/<Blog_pk>', blog_detail, name='blog_detail'),
    path('article_list/<blog_with_type>', blog_with_type,name='blog_with_type'),
    path('article_date/<int:year>/<int:month>', blog_with_date,name='blog_with_date'),
]

from urllib.parse import urlparse
from django.urls import path
from .views import BlogDetail, BlogList, create_account, create_blog, search_blog,add_comment

app_name = 'blog'
urlpatterns = [
    path('',BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail'),
    path('create/', create_blog, name='create'),
    path('search/', search_blog, name='search'),
    path('signup/', create_account, name='signup'),
    path('comment/<int:pk>/',add_comment, name='add_comment')
]

from django.urls import path
from blog.views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:blog_pk>/', BlogDetailView.as_view(), name='blog_detail')
]

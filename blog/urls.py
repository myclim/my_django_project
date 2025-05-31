from django.urls import path
from blog.views import BlogListView, BlogDetailView, CreateBlogView, UserBlogListView, UserUpdateBlogView, UserBlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:blog_pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create_blog/', CreateBlogView.as_view(), name='create_blog'),
    path('user_list/', UserBlogListView.as_view(), name='user_list'),
    path('update/<int:pk>/', UserUpdateBlogView.as_view(), name='update_blog'),
    path('delete/<int:delete_pk>/', UserBlogDeleteView.as_view(), name='delete_blog'),
]

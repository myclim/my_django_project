from django.shortcuts import render
from django.views.generic import ListView
from blog.models import BlogModel


class BlogListView(ListView):
    model = BlogModel
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Blog - page'
        return context
    
from django.views.generic import DetailView, ListView
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
    


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog/blog_single.html'
    context_object_name = 'blog_detail'
    pk_url_kwarg = 'blog_pk'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.watched += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Blog - single'
        return context
    
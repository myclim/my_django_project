from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import BlogModel
from blog.forms import CreateBlogForm, UserUpdateBlogForm


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
        if obj.author != self.request.user:
            obj.watched += 1
            obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Blog - single'
        return context
    

class CreateBlogView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create_blog.html'
    form_class = CreateBlogForm
    model = BlogModel
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create - page'
        return context


class UserBlogListView(LoginRequiredMixin, ListView):
    model = BlogModel
    template_name = 'blog/user_list.html'
    context_object_name = 'user_blogs'
    paginate_by = 4

    def get_queryset(self):
        return BlogModel.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create - page'
        return context


class UserUpdateBlogView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/user_single_blog.html'
    model = BlogModel
    form_class = UserUpdateBlogForm
    context_object_name = 'blog_detail'
    success_url = reverse_lazy("blog:user_list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied("Вы не можете редактировать эту статью")
        return obj
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Update - page'
        return context
    

class UserBlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogModel
    success_url = reverse_lazy('blog:user_list')
    pk_url_kwarg = 'delete_pk'
    template_name = 'blog/blogmodel_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author == self.request.user:
            return obj
        else:
            raise PermissionDenied("Вы можете удалять только свои статьи")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Delete - page'
        return context
from django.contrib import auth, messages
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from users.models import UserModel



class LoginUserView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main:index')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'{self.request.user.username} - Вы вошли в аккаунт')
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Login - page'
        return context
    

class RegisterUserView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        user = form.instance
        auth.login(self.request, user)
        messages.success(self.request, f'{user.username} - Регистрация прошла успешно')
        return response

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Register - page' 
        return context
    

class ProfileUserView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Profile - page'
        context['user'] = UserModel.objects.get(username=self.request.user)
        return context



class UpdateUserView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('user:profile')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Профиль обновлен')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Произошла ошибка')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Update - page'
        return context



def logout(request):
    auth.logout(request)
    return redirect('main:index')
    
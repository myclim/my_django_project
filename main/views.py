from django.views.generic import TemplateView

from users.models import UserModel



class MainView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Music blog'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'About page'
        context['user'] = UserModel.objects.get(username='admin')
        return context
    
from django.urls import path
from main.views import MainView, AboutView

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
]

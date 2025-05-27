from django.urls import path
from main.views import MainView, AbountView

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('about/', AbountView.as_view(), name='about'),
]
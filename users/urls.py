from django.urls import path
from users.views import LoginUserView, logout, RegisterUserView

app_name = 'user'

urlpatterns = [
    path('', LoginUserView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register')
]

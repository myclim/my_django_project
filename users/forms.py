from django import forms
from users.models import UserModel
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



class UserLoginForm(AuthenticationForm):
    pass


class UserRegisterForm(UserCreationForm):
    phone = forms.CharField()

    class Meta:
        model = UserModel
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password1',
            'password2',
        )
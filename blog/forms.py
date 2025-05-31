from django import forms
from blog.models import BlogModel


class CreateBlogForm(forms.ModelForm):
    blog_title = forms.CharField()
    description = forms.TextInput()
    class Meta:
        model = BlogModel
        fields = (
            'blog_title',
            'description',
            'image',
        )


class UserUpdateBlogForm(forms.ModelForm):
    blog_title = forms.CharField()
    description = forms.TextInput()

    class Meta:
        model = BlogModel
        fields = (
            'blog_title',
            'description',
            'image',
        )
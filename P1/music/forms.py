from django.contrib.auth.models import  User
from django import forms

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        password = forms.CharField(widget=forms.PasswordInput)
        fields = ['username', 'email', 'password']

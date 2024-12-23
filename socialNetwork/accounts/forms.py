from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='E-mail',
        max_length=50,
        widget=forms.EmailInput(attrs={"placeholder": 'Email'}),
        required=True
    )

    username = forms.CharField(
        label='username',
        max_length=25,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
        help_text='Be sure you have a unique username'

    )
    password1 = forms.CharField(
        label='Password',
        min_length=8,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),

    )


    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


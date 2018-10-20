from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(attrs={
                                                                  'class': 'form-control',
                                                                  'placeholder': 'John',
                                                              }), required=True)
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs={
                                                                  'class': 'form-control',
                                                                  'placeholder': 'Doe',
                                                              }), required=True)
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={
                                                                  'class': 'form-control',
                                                                  'placeholder': 'yourname@example.com',
                                                              }), required=True)
    pass1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
                                                                  'class': 'form-control',
                                                              }), required=True)
    pass2 = forms.CharField(label=' Retype Password', widget=forms.PasswordInput(attrs={
                                                                  'class': 'form-control',
                                                              }), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email',
                  'password1', 'password2', )


class LoginForm(forms.Form):

    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={
                                                                  'class': 'form-control',
                                                                  'placeholder': 'yourname@example.com',
                                                              }), required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
                                                                  'class': 'form-control',
                                                                  'placeholder': 'Password',
                                                              }), required=True)


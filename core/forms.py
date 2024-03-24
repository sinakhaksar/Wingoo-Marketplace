from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl max-auto'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl max-auto'
    }))



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields= ('username','email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl max-auto'
    }))


    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'w-full py-4 px-6 rounded-xl max-auto'
    }))


    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl max-auto'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'ReEnter Password',
        'class': 'w-full py-4 px-6 rounded-xl max-auto'
    }))

# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({
#             'placeholder': 'Your Username',
#             'class': 'w-full py-4 px-6 rounded-xl max-auto'
#         })
#         self.fields['email'].widget.attrs.update({
#             'placeholder': 'Your Email',
#             'class': 'w-full py-4 px-6 rounded-xl max-auto'
#         })
#         self.fields['password1'].widget.attrs.update({
#             'placeholder': 'Your Password',
#             'class': 'w-full py-4 px-6 rounded-xl max-auto'
#         })
#         self.fields['password2'].widget.attrs.update({
#             'placeholder': 'Re-enter Password',
#             'class': 'w-full py-4 px-6 rounded-xl max-auto'
#         })

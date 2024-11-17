from cProfile import label

from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Имя:', widget=forms.TextInput(attrs={
        'class': 'form_block__input'
    }))
    password = forms.CharField(label='Пароль:',widget=forms.PasswordInput(attrs={
        'class': 'form_block__input'
    }))


class UserResetPasswordForm(PasswordResetForm):
    email = forms.CharField(label='Адрес эл. почты',widget=forms.TextInput(attrs={
        'class': 'form_block__input'
    }))


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Новый пароль',widget=forms.PasswordInput(attrs={
        'class': 'form_block__input'
    }))
    new_password2 = forms.CharField(label='Подтвердите новый пароль',widget=forms.PasswordInput(attrs={
        'class': 'form_block__input'
    }))


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль',widget=forms.PasswordInput(attrs={
        'class': 'form_block__input'
    }))
    new_password1 = forms.CharField(label='Новый пароль',widget=forms.PasswordInput(attrs={
        'class': 'form_block__input'
    }))
    new_password2 = forms.CharField(label='Подтвердите новый пароль',widget=forms.PasswordInput(attrs={
        'class': 'form_block__input'
    }))

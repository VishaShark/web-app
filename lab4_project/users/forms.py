from django import forms
from .models import Client

class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтвердите пароль',
            'class': 'form-input'
        }),
        label='Подтвердите пароль'
    )

    class Meta:
        model = Client
        fields = ['name', 'email', 'password', 'about']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'class': 'form-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ваш email',
                'class': 'form-input'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Пароль',
                'class': 'form-input'
            }),
            'about': forms.Textarea(attrs={
                'placeholder': 'О себе',
                'class': 'form-textarea',
                'rows': 3
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают.')
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Ваш email',
            'class': 'form-input'
        }),
        label='Email'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-input'
        }),
        label='Пароль'
    )
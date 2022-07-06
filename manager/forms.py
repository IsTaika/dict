from django.contrib.auth.models import User
from django import forms


class UserRegistrForm(forms.ModelForm):
    password = forms.CharField(label='Passwords', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat passwords', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['passwords'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


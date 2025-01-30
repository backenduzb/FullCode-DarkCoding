from django import forms
from .models import Post,Content
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username']
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError("Parollar mos kelmadi!")
        return password_confirm

class ContentForm(forms.ModelForm):
    class Meta:
        model=Content
        fields=['nomi','nimaga','tili','turlari','izoh','kod']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['image', 'date', 'text']

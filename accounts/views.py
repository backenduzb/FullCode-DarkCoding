from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import SignUpForm
from django.shortcuts import redirect


class SignUpView(CreateView):
    form_class=SignUpForm
    template_name='register/signup.html'
    success_url=reverse_lazy('home')  
    def form_valid(self, form):
        user=form.save()
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return redirect(self.success_url)

class Loginview(LoginView):
    template_name="register/login.html"
    success_url=reverse_lazy('home') 

    def get_success_url(self):
        return self.success_url
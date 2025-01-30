from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,DetailView
from .models import Post,Content
from .forms import PostForm,ContentForm
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name="index.html"

class AddPost(CreateView):
    template_name="addpost.html"
    context_object_name="post"
    form_class=PostForm
    success_url=reverse_lazy('blogla')
    
    def form_valid(self,form):
        return super().form_valid(form)


class AddContent(CreateView):
    template_name="content.html"
    context_object_name="content"
    form_class=ContentForm
    success_url=reverse_lazy('home')


class Posts(ListView):
    model=Post  
    template_name="list.html"
    context_object_name="post"

class PythonContent(ListView):
    model=Content
    context_object_name="content"
    template_name="codes/list.html"

    def get_queryset(self):
        return Content.objects.filter(tili="Python")

class JSContent(ListView):
    model=Content
    context_object_name="content"
    template_name="codes/list.html"

    def get_queryset(self):
        return Content.objects.filter(tili="Java Script")

class GolangContent(ListView):
    model=Content
    context_object_name="content"
    template_name="codes/list.html"

    def get_queryset(self):
        return Content.objects.filter(tili="Golang")

class BatContent(ListView):
    model=Content
    context_object_name="content"
    template_name="codes/list.html"

    def get_queryset(self):
        return Content.objects.filter(tili="Bat")



class PostDetailView(DetailView):
    model=Content
    template_name='codes/detail.html'  
    context_object_name='post' 

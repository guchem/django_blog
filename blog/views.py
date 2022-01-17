from django.shortcuts import render, redirect
from .models import Blog, Comment
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

class BlogList(ListView):
    model = Blog
    template_name = 'base.html'

class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/details.html'

@login_required
def create_blog(request):
    if request.method=='POST':
        title = request.POST['title']
        content = request.POST['content']
        Blog.objects.create(author=request.user, title=title, content=content)
        return redirect('blog:list')
    return render(request, 'blog/create.html')


def search_blog(request):
    if request.method=='POST':
        phrase = request.POST['search_phrase']
        blogs = Blog.objects.filter(title__contains=phrase)
        return render(request, 'base.html',{'blog_list':blogs})


def create_account(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        live_user = authenticate(username=username,password=password)
        login(request, live_user)
        return redirect('blog:list')

    return render(request, 'accounts/signup.html')

@login_required
def add_comment(request, pk):
    if request.method=='POST':
        blog = Blog.objects.get(pk=pk)
        content = request.POST['comment']
        Comment.objects.create(blog=blog, author=request.user, content=content)
        return redirect('blog:detail', pk=pk)
    return redirect('blog:detail', pk=pk)
    
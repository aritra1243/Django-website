from django.shortcuts import render
from .models import Post

# Create your views here.
def homepage(request) :
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts'  :posts})

def dashboard(request) :
    return render(request, 'dashboard.html')


def about(request) :
    return render(request, 'about.html')


def contact(request) :
    return render(request, 'contact.html')




from django.shortcuts import render
from .models import Post
# Create your views here.
from django.core.mail import send_mail
def home(request):
    post=Post.objects.all()
    return render(request,'blog/home.html',{'posts':post})
def about(request):
    return render(request,'blog/about.html')


def contact(request):
    return render(request,'blog/contact.html')

def post(request,id):
    post_id=Post.objects.get(id=id)
    return render(request,'blog/post.html',{'post':post_id})


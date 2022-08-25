from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts= [
    {
        'author':'Babak zare',
        'title':'First post of my blog!',
        'content':'this is the first post of my blog! I am so happy :)',
        'date_posted':'8/20/2022'
    },
    {
        'author':'Saeed Lashkari',
        'title':'What a Walking dead!',
        'content':'The walking dead show is amazing. I LOVE IT!',
        'date_posted':'8/21/2022'
    }
]
def home(request):
    context = {
        'posts': Post.objects.all() ,
        'title':'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
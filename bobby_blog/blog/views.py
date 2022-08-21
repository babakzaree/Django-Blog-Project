from django.shortcuts import render
from django.http import HttpResponse

posts= [
    {
        'user':'Babak zare',
        'title':'First post of my blog!',
        'content':'this is the first post of my blog! I am so happy :)',
        'date_posted':'8/20/2022'
    },
    {
        'user':'Saeed Lashkari',
        'title':'What a Walking dead!',
        'content':'The walking dead show is amazing. I LOVE IT!',
        'date_posted':'8/21/2022'
    }
]
def home(request):
    context = {
        'posts': posts ,
        'title':'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
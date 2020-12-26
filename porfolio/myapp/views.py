from django.shortcuts import render
from .models import aboutme,myblog

# Create your views here.
def index(request):
    about_me = aboutme.objects.all()
    my_blog = myblog.objects.all().order_by('-id')[:3]
    context = {
        'about_me':about_me,
        'my_blog':my_blog,
    }
    return render(request, 'index.html', context)
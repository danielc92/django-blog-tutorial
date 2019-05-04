from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
def index(request):
	
	posts = Posts.objects.all()

	data = {
		'title': 'Blog Posts',
		'posts': posts
	}

	return render(request, 
				  'blog/index.html', 
				  data)
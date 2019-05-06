from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.urls import reverse

# Create your views here.
def index(request):
	
	admin_route = reverse('admin-route')

	posts = Posts.objects.all()

	data = {
		'title': 'Blog Posts',
		'posts': posts,
		'admin-route': admin_route
	}

	return render(request, 
				  'blog/index.html', 
				  data)
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Volunteer

def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def about(request):
	context = {}
	# template = 'about.html'
	# return render(request,template,context)
	return render(request, "about.html", context)

def team(request):
	context = {}
	template = 'team.html'
	return render(request,template,context)

def developers(request):
	context = {}
	template = 'developers.html'
	return render(request,template,context)

def contact(request):
	context = {}
	template = 'contact.html'
	return render(request,template,context)
@login_required
def userProfile(request):
	user = request.user
	context = {'user': user }
	template = 'profiles.html'
	return render(request,template,context)

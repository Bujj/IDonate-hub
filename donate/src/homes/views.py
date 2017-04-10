from urllib import quote_plus

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import HomeForm
from .models import Home

# Create your views here.


def home_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	form = HomeForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request,  "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "home_form.html", context)

def home_detail(request, slug=None):
	instance = get_object_or_404(Home, slug=slug) 
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.about_home)
	context = {
	"title": "Single Template",
	"instance": instance,
	"share_string": share_string,
	}
	return render(request, "single_home.html", context)

def home_list(request):
	today = timezone.now().date()
	queryset_list = Home.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Home.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(home_name__icontains=query)|
				Q(about_home__icontains=query)|
				Q(email__icontains=query)|
				Q(managers_name__icontains=query)|
				# Q(about_home__icontains=query)|
				Q(phone_number__icontains=query)|
				Q(managers_id_no__icontains=query)
				# Q(about_manager__icontains=query)|
				# Q(county__icontains=query)|
				# Q(constituency__icontains=query)|
				# Q(ward__icontains=query)|
				# Q(children_gender__icontains=query)|
				# Q(user__first_name__icontains=query) |
				# Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "search"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
	"object_list": queryset,
	"title": "List",
	"page_request_var": page_request_var,
	"today": today,
	}
	return render(request, "home.html", context)
	
def home_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	instance = get_object_or_404(Home, slug=slug) 
	form = HomeForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "The home was changed successfully.")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"title": "Edit",
	"instance": instance,
	"form": form,
	}
	return render(request, "home_form.html", context)

def home_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	instance = get_object_or_404(Home, slug=slug)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("list")

def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context)

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
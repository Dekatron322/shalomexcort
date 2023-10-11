from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Count

from django.core.mail import send_mail
from . models import *
from datetime import datetime
import datetime as dt



def IndexView(request):

	if request.method == "POST":
		email = request.POST.get("email")
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		message = request.POST.get("message")

		contact = Contact.objects.create(
			name=name,  
			email=email, 
			phone=phone, 
			message=message, 
		)
		contact.save()

		messages.warning(request, "Message Delivered!")
		return HttpResponseRedirect(reverse("main:index"))

	else:
		context = {}
		return render(request, "main/index.html", context )


def FuneralView(request):

	if request.method == "POST":
		pass

	else:
		context = {}
		return render(request, "main/funeral.html", context )


def ShowroomView(request):

	if request.method == "POST":
		pass

	else:
		showroom = Showroom.objects.all().order_by('-pub_date')
		context = {"showroom":showroom}
		return render(request, "main/showroom.html", context )


def ExclusiveView(request):

	if request.method == "POST":
		pass

	else:
		context = {}
		return render(request, "main/exclusive.html", context )


def CremationView(request):

	if request.method == "POST":
		pass

	else:
		context = {}
		return render(request, "main/cremation.html", context )


def AboutView(request):

	if request.method == "POST":
		email = request.POST.get("email")
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		message = request.POST.get("message")

		contact = Contact.objects.create(
			name=name,  
			email=email, 
			phone=phone, 
			message=message, 
		)
		contact.save()

		messages.warning(request, "Message Delivered!")
		return HttpResponseRedirect(reverse("main:index"))

	else:
		context = {}
		return render(request, "main/about.html", context )


def ContactView(request):

	if request.method == "POST":
		email = request.POST.get("email")
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		message = request.POST.get("message")

		contact = Contact.objects.create(
			name=name,  
			email=email, 
			phone=phone, 
			message=message, 
		)
		contact.save()

		messages.warning(request, "Message Delivered!")
		return HttpResponseRedirect(reverse("main:index"))

	else:

		context = {}
		return render(request, "main/contact.html", context )



from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Contact(models.Model):
	name = models.TextField(default="", null=True)
	email = models.CharField(default="",max_length=2000)
	subject = models.TextField(default="",max_length=1000000)
	phone =	models.CharField(default="",max_length=1000)

	message = models.TextField(default="",max_length=1130, null=True)
	
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name


class Showroom(models.Model):
	title = models.CharField(max_length=250)
	image = models.ImageField(upload_to='images/', blank=True, default="default_files/default_face.jpg")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
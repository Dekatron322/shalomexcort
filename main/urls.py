from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("about", views.AboutView, name="about"),
	path("contact/", views.ContactView, name="contact"),
	path("funeral/", views.FuneralView, name="funeral"),
	path("vip-exclusive/", views.ExclusiveView, name="vip_exclusive"),
	path("cremation/", views.CremationView, name="cremation"),
	path("showroom/", views.ShowroomView, name="showroom"),


]
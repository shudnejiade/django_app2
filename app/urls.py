from django.conf.urls import  url
from . import views
urlpatterns=[
	url(r'',views.welcome),
	# url (r'^app/$', views.welcome),
	url(r'moments_input',views.moments_input),

]
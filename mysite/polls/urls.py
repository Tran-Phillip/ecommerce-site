# third party
from django.urls import path

# internal 
from . import views 

urlpatterns = [ 
	path('', views.index, name='index'),
	path('philip', views.index, name = 'ok'),
]
from django.urls import path
#from . import views
from .views import HomeView, DetailView, CreateView

urlpatterns = [
#	path('', views.home, name="home"),
	path('', HomeView.as_view(), name="home"),
	path('post/<int:pk>', DetailView.as_view(), name="posts"),
	path('create/', CreateView.as_view(), name='add_post'),
]

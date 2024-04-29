from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


app_name = 'shops' 

"""
This creates a problem of no reverse 
url for the navigation. e.g. {% url 'shops:contact' %}
"""
#from .forms import LoginForm


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    #path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html' """ You first of all add comma before this: Authentication_form=LoginForm if you are using MAC OS."""), name='login'),
]
from django.urls import path
from . import views

# FRONT END POINTS

urlpatterns = [
    
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('boe/', views.boe),
    path('count/',views.count,name='count'),
    path('about/',views.about,name='about'),
    
]

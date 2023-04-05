from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home_page),
    #path('requiem/', views.requiem),
    #path('project/', views.project),
    #path('candidate/', views.candidate),
]
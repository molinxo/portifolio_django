from django.urls import path 
from . import views

app_name = 'projects'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('', views.projects, name='projects')
]
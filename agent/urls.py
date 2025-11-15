from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_list, name='agent_list'),
    path('add/', views.add_agent, name='add_agent'),
]
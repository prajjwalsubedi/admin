from django.urls import path
from .views import *


urlpatterns = [
    path('',DashboardView, name='dashboard'),
]

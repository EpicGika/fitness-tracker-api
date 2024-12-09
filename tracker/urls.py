from django.urls import path
from .views import fetch_activities, add_activity

urlpatterns = [
    path('activities/', fetch_activities, name='fetch_activities'),
    path('activities/add/', add_activity, name='add_activity'),
]

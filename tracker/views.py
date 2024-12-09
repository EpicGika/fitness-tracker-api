from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Activity
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def fetch_activities(request):
    if request.method == 'GET':
        activities = Activity.objects.all().values()
        return JsonResponse(list(activities), safe=False)

@csrf_exempt
def add_activity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=data['user_id'])
        activity = Activity.objects.create(
            user=user,
            activity_type=data['activity_type'],
            duration=data['duration'],
            calories_burned=data['calories_burned'],
            date=data['date']
        )
        return JsonResponse({'id': activity.id, 'status': 'Activity added'})

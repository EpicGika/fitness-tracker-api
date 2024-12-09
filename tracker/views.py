from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Activity
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_activities(request):
    activities = Activity.objects.filter(user=request.user).values()
    return Response(activities)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_activity(request):
    data = request.data
    activity = Activity.objects.create(
        user=request.user,
        activity_type=data['activity_type'],
        duration=data['duration'],
        calories_burned=data['calories_burned'],
        date=data['date']
    )
    return Response({'id': activity.id, 'status': 'Activity added'})
from django.http import HttpResponse, JsonResponse

from main.forms import UserLoginForm
from main.models import *
from .serializers import TrackSerializer, UserSerializer, TrackTypeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated

def all_apis(request):
    return HttpResponse('ALL_APIS')

@api_view(['GET'])
def all_track_types(request):
    if request.method == 'GET':
        serializer = TrackTypeSerializer(TrackType.objects.all(), many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def all_tracks(request):
    if request.method == 'GET':
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def track(request, track_id):
    track = Track.objects.get(pk=track_id)
    if request.method == 'GET':
        serializer = TrackSerializer(track)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = TrackSerializer(track, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PATCH'])
def user(request, username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def user_logout(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

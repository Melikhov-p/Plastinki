from django.urls import path
from .views import all_track_types, all_tracks, all_apis, track, all_users, user, user_logout, user_login

urlpatterns = [
    path('', all_apis, name='all_apis'),
    path('all_track_types', all_track_types),
    path('all_tracks/', all_tracks, name='all_tracks'),
    path('track/<int:track_id>', track, name='track'),
    path('all_users/', all_users, name='all_users'),
    path('user/<str:username>/', user, name='user'),
    path('logout/', user_logout),
    path('login/', user_login)
]
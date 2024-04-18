from django.urls import path
from . import views

urlpatterns = [
    path('submit_request/', views.submit_request, name='submit_request'),
    path('track_request/<int:request_id>/', views.track_request, name='track_request'),
    path('account_info/', views.account_info, name='account_info'),
]

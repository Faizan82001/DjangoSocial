from django.urls import path
from groups import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroupView.as_view(), name='all'),
    path('new/', views.CreateGroupView.as_view(), name='create'),
    path('posts/in/<str:slug>/', views.GroupDetailView.as_view(), name='single'),
    path('join/<str:slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<str:slug>/', views.LeaveGroup.as_view(), name='leave'),
]

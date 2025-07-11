from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('tweets/create/', views.tweet_create, name='tweet_create'),
    path('tweets/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('tweets/<int:tweet_id>/like/', views.tweet_like_toggle, name='tweet_like_toggle'),
    path('tweets/<int:tweet_id>/comment/', views.add_comment, name='add_comment'),
    path('register/', views.register, name='register'),

]

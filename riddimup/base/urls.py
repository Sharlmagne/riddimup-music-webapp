from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('charts/', views.charts, name="charts"),
    path('track/<slug:slug>/', views.TrackDetailView.as_view(), name="track"),
    path('like/', views.like, name="like"),
    path('search/', views.search, name="search"),
]
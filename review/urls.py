from django.urls import path
from .views import ReviewListView, ReviewDetailView, SeltzerDetailView
from . import views

urlpatterns = [
    path('', ReviewListView.as_view(), name='review-home'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('seltzer/<int:pk>/', SeltzerDetailView.as_view(), name='seltzer-detail'),
    path('about/', views.about, name='review-about'),
]
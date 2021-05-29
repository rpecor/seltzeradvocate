import review
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Seltzer
from .models import Review
from django.db.models import Avg

def home(request):
  context = {
      'reviews': Review.objects.all()
  }
  return render(request, 'review/home.html', context)

class SeltzerListView(ListView):
  model = Seltzer
  template_name = 'review/home.html'
  context_object_name = 'seltzers'

class ReviewListView(ListView):
  model = Review
  template_name = 'review/home.html'
  context_object_name = 'reviews'
  ordering = ['-date_posted']

class ReviewDetailView(DetailView):
  model = Review

class SeltzerDetailView(DetailView):
  model = Seltzer
  
def about(request):
  return render(request, 'review/about.html', {'title': 'About'})
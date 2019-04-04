from django.shortcuts import render

reviews = [
  {
      'author': 'Ryan',
      'seltzer': 'Kroger CranLime',
      'content': 'Its guud',
      'date_reviewed': 'August, 27, 2018'
  },
  {
      'author': 'Jane',
      'seltzer': 'Kroger Lime',
      'content': 'Its not good',
      'date_reviewed': 'Jan, 4, 2010'
  }
]


def home(request):
  context = {
      'reviews': reviews
  }
  return render(request, 'review/home.html', context)

def about(request):
  return render(request, 'review/about.html', {'title': 'About'})
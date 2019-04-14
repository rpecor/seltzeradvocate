from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Seltzer(models.Model):
  name = models.CharField(max_length = 100)
  manufacturer = models.CharField(max_length = 100)
  date_added = models.DateTimeField(default=timezone.now)
  abv = models.DecimalField(max_digits=3, decimal_places=2)

  def __str__(self):
    return self.name

class Review(models.Model):
  seltzer = models.ForeignKey(Seltzer, on_delete=models.CASCADE)
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length = 50)
  content = models.TextField()
  smell = models.DecimalField(max_digits=3, decimal_places=2)
  taste = models.DecimalField(max_digits=3, decimal_places=2)
  carbonation = models.DecimalField(max_digits=3, decimal_places=2)
  overall = models.DecimalField(max_digits=3, decimal_places=2)

  def __str__(self):
    return self.title
 
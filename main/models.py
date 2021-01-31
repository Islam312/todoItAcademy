from django.db import models
from django.db.models.query_utils import subclasses

# Create your models here.

class ToDo(models.Model):
  describe_text = models.CharField(max_length=50)
  time_create = models.DateTimeField(auto_now_add=True)
  is_done = models.BooleanField(default=False)
  is_important = models.BooleanField(default=False)


class Books(models.Model):
  title = models.CharField(max_length=50)
  subtitle = models.CharField(max_length=50)
  description = models.CharField(max_length=50)
  price = models.CharField(max_length=6)
  genre = models.CharField(max_length=30)
  author = models.CharField(max_length=30)
  year = models.CharField(max_length=4)
  date = models.DateTimeField(auto_now_add=True)
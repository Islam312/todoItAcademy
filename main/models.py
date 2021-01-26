from django.db import models

# Create your models here.

class ToDo(models.Model):
  describe_text = models.CharField(max_length=50)
  time_create = models.DateField(auto_now_add=True)
  is_done = models.BooleanField(default=False)
  is_important = models.BooleanField(default=False)
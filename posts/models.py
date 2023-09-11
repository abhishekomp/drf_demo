from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=50, blank=False, null=False)
  content = models.TextField(max_length=500)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

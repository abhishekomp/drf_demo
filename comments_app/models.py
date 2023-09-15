from django.db import models

# Create your models here.


class Comment(models.Model):
    content = models.TextField(max_length=250, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

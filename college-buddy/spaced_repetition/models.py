from django.db import models

# Create your models here.

class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(name="title", max_length=200)
    completed = models.BooleanField(name="completed", default=False)
    
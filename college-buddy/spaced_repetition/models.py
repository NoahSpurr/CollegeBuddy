from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

from datetime import date

# Create your models here.

class Reminders(models.Model):
    default_list = [1, 3, 7, 21] # every 1 day, 3 days, 1 week, 3 weeks 

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders", null=True, blank=True)
    created_date = models.DateField(name="date", auto_now_add=True)
    items = ArrayField(name="items", base_field=models.IntegerField(null=True, blank=True), blank=True, default=default_list) # So to calculate the reminders, you do created_date + datetime.timedelta(days=numDays)

    def __str__(self):
        return f"Reminders ({self.id}): {self.items}"

def get_default_reminder():
    obj, created = Reminders.objects.get_or_create(
        items=Reminders.default_list,
    )
    return obj.id

class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos", null=True, blank=True)
    reminders = models.ForeignKey(name="reminders", to=Reminders, on_delete=models.SET_DEFAULT, default=get_default_reminder) # when delete Reminder linked to todoitem, set reminders to default
    title = models.CharField(name="title", max_length=200)
    completed = models.BooleanField(name="completed", default=False)

    def __str__(self):
        return f"Reminders ({self.id}): {self.items}"

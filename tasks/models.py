from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    TASK_STATUS = (
        ('un', 'unassigned'),
        ('r', 'running'),
        ('p', 'pending'),
        ('c', 'completed'),
    ) 

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=TASK_STATUS, default='un')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

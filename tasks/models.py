from django.db import models

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

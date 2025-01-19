from django.db import models

from officer.models import Officer

class Ticket(models.Model):
    subject = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    created_by = models.ForeignKey(Officer, on_delete=models.CASCADE, related_name="created_tickets")
    assigned_to = models.ForeignKey(Officer,blank = True, null = True, on_delete=models.SET_NULL, related_name="assigned_tickets")
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
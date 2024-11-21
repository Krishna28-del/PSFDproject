from django.db import models

class Incident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_reported = models.DateTimeField(auto_now_add=True)

class HelpRequest(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    description = models.TextField()
    date_requested = models.DateTimeField(auto_now_add=True)

class SupplyRequest(models.Model):
    supplies_needed = models.TextField()
    quantity = models.IntegerField()
    date_requested = models.DateTimeField(auto_now_add=True)
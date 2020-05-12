from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    rota = models.CharField(max_length=200)
    rota_ID = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=200)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name

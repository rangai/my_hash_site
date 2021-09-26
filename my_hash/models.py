from django.conf import settings
from django.db import models

class MyHash(models.Model):
    message = models.TextField()
    my_hash = models.CharField(max_length=200)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.message
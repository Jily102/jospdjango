from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
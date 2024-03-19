from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=700)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"

from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=700)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"

# Create your models here.

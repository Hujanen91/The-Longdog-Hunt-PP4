from django.db import models


class Contact(models.Model):
    """
    Model to handle the contact form
    submission.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=700)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"

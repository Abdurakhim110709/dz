from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField(default=0)
    salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.name

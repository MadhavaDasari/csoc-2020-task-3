from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title  


class Collaborate(models.Model):

    user = models.ForeignKey(User,related_name="collaborator",on_delete=models.CASCADE)
    title = models.ForeignKey(Todo,related_name="task",on_delete=models.CASCADE)

    



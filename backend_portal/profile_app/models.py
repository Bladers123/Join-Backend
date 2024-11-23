from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    tasks = models.ManyToManyField('Task', blank=True, related_name="tasks") 
    contacts = models.ManyToManyField('Contact', blank=True, related_name="contacts") 

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    backgroundColor = models.CharField(max_length=20) 
    isSelected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}'s Contact"
    

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    dueDate = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=50, default='Medium')
    category = models.CharField(max_length=255)
    progress = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class Assigned(models.Model):
    task = models.ForeignKey(Task, related_name='assignedTo', on_delete=models.CASCADE)
    name = models.CharField(max_length=255) 
    backgroundColor = models.CharField(max_length=20, blank=True, null=True) 

    def __str__(self):
        return self.name
    
class Subtask(models.Model):
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({'Completed' if self.completed else 'Pending'})"




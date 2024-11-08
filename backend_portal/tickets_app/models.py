from django.db import models
from profile_app.models import Profile

class AssignedUser(models.Model):
    name = models.CharField(max_length=100)
    bg_color = models.CharField(max_length=7)  # z.B. Hex-Farbe wie "#FF5733"

    def __str__(self):
        return self.name

class Subtask(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    identifier = models.FloatField()  # Zufällige ID wie in getTaskData()

    def __str__(self):
        return f"{self.title} - {'Completed' if self.completed else 'Incomplete'}"

class Ticket(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="tickets")
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    assigned_to = models.ManyToManyField(AssignedUser, blank=True, related_name="tickets")
    progress = models.IntegerField(default=0)  # z.B. Prozentangabe des Fortschritts
    subtasks = models.ManyToManyField(Subtask, blank=True, related_name="tickets")
    created_at = models.DateTimeField(auto_now_add=True)  # Automatische Erstellung

    def __str__(self):
        return f"{self.title} - {self.priority}"

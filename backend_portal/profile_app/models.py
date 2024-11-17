# profile_app/api/models.py



from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    ticket = models.ManyToManyField('Ticket', blank=True, related_name="ticket") 
    contacts = models.ManyToManyField('Contact', blank=True, related_name="contacts") 

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    backgroundColor = models.CharField(max_length=20, default="#000000")  # Standard-Hintergrundfarbe
    isSelected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}'s Contact"
    

from django.db import models

class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)  # ID des Tickets
    title = models.CharField(max_length=255)  # Titel des Tickets
    description = models.TextField(blank=True, null=True)  # Beschreibung
    due_date = models.DateField(blank=True, null=True)  # Fälligkeitsdatum
    priority = models.CharField(max_length=50, choices=[
        ('Urgent', 'Urgent'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ])  # Priorität
    category = models.CharField(max_length=255)  # Kategorie
    progress = models.CharField(max_length=255)  # Fortschritt in Prozent

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return self.title

class Assigned(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='assigned_to', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Name der zugewiesenen Person
    backgroundColor = models.CharField(max_length=7, blank=True, null=True)  # Hintergrundfarbe oder anderes Attribut (z. B. Hex-Farbcode)

    def __str__(self):
        return self.name
    
class Subtask(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # Titel der Unteraufgabe
    completed = models.BooleanField(default=False)  # Status der Unteraufgabe
    subtask_id = models.FloatField()  # Zufällige ID wie in der JS-Funktion

    def __str__(self):
        return f"{self.title} ({'Completed' if self.completed else 'Pending'})"

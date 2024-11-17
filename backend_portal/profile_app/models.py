# profile_app/api/models.py



from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    tickets = models.ManyToManyField('Ticket', blank=True, related_name="tickets") 
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
    

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    dueDate = models.DateField(blank=True, null=True)
    priority = models.CharField(
        max_length=50,
        choices=[('Urgent', 'Urgent'), ('Medium', 'Medium'), ('Low', 'Low')]
    )
    category = models.CharField(max_length=255)
    progress = models.CharField(max_length=255)
    assignedTo = models.ManyToManyField('Assigned', related_name='assigned_contacts')  # Kein Konflikt
    subtasks = models.ManyToManyField('Subtask', related_name='ticket_subtasks')  # Eindeutiger related_name



class Assigned(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='assigned_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Name der zugewiesenen Person
    backgroundColor = models.CharField(max_length=7, blank=True, null=True)  # Hintergrundfarbe oder anderes Attribut (z. B. Hex-Farbcode)

    def __str__(self):
        return self.name
    
class Subtask(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='subtask_tickets', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    subtask_id = models.FloatField()

    def __str__(self):
        return f"{self.title} ({'Completed' if self.completed else 'Pending'})"




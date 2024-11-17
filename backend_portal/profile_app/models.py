# profile_app/api/models.py



from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    ticket = models.ManyToManyField('tickets_app.Ticket', blank=True, related_name="profiles")  # Tickets, die dem Profil zugeordnet sind
    contacts = models.ManyToManyField('Contact', blank=True)  # Beziehung zu Contact

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
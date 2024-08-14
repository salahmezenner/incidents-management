from django.db import models
from django.contrib.auth.models import User


class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    url = models.URLField()

class Meta:
        app_label = 'incidents'

class Incident(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=255)
    solution = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    evaluation = models.IntegerField(default=1)
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)



class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('adminapp', 'adminapp'),
        ('superviseur', 'superviseur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='adminapp')



class CelluleDeCrise(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Max, F, Value, IntegerField, ExpressionWrapper, Subquery, OuterRef
from django.db.models.functions import Substr


class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.nom

class Couche(models.Model):
    couche = models.CharField(max_length=255)
    technologie = models.CharField(max_length=255)
    def __str__(self):
        return self.technologie

class Incident(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    intitule = models.CharField(max_length=255)
    resume = models.TextField()
    solution = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    evaluation = models.IntegerField(default=1)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    couche = models.ForeignKey(Couche, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            platform_id = self.platform.id if self.platform else "0"
            couche_initial = self.couche.couche[0].upper() if self.couche and self.couche.couche else "X"

            prefix = f"{platform_id}{couche_initial}"

            max_id = Incident.objects.filter(
                id__startswith=prefix
            ).annotate(
                num_part=ExpressionWrapper(
                    Substr('id', len(prefix) + 1, 4),
                    output_field=IntegerField()
                )
            ).aggregate(
                max_num_part=Max('num_part')
            )['max_num_part']

            if max_id:
                sequential_number = max_id + 1
            else:
                sequential_number = 1

            self.id = f"{prefix}{sequential_number:04d}"

        super().save(*args, **kwargs)


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

class Event(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    events = models.JSONField(null=True)

    def __str__(self):
        return f"Event on {self.day}/{self.month}/{self.year}"
    
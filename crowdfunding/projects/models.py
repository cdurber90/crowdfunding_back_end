from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class HealthcareHero(models.Model):
    name = models.CharField(max_length=200)
    workplace = models.CharField(max_length=200)
    bio = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_heroes'
        )
    

class Donation(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    healthcarehero = models.ForeignKey(
    'Healthcare Hero',
    on_delete=models.CASCADE,
    related_name='donations'
    )
    
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_donations'
    )
    

from django.db import models

# Create your models here.
class Pet(models.Model):
    pet_name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    owner_name = models.CharField(max_length=150)
    owner_contact_number = models.CharField(max_length=20)
    date_registered = models.DateField(auto_now_add=True)
    health_vaccination_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pet_name
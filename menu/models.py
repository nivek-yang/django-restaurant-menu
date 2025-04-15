from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    is_available = models.BooleanField(default=True)
    is_spicy = models.BooleanField(default=False)


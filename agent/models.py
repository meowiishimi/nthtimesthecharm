from django.db import models
from django.core.exceptions import ValidationError

class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.city})"


class Agent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='agent')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Venue(models.Model):
    VENUE_TYPES = [
        ('Conference', 'Conference Room'),
        ('Hall', 'Hall'),
        ('Studio', 'Studio'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=VENUE_TYPES)
    floor = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    floor_area = models.DecimalField(max_digits=8, decimal_places=2)
    under_renovation = models.BooleanField(default=False)

    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='venues')
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name='venues')

    def clean(self):
        if self.agent.building != self.building:
            raise ValidationError("Agent and Venue must belong to the same building.")

    def __str__(self):
        return f"{self.name} ({self.building.name})"


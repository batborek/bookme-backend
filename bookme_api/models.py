from django.db import models

# Create your models here.


class Room(models.Model):
    price = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    is_booked = models.BooleanField(default=False)
    is_clean = models.BooleanField(default=True)

    def __str__(self):
        return self.type
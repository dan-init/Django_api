from django.db import models

class Card(models.Model):
    front_side = models.CharField(max_length=100)
    back_side = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.front_side + self.back_side
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.name}'
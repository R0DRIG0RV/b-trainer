from django.db import models


class Plan(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.BigIntegerField(default=0)
    duration = models.BigIntegerField(default=0)
    discount = models.BooleanField(default=False)
    price_discount = models.BigIntegerField(default=0, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}: {self.price}'
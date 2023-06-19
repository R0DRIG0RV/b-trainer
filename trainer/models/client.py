from django.db import models

class Client(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    plan = models.ForeignKey('Plan', on_delete=models.SET_NULL, null=True)
    dni = models.CharField(max_length=12)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.dni}: {self.firstname}'
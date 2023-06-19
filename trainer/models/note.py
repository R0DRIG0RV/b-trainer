from django.db import models


class Note(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.text}'
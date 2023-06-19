from django.db import models

class ClientDocument(models.Model):
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    document = models.ForeignKey('Document', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.client.dni}: {self.document.name}'
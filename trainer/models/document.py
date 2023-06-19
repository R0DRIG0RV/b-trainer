from django.db import models


class Document(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    url_file = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}'
from django.db import models


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return f'{self.id} - {self.title}' # type: ignore

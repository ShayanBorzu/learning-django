from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(default=None, null=True, blank=True, max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return f'{self.id} - {self.subject}' # type: ignore

class NewsLetter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return f'{self.id} - {self. email}' # type: ignore
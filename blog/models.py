from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return (
            f"{self.id} - {self.name}"  # pyright: ignore[reportAttributeAccessIssue]
        )

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # tags
    category = models.ManyToManyField(Category)
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return (
            f"{self.id} - {self.title}"  # pyright: ignore[reportAttributeAccessIssue]
        )

from django.db import models


# Create your models here.
class Post(models.Model):
    # img
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags
    # category
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

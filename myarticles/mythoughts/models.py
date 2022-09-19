from django.db import models
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField(max_length = 1000)
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"Article object: {self.title}"

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    copies_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

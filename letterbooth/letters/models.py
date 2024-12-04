from django.db import models

class Letter(models.Model):
    text = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=50, default='General')

    def __str__(self):
        return self.text

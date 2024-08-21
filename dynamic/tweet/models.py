from django.db import models

class Tweet(models.Model):
    username=models.CharField(max_length=50)
    tweet = models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)



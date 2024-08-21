from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField



# Create your models here.
class Blogs(models.Model):
    Title = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    Photos = models.ImageField(upload_to='blogs/',max_length=250,null=True,default=None)
    Description = HTMLField()
    slugdata = AutoSlugField(populate_from='Title',unique=True,null=True,default=None)
    
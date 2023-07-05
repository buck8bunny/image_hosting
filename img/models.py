from django.db import models

# Create your models here.
from django.db import models

class Photo(models.Model):
    image = models.FileField(upload_to='photos/')
    caption = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)

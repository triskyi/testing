from django.db import models

class Destin(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')  # Specify the upload_to path
    dsc = models.TextField()
    offer = models.BooleanField(default=False)
  


from django.db import models

# Create your models here.
class Tables(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    address=models.TextField()
    def __str__(self):
        return self.first_name
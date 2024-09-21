from django.db import models

# Create your models here.
class Products(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=220)
    content = models.TextField(null = True, blank=True)
    price = models.IntegerField(default=0)


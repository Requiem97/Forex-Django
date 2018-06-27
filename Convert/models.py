from django.db import models

# Create your models here.
class Forex(models.Model):
    php_amount = models.FloatField()
    result = models.FloatField()
    currency = models.CharField(max_length = 3)
    
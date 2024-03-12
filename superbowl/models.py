from django.db import models

# Create your models here.
class Commercial(models.Model):
    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    sburl = models.URLField(null=True)
    yturl = models.URLField()
    funny = models.BooleanField()
    show_product_quickly = models.BooleanField()
    patriotic = models.BooleanField()
    celebrity = models.BooleanField()
    danger = models.BooleanField()
    animals = models.BooleanField()
    use_sex = models.BooleanField()
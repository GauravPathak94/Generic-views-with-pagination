from django.db import models

# Create your models here.
class LandRec(models.Model):
    farmer_name = models.CharField(max_length=50)
    survey_number = models.CharField(max_length=10)
    village = models.CharField(max_length=50)
    farm_area = models.CharField(max_length=20)

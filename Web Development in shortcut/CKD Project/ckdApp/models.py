from django.db import models

# Create your models here.
class ckdModel(models.Model):

    subscription_length=models.FloatField()
    vehicle_age=models.FloatField()
    customer_age=models.FloatField()
    region_density=models.FloatField()
    turning_radius=models.FloatField()
    length=models.FloatField()
    width=models.FloatField()
    gross_weight=models.FloatField()
    engine_type=models.FloatField()
    
 
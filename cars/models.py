from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    color = models.CharField(max_length=30)
    year = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    created_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.model

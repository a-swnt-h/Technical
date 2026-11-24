from django.db import models

class employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField()
    depaertment=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    salary=models.IntegerField()
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
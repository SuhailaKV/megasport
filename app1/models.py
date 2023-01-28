from django.db import models

# Create your models here.
class Category(models.Model):
    Name=models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class Products(models.Model):
    Name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='media')
    Description=models.CharField(max_length=1000)
    Net_weight=models.CharField(max_length=200)
    Directions=models.CharField(max_length=1000)
    Warnings=models.CharField(max_length=800)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.Name

class Ingrediants(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    i_name=models.CharField(max_length=200)
    value1=models.CharField(max_length=200)
    value2=models.CharField(max_length=200)

    def __str__(self):
        return self.i_name

class modelpic(models.Model):
    Name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='media')

    def __str__(self):
        return self.Name

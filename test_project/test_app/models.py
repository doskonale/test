from django.db import models
from django.core.validators import MinLengthValidator

class Product(models.Model):
    name = models.CharField(max_length=100,blank=False, null=True,
    	help_text='Please input product name', 
    	validators=[MinLengthValidator(4, "Project name should be at least 4 characters, ex. T825")])
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
    	help_text='Please input product price')
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)

    def __str__(self):
        return self.name, self.price

class Project(models.Model):
    name = models.CharField(max_length=100,blank=False, null=True, 
    	help_text='Please input project name', 
    	validators=[MinLengthValidator(4, "Project name should be at least 4 characters, ex. G965F")])
    country = models.CharField(
    	max_length=100,blank=False, null=True,
    	help_text='Please input country name',
    	validators=[MinLengthValidator(2, "Country name should be at least 2 characters")]
    	)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)

    def __str__(self):
        return self.name, self.country
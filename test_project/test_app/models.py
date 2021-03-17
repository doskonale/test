from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100,blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    country = models.CharField(max_length=100, blank=False, null=True)
    def __str__(self):
        return self.name
        
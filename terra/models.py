from django.db import models

# Create your models here.

class Terrarium(models.Model):
    size = models.CharField('size',name='size',max_length=11)
    material = models.CharField('material', name='material',max_length=200)
    year_of_prod = models.CharField('year_of_prod', name='year_of_prod',max_length=4)
    price = models.PositiveIntegerField('price', name='price')
    
    def __str__(self) ->str:
        return self.size + " "+  self.material + " " + self.year_of_prod + " " + str(self.price)
    
# class Client(models.Model):
#     email 
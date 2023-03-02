from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Terrarium(models.Model):
    user = models.ManyToManyField(User)
    size = models.CharField('size',name='size',max_length=11)
    material = models.CharField('material', name='material', max_length=200)
    year_of_prod = models.CharField(
        'year_of_prod', name='year_of_prod', max_length=4)
    price = models.PositiveIntegerField('price', name='price')
    count = models.PositiveIntegerField('count', name='count', default=4)

    def __str__(self) -> str:
        return self.size + " " + self.material + " " + self.year_of_prod + " " + str(self.price)




from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Named(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Currency(Named):
    code = models.CharField(max_length=3)
    exchange = models.FloatField()


class Priced(models.Model):
    class Meta:
        abstract = True
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.SET_DEFAULT, default=1)


class Component(Named, Priced):
    mass = models.IntegerField()


class Product(Named, Priced):
    image = models.ImageField(upload_to='products', null=True)
    description = models.TextField(null=True)


class City(Named):
    pass


class Consumer(models.Model):
    class Meta(User.Meta):
        verbose_name = 'consumer'
        verbose_name_plural = 'consumers'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    wish_list = models.ManyToManyField(Product)

from django.db import models
from django.utils.translation import ugettext_lazy as _

class ProductCategory(models.Model):
    name = models.CharField(_("Category name"), max_length=200)
    description = models.TextField()
    index = models.IntegerField(_("Index order"), default=0)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_("Product name"), max_length=1000)
    description = models.TextField()
    price = models.FloatField(_("Price"), default=0)
    amount = models.FloatField(_("Amount"), default=0)

    def __str__(self):
        return self.name

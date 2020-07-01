import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from product.models import Product
from core.models import User


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class OrderProduct(models.Model):
    amount = models.PositiveIntegerField(_("Amount"), default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('order', 'product')

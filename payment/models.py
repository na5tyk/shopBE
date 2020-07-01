import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from order.models import Order


class PaymentMethods(models.Model):
    name = models.CharField(_("Payment name"), max_length=200)
    active = models.BooleanField(_("Active"), default=False)

    def __str__(self):
        return self.name2

class Payment(models.Model):
    STATUSES = (
        (0, _("Awaiting")),
        (1, _("Paid")),
        (2, _("Canceled")),
        (3, _("Returned")),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.IntegerField(_("Status"), choices=STATUSES, default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

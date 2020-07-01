import uuid

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), unique=True)
    first_name = models.CharField(_('First name'), max_length=200, blank=True, null=True)
    last_name = models.CharField(_('Last name'), max_length=200, blank=True, null=True)

    is_active = models.BooleanField(_('Active'), default=False)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_superuser = models.BooleanField(_('Is Super User'), default=False)

    phone = models.CharField(_("Phone"), max_length=16)

    created = models.DateTimeField(_('Date joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserAddress(models.Model):

    first_name = models.CharField(_('First name'), max_length=200)
    last_name = models.CharField(_('Last name'), max_length=200)

    street = models.CharField(_("street"), max_length=300, blank=True, null=True)
    number = models.CharField(_("number"), max_length=10, blank=True, null=True)
    premise_number = models.CharField(_("premise_number"), max_length=10, blank=True, null=True)
    zip_code = models.CharField(_("Zip code"), max_length=16)
    city = models.CharField(_("City"), max_length=200)
    phone = models.CharField(_("Phone"), max_length=16, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

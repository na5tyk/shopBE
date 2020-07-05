from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from .models import UserAddress, User

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    default_error_messages = {
        'fields_required': _("Email and password are required")
    }

    def validate(self, attrs):
        try:
            assert attrs['email'] is not None or attrs['password'] is not None, 'fields_required'
        except AssertionError as e:
            self.fail(str(e))
        return super(RegisterSerializer, self).validate(attrs)


    class Meta:
        model = User
        exclude = ['groups', 'user_permissions']

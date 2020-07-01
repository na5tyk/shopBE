from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import UserAddressSerializer
from .models import UserAddress

class UserAddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited addresses
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = UserAddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
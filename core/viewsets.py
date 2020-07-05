from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.translation import ugettext_lazy as _

from .serializers import UserAddressSerializer, RegisterSerializer
from .models import UserAddress, User

class UserAddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited addresses
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = UserAddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Register user
    """
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_user = User.objects.create_user(serializer.data['email'], serializer.data['password'])
        return Response(status=201)

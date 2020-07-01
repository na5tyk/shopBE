from rest_framework.permissions import DjangoModelPermissions
from rest_framework.request import Request

from districts.models import AppDistrict
from gis_portal.utils import get_district_key
from .models import UserRole


class RolePermissionBase(DjangoModelPermissions):
    ROLE_INDEX = None

    def has_permission(self, request: Request, view):
        return self.validate_role(request, view)

    def validate_role(self, request, view):
        user = request.user

        if not self.is_authenticated(user):
            return False

        return user.get_user_role_index() >= self.ROLE_INDEX

    def is_authenticated(self, user):
        """
        Returns true if user is authenticated
        """
        return user and user.is_authenticated or not self.authenticated_users_only

class IsSuperAdmin(RolePermissionBase):
    """
    Checks if user is super admin
    """
    ROLE_INDEX = UserRole.SUPERADMIN_INDEX


class IsAdmin(RolePermissionBase):
    """
    Checks if user is admin
    """
    ROLE_INDEX = UserRole.ADMIN_INDEX


class IsModerator(RolePermissionBase):
    """
    Checks if user is moderator
    """
    ROLE_INDEX = UserRole.MOD_INDEX


class IsUser(RolePermissionBase):
    """
    Checks if user is user
    """
    ROLE_INDEX = UserRole.USER_INDEX

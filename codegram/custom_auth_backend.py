from django.contrib.auth.backends import ModelBackend
from .models import MyUserModel

class OrganizationUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = MyUserModel.objects.get(username=username)
        except MyUserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
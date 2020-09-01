from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, authentication, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.serializers import UserSerializer, ChangeUserPasswordSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the app on the public api URL"""
    serializer_class = UserSerializer


class ManagerUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


class ChangeUserPasswordView(generics.UpdateAPIView):
    """Change user password endpoint"""

    model = get_user_model()
    serializer_class = ChangeUserPasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            """Check old password"""
            old_pwd = serializer.data.get('old_password')
            new_pwd1 = serializer.data.get('new_password1')
            new_pwd2 = serializer.data.get('new_password2')

            if not self.object.check_password(old_pwd):
                return Response(
                    {'old_password': _('Wrong password.')},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not new_pwd1 == new_pwd2:
                return Response(
                    {'new_password': _('The new password don\'t match.')},
                    status=status.HTTP_400_BAD_REQUEST
                )

            self.object.set_password(new_pwd1)
            self.object.save()
            return Response(
                _('The password has been changed successful.'),
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

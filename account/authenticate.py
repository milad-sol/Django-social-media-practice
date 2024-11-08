from django.contrib.auth.models import User


class EmailBackend:

    def authenticate(self, request, username=None, password=None):

        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except User.DoesNotExist:
            return None

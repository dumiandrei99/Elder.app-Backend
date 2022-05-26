from rest_framework import serializers;
from ...models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'username', 'email', 'password', 'date_of_birth', 'first_name', 'last_name']
        
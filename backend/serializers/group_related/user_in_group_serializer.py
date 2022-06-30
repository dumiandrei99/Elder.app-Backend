from rest_framework import serializers;
from  ...models.group_related.user_in_group_model import UserInGroup


class UserInGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInGroup
        fields = '__all__'
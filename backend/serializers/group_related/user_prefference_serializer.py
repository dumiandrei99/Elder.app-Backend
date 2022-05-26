from rest_framework import serializers;
from  ...models.group_related.user_prefference_model import UserPrefference


class UserPrefferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPrefference
        fields = '__all__'

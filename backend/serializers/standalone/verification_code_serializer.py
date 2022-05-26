from rest_framework import serializers;
from ...models.standalone.verification_code_model import VerificationCode


class VerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationCode
        fields = '__all__'
        
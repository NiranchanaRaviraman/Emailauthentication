from myapp.models import EmailVerify
from rest_framework import serializers


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmailVerify
        fields=('email','otp','verify','otp_time')
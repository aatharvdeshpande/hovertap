from rest_framework import serializers
from .models import master_user


class master_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = master_user
        fields = ['user_m_no', 'otp_status', 'user_name']
from rest_framework import serializers

from shop.models import Polzovatel


class LoginSerializer(serializers.Serializer):
    nickname_mail = serializers.CharField(required=True)
    parol = serializers.CharField(required=True)


class RegistrationSerializer(serializers.Serializer):
    nickname = serializers.CharField(required=True)
    mail = serializers.EmailField(required=True)
    parol = serializers.CharField(required=True)


class PolzovatelSerializer(serializers.ModelSerializer):
    class Meta():
        model = Polzovatel
        fields = 'all'


class PolzovatelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polzovatel
        fields = [
            'image',
        ]

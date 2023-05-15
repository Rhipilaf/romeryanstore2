from rest_framework import serializers
from django.templatetags.static import static
from rest_framework import serializers

from shop.models import Polzovatel, Account


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

class AccountAvtodopolnenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'title', 'description', 'img']

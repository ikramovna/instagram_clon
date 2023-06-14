from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, UUIDField

from apps.users.models import User


class SignUpSerializer(ModelSerializer):
    id = UUIDField(read_only=True)

    def __int__(self, *args, **kwargs):
        super(SignUpSerializer, self).__init__(*args, **kwargs)
        self.fields['email_phone_number'] = CharField(required=False)



    class Meta:
        model = User
        fields = (
            'id',
            'auth_type',
            'auth_status'
        )
        extra_kwargs = {
            'auth_type': {'read_only': True, 'required': False},
            'auth_status': {'read_only': True, 'required': False}

        }

    def validate(self, data):
        super(SignUpSerializer, self).validate(data)
        data = self.auth_validate(data)
        return data

    @staticmethod
    def auth_validate(attrs):
        print(attrs)
        user_input = str(attrs.get('email_phone_number')).lower()
        return data
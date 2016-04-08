"""
This module is used to define serializer
"""

from rest_framework import serializers
from user.models import User, UniqueRegistration


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """
    password = serializers.CharField(
        style= {'input_type':'password'}
    )
    class Meta:
        model = User

    def create(self, validated_data):
        """
        Create and return a new `User` instance
        given the validated data.
        """
        print(validated_data)
        u=User.objects.create(**validated_data)
        u.set_password(validated_data['password'])
        u.save();
        return u;

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance,
        given the validated data
        """
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.middle_name = validated_data.get(
            'middle_name', instance.middle_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get(
            'email', instance.email)
        instance.is_staff = validated_data.get(
            'is_staff', instance.is_staff)
        instance.contact = validated_data.get(
            'contact', instance.contact)
        instance.address = validated_data.get(
            'address', instance.address)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.roll_no = validated_data.get(
            'roll_no', instance.roll_no)
        instance.description = validated_data.get(
            'description', instance.description)
        if validated_data.get('password', None):
           instance.set_password(validated_data.get(
               'password', instance.password))
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """
    password = serializers.CharField(
        style= {'input_type':'password'}
    )
    class Meta:
        model = User
        fields = ('id',
                  'email', 'password')
class UserBesicDataSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """
    class Meta:
        model = User
        fields = ('roll_no',
                  'first_name', 'middle_name', 'last_name', 'email', 'is_active')
    def validate_email(self, value):
        try:
            User.objects.get(email=value)
            return False
        except:
            return value

class UniqueRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """

    def to_representation(self, instance):
        ret = super(serializers.ModelSerializer, self).to_representation(instance)
        request = self.context.get('request')
        print("asdas", instance)
        # Return bookings as well if requested.
        if request and request.query_params.get('include_user') == 't':
            user = User.objects.get(id=instance.user.id)
            serializer = UserDetailSerializer(user)
            ret['user'] = serializer.data
        return ret

    class Meta:
        model = UniqueRegistration
        fields = ('code','user',
                  'is_active', 'is_universal', 'valid_from', 'valid_to')

class ExcelFileSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)
    def create(self, validated_data):
            return "dadasd"

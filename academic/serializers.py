"""
This module is used to define serializer
"""

from rest_framework import serializers
from academic.models import AcademicDetail, CampusDrive, PGSem,SpecialCriteria, Interested
from user.models import User

class AcademicDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """
    def create(self, validated_data):
        print("hiiiii", validated_data)
        validated_data['student'] = User.objects.get(id=validated_data['student'])
        obj = AcademicDetail(**validated_data)
        obj.save()
        return obj
    def to_representation(self, instance):
        ret = super(serializers.ModelSerializer, self).to_representation(instance)
        request = self.context.get('request')
        if request and request.query_params.get('include_pg_sem') == 't':
            pg_sem_list = PGSem.objects.filter(academic=instance)
            serialized_data = []
            print("length", len(pg_sem_list))
            for pg_sem in pg_sem_list:
                serializer = PGSemSerializer(pg_sem)
                print("working")
                serialized_data.append(serializer.data)
            ret['pg_sem'] = serialized_data
        return ret

    class Meta:
        model = AcademicDetail


class CampusDriveSerializer(serializers.ModelSerializer):
    """
    Serializer for CampusDrive Model
    """
    class Meta:
        model = CampusDrive

class PGSemSerializer(serializers.ModelSerializer):
    """
    Serializer for PGSem Model
    """
    class Meta:
        model = PGSem

class SpecialCriteriaSerializer(serializers.ModelSerializer):
    """
    Serializer for SpecialCriteria Model
    """
    class Meta:
        model = SpecialCriteria

class InterestedSerializer(serializers.ModelSerializer):
    """
    Serializer for Interested Model
    """
    class Meta:
        model = Interested

"""
This module is used to define serializer
"""

from rest_framework import serializers
from academic.models import AcademicDetail, CampusDrive, Criteria, SpecialCriteria, Interested
from user.models import User
from academic.tasks import get_eligible_student_and_send_mail
class AcademicDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """
    def create(self, validated_data):
        validated_data['student'] = User.objects.get(id=validated_data['student'])
        obj = AcademicDetail.objects.create(**validated_data)
        return obj

    class Meta:
        model = AcademicDetail


class CampusDriveSerializer(serializers.ModelSerializer):
    """
    Serializer for CampusDrive Model
    """
    def create(self, validated_data):
        campus_drive = CampusDrive(**validated_data)
        campus_drive.save()
        #get_eligible_student_and_send_mail(campus_drive)
        return campus_drive

    class Meta:
        model = CampusDrive

# class PGSemSerializer(serializers.ModelSerializer):
#     """
#     Serializer for PGSem Model
#     """
#     class Meta:
#         model = PGSem

class CriteriaSerializer(serializers.ModelSerializer):
    """
    Serializer for Criteria Model
    """
    def create(self, validated_data):
        print(validated_data)
        validated_data['campus_drive'] = CampusDrive.objects.get(id=validated_data['campus_drive'])
        print(validated_data)
        obj = Criteria(**validated_data)
        obj.save()
        return obj

    class Meta:
        model = Criteria

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
    def to_representation(self, instance):
        from user.serializers import UserBesicDataSerializer
        ret = super(serializers.ModelSerializer, self).to_representation(instance)
        request = self.context.get('request')
        if request and request.query_params.get('campus_drive_id', None):
            student_serializer = UserBesicDataSerializer(instance.student)
            academic_detail = AcademicDetail.objects.filter(pk=instance.student.id)[0]
            academic_detail_serializer = AcademicDetailSerializer(academic_detail)
            ret['student'] = student_serializer.data
            ret['academic_detail'] = academic_detail_serializer.data
        return ret

    class Meta:
        model = Interested

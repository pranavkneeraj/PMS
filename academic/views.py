"""
This view module is used to specify the User Details
"""

from academic.models import AcademicDetail, CampusDrive, Criteria, SpecialCriteria, Interested
from rest_framework import viewsets
from django.contrib.auth.views import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
import json
from rest_framework import status, views
from django.views.decorators.csrf import csrf_exempt
from academic.serializers import AcademicDetailSerializer, CampusDriveSerializer, CriteriaSerializer, SpecialCriteriaSerializer, InterestedSerializer
from django.db.models import Q
class AcademicDetailViewSet(viewsets.ModelViewSet):
    # pylint: disable = too-many-ancestors
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AcademicDetailSerializer
    queryset = AcademicDetail.objects.filter(deleted_on=None)


class CampusDriveViewSet(viewsets.ModelViewSet):
    # pylint: disable = too-many-ancestors
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CampusDriveSerializer
    queryset = CampusDrive.objects.filter(deleted_on=None)

# class PGSemViewSet(viewsets.ModelViewSet):
#     # pylint: disable = too-many-ancestors
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = PGSemSerializer
#     base_name = 'academic-pgsem'
#     #queryset = PGSem.objects.filter(deleted_on=None)
#     def get_queryset(self):
#         params = self.request.query_params
#         queryset = PGSem.objects.filter(deleted_on=None)
#         q = Q()
#         if params.get('academic_detail_id'):
#             q = q & Q(academic_id=params.get('academic_detail_id'))
#         return queryset.filter(q).order_by('-created_on')

class CriteriaViewSet(viewsets.ModelViewSet):
    # pylint: disable = too-many-ancestors
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CriteriaSerializer
    queryset = Criteria.objects.filter(deleted_on=None)



class SpecialCriteriaViewSet(viewsets.ModelViewSet):
    # pylint: disable = too-many-ancestors
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = SpecialCriteriaSerializer
    queryset = SpecialCriteria.objects.filter(deleted_on=None)

from user.serializers import UserBesicDataSerializer
class InterestedViewSet(viewsets.ModelViewSet):
    # pylint: disable = too-many-ancestors
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = InterestedSerializer
    def get_queryset(self):
        campus_drive_id = self.request.query_params.get('campus_drive_id', None)
        if campus_drive_id:
            interested_list = Interested.objects.filter(deleted_on=None, campus_drive=campus_drive_id)

            return interested_list
        return Interested.objects.filter(deleted_on=None)

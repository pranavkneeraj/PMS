"""
This view module is used to specify the User Details
"""

from academic.models import AcademicDetail, CampusDrive, PGSem
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
from academic.serializers import AcademicDetailSerializer, CampusDriveSerializer, PGSemSerializer
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

class PGSemViewSet(viewsets.ModelViewSet):
    # pylint: disable = too-many-ancestors
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PGSemSerializer
    base_name = 'academic-pgsem'
    #queryset = PGSem.objects.filter(deleted_on=None)
    def get_queryset(self):
        params = self.request.query_params
        queryset = PGSem.objects.filter(deleted_on=None)
        q = Q()
        if params.get('academic_detail_id'):
            q = q & Q(academic_id=params.get('academic_detail_id'))
        return queryset.filter(q).order_by('-created_on')

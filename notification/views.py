"""
This view module is used to specify the User Details
"""

from notification.models import Notification
from rest_framework import viewsets

from notification.serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    # pylint: disable = too-many-ancestors
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

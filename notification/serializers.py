"""
This module is used to define serializer
"""

from rest_framework import serializers
from notification.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for Criteria Model
    """
    class Meta:
        model = Notification

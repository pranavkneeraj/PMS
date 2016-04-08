"""This module is defined for Notification model"""

from django.db import models
from core.models import BaseModel
class Notification(BaseModel):
    """
    This model Notification holds the
    information about the notification
    """
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True
        )
    description = models.CharField(
        max_length=1000
        )
    catagory = models.CharField(
        max_length=100,
        blank=True,
        null=True
        )
    display = models.BooleanField(default=True)

"""This module is defined for user model"""

from django.db import models
from django.core.validators import RegexValidator
from core.base_user.models import AbstractEmailUser
import uuid
from core.models import (
    BaseModel,CreatedFlagModelMixin,
    UpdatedFlagModelMixin,
    DeletedFlagModelMixin
)

from datetime import datetime

class User(AbstractEmailUser, BaseModel):
    """
    This model User holds the
    information about the registering User
    """
    roll_no = models.IntegerField(
        blank=True,
        null=True
        )
    middle_name = models.CharField(
        max_length=100,
        blank = True,
        null=True
        )
    address = models.TextField(
        max_length=500,
        blank = True
        )
    description = models.TextField(
        max_length=500,
        blank = True
        )

    contact = models.IntegerField(
        validators=[RegexValidator(
            regex='^[0-9]{10}$',
            message='Length has to be 10',
            code='nomatch')],
            null=True,
            blank=True
)


class UniqueRegistration(CreatedFlagModelMixin,
                         UpdatedFlagModelMixin,
                         DeletedFlagModelMixin,
                         models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    is_universal = models.BooleanField(default=False)
    valid_from = models.DateTimeField(default=datetime.now, blank=True)
    valid_to = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, null=True)

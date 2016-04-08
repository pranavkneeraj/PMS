"""This module is defined for user model"""
from django.db import models
from core.models import (
    BaseModel,
    CreatedFlagModelMixin,
    UpdatedFlagModelMixin,
    DeletedFlagModelMixin
)
from user.models import User
from django.utils import timezone
class AcademicDetail(CreatedFlagModelMixin,
                     UpdatedFlagModelMixin,
                     DeletedFlagModelMixin):
    """
    This model User holds the
    information about the registering User
    """
    BCA = 'bca'
    BCS = 'bcs'
    BE = 'be',
    OTHER = 'other'
    UGCOURSE = (
        (BCS, 'Bsc(Computer Science)'),
        (BCA, 'BCA'),
        (BE, 'BE'),
        (OTHER, 'Other')
    )
    student = models.OneToOneField(
                User,
                on_delete=models.CASCADE,
                primary_key=True,
    )
    hsc_marks = models.CharField(
        max_length=200
    )
    hsc_percentage = models.CharField(
        max_length=200
    )
    hsc_passout_year = models.CharField(
        max_length=200
    )
    ssc_marks = models.CharField(
        max_length=200
    )
    ssc_percentage = models.CharField(
        max_length=200
    )
    ssc_passout_year = models.CharField(
        max_length=200
    )
    ug_course =  models.CharField(
        max_length=10,
        choices=UGCOURSE,
        default=BCA
    )
    ug_marks = models.CharField(
        max_length=200
    )
    ug_percentage = models.CharField(
        max_length=200
    )
    ug_passout_year = models.CharField(
        max_length=200
    )
    exprience = models.CharField(
        max_length=200
    )
    current_pg_sem = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    def __str__(self):

        return str(self.student.first_name)

class PGSem(BaseModel):
    """
    This model User holds the
    information about the registering User
    """
    academic  = models.ForeignKey(AcademicDetail, on_delete=models.CASCADE)
    sem_number = models.CharField(
        max_length=200
        )
    marks = models.CharField(
        max_length=200
        )
    percentage = models.CharField(
        max_length=200

    )
    no_of_backlogs = models.CharField(
        max_length=200
    )


class CampusDrive(BaseModel):
    MALE = 'M'
    FEMALE = 'F'
    ANY = 'Any'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (ANY, 'Any')
    )
    company_name = models.CharField(
        max_length=200
    )
    company_description = models.CharField(
        max_length=200
    )
    drive_on = models.DateTimeField(default=timezone.now())

    throughout = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    no_of_gap =  models.CharField(
        max_length=200,
        blank=True
    )
    batch_year =  models.CharField(
        max_length=200
    )
    gender =  models.CharField(
        max_length=10,
        choices=GENDER,
        default=ANY
    )
    exprience =  models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

class SpecialCriteria(BaseModel):
    SSC = 'SSC'
    HSC = 'HSC'
    UG = 'UG'
    PG = 'PG'
    OTHER = 'Other'
    COURSE = (
        (SSC, 'SSC'),
        (HSC, 'HSC'),
        (UG, 'UG'),
        (PG, 'PG'),
        (OTHER, 'Other')
    )
    criteria_for = models.CharField(
        max_length=10,
        choices=COURSE,
        default=UG
    )
    percentage = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    no_of_backlogs = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

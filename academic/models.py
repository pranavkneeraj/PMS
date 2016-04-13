"""This module is defined for user Academic detail"""
from django.contrib.postgres.fields import ArrayField
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
    hsc_marks = models.IntegerField()
    hsc_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    hsc_passout_year = models.IntegerField()
    ssc_marks = models.IntegerField()
    ssc_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    ssc_passout_year = models.IntegerField()
    ug_course =  models.CharField(
        max_length=10,
        choices=UGCOURSE,
        default=BCA
    )
    ug_marks = models.CharField(
        max_length=200
    )
    ug_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    ug_passout_year = models.CharField(
        max_length=200
    )
    exprience = models.IntegerField()
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
    sem_number = models.IntegerField()
    marks = models.IntegerField()
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    no_of_backlogs = models.IntegerField()
    class Meta:
        unique_together = ('academic', 'sem_number')

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

    throughout = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    no_of_gap =  models.IntegerField(
        blank=True,
        null=True
    )
    batch_year =  ArrayField(
        models.IntegerField(),
        blank=True,
        null=True
    )
    gender =  models.CharField(
        max_length=10,
        choices=GENDER,
        default=ANY
    )
    exprience =  models.IntegerField(
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
    campus_drive = models.ForeignKey(CampusDrive)
    criteria_for = models.CharField(
        max_length=10,
        choices=COURSE,
        default=UG
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    no_of_backlogs = models.IntegerField(
        blank=True,
        null=True
    )


class Interested(CreatedFlagModelMixin,
                         UpdatedFlagModelMixin,
                         DeletedFlagModelMixin,
                         models.Model):
    student = models.ForeignKey(User)
    is_interested = models.BooleanField(default=False)
    campus_drive = models.ForeignKey(CampusDrive)

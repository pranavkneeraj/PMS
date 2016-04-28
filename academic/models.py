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
    This model AcademicDetail holds the
    information about the academic details of the student
    """
    BCA = 'bca'
    BCS = 'Bsc(Computer Science)'
    BE = 'be',
    OTHER = 'other'
    UGCOURSE = (
        (BCS, 'Bsc(Computer Science)'),
        (BCA, 'BCA'),
        (BE, 'BE'),
        (OTHER, 'Other')
    )
    MCA = 'MCA'
    MCS = 'MSc(Computer Science)'
    OTHER = 'other'
    PGCOURSE = (
        (MCA, 'MCA'),
        (MCS, 'MSc(Computer Science)'),
        (OTHER, 'Other')
    )
    student = models.OneToOneField(
                User,
                on_delete=models.CASCADE,
                primary_key=True,
    )
    hsc_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    hsc_passout_year = models.IntegerField()
    ssc_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    ssc_passout_year = models.IntegerField()
    ug_course =  models.CharField(
        max_length=100,
        choices=UGCOURSE,
        blank=True,
        null=True
    )
    ug_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    ug_passout_year = models.CharField(
        max_length=200,
        blank=True
    )

    pg_course = models.CharField(
        max_length=20,
        choices=PGCOURSE,
        blank=True,
        null=True
    )
    pg_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    pg_passout_year = models.IntegerField(
        blank=True,
        null=True
    )
    # current_pg_sem = models.CharField(
    #     max_length=200,
    #     blank=True,
    #     null=True
    # )

    no_of_backlogs = models.IntegerField(default=0)

    no_of_gap = models.IntegerField(default=0)

    exprience = models.IntegerField(default=0)

    def __str__(self):
        return str(self.student.first_name)

# class PGSem(BaseModel):
#     """
#     This model User holds the
#     information about the registering User
#     """
#     academic  = models.ForeignKey(AcademicDetail, on_delete=models.CASCADE)
#     sem_number = models.IntegerField()
#     marks = models.IntegerField()
#     percentage = models.DecimalField(
#         max_digits=5,
#         decimal_places=2
#     )
#     no_of_backlogs = models.IntegerField()
#     class Meta:
#         unique_together = ('academic', 'sem_number')

class CampusDrive(BaseModel):

    POOL = 'pool'
    CAMPUS = 'campus'
    RECRUITMENT_TYPE = (
        (POOL, "Pool"),
        (CAMPUS, "Campus"),
    )
    NO_CRITERIA = "none"
    GENERAL_CRITERIA = "general"
    SPECIAL_CRITERIA = "special"
    BOTH = "both"
    CRITERIA_TYPE = (
        (NO_CRITERIA , "No Criteria"),
        (GENERAL_CRITERIA, "General Criteria"),
        (SPECIAL_CRITERIA, "Special Criteria"),
        (BOTH, "Both"),
    )
    company_name = models.CharField(
        max_length=200
    )
    company_description = models.CharField(
        max_length=1000
    )
    drive_on = models.DateTimeField(default=timezone.now())
    recruitment_type = models.CharField(
        max_length=10,
        choices=RECRUITMENT_TYPE,
        default=CAMPUS
    )
    course_list = ArrayField(
        models.CharField(max_length=200),
        blank=True,
        null=True
    )
    batch_year =  ArrayField(
        models.IntegerField(),
        blank=True,
        null=True
    )
    criteria_type = models.CharField(
        max_length=20,
        choices=CRITERIA_TYPE,
        default=NO_CRITERIA
    )

class Criteria(CreatedFlagModelMixin,
                     UpdatedFlagModelMixin,
                     DeletedFlagModelMixin):
    MALE = 'M'
    FEMALE = 'F'
    ANY = 'Any'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (ANY, 'Any')
    )
    campus_drive = models.OneToOneField(
        'CampusDrive',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    throughout = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )
    no_of_gap =  models.IntegerField(
        default=0
    )
    gender =  models.CharField(
        max_length=10,
        choices=GENDER,
        default=ANY
    )
    no_of_backlogs = models.IntegerField(default=0)
    exprience =  models.IntegerField(
        default=0
    )

class SpecialCriteria(BaseModel):
    SSC = 'ssc'
    HSC = 'ssc'
    UG = 'ug'
    PG = 'pg'
    OTHER = 'other'
    COURSE = (
        (SSC, 'SSC'),
        (HSC, 'HSC'),
        (UG, 'UG'),
        (PG, 'PG'),
        (OTHER, 'Other')
    )
    campus_drive = models.ForeignKey('CampusDrive', on_delete=models.CASCADE)
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

class Interested(CreatedFlagModelMixin,
                         UpdatedFlagModelMixin,
                         DeletedFlagModelMixin,
                         models.Model):
    student = models.ForeignKey(User)
    campus_drive = models.ForeignKey('CampusDrive', on_delete=models.CASCADE)
    is_interested = models.BooleanField(default=False)

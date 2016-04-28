""" This module is used to include the urls with
respect to their functionality """

from django.conf.urls import url, include
from academic import views
from rest_framework import routers
print("Hello..............")
router = routers.DefaultRouter()  # pylint: disable=C0103
router.register(r'detail', views.AcademicDetailViewSet)
router.register(r'campusdrive', views.CampusDriveViewSet)
#router.register(r'pgsem', views.PGSemViewSet, base_name='academic-pgsem')
router.register(r'special_criteria', views.SpecialCriteriaViewSet)
router.register(r'criteria', views.CriteriaViewSet)

router.register(r'interested', views.InterestedViewSet, base_name="interested")

urlpatterns = [
    url(r'', include(router.urls)),
]

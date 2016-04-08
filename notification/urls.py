""" This module is used to include the urls with
respect to their functionality """

from django.conf.urls import url, include
from notification import views
from rest_framework import routers
router = routers.DefaultRouter()  # pylint: disable=C0103
router.register(r'', views.NotificationViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]

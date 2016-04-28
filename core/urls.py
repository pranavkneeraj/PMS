from django.conf.urls import include, patterns, url
from core.views import IndexView
from user import urls as user_urls
from user.views import AuthUserViewSet, RegistrationViewSet, InterestedForCampusDrivetViewSet, JoiningConfirmationViewSet, PlacementNotificationViewSet
from academic import urls as academic_urls
from notification import urls as notification_urls
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),url(r'^admin/', admin.site.urls),
    url(r'^user/auth/$', AuthUserViewSet.as_view()),
    url(r'api/academic/', include(academic_urls)),
    url(r'api/user/', include(user_urls)),
    url(r'api/notification', include(notification_urls)),
    url(r'^user/registration/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', RegistrationViewSet.as_view()),
    url(r'^student/placement/campusdrive_interest/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', InterestedForCampusDrivetViewSet.as_view()),
    url(r'^student/placement/joinning_confirmation/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', JoiningConfirmationViewSet.as_view()),
    url(r'^student/placement/notification/$', PlacementNotificationViewSet.as_view()),

    url(r'^user/registration/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', RegistrationViewSet.as_view()),

    url(r'', IndexView.as_view(), name='index'),
]

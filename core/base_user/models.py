"""
Module for AbstractEmailUser
"""
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
#from django.contrib.auth.models import Group
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    """
    This allows adding new users with
    ```email``` and ```password`` field
    """

    def create_user(self, email, password=None, **kwargs):
        """
        Create a user
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)  # pylint: disable = E1101
        user.set_password(password)
        user.save(using=self._db)  # pylint: disable = E1101
        return user

    def create_superuser(self, **kwargs):
        """
        Create superuser
        """
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)  # pylint: disable = E1101
        return user


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin):

    """
    An abstract django model that uses email to identify user
    """
    first_name = models.CharField(
        _('First Name'), max_length=30, blank=True, null=True, default=None)
    last_name = models.CharField(
        _('Last Name'), max_length=30, blank=True, null=True, default=None)
    email = models.EmailField(
        _('Email'), max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('Staff Status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as '
        'active.  Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
        ordering = ['email', ]

    def get_full_name(self):
        fullname = ("%s %s" % (self.first_name, self.last_name)).strip()
        return fullname if fullname else self.email

    def get_short_name(self):
        return self.first_name if self.first_name else self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
'''
class ProxyGroup(Group):

        """
    proxy group model so that it can be imported whereever we want to
    register group admin
    """
        class Meta:
            proxy = True
            verbose_name = _('Group')
            verbose_name_plural = _('Groups')
'''

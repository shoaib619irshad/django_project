from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    ADMIN = 'admin'
    MANAGER = 'manager'
    EMPLOYEE = 'employee'
    ROLE = (
       (ADMIN, _('admin')),
       (MANAGER, _('manager')),
       (EMPLOYEE, _('employee')),
   )
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(max_length=10, choices=ROLE, default=EMPLOYEE)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
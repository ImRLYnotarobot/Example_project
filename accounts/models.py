from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

USERNAME_REGEX = r'^[a-zA-Z0-9.-_]*$'


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **perms):
        if not email:
            raise ValueError('!EMAIL')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **perms
        )
        user.set_password(password)
        user.save()
        # user.save(using=self._db)
        return user

    def create_superuser(self, *args, **perms):
        perms.setdefault('is_admin', True)
        perms.setdefault('is_staff', True)

        return self.create_user(*args, **perms)


class User(AbstractBaseUser):

    objects = UserManager()

    username = models.CharField(
        max_length=255,
        validators=[RegexValidator(
            regex=USERNAME_REGEX,
            message='username must contain ascii letters, numbers and (-_.)',
            code='invalid_username'
        )],
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email'
    )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return '{}: [{}]'.format(self.username, self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

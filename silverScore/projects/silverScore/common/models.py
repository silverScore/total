from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.

# phone, created_at 추가.
class ExtendedUserForm(AbstractUser):  # -> config/settings.py 에 AUTH_USER_MODEL = 'common.ExtendedUserForm' 로서 추가. why? : AbstractUser 로서 사용하므로
    phone_regex = RegexValidator(regex=r'^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.") # 정규식 011-123-4567 혹은 010-1234-5678 기준
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True, verbose_name='phone') # 010-1234-5678 기준 갯수
    created_at = models.DateTimeField() # For DateTimeField: default=timezone.now - from django.utils.timezone.now() # ref : https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.DateField.auto_now_add

    class Meta:
        abstract = True
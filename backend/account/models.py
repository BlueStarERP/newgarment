from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from mr.models import *
# from production.models import *
# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_mgr = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)
    is_qc = models.BooleanField(default=False)
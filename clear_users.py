import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_users.settings")

import django
django.setup()

from django.contrib.auth.models import User
from basic_app.models import UserInfo

User.objects.all().delete()
UserInfo.objects.all().delete()

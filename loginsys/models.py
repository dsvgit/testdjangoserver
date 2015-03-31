#Наследвание от модели User и добавление к ней необходимых полей
#Описано тут: http://djbook.ru/examples/6/

from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUser(User):

	 flag = models.CharField(max_length = 100, default='Yes')

	 objects = UserManager()

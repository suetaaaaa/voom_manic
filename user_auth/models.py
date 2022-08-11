from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class VoomUser(User):

	def __str__(self):
		return self.username
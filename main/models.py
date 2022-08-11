from django.db import models


class Skills(models.Model):
	title = 'Навыки'
	skills = models.TextField()

	class Meta:
		verbose_name_plural = 'Навыки'

	def __str__(self):
		return self.title
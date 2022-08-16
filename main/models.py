from django.db import models
from django.urls import reverse


# main.html

class MainPhoto(models.Model):
	main_photo_title = 'Фото на главной странице'
	main_photo = models.ImageField(upload_to='main/main_photo/')

	class Meta:
		verbose_name = 'Фото на главной странице'
		verbose_name_plural = 'Фото на главной странице'

	def __str__(self):
		return self.main_photo_title


class Skills(models.Model):
	skill = models.TextField()

	class Meta:
		verbose_name = 'Навык'
		verbose_name_plural = 'Навыки'

	def __str__(self):
		return self.skill


class CertImages(models.Model):
	cert_name = models.TextField()
	cert_image = models.ImageField(upload_to='main/certificates/')

	class Meta:
		verbose_name = 'Сертификат'
		verbose_name_plural = 'Сертификаты'

	def __str__(self):
		return self.cert_name


class Services(models.Model):
	title = models.CharField(max_length=255, default='')
	text = models.TextField(default='')
	button_text = models.CharField(max_length=50, default='')
	slug = models.SlugField(max_length=100, default='')
	service_image = models.ImageField(upload_to='main/services/')

	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'
	
	def __str__(self):
		return self.title


class PortfolioImages(models.Model):
	title = 'Фото для портфолио'
	portfolio_photo = models.ImageField(upload_to='main/portfolio/')

	class Meta:
		verbose_name = 'Фото для портфолио'
		verbose_name_plural = 'Фото для портфолио'
	
	def __str__(self):
		return self.title


class PortfolioText(models.Model):
	text = models.TextField()

	class Meta:
		verbose_name = 'Текст для портфолио'
		verbose_name_plural = 'Текст для портфолио'
	
	def __str__(self):
		return self.text

# main.html


# training.html

class TrainingStudentWork(models.Model):
	title = 'Фото работ учеников'
	student_work_photo = models.ImageField(upload_to='training/student_work_photo/')

	class Meta:
		verbose_name = 'Фото работ учеников'
		verbose_name_plural = 'Фото работ учеников'
	
	def __str__(self):
		return self.title


class TrainingText(models.Model):
	text = models.TextField()

	class Meta:
		verbose_name = 'Текст для страницы обучения'
		verbose_name_plural = 'Текст для страницы обучения'
	
	def __str__(self):
		return self.text


class TrainingCourses(models.Model):
	title = models.CharField(max_length=255, default='')
	text = models.TextField()
	slug = models.SlugField(max_length=100, default='')
	
	class Meta:
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'
	
	def __str__(self):
		return self.title


# training.html
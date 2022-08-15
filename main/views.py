from django.shortcuts import render

from main.models import Skills, CertImages, MainPhoto, Services, PortfolioImages, PortfolioText


def index(request):
	skills_list = Skills.objects.all()
	cert_images_list = CertImages.objects.all()
	main_photo_list = MainPhoto.objects.all()
	services_list = Services.objects.all()
	portfolio_images_list = PortfolioImages.objects.all()
	portfolio_text_list = PortfolioText.objects.all()

	data_index = {
		'title': 'VOOM.MANIC',
		'skills_list': skills_list,
		'cert_images_list': cert_images_list,
		'main_photo_list': main_photo_list,
		'services_list': services_list,
		'portfolio_images_list': portfolio_images_list,
		'portfolio_text_list': portfolio_text_list
	}

	return render(request, 'main/index.html', data_index)


def training(request):
	data_training = {
		'title': 'Обучение оффлайн'
	}

	return render(request, 'main/training.html', data_training)


def studio(request):
	data_studio = {
		'title': 'Студия VOOM.MANIC'
	}

	return render(request, 'main/studio.html', data_studio)


def manicure_basic_course(request):
	data_manicure_basic_course = {
		'title': 'Базовый курс по маникюру'
	}

	return render(request, 'main/manicure_basic_course.html', data_manicure_basic_course)


def nail_extension_course(request):
	data_nail_extension_course = {
		'title': 'Курс по наращиванию ногтей'
	}

	return render(request, 'main/nail_extension_course.html', data_nail_extension_course)
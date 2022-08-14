from django.shortcuts import render

from main.models import Skills


def index(request):

	skills_list = Skills.objects.all()

	data_index = {
		'title': 'VOOM.MANIC',
		'skills_list': skills_list
	}

	return render(request, 'main/index.html', data_index)


def training(request):

	data_training = {
		'title': 'Обучение оффлайн'
	}

	return render(request, 'main/training.html', data_training)
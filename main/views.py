from django.shortcuts import render


def index(request):

	data_index = {
		'title': 'VOOM.MANIC'
	}

	return render(request, 'main/index.html', data_index)


def training(request):

	data_training = {
		'title': 'Обучение оффлайн'
	}

	return render(request, 'main/training.html', data_training)
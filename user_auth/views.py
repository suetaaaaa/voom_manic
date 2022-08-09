from django.shortcuts import render


def login(request):

	data_login = {
		'title': 'Войти'
	}

	return render(request, 'user_auth/login.html', data_login)
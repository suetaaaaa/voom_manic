from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('studio', views.studio, name='studio'),
	path('training', views.training, name='training'),
	path('training/manicure_basic_course', views.manicure_basic_course, name='manicure_basic_course'),
	path('training/nail_extension_course', views.nail_extension_course, name='nail_extension_course'),
]

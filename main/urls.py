from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('studio/', views.studio, name='studio'),

	# path('training/', views.training, name='training'),
	path('training/<slug:slug>/', views.CoursesDetailView.as_view(), name='course_detail'),
	path('training/', views.CoursesListView.as_view(), name='training_list'),

	path('training/manicure_basic_course', views.manicure_basic_course, name='manicure_basic_course'),
	path('training/nail_extension_course', views.nail_extension_course, name='nail_extension_course'),
]

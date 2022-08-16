from django.urls import path
from . import views

urlpatterns = [
	path('', views.IndexListView.as_view(), name='home'),
	path('studio/', views.studio, name='studio'),
	path('training/', views.CoursesListView.as_view(), name='training_list'),
	path('training/<slug:slug>/', views.CoursesDetailView.as_view(), name='course_detail'),
]

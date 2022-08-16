from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Skills, CertImages, MainPhoto, Services, PortfolioImages, PortfolioText, TrainingCourses, TrainingStudentWork, TrainingText


class IndexListView(ListView):
	model = MainPhoto
	template_name = 'main/index.html'
	context_object_name = 'main_photo_list'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['skills_list'] = Skills.objects.all()
		context['cert_images_list'] = CertImages.objects.all()
		context['services_list'] = Services.objects.all()
		context['portfolio_images_list'] = PortfolioImages.objects.all()
		context['portfolio_text_list'] = PortfolioText.objects.all()

		return context


class CoursesListView(ListView):
	model = TrainingCourses
	template_name = 'main/training_list.html'
	context_object_name = 'courses'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['photos'] = TrainingStudentWork.objects.all()
		context['texts'] = TrainingText.objects.all()
		
		return context


class CoursesDetailView(DetailView):
	model = TrainingCourses
	template_name = 'main/course_detail.html'
	context_object_name = 'course'


def studio(request):
	data_studio = {
		'title': 'Студия VOOM.MANIC'
	}

	return render(request, 'main/studio.html', data_studio)
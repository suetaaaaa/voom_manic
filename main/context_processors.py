from main.models import TrainingCourses


def add_variables_to_context(request):

    return {
        'nav_courses': TrainingCourses.objects.all()
    }

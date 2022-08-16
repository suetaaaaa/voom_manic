from django.contrib import admin

from . import models


@admin.register(models.Services)
class ServicesAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']


@admin.register(models.TrainingCourses)
class TrainingCoursesAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Skills)
admin.site.register(models.CertImages)
admin.site.register(models.MainPhoto)
admin.site.register(models.PortfolioImages)
admin.site.register(models.PortfolioText)

admin.site.register(models.TrainingStudentWork)
admin.site.register(models.TrainingText)
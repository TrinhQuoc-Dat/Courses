from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from courses.models import Category, Courses, Lesson, Tag, User
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.urls import path

class LessonForm(forms.BaseForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson,
        fields = '__all__'


class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'created_date', 'courses_id']
    search_fields = ['subject', 'content']
    list_filter = ['id', 'created_date', 'subject']
    readonly_fields = ['image_view']
    form = LessonForm

    def image_view(self, lesson):
        if lesson:
            return mark_safe(f"<img src='/static/{lesson.image.name}' width='120'/>")

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }
        js = {
            'js': ('/static/js/script.js', )
        }


class CourseAppAdminSite(admin.AdminSite):
    site_header = "Khóa học lập trình Pyhthon"

    def get_urls(self):
         return [
             path('courses-stats/', self.stats_view)
         ] + super().get_urls()

    def stats_view(self, request):
        count = Courses.objects.filter(active=True).count()
        stats = Courses.objects \
            .annotate(lesson_count=Count('lesson__id')) \
            .values('id', 'subject', 'lesson_count')
        return TemplateResponse(request,'admin/course-stats.html', {
                                    'course_count': count,
                                    'course_stats': stats
                                })



admin_site = CourseAppAdminSite(name='Admin site');


admin_site.register(Category)
admin_site.register(Courses)
admin_site.register(Lesson)
admin_site.register(Tag)
admin_site.register(User)

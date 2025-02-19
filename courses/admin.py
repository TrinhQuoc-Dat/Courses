from django.contrib import admin
from django.utils.safestring import mark_safe

from courses.models import Category, Courses, Lesson, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms



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




admin.site.register(Category)
admin.site.register(Courses)
admin.site.register(Lesson)
admin.site.register(Tag)

from django.urls import path, include
from courses import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('categorys', views.CategoryViewSet, basename='categorys')
router.register('courses', views.CourseViewSet, basename='courses')
router.register('lessons', views.LessonViewSet, basename='lessons')
router.register('users', views.UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls))
]

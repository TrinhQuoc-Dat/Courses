from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Courses, Category, Tag, Lesson, User


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class BaseSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    image = SerializerMethodField(source='image')

    def get_image(self, courses):
        request = self.context.get('request')
        if courses.image:
            if request:
                return request.build_absolute_uri('/static/%s' % courses.image.name)
            return '/static/%s' % courses.image.name


class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(BaseSerializer):
    image = SerializerMethodField(source='image')

    class Meta:
        model = Courses
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user







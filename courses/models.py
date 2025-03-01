from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    avatar = CloudinaryField('avatar')


class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True,
        ordering = ['-id']


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Courses(BaseModel):
    subject = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'category')

    def __str__(self):
        return self.subject


class Lesson(BaseModel):
    subject = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='lesson/%Y/%m/', null=True, blank=True)
    content = RichTextField(null=True)

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'course')

    def __str__(self):
        return self.subject


class Comment(BaseModel):
    content = models.TextField(null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name


class Interaction(BaseModel):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Like(Interaction):
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'lesson')


class Comment(Interaction):
    content = models.TextField(max_length=255, null=False)




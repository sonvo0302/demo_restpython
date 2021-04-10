from rest_framework import serializers
from .models import Course


class GetAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id',
                  'title',
                  'price',
                  'description',
                  'published',)

class CourseSerializer(serializers.ModelSerializer):
    title1=serializers.CharField(max_length=50)
    price1=serializers.IntegerField()
    description1=serializers.CharField(max_length=200)
    published1=serializers.BooleanField(default=False)

    class Meta:
        model = Course
        fields = ('id',
                  'title1',
                  'price1',
                  'description1',
                  'published1',)
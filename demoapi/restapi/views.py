from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import GetAllCourseSerializer,CourseSerializer
from .models import Course
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
# Create your views here.

class getCourse(APIView):
    def get(self,request):
        list_course = Course.objects.all()
        p=GetAllCourseSerializer(list_course,many=True)
        return JsonResponse(data=p.data,safe=False)
    def post(self,request):
        # mydata=CourseSerializer(data=request.data)
        # if not mydata.is_valid():
        #     return JsonResponse('Error',status=status.HTTP_400_BAD_REQUEST)
        # title=mydata.data['title1']
        # price=mydata.data['price1']
        # description=mydata.data['description1']
        # published=mydata.data['published1']
        # cs=Course.objects.create(title=title,price=price,description=description,published=published)
        # return JsonResponse(data=cs.id,status=status.HTTP_201_CREATED)
        # return JsonResponse(data=cs.data,status=status.HTTP_400_BAD_REQUEST)
        course_data=JSONParser().parse(request)
        course_serializer=GetAllCourseSerializer(data=course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse(data=course_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(data=course_serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        course_data=Course.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(course_data[0])},status=status.HTTP_204_NO_CONTENT)

class getCourseDetail(APIView):
    def get(self,request,course_id):
        try:
            course = Course.objects.get(pk=course_id)
        except course.DoesNotExists:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        course_serializer = GetAllCourseSerializer(course)
        return JsonResponse(data=course_serializer.data,status=status.HTTP_200_OK)
    def put(self,request,course_id):
        try:
            course = Course.objects.get(pk=course_id)
        except course.DoesNotExists:
            return JsonResponse({'message': 'The course does not exist'}, status=status.HTTP_404_NOT_FOUND)
        course_data=JSONParser().parse(request)
        course_serializer=GetAllCourseSerializer(course,data=course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse(data=course_serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(data=course_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,course_id):
        try:
            course = Course.objects.get(pk=course_id)
        except course.DoesNotExists:
            return JsonResponse({'message': 'The course does not exist'}, status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return JsonResponse({'message': 'Course was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)
#
#     if request.method == 'GET':
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
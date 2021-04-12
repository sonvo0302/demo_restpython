from django.urls import path
from django.conf.urls import url
from .views import getCourse,getCourseDetail,getCourse_Published

urlpatterns = [
    url(r'^api/course$',getCourse.as_view()),
    url(r'^api/course/(?P<course_id>[0-9]+)/$', getCourseDetail.as_view()),
    url(r'^api/courses/published$', getCourse_Published.as_view(),name='getPublishedCourse')
]
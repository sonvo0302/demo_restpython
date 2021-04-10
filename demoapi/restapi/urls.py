from django.urls import path
from django.conf.urls import url
from .views import getCourse,getCourseDetail

urlpatterns = [
    url(r'^api/course$',getCourse.as_view()),
    url(r'^api/course/(?P<course_id>[0-9]+)/$', getCourseDetail.as_view()),
    # url(r'^api/tutorials/published$', tutorial_list_published)
]
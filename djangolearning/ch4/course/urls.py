
from django.urls import path
from course.views import coursename
urlpatterns = [
    path('dj/',coursename,name='course-name')
]
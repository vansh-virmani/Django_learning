from django.urls import path,include
from course.views import learn_django,learn_python
urlpatterns = [
 
    path('dj/',learn_django,name='learn_djagno'),
     path('pj/',learn_python,name='learn_python')
    
]
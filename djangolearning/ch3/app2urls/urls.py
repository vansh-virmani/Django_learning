from django.urls import path,include
from app2urls import views
## path(route, view, kwargs, name) kwargs=status:ok
urlpatterns = [
  
    path('structure/',views.learn,name='structure'), #/course/structure
    path('about/',views.learn,{'status':'ok'},name='about') #/course/about
]

from django.urls import path,include
from app1urls import views
## path(route, view, kwargs, name) kwargs=status:ok
urlpatterns = [
  
    path('home/',views.learn,name='home'),
    path('about/',views.learn,{'status':'ok'},name='about')
]

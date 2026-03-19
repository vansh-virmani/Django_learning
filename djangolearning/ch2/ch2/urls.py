"""
URL configuration for ch2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from app1 import views
# from app2 import views error
# from app1 import views as v1
# from app2 import views as v2

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',v1.home,name='home'),
#     path('function1/', v1.fn1,name='function1'),
#     path('function2/',v2.fn2,name='function2')
# ]
#or
from app1.views import home,fn1
from app2.views import fn2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('function1/', fn1,name='function1'),
    path('function2/',fn2,name='function2')
]

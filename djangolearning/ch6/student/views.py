from django.shortcuts import render
from student.models import Profile
# Create your views here.
def all_data(req):
    student=Profile.objects.all()

    return render(req,'student/all.html',{'students': student})


def single_data(req):
    student=Profile.objects.get(name='Vansh')

    return render(req,'student/single.html',{'students': student})
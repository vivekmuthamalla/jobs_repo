from django.shortcuts import render
from testapp.models import hydjobs,knrjobs,ngpjobs
# Create your views here.
def homepage_view(request):
    return render(request,"testapp/index.html")

def hydjobs_view(request):
    jobs_list = hydjobs.objects.all()
    my_dict ={"jobs_list":jobs_list}
    return render(request,"testapp/hydjobs.html",my_dict)

def knrjobs_view(request):
    jobs_list = knrjobs.objects.all()
    my_dict ={"jobs_list":jobs_list}
    return render(request,"testapp/knrjobs.html",my_dict)

def ngpjobs_view(request):
    jobs_list = ngpjobs.objects.all()
    my_dict ={"jobs_list":jobs_list}
    return render(request,"testapp/ngpjobs.html",my_dict)



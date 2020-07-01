from django.shortcuts import render, get_object_or_404
from core.models import Project, Courses, Publication

# Create your views here.
def index(request):
    objs = Project.objects.all()
    courses_objs = Courses.objects.all()
    pub_objs = Publication.objects.all()
    context = {
        'objs':objs,
        'courses_objs':courses_objs,
        'pub_objs':pub_objs
    }
    return render(request,'index.html',context)

def details(request,pk):
    obj = get_object_or_404(Project,id=pk)
    objs = Project.objects.all()
    context = {
        'obj':obj,
        'objs':objs
    }
    return render(request,'details.html',context)

def courses_details(request,pkk):
    obj = get_object_or_404(Courses,id=pkk)
    objs = Courses.objects.all()
    context = {
        'obj':obj,
        'objs':objs
    }
    return render(request,'courses_details.html',context)

def publications_details(request,pkkk):
    obj = get_object_or_404(Publication,id=pkkk)
    objs = Publication.objects.all()
    context = {
        'obj':obj,
        'objs':objs
    }
    return render(request,'publications_details.html',context)
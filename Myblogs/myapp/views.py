from django.shortcuts import render,redirect
from django.http import HttpResponse 
from myapp.models import Projects
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def programming(request):
    All_projects = Projects.objects.filter(type_of_project='Programming')
    Type_project = "Programming"
    return render(request, 'projects.html',{'Projects': All_projects,'Type_project':Type_project})

def aviation(request):
    All_projects = Projects.objects.filter(type_of_project='Aviation')
    Type_project = "Aviation"
    return render(request, 'projects.html',{'Projects': All_projects,'Type_project':Type_project})

def robotics(request):
    All_projects = Projects.objects.filter(type_of_project='Robotics')
    Type_project = "Robotics"
    return render(request, 'projects.html',{'Projects': All_projects,'Type_project':Type_project})

def technology(request):
    All_projects = Projects.objects.filter(type_of_project='Technology')
    Type_project = "Technology"
    return render(request, 'projects.html',{'Projects': All_projects,'Type_project':Type_project})

def analytics(request):
    All_projects = Projects.objects.filter(type_of_project='Analytics')
    Type_project = "Data analytics"
    return render(request, 'projects.html',{'Projects': All_projects,'Type_project':Type_project})

def others(request):
    All_projects = Projects.objects.filter(type_of_project='Others')
    Type_project = "Others"
    return render(request, 'projects.html',{'Projects': All_projects,'Type_project':Type_project})

def add_project(request):
    if request.method == 'POST':
        # Get data
        name_of_project = request.POST['name_of_project']
        file_upload = request.POST['file-upload']
        description = request.POST['description']
        type_of_project = request.POST['type_of_project']
        # Record data
        project = Projects.objects.create(
            name_of_project = name_of_project,
            image_url = file_upload,
            description = description,
            type_of_project = type_of_project,
        )
        project.save()
        messages.success(request, "Successfully record",extra_tags='green')
        # Change routh
        return redirect('/')
    else :
        return render(request, 'add_project.html')

def edit_project(request,project_id):
    if request.method == 'POST':
        # Get data
        project = Projects.objects.get(id=project_id)

        project.name_of_project = request.POST['name_of_project']
        project.file_upload = request.POST['file-upload']
        project.description = request.POST['description']
    
        project.save()
        messages.success(request, "Successfully updated",extra_tags='orange')
        # Change routh 
        return redirect('/')
    else :
        project = Projects.objects.get(id=project_id)
        return render(request, 'edit_project.html',{'project':project})

def delete_project(request,project_id):
        project = Projects.objects.get(id=project_id)
        project.delete()
        messages.success(request, "Successfully delete",extra_tags='red')          
        return redirect('/')




from django.shortcuts import render, HttpResponse, redirect
from .models import Index, Contact,Skills,Projects,People
# Create your views here.
def index1(request):
    Indexs=Index.objects.all()
    params={'Index':Indexs}
    return render(request, 'index1.html',params)
def about(request):
    Indexs=Index.objects.all()
    params={'Index':Indexs}
    return render(request, 'about.html',params)

def services(request):
    Project=Projects.objects.all()
    params={'Project':Project}
    return render(request, 'projects.html',params)

def skills(request):
    Skill=Skills.objects.all()
    params={'Skill':Skill}
    return render(request, 'skills.html',params)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        desc=request.POST.get('desc','')
        people=People(name=name, email=email, subject=subject, description=desc)
        people.save()
    Contacts=Contact.objects.all()
    params={'Contact':Contacts}
    return render(request, 'contact.html',params)


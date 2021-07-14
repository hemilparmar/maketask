from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from todo.models import Work
import datetime

# Create your views here.
def index(request):
    sno = None
    title = None
    desc = None
   
    values = {}
    if request.method == "POST":
        sno = request.POST.get('sno')
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        time = datetime.datetime.now().strftime("%H:%M:%S")
       
        
        work = Work(sno=sno, title=title, desc=desc, time=time)
        work.save()
        
    all = Work.objects.all()
    values = all.values()
        # print(values) 

    values = {
        "values":values
    }
        
    return render(request, "index.html", values)


def about(request):
    return render(request, "about.html")

def delete(req, sno):
    task = Work.objects.filter(sno=sno).first()
    task.delete()

    return redirect("/")

   

def update(request, sno):

    if request.method == "POST":
        
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        time = datetime.datetime.now().strftime("%H:%M:%S")
    
    
        task = Work.objects.filter(sno=sno).first()
        task.title = title
        task.desc = desc
        task.time = time
        task.save()

        return redirect("/")
        
    task = Work.objects.filter(sno=sno).first()
    val = {
        "task":task
    }
    
    return render(request, "update.html", val)






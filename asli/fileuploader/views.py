from django.shortcuts import render
from django.http import HttpResponse
from .models import pic
from .forms import picform


# Create your views here.
def index(request):
    form=picform()
    if request.method=='POST':
        form=picform(request.POST , request.FILES)
        if form.is_valid():
            #pic.objaects.creat(**form.cleaned_data)
            form.save()
    contex={
            "form":form
            }
    return render(request,'index.html',contex)


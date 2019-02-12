from django.shortcuts import render,redirect
from django.http import HttpResponse
from fileuploader.forms import picform
from fileuploader.models import pic
from PIL import Image
import random
import string
import sys
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Create your views here.
def Edit(request):
	if request.method=='POST':
		form=picform(request.POST , request.FILES)
		if (form.is_valid()) :
			global anghezi
			anghezi=pic.objects.create(**form.cleaned_data)
			global epic
			epic=anghezi.pic
			#anghezi.hvalu=random.randint(1,100)
			#c=randomString()+epic.url[-5:]
			#epic.name=c
			#anghezi.pic.url=c
			print(epic.name)			
			anghezi.save
			#form.save()
			#contex={"form":form}
		contex={"item":anghezi}
		return render(request,'edit.html',contex)
def show(request):
	global epic
	im = Image.open(epic.url[1:])
	return render(request,'show.html',{"im":epic})
def bw(request):
	global epic
	im = Image.open(epic.url[1:]) 
	im = im.convert('1')
	im.save(epic.url[1:])
	return redirect("/media/")
def rotate(request):
	global epic
	degree=request.POST['degree']
	im = Image.open(epic.url[1:])
	im = im.rotate(int(degree))
	im.save(epic.url[1:])
	return redirect("/media/")
def resize(request):
	try:
		global epic
		x=int(request.POST['x'])
		y=int(request.POST['y'])
		im = Image.open(epic.url[1:])
		im = im.resize((x,y))
	except ValueError:
		print("jjjjjjjjjjjjjjjjjjjj")
		return render(request,'error.html')
	else:
		im.save(epic.url[1:])
		return redirect("/media/")
def crop(request):
	try:
		global epic
		l=int(request.POST['l'])
		u=int(request.POST['u'])
		r=int(request.POST['r'])
		d=int(request.POST['d'])
		im = Image.open(epic.url[1:])
		im= im.crop((l,u,r,d)).save(epic.url[1:])
	except ValueError:
		return render(request,'error.html')
	except SystemError:
		return render(request,'error.html')
	else:
		return redirect("/media/")		

def share(request):
	global anghezi
	anghezi.shar=True
	anghezi.save()
	p=pic.objects.filter(shar=True).order_by("uploaded_at")
	print(p)
	return render(request,'share.html',{'p':p})

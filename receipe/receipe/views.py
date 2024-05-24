from django.shortcuts import render, redirect
from menu.models import Receipe
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def dishes(request):
    if request.method=='POST':
        receipe_name=request.POST.get('receipe_name')
        receipe_description=request.POST.get('receipe_description')
        receipe_image= request.FILES.get('receipe_image')
        
        s=Receipe(receipe_name=receipe_name, receipe_description=receipe_description,receipe_image=receipe_image)
        s.save()  
    return render(request, 'receipes.html')




def show(request):
    s=Receipe.objects.all()
    return render(request,'display.html',{'s':s})

@login_required(login_url='/login/')
def delete_recepie(request,id):
    q= Receipe.objects.get(id=id)
    q.delete()
    return redirect('/show/')

@login_required(login_url='/login/')
def update_receipe(request,id):
    q= Receipe.objects.get(id=id)
    if request.method == "POST":
        receipe_name=request.POST.get('receipe_name')
        receipe_description=request.POST.get('receipe_description')
        
        q.receipe_name=receipe_name
        q.receipe_description=receipe_description
        
        q.save()
        return redirect('/dishes/',{'q':q})
    context= {'receipe':q}
    return render(request , 'update.html',context)
        
        
        
def login_page(request):
   if request.method=='POST':
       username=request.POST.get('username')
       password= request.POST.get('password')
        
       if  not User.objects.filter(username=username).exists():
           messages.info(request, ' Invalid username ')
           return redirect('/login/')
       
       user= authenticate(username = username, password = password)
       
       if user is None:
           messages.error(request  , 'Invalid Credentials ')
           return redirect ('/login/')
       else:
           login(request,user)
           return redirect('/show/')
        
   return render(request , 'login.html')
        

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username=request.POST.get('username')
        password= request.POST.get('password')
        
        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request, 'username already taken')
            return redirect('/register/')
            
        
        user= User.objects.create(
            
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        user.set_password(password)
        user.save()
        messages.info(request, 'account created sucecssfully ! ')
        return redirect('/login/')
    return render(request, 'register.html')


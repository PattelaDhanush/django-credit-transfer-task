from django.shortcuts import render, redirect
from .models import Members, Tran
from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request,"main.html")
def Info(request):
    dests= Members.objects.all()
    return render(request,"view.html",{'dests':dests})    
    
def Transfer(request):
    a= request.POST['sender']
    dests= Members.objects.all()
    c= int(request.POST['send'])
  
    for dest in dests:
        if a == dest.email:
           
            global d
            d=c
            e=dest.credit
            #request.session.get('s',dest.name)
            global s
            s=dest.name
            
            break
    if c>e: 
        messages.info(request,"Entered Credits are Greater that Member Credits.Please enter credits correctly.")
        return redirect('Info')
    else:
        dest.credit-=c
        dest.save()
        return render(request,"view1.html",{'dests':dests, 'a':a})
def Transfer1(request):
    dests= Members.objects.all()
    b= request.POST['getter'] 
    for dest in dests:
        if b == dest.email:
            global r
            r= dest.name
            dest.credit+=d
            dest.save()
    tran_instance = Tran.objects.create(s_name=s, r_name=r, t_credit=d)
    tran_instance.save()
    return redirect('TranInfo')
        
def TranInfo(request):
    trans= Tran.objects.all()
    return render(request,"transfer.html",{'trans':trans})
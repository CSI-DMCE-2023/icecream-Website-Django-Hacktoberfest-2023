from django.shortcuts import redirect, render,HttpResponse
from datetime import datetime
from django.contrib import messages
from home.models import Contact, cartitem, login
from home.models import user,comments
from django.contrib.auth import authenticate
from django.db.models import Sum
rate_small={
    'Butterscotch':60,
'chocolate':70,
'strawberry':50,
'pistachio':99,
'vanilla':45,
'rasberry':120,
'matcha':75,
'moose':65,
'eggnog':120,
}
rate_sofy={
    'mango':55,
'vanilla':78,
'chocolate':85
}
rate_family={
    'vanilla':200,
'kasata':150,
'butterscotch':200,
'chocolate':199
}
# Create your views here.
def index(request):
    com=comments.objects.all()
    return render(request,"index.html",{'com':com})

    #return HttpResponse("this is homepage")

def about(request):
        if 'loggin' in request.session:
            return render(request,'services.html',{'login':request.session['loggin'],'name':request.session['name']})
        else:
            messages.error(request,'You need to login first to add items !!')
            return render(request,"services.html",{'login':False,'name':'UNKNOWN'})
    #return HttpResponse("this is about page")
def propayment(request):
    name=request.session['name']
    getitem=cartitem.objects.filter(username=name)
    total=getitem.aggregate(Sum('itemrate'))
    return render(request,'cart.html',{'login':request.session['loggin'],'name':request.session['name'],'item':getitem,'total':total})

def cartit(request):
    if request.method=='POST':
        dict_item={}
        if 'loggin' in request.session:
            print('shukl')
            name=request.session['name']
            if request.POST.get('ice') is not None:
                ice=request.POST.get('ice')
                dict_item[ice]=rate_small[ice]
            if request.POST.get('softy') is not None:
                softy=request.POST.get('softy')
                dict_item[softy]=rate_sofy[softy]
            if request.POST.get('familypack') is not None:
                familypack=request.POST.get('familypack')
                dict_item[familypack]=rate_family[familypack]
            queryset=cartitem.objects.filter(username=name)
            if queryset.count()>0:
                for item in queryset.values():
                    no_item=item['noofitem'] + len(dict_item)  
                for key,value in dict_item.items():
                    cartitem.objects.create(username=name,item=key,noofitem=no_item,itemrate=value)
            else:
                key_no=0
                for key,value in dict_item.items():
                    key_no+=1
                    cartitem.objects.create(username=name,item=key,noofitem=key_no,itemrate=value)
            item_fetch=cartitem.objects.filter(username=name).last()
            return render(request,'services.html',{'login':request.session['loggin'],'name':request.session['name'],'item':item_fetch})    
                
        else:
            messages.error(request,'You need to login first to add items !!')
            return render(request,'services.html',{'login':False,'name':'UNKNOWN'})        
    else:
        if 'loggin' in request.session:
            name=request.session['name']
            queryset=cartitem.objects.filter(username=name)
            if queryset.count()>0:
                item_fetch=cartitem.objects.filter(username=name).last()
                return render(request,'services.html',{'login':request.session['loggin'],'name':request.session['name'],'item':item_fetch})
            return render(request,'services.html',{'login':request.session['loggin'],'name':request.session['name']})
        else:
            messages.error(request,'You need to login first to add items !!')
            return render(request,"services.html",{'login':False,'name':'UNKNOWN'})
            
            

    #return HttpResponse("this is services page")

def contact(request):
    if request.method =="POST":
        name = request.POST.get("name")
        request.session["name"]=name
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        if 'loggin' in request.session:
            return render(request,"contact.html",{'login':request.session['loggin'],'name':request.session['name']})
        else:
            return render(request,"contact.html",{'login':False,'name':request.session['name']})
    else:
        if 'loggin' in request.session:
            return render(request,"contact.html",{'login':request.session['loggin'],'name':request.session['name']})
        else:
            return render(request,"contact.html",{'login':False,'name':'UNKNOWN'})
        
    #return HttpResponse("this is contact page")
    #making queries django
    #__startswith
def signupform(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        passw=request.POST.get('password')
        user.objects.create(fname=fname,lname=lname,username=uname,email=email,password=passw)
        return render(request,'index.html')

def loginform(request):
    if request.method=='POST':
        uname=request.POST.get('Username')
        pword=request.POST.get('password')
        if authenticate(request,username=uname,password=pword):
            user1=authenticate(request,username=uname,password=pword)
            login(request,user1)
            messages.success(request,uname+' has successfully logged in AS ADMIN')
            request.session['loggin']=True
            request.session['adminloggin']=True
            request.session['name']=uname
            return render(request,'index.html',{'login':request.session['loggin'],'name':request.session['name'],'admin':request.session['adminloggin']})     
        elif user.objects.filter(username=uname,password=pword).count()>0:
            login.objects.update_or_create(username=uname)
            messages.success(request,uname+' has successfully logged in')
            request.session['loggin']=True
            request.session['adminloggin']=False
            request.session['name']=uname
            return render(request,'index.html',{'login':request.session['loggin'],'name':request.session['name'],'admin':request.session['adminloggin']}) 
        else:
            messages.error(request,'Something went wrong')
            return render(request,'index.html') 
    else:
        return render(request,'index.html') 
    
def logout(request):
    print(request.session.values())
    if 'name' in request.session:
        del request.session['name']
        del request.session['loggin']
        messages.error(request,'you have been successfully logged out!!!')
        return render(request,'index.html')
    else:
        return render(request,'index.html')
    
def comment(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('username')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        comment=request.POST.get('com')
        gender=request.POST.get('gender')
        comments.objects.create(fname=fname,lname=lname,username=uname,city=city,state=state,zip=zip,gender=gender,comments=comment)
        messages.success(request,'Your comments has been added !!!')
        return redirect(request.META['HTTP_REFERER'])
    else:
        if 'loggin' in request.session:
            return render(request,"index.html",{'login':request.session['loggin'],'name':request.session['name']})
        else:
            return render(request,"index.html",{'login':False,'name':request.session['name']})
        
def deleteitem(request,id):
    if request.method=='POST':
        item=cartitem(id=id)
        item.delete()
        messages.success(request,'Item has been deleted successfully!!')
        name=request.session['name']
        getitem=cartitem.objects.filter(username=name)
        total=getitem.aggregate(Sum('itemrate'))
        return render(request,'cart.html',{'login':request.session['loggin'],'name':request.session['name'],'item':getitem,'total':total})
    else:
        name=request.session['name']
        getitem=cartitem.objects.filter(username=name)
        total=getitem.aggregate(Sum('itemrate'))
        return render(request,'cart.html',{'login':request.session['loggin'],'name':request.session['name'],'item':getitem,'total':total})
 
def payment(request):
    request.session.set_expiry(20)
    return render(request,'payment.html',{'login':request.session['loggin'],'name':request.session['name']})
   
def successpay(request):
    if request.method=='POST':
        if 'name' in request.session:
            name=request.session['name']
            messages.success(request,'Your order has been shift!!!')
            request.session.modified=True
            item=cartitem.objects.filter(username=name)
            item.delete()
            return render(request,'index.html',{'login':request.session['loggin'],'name':request.session['name']})
        
        else:
            messages.error(request,'session expired!!!!')
            return render(request,'index.html',{'login':False,'name':'UNKNOWN'})   
    else:
        if 'loggin' in request.session:
            return render(request,"index.html",{'login':request.session['loggin'],'name':request.session['name']})
        else:
            return render(request,"index.html",{'login':False,'name':request.session['name']})
                
def admin(request):
    user1=user.objects.all()
    cont=Contact.objects.all()
    com=comments.objects.all()
    return render(request,'admin.html',{'login':request.session['loggin'],'name':request.session['name'],'user':user1,'contact':cont,'com':com}) 

 
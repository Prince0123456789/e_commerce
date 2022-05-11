from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from shop1 import models
# Create your views here.
def index(request):
    
    return render(request, 'shop/index.html')
def userlogin(request):
    return render(request, 'login/login.html')
def signup(request):
    return render(request, 'signup/signup.html')

def saveuser(request):
    if request.method=='POST':
        uname=request.POST['username']
        passw=request.POST['password']
        uemail=request.POST['email']
        umob=request.POST['mob']
        print(uname+passw)
        myuser=models.user()
        myuser.username=uname
        myuser.password=passw
        myuser.email=uemail
        myuser.mob=umob
        myuser.save()
        print(myuser.username+myuser.password)
        messages.success(request, "Signup Successfull")
        return HttpResponseRedirect('/')
        #check credentials
    else:
        return HttpResponse("not found")
    
def loginvalidate(request):
    if request.method=='POST':
        lusername=request.POST['username']
        lpassword=request.POST['password']
        myuser=models.user.objects.get(username=lusername,password=lpassword)
                
        if myuser :
            d={}
            d['smsg']='Login Successfull'
            d['myuser']=lusername
            return render(request, 'shop/index.html', d)
            
        else:
            return HttpResponseRedirect('/')   
    else:
        return HttpResponse("Not Logged In")

def userlogout(request):
    return render(request, 'shop/index.html')

#PRODUCTS

def product(request):
    products=models.product.objects.all()
    d={}
    d['products']=products
    try:
        user=request.GET['user']
        muser=models.user.objects.get(username=user)
        if muser:
            d['myuser']=user
            return render(request, 'shop/product.html', d)
    except:
        return render(request, 'shop/product.html',d)

def loginproduct(request):
        user=request.GET['user']
        muser=models.user.objects.get(username=user)
        if muser:
            d={}
            d['myuser']=user
            return render(request, 'shop/product.html', d)
        else:
            return HttpResponse('Not login')
               
def cart(request):
    try:
        
        add_item=models.cart_items()
        user=request.GET['user']
        itm_name=request.GET['iname']
        itm_price=request.GET['price']
        add_item.item_name=itm_name
        add_item.item_price=float(itm_price)
        add_item.item_user=user
        add_item.save()
        return HttpResponse('Added to cart')
    except:
        return HttpResponse('Item Not added')
            
from django.shortcuts import render
from app1.models import *
from django.core.mail import send_mail
from django.views import View


def index(request):
    obj=Category.objects.all()
    obj2=Products.objects.all()
    return render(request,'index.html',{'u':obj,'x':obj2})

   


def Header(request):
    obj=Category.objects.all()
    return render(request,'header.html',{'u':obj})

def aboutus(request):
    obj=Category.objects.all()
    return render(request,'about.html',{'u':obj})

def contactus(request):
    obj=Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        data={
            'name':name,
            'email':email,
            'message':message,
        }
        message = '''
        New message: {}
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['name'],message,'',['suhailamufeedh@gmail.com'],fail_silently=False)
        

    return render(request,'contact.html',{'u':obj})   

def viewall(request):
    objcat=Category.objects.all()
    obj=Products.objects.all()
    return render(request,'products.html',{'x':obj,'u':objcat})

def viewproducts(request,id):
     objcat=Category.objects.all()
     obj=Products.objects.filter(id=id)
     obj2=Ingrediants.objects.filter(product=id)
     return render(request,'single-product.html',{'x':obj,'t':obj2,'u':objcat})

def ViewCategoryItem(request,id):
    cat=Category.objects.get(id=id)
    obj=Products.objects.filter(Category=cat)
    objcat=Category.objects.all()
    return render(request,'category.html',{'x':obj,'u':objcat,'v':cat})


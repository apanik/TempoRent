from django.shortcuts import render,redirect
from .models import *
from .urls import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def productview(request):
    obj = Product.objects.all()
    cat = Catagory.objects.all()
    return render(request,'products/products_new.html',{'obj': obj},{'cat':cat})

@login_required(login_url='login')
def addproducts(request):
    obj = Product.objects.all()
    form = ProductForm()
    if request.method =="POST":
        form =ProductForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
           messages.success(request,'Product added successfully')


           return redirect('addproducts')
        else:
            print(form.errors)
            form = ProductForm()

            return render(request,'products/addproducts.html',{'form':form})
    else:
        return render(request,'products/addproducts.html',{'form': form})







def productdetails(request,id):
    obj = Product.objects.get(pk=id)
    return render(request,'products/viewproducts.html',{'obj':obj})




def catagories(request):
    cat = Catagory.objects.all()

    return render(request,'Base/base.html',{'cat':cat})

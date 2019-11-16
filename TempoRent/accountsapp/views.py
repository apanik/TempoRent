from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse



def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 =request.POST['password1']

        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.warning(request,"username taken")
                return render(request,'accounts/userregistration.html')
            elif User.objects.filter(email =email).exists():
                messages.warning(request,"email taken")
                return render(request,'accounts/userregistration.html')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                messages.success(request,"user created successfull")
                print("user created")
                return redirect('register')
                return HttpResponse('')
        else:
            messages.warning(request,"Password not matched")
            print(messages)
            return render(request,'accounts/userregistration.html')

    else:
        return render(request,'accounts/userregistration.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password)

        if user is not None:
            auth.login(request,user)
            return redirect('addproducts')

        else:
            print("user not exist")
            return render(request,'accounts/userlogin.html')
    else:
        return render(request,'accounts/userlogin.html')

def logout(request):
    auth.logout(request)
    return redirect('login')



    


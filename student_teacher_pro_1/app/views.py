from django.shortcuts import redirect, render

from app.emailbackend import EmailBackend

from django.contrib.auth import authenticate , login, logout


# Create your views here.



def dologin(request):
    if request.method == "POST":
        user = EmailBackend.authenticate( username= request.POST.get('email') ,  password = request.POST.get('password')  )
        if user != None:
            login(request,user)
            user_type = user.user_type 
            if user_type == '1':
                return render(request , 'teacher/teacher_temp.html')
            elif user_type == "2":
                pass
            elif user_type=="3":
                pass
            else:
                return redirect('/login/')






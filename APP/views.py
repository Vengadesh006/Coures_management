from django.views import View
from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth import authenticate , login , logout
from Students.models import *
from Students.forms import *
from authentication.forms import User_form
from Coures.models import Coures
from django.contrib.auth.models import User

class Student_details(View) :

    def get(self , req) :

        data = {'forms' : Student_Forms() , 'userform' : User_form() }
        
        return render(req , 'Student.html' , data)

    def post(self , req) : 

        user_form = User_form(req.POST)
        
        student_form = Student_Forms(req.POST, req.FILES)

        if user_form.is_valid() and student_form.is_valid():
            #user----------------------------------------------------------
            user = user_form.save(commit=False)
            user.set_password(req.POST['password'])
            user.save()
            #user---------------------------------------------------------
            course_instance = Coures.objects.get(id = req.POST['selected_coures'])
            # Coures.objects.get(id = req.POST['selected_course'])
           
            fees = course_instance.fees
           
            gst  = course_instance.gst
           
            total = course_instance.final_fees
           
            rm_fees= fees - int(req.POST["paid_fees"])
           
            if req.POST["placement"] == "Yes":

                plm = True
            else:
                plm = False

            student_instance = Student(
                                users = user,
                                name        = req.POST["name"],
                                moblie      = req.POST["moblie"],
                                address     = req.POST["address"] ,                           
                                selected_coures_id = req.POST["selected_coures"],
                                placement    = plm,
                                paid_fees    = req.POST["paid_fees"],                              
                                fees         = fees,                              
                                gst          = gst, 
                                total_fees   = total,
                                remaining_fees = rm_fees,  
                                pictuer      = req.FILES["pictuer"]
                )
            student_instance.save()
            return redirect('/')

       
        else:
            print("user form error : ",user_form.errors)
            print("student form error : ",student_form.errors)
            courses = Coures.objects.all()

            data = {
                "uform": user_form,
                "sform": student_form,
                "coursedetails": courses
            }

            return redirect('/django/student/')


def LogOut(req) :

    logout(req)

    return redirect("/")


class UserLogin(View) :

    def get(self , req) :

        return render(req , 'User.html')

    def post(self , req) :

        meg = {'Error' : ""}

        check = authenticate(username = req.POST['username'] , password = req.POST['password'])

        if check is not None : 

            login(req , check)

            return redirect('/django/home/')

        else :

            msg = { "Error" : "Invalid Username  or Password " }

            return render(req , 'User.html' , msg)


class AdminLogin(View) :

    meg = {'Error' : ""}
            
    def get(self , req) :

        return render(req , 'Admin.html')
    
    def post(self , req) :

        check = authenticate(username = req.POST['username'] , password = req.POST['password'])

        if check is not None :

            logged_user = User.objects.get(username = check)

            if logged_user.is_staff:

                
                login(req , check)

                return redirect('/django/adminhome/')
            else:

                msg = { "Error" : "you don't have permission  " }

                return render(req , 'Admin.html' , msg)


        else :

            msg = { "Error" : "Invalid Username  or Password  " }

            return render(req , 'Admin.html' , msg)
from django.shortcuts import render , HttpResponse , redirect
from Students.models import Student  , FeedBack
from Students.forms import *
from .models import Coures , Card
from django.views import View
from .forms import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import AbstractUser
from authentication.forms import User_form
from django.contrib.auth.models import User

# Create your views here.

class Landing(View) :

    def get(self , req) :

        return render(req , 'Landing.html')

class Studentd_list(View) :

    def get(self , req , id) :
        
        logged = User.objects.filter(id = id)

        student = Student.objects.get(id = id)

        info =  authenticate(logged)

        if info in student :

            data = {
                "name" : student.name , 
                "address" : student.address ,
                "moblie" : student.moblie ,
                "select_coures" : student.selected_coures ,
                "total_fees" : student.total_fees , 
                "paid_fees" : student.paid_fees,
                "remining" : student.remaining_fees , 
                "image" : student.pictuer
            }

            return render(req , 'Studentlist.html' , data)

class Students_feedBack(View) :

    def get(self, req) :

        return render(req , 'StudentFB.html' , {'forms' : FeedBack_Form()})

    def post(self , req) : 

        feed = FeedBack(
                    Title = req.POST['Title'] , 
                    Body=req.POST['Body'] , 
                    slug = req.POST['slug']    
                )

        feed.save()
            
        return redirect('/django/studentFeed/') 

# Admin 

class Admin(View) :
    
    def get(self , req) :

        return render(req , 'Admin.html')

class Admin_List(View) :

    def get(self , req) : 

        details = {'iterate' : Student.objects.all()}

        return render(req , 'AdminList.html' , details)


class AminHome(View) :

    def get(self, req ) :

        data = {'iterate' : Card.objects.all()}
            
        return render(req , 'AdminHome.html' , data)

class homepage(View):

      def get(self, req ) :
        
        data = {'iterate' : Card.objects.all() }

        return render(req , 'home.html' , data)


class CouresForms(View) :

    def get(self, req) :

        data = {'forms' : Coures_form() }

        return render(req , 'AdminForms.html' , data)

    def post(self , req) :
        
        details = Coures_form(req.POST)

        if details.is_valid() :

            details.save()

            return redirect('/django/admincoures/')
      

class AddCoures(View) :

    def post(self , req , id ) :

        select_update = Coures.objects.id(id = id )

        form = Coures_form(instance= select_update)


class Coures_details(View) :

    def get(self , req) :

        data = {'iterate' : Coures.objects.all()}
        print(data)

        return render(req , 'Coures.html' , data)

class ACoures__details(View) :

    def get(self , req) :

        data = {'iterate' : Coures.objects.all()}

        return render(req , 'AdminCoures.html' , data)

class Admin_Delete(View) :

    def get(self , req , id) :

        delete_r = Coures.objects.get(id = id )

        delete_r.delete()

        return redirect('/django/admincoures/')

class Admin_data_delete(View) :

    def get(self , req , id) :

        delete_r = Student.objects.get(id = id )

        delete_r.delete()

        return redirect('/django/adminlist/')

class Admin_update(View) :

    def get(self , req , id) :

        update = Coures.objects.get(id = id )

        data = {'forms' : Coures_form(instance = update )}

        return render(req , 'AdminForms.html' , data)

    def post(self , req , id ) :

        update = Coures.objects.get(id = id )

        details = Coures_form(req.POST , instance = update)

        if details.is_valid() :

            details.save()

            return redirect('/django/admincoures/')

class  Card_add(View) : 

    def get(self , req) : 

        return render(req , 'Card.html' , {'forms' : Cart_form()})

    def post(self , req) :

        details = Card(
            title=req.POST['title'] , 
            content=req.POST['content'],
            image = req.FILES["image"]
            )

        details.save()

        return redirect('/django/adminhome/')



    






   


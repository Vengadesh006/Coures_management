from django.contrib import admin
from .models import *
from Students.models import FeedBack

# Register your models here.

admin.site.register(Coures)
admin.site.register(Card)
admin.site.register(FeedBack)

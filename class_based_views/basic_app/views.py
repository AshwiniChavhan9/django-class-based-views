from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

class CBViews(View):
    def get(self,request):
        return HttpResponse("Class based views are cool !")

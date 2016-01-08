from django.shortcuts import render
import datetime


def main(request):
    now = datetime.datetime.now()
    context = {'message':'welcome', 'now':now }
    return render(request,'main/main.html',context)
from django.db.models import Count
from django.shortcuts import render, redirect


# Create your views here.
from management.models import UploadModel
from passenger.models import PaymentModel, RegisterModel


def adminlogin(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('userid')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('upload_airport')

    return render(request,'management/adminlogin.html')

def upload_airport(request):
    if request.method == "POST":
        departure = request.POST.get('departure')
        flight = request.POST.get('flight')
        airline = request.POST.get('airline')
        planetype = request.POST.get('planetype')

        UploadModel.objects.create(departure=departure, flight=flight, airline=airline, planetype=planetype,)

    return render(request,"management/upload_airport.html")

def view_upload(request):
    obj=UploadModel.objects.all()
    return render(request,'management/view_upload.html',{'objects':obj})

def view_feedback(request):
    obj=PaymentModel.objects.all()
    return render(request,'management/view_feedback.html',{'objects':obj})

def chart_page(request,chart_type):
    chart = PaymentModel.objects.values('analysis').annotate(dcount=Count('analysis'))
    return render(request,'management/chart_page.html',{'chart_type':chart_type,'objects':chart})

def pass_chart(request,chart_type2):
    chart = RegisterModel.objects.values('passenger').annotate(dcount=Count('passenger'))
    return render(request,'management/pass_chart.html',{'chart_type2':chart_type2,'objects':chart})

def country_chart(request,chart_type1):
    chart = RegisterModel.objects.values('country').annotate(dcount=Count('country'))
    return render(request,'management/country_chart.html',{'chart_type1':chart_type1,'objects':chart})
import re

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from management.models import UploadModel
from passenger.forms import RegisterForms
from passenger.models import RegisterModel, PaymentModel

def register(request):
    if request.method == "POST":
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = RegisterForms()
    return render(request, 'passenger/register.html',{'form':form})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user is not None and user.check_password(password):
            request.session['name'] = user.id  # Change 'user_id' to 'name'
            return redirect('mydetails')
        else:
            error = "Invalid username or password"
    else:
        error = None
    return render(request, 'passenger/login.html', {'error': error})

def mydetails(request):
    name = request.session['name']
    ted = RegisterModel.objects.get(id=name)

    return render(request, 'passenger/mydetails.html',{'objects':ted})

def updata_details(request):
    name = request.session['name']
    obj = RegisterModel.objects.get(id=name)
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        passenger = request.POST.get('passenger')
        country = request.POST.get('country')


        obj = get_object_or_404(RegisterModel, id=name)
        obj.firstname = firstname
        obj.lastname = lastname
        obj.userid = userid
        obj.password = password
        obj.phoneno = phoneno
        obj.email = email
        obj.gender = gender
        obj.passenger = passenger
        obj.country = country


        obj.save(update_fields=["firstname","lastname",  "userid", "password", "phoneno","email","gender","passenger","country"])
        return redirect('mydetails')

    return render(request, 'passenger/updata_details.html',{'form':obj})


def feedback(request,pk):
    name = request.session['name']
    obj = RegisterModel.objects.get(id=name)
    gymObj = UploadModel.objects.get(id=pk)
    se=''
    pos = []
    nos = []
    sa=''
    cat=''
    ss=''
    if request.method=="POST":
        web=request.POST.get('ItemID')

        cht = request.POST.get('feedback')

        c = (re.findall(r"[\w']+", str(cht)))
        for f in c:

            if f in ('bad','worst', 'poor', 'beteer', 'tolate'):

                pos.append(f)
            elif  f in ('Awesome','good', 'nice', 'beteer', 'best', 'excellent', 'extraordinary', 'happy' , 'won' , 'love' , 'greate' ,'thanking','thank', 'omg','like'):


                nos.append(f)

        if len(pos):
            cat="Negative "
        elif len(nos):
            cat="Positive "

        else:
            cat="neutral"

    if request.method=="POST":

        cht = request.POST.get('feedback')
        PaymentModel.objects.create( passid=obj, manaid=gymObj, feedback=cht,analysis=cat)
    return render(request,'passenger/feedback.html',{'obj':ss,'a':cat,'ji':sa,})


def view_checkin(request):
    obj=UploadModel.objects.all()
    return render(request,'passenger/view_checkin.html',{'objects':obj})

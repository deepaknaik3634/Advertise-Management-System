import smtplib

from django.shortcuts import render, redirect

from django.urls import reverse

from .models import UserLogin,EventPayment,InvoiceInfo,UserRegistration,NewspaperaddPayment,CustomerInfo,EventInfo,NewsPaper,NewspaperaddRequest
from django.core.files.storage import FileSystemStorage
import os
from adv_cmp.settings import BASE_DIR




def showhome(request):
    return render(request,"home1.html")

def adminhome(request):
    return render(request,"adminhome.html")

def customerhome(request):
    return render(request,"customer_home.html")

def login(request):
    if request.method =="POST":
        username = request.POST.get('t1')
        request.session['username']=username
        password = request.POST.get('t2')
        utype = request.POST.get('t3')
        ucheck=UserLogin.objects.filter(username=username).count()
        if ucheck>=1:
            udata=UserLogin.objects.get(username=username)
            upass=udata.password
            utype=udata.utype
            if upass==password:
                if utype=='admin':
                    return render(request,'adminhome.html')
                if utype=='customer':
                  return render(request,'customer_home.html')
            else:
                return render(request,'login3.html',{'msg':'invalid password'})
        else:
            return render(request,'login3.html',{'msg':'invalid username'})
    return render(request,'login3.html')



# Create your views here.
def insertuserreg(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')

        UserRegistration.objects.create(name=s1, city=s2, address=s3, email=s4, contact=s5)
        UserLogin.objects.create(username=s4, password=s5,utype='customer')
        return render(request, 'userdetails.html')
    return render(request, 'userdetails.html')

def showuserreg(request):
    userdict=UserRegistration.objects.all()
    return render(request,"viewuserregistration.html",{'userdict':userdict})



def insertcustomer(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        CustomerInfo.objects.create(name=s1, city=s2, address=s3, pincode=s4, contactno=s5, email=s6)
        UserLogin.objects.create(username=s6,password=s5,utype='customer')
        return render(request, 'customerdetails.html')
    return render(request, 'customerdetails.html')


def changepassword(request):
    if request.method == "POST":

        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')

        return render(request, 'changepassword.html')
    return render(request, 'changepassword.html')


def showCustomerInfo(request):
    userdict=CustomerInfo.objects.all()
    return render(request,"viewcustomerinfo.html",{'userdict':userdict})



def viewnewspayment(request):
    userdict=NewspaperaddPayment.objects.all()
    return render(request,"viewnewspaperaddpayment.html",{'userdict':userdict})

def showqr(request):
   return render(request,"qrpayment.html")



def inserteventinfo(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        s7 = request.POST.get('t7')
        s8 = request.POST.get('t8')

        EventInfo.objects.create(cust_id=s1, event_name=s2, advertisement_type=s3, size=s4, quality=s5, content=s6,
                             sample_photo=s7, order_date=s8, order_status='new')
        return render(request, 'infoEvent.html')
    return render(request, 'infoEvent.html')
def showEventInfo(request):
    userdict=EventInfo.objects.all()
    return render(request,"vieweventinfo.html",{'userdict':userdict})

def insertnewspaper(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        NewsPaper.objects.create(newspaper_name=s1, editor_name=s2, contact_no=s3, size=s4, cost=s5)
        return render(request, 'infonews.html')
    return render(request, 'infonews.html')

def insertnewpayment(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')

        NewspaperaddPayment.objects.create(news_id=s1, customer_id=s2, amount=s3, payment_status='cleared')
        return render(request, 'qrpayment.html')
    return render(request, 'customernewspayment.html')
def showNewsPaper(request):
    userdict=NewsPaper.objects.all()
    return render(request,"viewnewspaper.html",{'userdict':userdict})


def insertnewspaperadd(request) :
    if request.method == "POST" and request.FILES['myfile']:
        s1 = request.POST.get('t1')
        myfile=request.FILES['myfile']
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)

        NewspaperaddRequest.objects.create(cust_id=s1, photo=myfile, request_date=s3, date_to_posted=s4, request_status=s5)
        return render(request, 'newrequestnews.html')
    return render(request, 'newrequestnews.html')

def newrequest(request):
    if request.method == "POST" and request.FILES['myfile']:
        s1 = request.POST.get('t1')
        myfile = request.FILES['myfile']
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)

        NewspaperaddRequest.objects.create(cust_id=s1,photo=myfile,request_date=s3,date_to_posted=s4,
                                           request_status=s5)
        return render(request,'newrequestnews.html',{"msg": "Image Uploaded Successfully"})
    return render(request, 'newrequestnews.html')

def showNewspaperaddRequest(request):
    userdict=NewspaperaddRequest.objects.all()
    return render(request,"viewnewspaperaddrequest.html",{'userdict':userdict})

def inserteventpayment(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        EventPayment.objects.create(event_id=s1, customer_id=s2, amount=s3, pay_date=s4, payment_status='cleared')
        return render(request, 'qrpayment.html')
    return render(request, 'addeventpayment.html')

def showeventpayment(request):
    userdict=EventPayment.objects.all()
    return render(request,"vieweventpayment.html",{'userdict':userdict})


def insertinvoice(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        InvoiceInfo.objects.create(cust_id=s1, event_id=s2, amount=s3, grand_total=s4, invoice_status=s5)
        return render(request, 'infoinvoice.html')
    return render(request, 'infoinvoice.html')

def showinvoiceinfo(request):
    uname = request.session['username']
    userdict=InvoiceInfo.objects.filter(cust_id=uname).values()
    return render(request,"viewinvoiceinfo.html",{'userdict':userdict})

def forgetpass(request):
    if request.method=="POST":
        username=request.POST.get('t1')
        request.session['username']=username
        chcek=UserLogin.objects.filter(username=username).count()
        if chcek>=1:
            udata=UserLogin.objects.get(username=username)
            password=udata.password


            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('deepaknaik3634@gmail.com', 'djbw fllo cnlb apog')

            mail.sendmail('deepaknaik3634@gmail.com',username,password)
            mail.close()
            return render(request, 'forgetpass.html',{'msg':'Password Sent To Ur Email id'})
        else:
            return render(request, 'forgetpass.html',{'msg':'invalid username'})

    return render(request,'forgetpass.html')


def changepass(request):
    uname=request.session['username']
    if request.method == 'POST':
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')

        ucheck = UserLogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    UserLogin.objects.filter(username=uname).update(password=newpass)
                    base_url=reverse('login')
                    msg='password has been changed successfully'
                    return redirect(base_url,msg=msg)
                else:
                    return render(request, 'changepassword.html',{'msg': 'both the usename and password are incorrect'})
            else:
                return render(request, 'changepassword.html',{'msg': 'invalid username'})
    return render(request, 'changepassword.html')

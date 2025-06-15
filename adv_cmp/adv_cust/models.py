from django.db import models

class UserRegistration(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)

class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password=models.CharField(max_length= 20)
    utype=models.CharField(max_length= 20)


class EventInfo(models.Model):
    cust_id=models.CharField(max_length=50,null=True,blank=True)
    event_name=models.CharField(max_length=50)
    advertisement_type=models.CharField(max_length=30)
    size=models.CharField(max_length=30)
    quality=models.CharField(max_length=30)
    content=models.CharField(max_length=1000)
    sample_photo=models.FileField(upload_to='documents/')
    order_date=models.DateField()
    order_status=models.CharField(max_length=50)


class CustomerInfo(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    contactno=models.CharField(max_length=10)
    email=models.CharField(max_length=40)



class InvoiceInfo(models.Model):
    cust_id=models.CharField(max_length=50)
    event_id = models.CharField(max_length=50)
    amount=models.CharField(max_length= 50)
    grand_total=models.CharField(max_length= 50)
    invoice_status=models.CharField(max_length= 50)


class NewsPaper(models.Model):
    newspaper_name=models.CharField(max_length=50)
    editor_name=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    size=models.CharField(max_length=50)
    cost=models.CharField(max_length=50)


class NewspaperaddRequest(models.Model):
    cust_id = models.CharField(max_length=50)
    photo=models. FileField(upload_to='documents/')
    request_date=models.CharField(max_length=40)
    date_to_posted=models.CharField(max_length=40)
    request_status=models.CharField(max_length=50)


class NewspaperaddPayment(models.Model):
    news_id= models.CharField(max_length=50)
    customer_id= models.CharField(max_length=50)
    amount=models.IntegerField()
    payment_status= models.CharField(max_length=50)

class EventPayment(models.Model):
    event_id= models.CharField(max_length=50)
    customer_id= models.CharField(max_length=50)
    amount=models.IntegerField()
    pay_date=models.DateField()
    payment_status= models.CharField(max_length=50)

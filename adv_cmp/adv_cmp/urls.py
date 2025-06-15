"""adv_cmp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from adv_cust import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url('insertuserreg',views.insertuserreg,name='insertuserreg'),
    url('showuserreg',views.showuserreg, name='showuserreg'),
    url('insertcustomer',views.insertcustomer, name='insertcustomer'),
    url('showCustomerInfo',views.showCustomerInfo, name='showCustomerInfo'),
    url('inserteventinfo',views.inserteventinfo, name='inserteventinfo'),
    url('showEventInfo', views.showEventInfo, name='showEventInfo'),

    url('insertnewspaper',views.insertnewspaper, name='insertnewspaper'),
    url('showNewsPaper', views.showNewsPaper, name='showNewsPaper'),

    url('insertnewspaperadd', views.insertnewspaperadd, name='insertnewspaperadd'),
    url('showNewspaperaddRequest', views.showNewspaperaddRequest, name='showNewspaperaddRequest'),

    url('insertinvoice', views.insertinvoice, name='insertinvoice'),
    url('showinvoiceinfo', views.showinvoiceinfo, name='showinvoiceinfo'),
    url(r'^$', views.showhome, name='showhome'),
    url('viewnewspayment',views.viewnewspayment,name='viewnewspayment'),
    url('login', views.login, name='login'),
    url('forgetpass',views.forgetpass,name='forgetpass'),
    url('showqr',views.showqr,name='showqr'),
    url('showeventpayment',views.showeventpayment,name='showeventpayment'),
url('changepassword',views.changepassword,name='changepassword'),
url('inserteventpayment',views.inserteventpayment,name='inserteventpayment'),
url('changepass',views.changepass,name='changepass'),
    url('newrequest',views.newrequest,name='newrequest'),
url('adminhome',views.adminhome,name='adminhome'),
url('customerhome',views.customerhome,name='customerhome'),
url('insertnewpayment',views.insertnewpayment,name='insertnewpayment'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


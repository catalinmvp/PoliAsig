from django.db import models

# Create your models here.
from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from Customer.models import PhysicalCustomer
from pyinvoice.templates import SimpleInvoice
from Employee.models import AddEmployee
from Service.models import Service
doc = SimpleInvoice('invoice.pdf')

c1 = PhysicalCustomer.objects.all()[:1]
e1 = AddEmployee.objects.all()[:1]
s1= Service.objects.all()[:1]
# Paid stamp, optional
doc.is_paid = True
#PhysicalCustomer s = new PhysicalCustomer();
doc.invoice_info = InvoiceInfo(1023, datetime.now(), datetime.now())  # Invoice info, optional

# Service Provider Info, optional
doc.service_provider_info = ServiceProviderInfo(
    name=s1[0].description



)

# Client info, optional
doc.client_info = ClientInfo(

    name= c1[0].Cust_name,
    email= c1[0].Cust_email,

)

# Add Item
doc.add_item(Item('Service', 'Service_id', s1[0].Serv_id, '1.1'))


# Tax rate, optional
doc.set_item_tax_rate(20)  # 20%

# Transactions detail, optional
doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))



doc.finish()
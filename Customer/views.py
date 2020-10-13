from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cust_view(*args, **kwargs):
    return HttpResponse("""
           <h3>
   		<ul>
   			<li> <a href="/physicalcustomer">Pyhsical Customer</a> <a href="/company">Company</a>     </li>
   		</ul>
   		</h3>
   		[<a href="../">Back</a>]


    """)
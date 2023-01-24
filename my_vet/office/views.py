from django.shortcuts import render
from .models import customer
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import CustomerForm
from django.http import HttpResponseRedirect

def search_customers_result(request):
    # we need to determine if someone has just gone to this page
    # or if they have searched using the form.
    if request.method == "POST":
        # the result of the POST 
        search_cust = request.POST['search_cust']
        # search the customer database using filter for the search_cust term
        customers = customer.objects.filter(firstname__contains=search_cust)
        # pass the search term and the search results to the page.
        return render(request, 'office/search_customers_result.html', 
                                {'search_cust':search_cust,
                                'customers': customers})
    else:
        return render(request, 'office/search_customers_result.html', {})


def add_customers(request):
    submitted = False
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            # this send the submitted variable to the GET request 
            return HttpResponseRedirect('/add_customers?submitted=True')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'office/add_customers.html',{'form':form, 'submitted': submitted})

def allcustomers(request):
    mycustomers = customer.objects.all().values()
    customermodel = {
        'vetcustomers' : mycustomers,
    }
    return render(request, 'office/all_customers.html',context=customermodel )

def details(request, id):
    mycustomer = customer.objects.get(id=id)
    acustomer = {
        'acustomer' : mycustomer,
    }
    return render(request, 'office/details.html', context=acustomer)


def home(request):
    print(request.GET.get('username'))
    return render(request, 'office/home.html')

def dates(request, year, month):
    name = "Sarah"
    # makes sure the month passed in begins with a capital letter.
    month = month.capitalize()
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #create a calendar
    cal = HTMLCalendar().formatmonth(year,month_number)

    # get current year
    now = datetime.now()
    current_year = now.year

    #get current time
    time = now.strftime('%I:%M:%S %p')

    print(month)
    print(month_number)
    return render(request, 'office/dates.html', {
        "name" : name,
        "year" : year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })






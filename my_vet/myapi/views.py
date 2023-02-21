from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def users(request):

    # pull data from third party 
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    # convert response data into JSON
    users = response.json()
    print(users)

    return render(request, 'myapi/users.html', {'users': users})




from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index(request):
    info_here = "Hello i am from views.py"
    my_dict = {'insert_me': info_here}
    return render(request, 'index.html', my_dict)

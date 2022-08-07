from pprint import pprint
from django.shortcuts import render
from church import models

# Create your views here.


def index(request):
    start_date = '2022-07-20'

    

    return render(request, 'base.html', {'atts': 'atts', 'mems': 'mems'})

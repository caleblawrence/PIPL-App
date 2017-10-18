from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.template import loader
from piplapis.data import Person
from piplapis.data.fields import Address, Name, DOB
from piplapis.search import SearchAPIRequest
from django.http import HttpResponseRedirect
from piplapis.data import *
import pprint
import time
from ast import literal_eval
import csv
import json
import operator


def intelLinks(request):
	#latest_testresult_list = "test"

	# pipl api query
	

	context = {}
	return render(request, 'intelLinks.html', context)
    #return HttpResponse("Hello, world. You're at the polls index.")
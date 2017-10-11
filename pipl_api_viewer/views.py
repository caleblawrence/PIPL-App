from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.template import loader
from .forms import PIPLSearch
from piplapis.data import Person
from piplapis.data.fields import Address, Name, DOB
from piplapis.search import SearchAPIRequest
from .forms import PIPLSearch
from django.http import HttpResponseRedirect
from piplapis.data import *
import pprint
import time
from ast import literal_eval
import csv
import json
import operator




def index(request):
	latest_testresult_list = "test"

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = PIPLSearch(request.POST)
		# check whether it's valid:
		if form.is_valid():
			print(form.cleaned_data)

			# get rid of elements in form that are emtpy
			newDict={}
			for element, value in form.cleaned_data.items(): 
				if value != "":
					newDict[element] = value

			# loop through form and organize it into a query for the PIPL Api
			piplQuery = {}
			for element, value in newDict.iteritems(): 
				piplQuery[element] = value

			## UNCOMMENT HERE TO GET OUT OF TESTING 

			piplQuery["api_key"] ='BUSINESS-PREMIUM-DEMO-c8wuzpg3qklawoidqln3cgxx'
			print("****** printing query *******")
			pprint.pprint(piplQuery)
			request2 = SearchAPIRequest(**literal_eval(str(piplQuery)))

			#request2 = SearchAPIRequest(first_name=u'Caleb', last_name=u'Lawrence', api_key='vqnx9j3dfjxyq5sgmnspgvij')
			search_response = request2.send()
			json_response = search_response.to_dict()
			pprint.pprint(json_response)
			### UNCOMMENT HERE TO LOAD JSON TO FILE FOR FUTURE TESTING

			# with open('multiplepeople.json', 'w') as outfile:
			# 	json.dump(json_response, outfile)
			context = {}


			# with open("multiplepeople.json") as json_data:
			# 	json_response = json.load(json_data)
			# 	json_data.close()

			
			if "possible_persons" in json_response:
			# more than one person found
				# collection of person objects
				context = {}  
				context['people'] = {}
				totalPeople = 0

				# loop through possible persons
				for person in json_response["possible_persons"]:
					totalPeople += 1
					#print "printing person"
					#pprint.pprint(person)
					unique_name = person["@search_pointer"]
					context["people"][unique_name] = {}

					if "names" in person: 
						names = person["names"]
						context['people'][unique_name]['names'] = names
					if "emails" in person: 
						emails = person["emails"]
						context["people"][unique_name]['emails'] = emails
					if "phones" in person: 
						phones = person["phones"]
						context["people"][unique_name]['phones'] = phones
					if "gender" in person: 
						gender = person["gender"]
						context["people"][unique_name]['gender'] = gender
					if "dob" in person: 
						dob = person["dob"]
						context["people"][unique_name]['dob'] = dob
					if "addresses" in person:
						addresses = person["addresses"]
						context["people"][unique_name]['addresses'] = addresses
					if "jobs" in person: 
						jobs = person["jobs"]
						context["people"][unique_name]['jobs'] = jobs
					if "educations" in person: 
						educations = person["educations"]
						context["people"][unique_name]['educations'] = educations
					if "images" in person:
						images = person["images"]
						context["people"][unique_name]['images'] = images
					if "urls" in person: 
						urls = person["urls"]
						context["people"][unique_name]['urls'] = urls
					context["people"][unique_name]['personCounter'] = totalPeople


					#pprint.pprint(context["people"])


				# print "printing data in context: "

				# for item in context['people']:
				# 	pprint.pprint(item)
				# 	for item2 in context['people'][item]:
				# 		pprint.pprint(item2)

				context["totalPeople"] = totalPeople
				peopleCounter = range(1, totalPeople)
				context["peopleCounter"] = peopleCounter
				return render(request, 'response_multi.html', context)




			# only one person found
			else: 
				if "names" in json_response["person"]: 
					names = json_response["person"]["names"]
					context['names'] = names
				if "emails" in json_response["person"]: 
					emails = json_response["person"]["emails"]
					context['emails'] = emails
				if "phones" in json_response["person"]: 
					phones = json_response["person"]["phones"]
					context['phones'] = phones
				if "gender" in json_response["person"]: 
					gender = json_response["person"]["gender"]
					context['gender'] = gender
				if "dob" in json_response["person"]: 
					dob = json_response["person"]["dob"]
					context['dob'] = dob
				if "addresses" in json_response["person"]:
					addresses = json_response["person"]["addresses"]
					context['addresses'] = addresses
				if "jobs" in json_response["person"]: 
					jobs = json_response["person"]["jobs"]
					context['jobs'] = jobs
				if "educations" in json_response["person"]: 
					educations = json_response["person"]["educations"]
					context['educations'] = educations
				if "images" in json_response["person"]:
					images = json_response["person"]["images"]
					context['images'] = images
				if "urls" in json_response["person"]: 
					urls = json_response["person"]["urls"]
					context['urls'] = urls

				#context = {'names': names, 'emails': emails, 'phones': phones, 'gender': gender, 'dob': dob, 'addresses': addresses, 'jobs': jobs, 'educations': educations, 'images': images, 'urls': urls  }
	          
				return render(request, 'response.html', context)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = PIPLSearch()
	return render(request, 'home.html', {'form': form})




	context = {'latest_testresult_list': latest_testresult_list}
	return render(request, 'home.html', context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def response(request):
	latest_testresult_list = "test"

	# pipl api query
	

	context = {'latest_testresult_list': latest_testresult_list}
	return render(request, 'response.html', context)
    #return HttpResponse("Hello, world. You're at the polls index.")
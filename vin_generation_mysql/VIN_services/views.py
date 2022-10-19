from django.shortcuts import render
from . import models
import random
import re
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,"vin/home.html")

def creatVIN(request):
    return render(request,"vin/createVIN.html")

def getVIN(request):
    inputNumber = int(request.POST['inputNumber'])
    vinNumbers=generateVin(inputNumber)
    vinNumbers_dict=createList(inputNumber,vinNumbers)
    return render(request, "vin/showVIN.html",{'vinNumbers_dict': vinNumbers_dict})

def openretrieveVIN(request):
    return render(request,"vin/openretrieveVIN.html")

def openintervalVIN(request):
    return render(request, "vin/openintervalVIN.html")

def showVIN(request):
    fromTime=request.POST['fromTime']
    toTime=request.POST['toTime']
    context={
       'data': vinnumbers_new.objects.filter(datetime__range=(fromTime, toTime))
    }
    return render(request, "vin/showVIN_Interval.html",context)

def retrieveVIN(request):
    inputNumber = int(request.POST['vinCount'])
    vinNumbers=list(vinnumbers_new.objects.values_list('vinNumber', flat=True))
    vinNumbers_dict = createList(inputNumber, vinNumbers)
    return render(request, "vin/showVIN.html", {'vinNumbers_dict': vinNumbers_dict})

def openvalidateVIN(request):
    return render(request,"vin/validateVIN.html")

def isvalidVIN(request):
    isvalid=validateVIN(request.POST['vinNumber'])
    return render(request,"vin/isvalidVIN.html",{'isvalid':isvalid})

def createList(inputNumber,vinNumbers):
    list =[]
    for i in range(1,inputNumber+1):
        list.append(i)
    Dictionary = zip(list, vinNumbers)
    Dictionary =dict(Dictionary)
    return Dictionary

def getManufacturer():
    manufacturer_list = ["HG", "PG", "TY", "RE", "HJ", "KL"]
    rand_idx = random.randrange(len(manufacturer_list))
    return manufacturer_list[rand_idx]

def getPotrait():
     return (getBrand()+getEngineSize()+getType())

def getBrand():
    brand_list = ["BH", "PJ", "TT", "ES", "BK", "MJ"]
    rand_idx = random.randrange(len(brand_list))
    return brand_list[rand_idx]

def getEngineSize():
    return str(random.randrange(10,99))

def getType():
    type_list = ["A", "J", "G", "S", "L", "X"]
    rand_idx = random.randrange(len(type_list))
    return type_list[rand_idx]

def getAuthenticater():
    return "X"
def getModelYear():
    model_year = ["M", "N", "K", "O", "G", "V"]
    rand_idx = random.randrange(len(model_year))
    return model_year[rand_idx]

def getManufacturerPlant():
    plant_list = ["W", "E", "F", "N", "L", "Z"]
    rand_idx = random.randrange(len(plant_list))
    return plant_list[rand_idx]

def getSerialNumber():
    return str(random.randrange(111111, 999999))

def generateVin(inputNumber):
    vinNumbers = []
    for number in range(inputNumber):
        aggregateVinParts(number,vinNumbers)
    for i in range(len(vinNumbers)):
        vinnumbers_new.objects.create(vinNumber = vinNumbers[i])
    return vinNumbers

def aggregateVinParts(number,vinNumbers):
    return (vinNumbers.append(str(number + 1) + getManufacturer()+ getPotrait()+ getAuthenticater()+getModelYear()+getManufacturerPlant()+getSerialNumber()))

def validateVIN(input):
    return re.search("^[1-9]{1}[A-Za-z]{4}[02-9]{2}[A-Za-z]{4}[0-9]{6}$", input)
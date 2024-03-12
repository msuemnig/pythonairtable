from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
import os
from pyairtable import Api
from superbowl.datamanipulation.utils import Utils
from .models import Commercial


# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Heyo.")

def allData(request):
    commercials_list = Commercial.objects.all()
    template = loader.get_template("superbowl/allData.html")
    context = {
        "commercials_list": commercials_list
    }
    return HttpResponse(template.render(context, request))

def getAirtableData(request):
    api = Api(os.environ['AIRTABLE_API_KEY'])
    commercials = api.table('apphDpjDZko9FuKtC','tblkN08VW2doQ3xB8')
    output = commercials.all()
    return JsonResponse(output, safe=False)

def chart(request):
    api = Api(os.environ['AIRTABLE_API_KEY'])
    commercials = api.table('apphDpjDZko9FuKtC','tblkN08VW2doQ3xB8')
    output = commercials.all()
    utils = Utils()
    brands = utils.groupByBrand(output)
    brand_list = list(brands.keys())
    brand_count = list(brands.values())
    #return JsonResponse(brands, safe=False)
    return render(request, 'superbowl/chart.html', {'brand_list': brand_list, 'brand_count': brand_count})
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {}
    if(request.method == 'GET'):
        context['success'] = str(request.method)
        template = loader.get_template('home.html')
        return HttpResponse(template.render(context, request))
    else:
        context['error'] = str(request.method)
        template = loader.get_template('error.html')
        return HttpResponse(template.render(context, request))

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class index(TemplateView):
    template_name = 'index.html'

def func_template(request):
    return render(request, 'second_task/func_template.html')



class class_template(TemplateView):
    template_name = 'second_task/class_template.html'



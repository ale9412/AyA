from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.views.generic import TemplateView,ListView
from django.views import View
from django.urls import reverse_lazy

from services.utils import get_content,create_jsons
from data.models import ProxmoxData,ZabbixDB
from services.models import Servicio,CurrentUtilization

class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['Proxmox'] = ProxmoxData.objects.first()
        context['Zabbix'] = ZabbixDB.objects.first()
        return context

class About(TemplateView):
    template_name = 'about.html'


class ServiceListView(ListView):
    template_name = 'servicios.html'
    queryset = Servicio.objects.all().order_by('proxmox')
    context_object_name = 'service_list'
    paginate_by = 9

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DateRangeForm
        return context

    
class DeleteAllView(View):
    model = Servicio
    template_name = 'service_del.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
        self.model.objects.all().delete()
        return redirect('services:servicios_listar')

def start_procedure(requets):
    if requets.method == 'POST':
        create_jsons(ProxmoxData,ZabbixDB)
        return redirect('services:servicios_listar')

def gather_service(request):
    if request.method == 'POST':
        Servicio.objects.all().delete()
        get_content(Servicio,ProxmoxData)
        return redirect('services:servicios_listar')
    return render(request,'servicios.html')


def currentUtilization(request):
    template_name = 'current_util.html'
    if request.GET.get('metric') and request.GET.get('hypervisor'):
        metric = request.GET.get('metric').lower()
        hypervisor = request.GET.get('hypervisor').lower()
        services_list = Servicio.objects.filter(hypervisor=hypervisor)
        model = CurrentUtilization.objects.filter(metric=metric,servicio__in=services_list).order_by('servicio')
    else:
        model = CurrentUtilization.objects.all().order_by('servicio')
        metric = 'RAM'
        hypervisor = 'LXC'
    paginator = Paginator(model, 9) 
    page = request.GET.get('page')
    model_paginated = paginator.get_page(page)
    return render(request, template_name, {'page_obj':model_paginated, 'metric':metric,'hypervisor':hypervisor})

class FutureUtilization(TemplateView):
    template_name = 'future_util.html'

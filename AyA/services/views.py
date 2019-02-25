from django.shortcuts import render,redirect,render_to_response
from django.core.paginator import Paginator
from django.views.generic import TemplateView,ListView
from django.views import View
from django.urls import reverse_lazy

from services.utils import get_content
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


class ServiceLXCView(ListView):
    template_name = 'servicios.html'
    queryset = Servicio.objects.filter(hypervisor='lxc').order_by('proxmox')
    context_object_name = 'service_list'
    paginate_by = 9

    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        context['hypervisor'] = 'LXC'
        return context


class ServiceKVMView(ListView):
    template_name = 'servicios.html'
    queryset = Servicio.objects.filter(hypervisor='kvm').order_by('proxmox')
    context_object_name = 'service_list'
    paginate_by = 9

    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        context['hypervisor'] = 'KVM'
        return context

    
class DeleteAllView(View):
    model = Servicio
    template_name = 'service_del.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        self.model.objects.all().delete()
        return redirect('services:servicios_lxc')


def start_procedure(requets):
    if requets.method == 'POST':
        create_jsons(ProxmoxData,ZabbixDB)
        return redirect('services:servicios_lxc')


def gather_service(request):
    if request.method == 'POST':
        get_content(Servicio,ProxmoxData)
        return redirect('services:servicios_lxc')
    return render(request,'servicios.html')


def currentUtilization(request):
    template_name = 'current_util.html'
    if request.GET.get('metric') and not request.GET.get('hypervisor') == 'all':
        metric = request.GET.get('metric')
        hypervisor = request.GET.get('hypervisor')
        services_list = Servicio.objects.filter(hypervisor=hypervisor)
        model = CurrentUtilization.objects.filter(metric=metric,service__in=services_list).order_by('service')
    else:
        metric = 'RAM'
        model = CurrentUtilization.objects.filter(metric=metric.lower()).order_by('service')
        hypervisor = 'LXC'
    paginator = Paginator(model, 9) 
    page = request.GET.get('page')
    model_paginated = paginator.get_page(page)
    return render(request, template_name, {'page_obj':model_paginated, 'metric':metric,'hypervisor':hypervisor})


class FutureUtilization(TemplateView):
    template_name = 'future_util.html'



from datetime import datetime as dt

from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView,DeleteView,UpdateView,TemplateView
from django.urls import reverse_lazy

from data.forms import ProxmoxForm,ZabbixForm
from data.models import ProxmoxData,ZabbixDB
from data.forms import ExtraDataForm
from data.models import ExtraData
from services.utils import get_content
from services.models import Servicio

class ServerList(View):
    context = {}
    form_prox = ProxmoxForm()
    form_zabbix = ZabbixForm()
    context["form_prox"] = form_prox
    context["form_zabbix"] = form_zabbix
    def get(self,request,*args,**kwargs):
        self.context['proxmox'] = ProxmoxData.objects.all().order_by('servername')
        self.context['zabbix'] = ZabbixDB.objects.all()
        return render(request,'servers_info.html',self.context)

class ProxmoxDataView(CreateView):
    template_name = 'servers_data.html'
    form_class = ProxmoxForm
    model = ProxmoxData
    success_url = reverse_lazy('data:servers_list')
    
class ZabbixDataView(CreateView):
    template_name = 'servers_data.html'
    form_class = ZabbixForm
    model = ZabbixDB
    success_url = reverse_lazy('data:servers_list')

class ProxmoxUpdateView(UpdateView):
    # template_name = "servers_data.html"
    model = ProxmoxData
    form_class = ProxmoxForm
    success_url = reverse_lazy('data:servers_list')

class ZabbixUpdateView(UpdateView):
    template_name = "servers_data.html"
    model = ZabbixDB
    form_class = ZabbixForm
    success_url = reverse_lazy('data:servers_list')

class ProxmoxDelete(DeleteView):
    template_name = 'servers_list'
    model = ProxmoxData
    success_url = reverse_lazy('data:servers_list')

class ZabbixDelete(DeleteView):
    template_name = 'servers_list'
    model = ZabbixDB
    success_url = reverse_lazy('data:servers_list')


class ShowUsers(View):
    template_name = 'users.html'
    form = ExtraDataForm
    context = {}
    
    def get(self,request,*args,**kwargs):
        proxmox = ProxmoxData.objects.first()
        zabbix = ZabbixDB.objects.first()
        extra_data = ExtraData.objects.first()
        error = "No es posible iniciar el procedimiento porque no se han especificado todos los datos requeridos, por favor revise las instrucciones"
        self.context['form'] = self.form
        self.context['data'] = ExtraData.objects.first()
        if not all([proxmox,zabbix,extra_data]):
            self.context["Error"] = error
        else:
            if "Error" in self.context:
                self.context.pop("Error")
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        Servicio.objects.all().delete()
        get_content()
        return redirect("services:servicios_lxc")
        
class InsertUsers(CreateView):
    form_class = ExtraDataForm
    model = ExtraData
    success_url = reverse_lazy('data:user_list')


class EditUsers(UpdateView):
    template_name = 'create_users.html'
    form_class = ExtraDataForm
    model = ExtraData
    success_url = reverse_lazy('data:user_list')

    def post(self,request,*args,**kwargs):
        start = request.POST['start_time']
        end = request.POST['end_time']
        date_format = '%d/%m/%Y'
        if dt.strptime(start,date_format) >= dt.strptime(end,date_format):
            self.object = self.get_object()
            form = self.get_form()
            return redirect('data:user_list')
        return super().post(request,*args,**kwargs)


class DeleteUsers(DeleteView):
    template_name = 'delete_users.html'
    model = ExtraData
    success_url = reverse_lazy('data:user_list')




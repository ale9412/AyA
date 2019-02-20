from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from data.forms import ProxmoxForm,ZabbixForm
from data.models import ProxmoxData,ZabbixDB
from data.forms import ExtraDataForm
from data.models import ExtraData

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
    success_url = reverse_lazy('servers:servers_list')
    
class ZabbixDataView(CreateView):
    template_name = 'servers_data.html'
    form_class = ZabbixForm
    model = ZabbixDB
    success_url = reverse_lazy('servers:servers_list')

class ProxmoxUpdateView(UpdateView):
    template_name = "servers_data.html"
    model = ProxmoxData
    form_class = ProxmoxForm
    success_url = reverse_lazy('servers:servers_list')

class ZabbixUpdateView(UpdateView):
    template_name = "servers_data.html"
    model = ZabbixDB
    form_class = ZabbixForm
    success_url = reverse_lazy('servers:servers_list')

class ProxmoxDelete(DeleteView):
    template_name = 'servers_list'
    model = ProxmoxData
    success_url = reverse_lazy('servers:servers_list')

class ZabbixDelete(DeleteView):
    template_name = 'servers_list'
    model = ZabbixDB
    success_url = reverse_lazy('servers:servers_list')


class ShowUsers(View):
    template_name = 'users.html'
    form = ExtraDataForm
    context = {}
    def get(self,request,*args,**kwargs):
        self.context['form'] = self.form
        self.context['object_list'] = ExtraData.objects.all()
        return render(request,self.template_name,self.context)

class InsertUsers(CreateView):
    template_name = 'create_users.html'
    form_class = ExtraDataForm
    model = ExtraData
    success_url = reverse_lazy('users:user_list')

class EditUsers(UpdateView):
    template_name = 'create_users.html'
    form_class = ExtraDataForm
    model = ExtraData
    success_url = reverse_lazy('users:user_list')

class DeleteUsers(DeleteView):
    template_name = 'delete_users.html'
    model = ExtraData
    success_url = reverse_lazy('users:user_list')




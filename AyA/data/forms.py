from django import forms

from data.models import ProxmoxData, ZabbixDB, ExtraData

class ProxmoxForm(forms.ModelForm):

    class Meta:
        model = ProxmoxData

        fields = (
            'servername',
            'username',
            'password',
            'address',
        )

        labels = {
            'servername':'Proxmox Name',
            'username':'Username',
            'password':'Password',
            'address':'Ip Address',
        }

        widgets = {
            'servername':forms.TextInput(attrs={'class':'form-control','placeholder':'Server Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'address':forms.TextInput(attrs={'class':'form-control','pattern':r"(\d{1,3}.){3}\d{1,3}",'placeholder':'Ip Address'}),
        }

class ZabbixForm(forms.ModelForm):

    class Meta:
        model = ZabbixDB

        fields = (
            'username',
        	'address',
            'password',
        )

        labels = {
            'username':'Username',
            'address':'ZabbixDB Address',
            'password':'Password',
            
        }

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
        	'address':forms.TextInput(attrs={'class':'form-control','pattern':r"(\d{1,3}.){3}\d{1,3}",'placeholder':'Ip Address'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            
        }

class ExtraDataForm(forms.ModelForm):
    class Meta:
        model = ExtraData

        fields = (
            'current_users',
            'new_users',
            'future_users',
            'start_time',
            'end_time',
        )

        labels = {
            'current_users':'Usuarios Actuales',
            'new_users':'Usuarios Nuevos',
            'future_users':'Usuarios Futuros',
            'start_time':'Inicio',
            'end_time':'Final',
        }

        widgets = {
            'current_users':forms.TextInput(attrs={'class':'form-control','placeholder':'Usuarios Actuales','pattern':r'\d+'}),
            'new_users':forms.TextInput(attrs={'class':'form-control','placeholder':'Usuarios Nuevos','pattern':r'\d+'}),
            'future_users':forms.TextInput(attrs={'class':'form-control','placeholder':'Usuarios Futuros','pattern':r'\d+'}),
            'start_time':forms.TextInput(attrs={'class':'form-control','placeholder':r'dd/mm/yyyy HH:MM','pattern':r'\d{2}/\d{2}/\d{4}'}),
            'end_time':forms.TextInput(attrs={'class':'form-control','placeholder':r'dd/mm/yyyy HH:MM','pattern':r'\d{2}/\d{2}/\d{4}'}),
        }
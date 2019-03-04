import os
import json
from django.conf import settings
from datetime import datetime as dt

from data.models import ProxmoxData,ExtraData,ZabbixDB
from services.models import CurrentUtilization,Servicio,FutureUtilization

base_data_path = os.path.join(settings.BASE_DIR,'hosts_measurement','data')
curr_utilization_path = os.path.join(base_data_path,'utilizacion')
fut_utilization_path = os.path.join(base_data_path,'futura')

def save_utilization():

        for root,dirs,files in os.walk(base_data_path):
                # Obtener todos los archivos de utilizacion actual y futura de los servicios
                if root == curr_utilization_path:
                    curr_utilization_files = files
                elif root == fut_utilization_path:
                    fut_utilization_files = files
                else:
                    continue

        for current_file,future_file in zip(curr_utilization_files,fut_utilization_files):
            # Ir por cada archivo y guardar datos en base de datos de Django
                current_file_handler = open(os.path.join(curr_utilization_path,current_file))
                future_file_handler = open(os.path.join(fut_utilization_path,future_file))

                c_data = json.load(current_file_handler)
                f_data = json.load(future_file_handler)

                current_file_handler.close()
                future_file_handler.close()

                for c_metrics,f_metrics in zip(c_data,f_data):
                        curr_utilization_model = CurrentUtilization(
                                metric = c_metrics['item_name'],
                                service = Servicio.objects.get(name=os.path.splitext(current_file)[0]),
                                average = c_metrics['value_avg'],
                                maximum = c_metrics['value_max'],
                                percentil = c_metrics['percentil'],
                        )

                        fut_utilization_model = FutureUtilization(
                            metric = f_metrics['item_name'],
                            service = Servicio.objects.get(name=os.path.splitext(future_file)[0]),
                            average = f_metrics['value_avg'],
                            maximum = f_metrics['value_max'],
                            percentil = f_metrics['percentil'],
                            )

                        curr_utilization_model.save()
                        fut_utilization_model.save()


def get_content():
        for root,dirs,files in os.walk(base_data_path):
            if root == base_data_path:
                jsons = [os.path.join(root,file) for file in files if file.endswith('.json') and file.startswith('10.8')]
                break

        ips = [os.path.splitext(os.path.basename(json))[0] for json in jsons]
        
        for file,ip in zip(jsons,ips):
                
                fp = open(file)
                service_list = json.load(fp)
                fp.close()

                save_service(service_list,ip)
        save_utilization()
                

def save_service(service_list,proxmox_ip):
        
        try:
            proxmox = ProxmoxData.objects.get(address=proxmox_ip)
            for service in service_list:
                    
                    # Estraer de service cada uno de los campos e insertarlos en el modelo
                    #para guardarlo en la base de dato de Django
                    new_service = Servicio(name=service['nombre_servicio'],
                                           hypervisor='lxc',
                                           proxmox=proxmox,
                                           hostid=service['hostid'],
                                           cores=service['cores'],
                                           core_freq=float(service['frecuencia cpu prox']))

                    new_service.save()
        except:
            # No existe el proxmox guardado en la base de datos de django
            # guardarlo primero mediante la interfaz y despues obtener lista de servicios
            return
            

def start_procedure():
    data = ExtraData.objects.first()
    start_time = dt.strptime(data.start_time,"%d/%m/%Y")
    end_time = dt.strptime(data.end_time,'%d/%m/%Y')
    current_users = data.current_users
    future_users = data.future_users
    new_users = data.new_users

    proxmox_list = ProxmoxData.objects.all()
    ip_proxmox = [proxmox.address for proxmox in proxmox_list]
    passw_proxmoxs = [proxmox.password for proxmox in proxmox_list] 

    zabbix = ZabbixDB.objects.first()
    zabbix_ip = zabbix.address
    zabbix_user = zabbix.username
    zabbix_password = zabbix.password

    
    # Falta llamar a los datos de los Proxmox y Zabbix DB

    ###############################################
    # Tu codigo va aqui 
    # Seria bueno utilizar multiples procesos para 
    # agilizar el proceso pq va a ser muy lento
    ###############################################

    get_content()

import os
import json
from django.conf import settings
from datetime import datetime as dt

from data.models import ProxmoxData
from services.models import CurrentUtilization,Servicio

base_data_path = os.path.join(settings.BASE_DIR,'hosts_measurement','data')
curr_utilization_path = os.path.join(base_data_path,'utilizacion')


# def start_procedure(ProxmoxData,ZabbixDB,ExtraData):
#     data = ExtraData.objects.first()
#     start_time = dt.strptime(data.start_time,"%d/%m/%Y")
#     end_time = dt.strptime(data.end_time,'%d/%m/%Y')
#     current_users = data.current_users


def save_utilization():
        
        for root,dirs,files in os.walk(curr_utilization_path):
                # Obtener todos los archivos deutilizacion de los servicios
                utilization_files = files
                break

        for file in utilization_files:
                service_file = open(os.path.join(curr_utilization_path,file))
                service_data = json.load(service_file)
                service_file.close()
                utilization = CurrentUtilization(
                        metric = service_data['item_name'],
                        service = Servicio.objects.get(name=file.rstrip('.json')),
                        average = service_data['value_avg'],
                        maximum = service_data['value_max'],
                        percentil = service_data['percentil'],
                )
                utilization.save()

# Esta funcion es en caso de que se utilicen los jsons.
def get_content(path=base_data_path):

        # Ir por cada archivo y extraer los datos para guardar en Django
        #path: archivo donde se encuentran los archivos
        #del tipo 'ip_prox.json'
        for root,dirs,files in os.walk(path):
            if root == path:
                jsons = [os.path.join(root,file) for file in files if file.endswith('.json') and file.startswith('10.8')]
                break
        
        

        for root,dirs,files in os.walk(curr_utilization_path):
                # Obtener todos los archivos deutilizacion de los servicios
                utilization_files = files
                break

        ips = [os.path.splitext(os.path.basename(json))[0] for json in jsons]
        
        for file,ip in zip(jsons,ips):
                print('\nProcessing file:',os.path.basename(file)+'\n\n')
                fp = open(file)
                service_list = json.load(fp)
                fp.close()
                save_service(Servicio,ProxmoxData,service_list,ip)

        save_utilization()
                

def save_service(Servicio,Proxmox,service_list,proxmox_ip):
        '''

        1 - Servicio: modelo para almacenar cada servicio
        2 - service_list: lista con todos los datos por
        servicio perteneciente a cada proxmox.
        3 - Este modulo es llamado desde una de las vistas en la
        seccion servicios al ejecutar un metodo post.
        
        '''
        try:
            proxmox = Proxmox.objects.get(address=proxmox_ip)
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
            



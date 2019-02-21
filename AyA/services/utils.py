import os
import json
from django.conf import settings


def create_jsons(ProxmoxData,ZabbixDB):
    pass


# Esta funcion es en caso de que se utilicen los jsons.

def get_content(Servicio,Proxmox,path=os.path.join(settings.BASE_DIR,'hosts_measurement','data')):

        # Ir por cada archivo y extraer los datos para guardar en Django
        #path: archivo donde se encuentran los archivos
        #del tipo 'ip_prox.json'
        for root,dirs,files in os.walk(path):
            if root == path:
                jsons = [os.path.join(root,file) for file in files if file.endswith('.json') and file.startswith('10.8')]
                break
        #print(jsons)
        ips = [os.path.splitext(os.path.basename(json))[0] for json in jsons]
        
        for file,ip in zip(jsons,ips):
                print('\nProcessing file:',os.path.basename(file)+'\n\n')
                fp = open(file)
                service_list = json.load(fp)
                save_service(Servicio,Proxmox,service_list,ip)


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
                                           description='')
                    new_service.save()
        except:
            # No existe el proxmox guardado en la base de datos de django
            # guardarlo primero mediante la interfaz y despues obtener lista de servicios
            return
            



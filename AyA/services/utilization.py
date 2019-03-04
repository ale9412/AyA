import json
import os
import mysqldb
from datetime import datetime
#from readingdbmodif import percentil , rank , mean
from statistics import mean

#TODO:Revisar y quitar los comentarios
def utilization(user_zabbix, ip_zb, password_zabbix, db_addr, st, et, ip_prox ,usr_new ,usr_futurs):
    # Conversion de las fechas
    start_time = datetime.timestamp(datetime.strptime(st, "%d/%m/%Y"))
    end_time = datetime.timestamp(datetime.strptime(et, "%d/%m/%Y"))

    # with open('user_zabbix.json'.format(os.path.join(os.getcwd(),'data'))) as s:
    # 	user_zabbix = json.load(s)
    # dict_future = []
    # usuarios_presentes = int(16)
    # usuarios_nuevos = int(20)
    # usuarios_futuros = int(30)

    # importando variables
    # os.makedirs(os.path.join(os.getcwd(), 'data',
    #                          'utilizacion'), exist_ok=True)
    # os.makedirs(os.path.join(os.getcwd(), 'data', 'futura'), exist_ok=True)

    f = open('{}.json'.format(os.path.join(os.getcwd(), 'data', ip_prox)), 'r')
    parser = json.load(f)
    f.close()

    dic_parser = {}
    for element in parser:
        dic_parser[element['nombre_servicio']] = element['cores']
    # print(dic_parser)

    frecuency = round(float(parser[0]['frecuencia cpu prox']), 2)

    # count=1
    for dicc in parser:
        keys = dicc['nombre_servicio']
        # print(keys)
        hostid = dicc['hostid']
        # f = open('{}.json'.format(os.path.join(
        #     os.getcwd(), 'data', 'utilizacion', keys)), 'w')
        # g = open('{}.json'.format(os.path.join(
        #     os.getcwd(), 'data', 'futura', keys)), 'w')
        dic2 = mysqldb.get_service_values(
            keys, hostid, start_time, end_time, user_zabbix, ip_zb, password_zabbix, db_addr)
        vcpu_asig = dic_parser[keys]
        # print(vcpu_asig)
        # print("----------------------------------------",count,"--------------------------")
        #count = count+1
        lista_avg = []
        lista_max = []
# Arreglando RAM y 95%
        for element in dic2[0]['value_avg']:  # valor promedio de la RAM
            # print(element)
            lista_avg.append(round(element[0]/1000000, 2))

        try:
            dic2[0]['value_avg'] = round(mean(lista_avg), 2)
        except:
            dic2[0]['value_avg'] = "None"
        # print('diccionario ram', dic2[0]['value_avg'])

        for element in dic2[0]['value_max']:
            tmp = round(element[0]/1000000, 2)
            lista_max.append(tmp)
        try:
            dic2[0]['value_max'] = max(lista_max)
        except:
            dic2[0]['value_max'] = "None"
        try:
            dic2[0]['percentil'] = round(max(lista_max)*0.95, 2)
        except:
            dic2[0]['percentil'] = "None"
        lista_avg.clear()
        lista_max.clear()
        # lista_95 = []


# Espacio_disco

        for element in dic2[1]['value_avg']:
            # print(element)
            lista_avg.append(round(element[0]/1000000, 2))

        try:
            dic2[1]['value_avg'] = round(mean(lista_avg), 2)
        except:
            dic2[1]['value_avg'] = "None"

        for element in dic2[1]['value_max']:
            tmp = round(element[0]/1000000, 2)
            lista_max.append(tmp)
        try:
            dic2[1]['value_max'] = max(lista_max)
        except:
            dic2[1]['value_max'] = "None"
        try:
            dic2[1]['percentil'] = round(max(lista_max)*0.95, 2)
        except:
            dic2[1]['percentil'] = "None"
        lista_avg.clear()
        lista_max.clear()

# Incoming Network trafic
        for element in dic2[2]['value_avg']:
            # print(element)
            lista_avg.append(round(element[0]/1000, 2))

        try:
            dic2[2]['value_avg'] = round(mean(lista_avg), 2)
        except:
            dic2[2]['value_avg'] = "None"

        for element in dic2[2]['value_max']:
            # tmp=round(element[0]/1000000,2)
            lista_max.append(round(element[0]/1000, 2))
        try:
            dic2[2]['value_max'] = max(lista_max)
        except:
            dic2[2]['value_max'] = "None"
        try:
            dic2[2]['percentil'] = round(max(lista_max)*0.95, 2)
        except:
            dic2[2]['percentil'] = "None"
        lista_avg.clear()
        lista_max.clear()
# outgoin_network_trafic
        for element in dic2[3]['value_avg']:
            # print(element)
            lista_avg.append(round(element[0]/1000, 2))

        try:
            dic2[3]['value_avg'] = round(mean(lista_avg), 2)
        except:
            dic2[3]['value_avg'] = "None"

        for element in dic2[3]['value_max']:
            # tmp=round(element[0]/1000000,2)
            lista_max.append(round(element[0]/1000, 2))
        try:
            dic2[3]['value_max'] = max(lista_max)
        except:
            dic2[3]['value_max'] = "None"
        try:
            dic2[3]['percentil'] = round(max(lista_max)*0.95, 2)
        except:
            dic2[3]['percentil'] = "None"
        lista_avg.clear()
        lista_max.clear()


# CPU
        for element in dic2[4]['value_avg']:
            lista_avg.append(round(element[0]*frecuency*vcpu_asig, 2))

        try:
            dic2[4]['value_avg'] = round(mean(lista_avg), 2)
        except:
            dic2[4]['value_avg'] = "None"

        for element in dic2[4]['value_max']:
            # tmp=round(element[0]*frecuency*vcpu_asig,2)
            lista_max.append(round(element[0]*frecuency*vcpu_asig, 2))
            # lista_95.append(round(tmp*0.95,2))

        try:
            dic2[4]['value_max'] = max(lista_max)
        except:
            dic2[4]['value_max'] = "None"
        try:
            dic2[4]['percentil'] = round(max(lista_max)*0.95, 2)
        except:
            dic2[4]['percentil'] = "None"

        lista_max.clear()
        lista_avg.clear()

# Storage
# iostat
        for element in dic2[5]['value_avg']:
            lista_avg.append(round(element[0], 2))
        try:
            dic2[5]['value_avg'] = round(mean(lista_avg), 2)
        except:
            dic2[5]['value_avg'] = "None"

        for element in dic2[5]['value_max']:
            lista_max.append(round(element[0], 2))
        try:
            dic2[5]['value_max'] = max(lista_max)
        except:
            dic2[5]['value_max'] = "None"
        try:
            dic2[5]['percentil'] = round(max(lista_max)*0.95, 2)
        except:
            dic2[5]['percentil'] = "None"
        lista_max.clear()
        lista_avg.clear()

# read
        # print('Diccionario completo',dic2[6])
        # print(lista_avg)
        for element in dic2[6]['value_avg']:
            lista_avg.append(round(element[0], 2))
            # print(lista_avg)
        # a = mean(lista_avg)
        # print(a)
        try:
            dic2[6]['value_avg'] = round(mean(lista_avg), 2)
        except:
            dic2[6]['value_avg'] = "None"
        for element in dic2[6]['value_max']:
            lista_max.append(round(element[0], 2))
        try:
            dic2[6]['value_max'] = max(lista_max)
        except:
            dic2[6]['value_max'] = 'None'
        try:
            dic2[6]['percentil'] = round(max(lista_max)*0.95, 2)
        except:
            dic2[6]['percentil'] = "None"
        # print('Dicc de lectura',dic2[6])
        lista_max.clear()
        lista_avg.clear()

# write
        for element in dic2[7]['value_avg']:
            lista_avg.append(round(element[0], 2))
        try:
            dic2[7]['value_avg'] = round(mean(lista_avg), 2)
        except:
            dic2[7]['value_avg'] = "None"

        for element in dic2[7]['value_max']:
            lista_max.append(round(element[0], 2))
        try:
            dic2[7]['value_max'] = max(lista_max)
        except:
            dic2[7]['value_max'] = "None"
        try:
            dic2[7]['percentil'] = round(max(lista_max)*0.95, 2)
        except:
            dic2[7]['percentil'] = "None"
        lista_max.clear()
        lista_avg.clear()

        f = open('{}.json'.format(os.path.join(
            os.getcwd(), 'data', 'utilizacion', keys)), 'w')


        # print(dic2)
        json.dump(dic2, f)
        f.close()

# Utilizacion futura
        dict_future = []
        for element in dic2:
            # print(element['value_max'], type(element['value_max']))
            if element['value_max'] == 'None':
                element['value_max'] = 'None'
            else:
                element['value_max'] = round(
                    element['value_max'] * int(usr_new)/int(usr_futurs),2)

            if element['value_avg'] == 'None':pass
            else:
                element['value_avg'] = round(element['value_avg']* int(usr_new)/int(usr_futurs),2)

            if element['percentil'] == 'None':
                element['percentil'] = 'None'
            else:
                element['percentil'] = round(
                    element['percentil'] * int(usr_new)/int(usr_futurs),2)

            dict_future.append(element)
        g = open('{}.json'.format(os.path.join(
            os.getcwd(), 'data', 'futura', keys)), 'w')


        json.dump(dict_future, g)
        g.close()


# utilization("zabbixinfo", "10.8.6.164", '1234', 'zabbix',
#             '1/2/2019', '2/2/2019', "10.8.9.15")
# utilization ("zabbixinfo","10.8.6.164","1234","zabbix","18/12/2018",'20/12/2018','10.8.9.53')
# utilization ('zabbixinfo','10.8.6.164','1234','zabbix','18/12/2018','20/12/2018','10.8.9.57')

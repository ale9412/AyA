from services.relation import relation_prox_zabbix as rpz
from services.utilization import utilization
import os
#TODO:Quitar todos los comentarios y los scripts que no funcionan
def start(usrs_act, usrs_new, usrs_futrs ,ip_prox ,passwd_prox ,ip_zabbix ,usr_zabbix ,db_zabbix ,passwd_zabbix ,start_time ,end_time ):
    os.makedirs(os.path.join(os.getcwd(),'data',),exist_ok= True)
    os.makedirs(os.path.join(os.getcwd(),'data', 'utilizacion'),exist_ok= True)
    os.makedirs(os.path.join(os.getcwd(),'data', 'futura'),exist_ok= True)

    rpz(passwd_prox, ip_prox,usr_zabbix,passwd_zabbix, ip_zabbix,db_zabbix)
    utilization(usr_zabbix, ip_zabbix, passwd_zabbix, db_zabbix, start_time, end_time, ip_prox ,usrs_new ,usrs_futrs)

# start(10, 15, 20 ,"10.8.9.15" ,"team_manager*" ,"10.8.6.164" ,"zabbixinfo" ,'zabbix' ,'1234' ,"1/2/2019" ,'2/2/2019' )
# start(10, 15, 20 ,"10.8.9.53" ,"team_manager*" ,"10.8.6.164" ,"zabbixinfo" ,'zabbix' ,'1234' ,"1/2/2019" ,'2/2/2019' )
# start(10, 15, 20 ,"10.8.9.57" ,"team_manager*" ,"10.8.6.164" ,"zabbixinfo" ,'zabbix' ,'1234' ,"1/2/2019" ,'2/2/2019' )
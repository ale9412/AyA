from django.db import models

class ProxmoxData(models.Model):
    servername = models.CharField('Server Name',max_length=30)
    username = models.CharField('Username',max_length=30,default='root')
    password = models.CharField('Password',max_length=30)
    address = models.CharField('Ip Address',max_length=30)

class ZabbixDB(models.Model):
    username = models.CharField('Username',max_length=30,default='root')
    address = models.CharField('Zabbix Ip',max_length=30)
    password = models.CharField('Zabbix Password',max_length=30)
	
class ExtraData(models.Model):
    current_users = models.IntegerField()
    new_users = models.IntegerField()
    future_users = models.IntegerField()
    start_time = models.DateTimeField('Tiempo de Inicio')
    end_time = models.DateTimeField('Tiempo de Fin')




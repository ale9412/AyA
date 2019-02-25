from django.db import models

class ProxmoxData(models.Model):
    servername = models.CharField('Server Name',max_length=30)
    username = models.CharField('Username',max_length=30,default='root')
    password = models.CharField('Password',max_length=30)
    address = models.CharField('Ip Address',max_length=30)

    def __str__(self):
        return "{}".format(self.servername)

class ZabbixDB(models.Model):
    username = models.CharField('Username',max_length=30,default='root')
    address = models.CharField('Zabbix Ip',max_length=30)
    password = models.CharField('Zabbix Password',max_length=30)
	
class ExtraData(models.Model):
    current_users = models.IntegerField()
    new_users = models.IntegerField()
    future_users = models.IntegerField()
    start_time = models.CharField('Tiempo de Inicio',max_length=30)
    end_time = models.CharField('Tiempo de Fin',max_length=30)




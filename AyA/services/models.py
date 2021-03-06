from django.db import models

from data.models import ProxmoxData

class Servicio(models.Model):
    name = models.CharField('Service Name',max_length=30)
    proxmox = models.ForeignKey(ProxmoxData,on_delete=models.CASCADE)
    hostid = models.IntegerField(primary_key=True)
    hypervisor = models.CharField("Hypervisor",max_length=30)
    cores = models.IntegerField(verbose_name="Nucleos")
    core_freq = models.DecimalField(verbose_name='Frequencia del procesador', decimal_places=3,max_digits=10)

    def __str__(self):
    	return '{}'.format(self.name)


class CurrentUtilization(models.Model):
    metric = models.CharField("Metrica",max_length=30)
    service = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    average = models.CharField(max_length=30)
    maximum = models.CharField(max_length=30)
    percentil = models.CharField(max_length=30)

    def __str__(self):
    	return '{}'.format(self.metric)
        

class FutureUtilization(models.Model):
    metric = models.CharField("Metrica",max_length=30)
    service = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    average = models.CharField(max_length=30)
    maximum = models.CharField(max_length=30)
    percentil = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.metric)

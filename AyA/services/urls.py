from django.conf.urls import url
from services.views import ServiceLXCView,ServiceKVMView,DeleteAllView, gather_service,About,start_procedure,currentUtilization,\
    FutureUtilization

app_name = 'services'



urlpatterns = [
    url('^servicios_lxc/',ServiceLXCView.as_view(),name='servicios_lxc'),
    url('^servicios_kvm/',ServiceKVMView.as_view(),name='servicios_kvm'),
    url('^servicios_borrar/',DeleteAllView.as_view(),name='delete_all'),
    url('^gather_service/',gather_service,name='gather_service'),
    url('^about/',About.as_view(),name='about'),
    url('^start_procedure/',start_procedure, name='start_procedure'),
    url('^current/',currentUtilization,name='current'),
    url('^future/',FutureUtilization.as_view(),name='future'),
]


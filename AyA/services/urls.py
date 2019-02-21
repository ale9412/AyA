from django.conf.urls import url
from services.views import ServiceListView,DeleteAllView, gather_service,About,start_procedure,currentUtilization,\
    FutureUtilization

app_name = 'services'



urlpatterns = [
    url('^servicios_listar/',ServiceListView.as_view(),name='servicios_listar'),
    url('^servicios_borrar/',DeleteAllView.as_view(),name='delete_all'),
    url('^gather_service/',gather_service,name='gather_service'),
    url('^about/',About.as_view(),name='about'),
    url('^start_procedure/',start_procedure, name='start_procedure'),
]

urlpatterns = [
	url('^current/',currentUtilization,name='current'),
	# url('^future/',FutureUtilization.as_view(),name='future'),
]

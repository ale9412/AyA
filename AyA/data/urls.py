from django.conf.urls import url
from data.views import ProxmoxDataView,ZabbixDataView,ServerList,ProxmoxDelete,ZabbixDelete,ProxmoxUpdateView,ZabbixUpdateView,\
    EditUsers, ShowUsers, InsertUsers, DeleteUsers

app_name = 'data'

urlpatterns = [
	#url('^servers_data/',servers_data,name='servers_data'),
    url('^proxmox_data/',ProxmoxDataView.as_view(),name='proxmox_data'),
    url('^zabbix_data/',ZabbixDataView.as_view(),name='zabbix_data'),
    url('^servers_list/',ServerList.as_view(),name='servers_list'),
    url(r'^delete_prox/(?P<pk>\d+)/',ProxmoxDelete.as_view(),name='delete_prox'),
    url(r'^delete_zab/(?P<pk>\d+)/',ZabbixDelete.as_view(),name='delete_zab'),
    url(r'^update_prox/(?P<pk>\d+)/',ProxmoxUpdateView.as_view(),name='update_prox'),
    url(r'^update_zab/(?P<pk>\d+)/',ZabbixUpdateView.as_view(),name='update_zab'),
    url(r'edit_users/(?P<pk>\d+)/',EditUsers.as_view(), name='edit_users'),
    url('user_list/',ShowUsers.as_view(),name='user_list'),
    url('insert_users/',InsertUsers.as_view(),name='insert_users'),
    url(r'delete_users/(?P<pk>\d+)/',DeleteUsers.as_view(), name='delete_users'),
    url('user_list/',ShowUsers.as_view(),name='user_list'),    
    ]

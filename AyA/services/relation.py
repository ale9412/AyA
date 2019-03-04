import re,subprocess
import mysql.connector as mysql
import json,os

def relation_prox_zabbix(password_prox, ip_prox,user_zabbix,password_zabbix, ip_zabbix,database_zabbix):
	
	with subprocess.Popen(['sshpass','-p',password_prox,'ssh',"root" + "@" + ip_prox ,'cat','/proc/cpuinfo' ],stdout = subprocess.PIPE) as p:
		output = p.stdout.read().decode()
	info=output.split("\n")
	frecuency= [x.strip().split(":")[1] for x in info if "cpu MHz" in x]


	with subprocess.Popen(['sshpass','-p',password_prox,'ssh','root' + "@" + ip_prox,'pct', 'list'],stdout = subprocess.PIPE) as l:
		output0 = l.stdout.read().decode()
	
	pattern = re.compile(r'^(\d\d\d)', flags=re.MULTILINE)
	id_list = re.findall(pattern,output0) 
	
	ip_list = []
	# print(id_list)
	for i in id_list:
		dic={}
		with subprocess.Popen(['sshpass','-p',password_prox,'ssh','root' + "@" + ip_prox ,'pct','config', i ],stdout = subprocess.PIPE) as p:
			output = p.stdout.read().decode()
		patt1 = re.compile(r'ip=(.*)/')
		try:
			patt2 = re.compile(r'cores:(.*)')
			core = patt2.search(output).group(1)
		except AttributeError as a:
			patt2 = re.compile(r'cpulimit:(.*)')
			core = patt2.search(output).group(1)
		
		IP_PROX = patt1.search(output).group(1)
		# print('core:',core,'id:',i,'ip:',IP_PROX)
		
		dic["cores"]=int(core)
		dic["id"]=str(i)
		dic["ip"]=str(IP_PROX)	
		ip_list.append(dic)
		# print(ip_list)
		# dic.clear()
		# print(ip_list)
	
	
	name_zabbix = []
	# Es una herramienta aparte para saber los hosts que no se estan monitorizando en el zabbix
	ip_no_monitorizados=[]
	conn = mysql.connect(user=user_zabbix , password=password_zabbix, host=ip_zabbix ,database=database_zabbix)
	cursor = conn.cursor(buffered=True)
	dic1={}
	# print(ip_list)
	for i in ip_list:
		cursor.execute('select hostid from interface where ip ="%s";'%i["ip"])        
		data = cursor.fetchone()
		if str(data)=='None':
			ip_no_monitorizados.append(i["ip"])	
		else:
			hostid=str(data[0])
			cursor.execute('select name from hosts where hostid="%s";'%hostid)        
			name = str(cursor.fetchone()[0])

			dic1[name]={}
			dic1[name]["id"]=i["id"]
			dic1[name]["hostid"]=hostid		
			dic1[name]["ip"]=i["ip"]
			dic1[name]["cores"]=i["cores"]	
			print(dic1)
	list_lxc = []

	for name in dic1.keys():
		dic={}
		dic["nombre_servicio"]=name
		dic["frecuencia cpu prox"]=str(frecuency[0])
		dic['hostid']=dic1[name]['hostid']
		dic['cores']=dic1[name]['cores']
		list_lxc.append(dic)
		# dic.clear()

	print(list_lxc)	
	
	with open('{}.json'.format(os.path.join(os.getcwd(), 'data', ip_prox)), 'w') as f:
        	json.dump(list_lxc,f)
        	f.close()



    #Devuelve el json que esta en /data/(ip_prox).json
	return list_lxc 		






	
import mysql.connector as mysql
from datetime import datetime

trends_list = ['CPU Usage','iostat.sda', 'read.sda', 'write.sda', ]
trends_uint_list = ['RAM-used', 'Used disk space on $1','Incoming network traffic on $1','Outgoing network traffic on $1']
itemid_trends = []
itemid_uint_trends = []




def values_trends( cursor,itemid_list, start_time, end_time):
	item_values = []
	dicc={}
	for dic in itemid_list:
		cursor.execute('select value_avg from trends where itemid="%s" and clock>="%s" and clock<="%s" ;' % (dic['itemid'], start_time, end_time))
		avg = cursor.fetchall()
		cursor.execute('select value_max from trends where itemid="%s" and clock>="%s" and clock<="%s" ;' % (dic['itemid'], start_time, end_time))
		maxm = cursor.fetchall()
		dicc['item_name']=dic['item_name']
		dicc['value_max']= maxm
		dicc['value_avg']= avg
		item_values.append(dicc)
		dicc={}
	# print(item_values)        
	return item_values

def values_trends_uints(cursor, itemid_list, start_time, end_time):
    item_values = []
    dicc={}
    for dic in itemid_list:
        cursor.execute('select value_avg from trends_uint where itemid="%s" and clock>="%s" and clock<="%s";' % (dic['itemid'], start_time, end_time))
        avg = cursor.fetchall()
        cursor.execute('select value_max from trends_uint where itemid="%s" and clock>="%s" and clock<="%s";' % (dic['itemid'], start_time, end_time))
        maxm = cursor.fetchall()
        dicc['item_name']= dic['item_name']
        dicc['value_max']= maxm
        dicc['value_avg']= avg
        item_values.append(dicc)
        dicc={}
    return item_values

def get_service_values(name, hostid , start_time,end_time, zb_user,zb_ip,zb_psswd,zb_db):
	conn = mysql.connect(user=zb_user, host=zb_ip, password=zb_psswd, database=zb_db)
	cursor = conn.cursor(buffered=True)
	list_trends_name_itemid = []
	dic={}
	
	
	for item_name in trends_list:
		#print(item_name)
		sintax = 'select itemid from items where hostid="%s" and name="%s" ;' % (hostid, item_name)
		cursor.execute(sintax)
		item = cursor.fetchone()
		dic['item_name'] = item_name
		dic['itemid'] = item[0]
		#print(type(item[0]))
		list_trends_name_itemid.append(dic)
		#print(list_trends_name_itemid)
		dic={}
	trends_values = values_trends( cursor,list_trends_name_itemid, start_time, end_time)
	#print(trends_values)
	list_tu_name_itemid = []

	for item_name in trends_uint_list:
		#print(item_name)
		sintax = 'select itemid from items where hostid="%s" and name="%s" ;' % (hostid, item_name)
		cursor.execute(sintax)
		item = cursor.fetchone()
		#print(item)
		if item != None:
			dic['item_name'] = item_name
			dic['itemid'] = item[0]
			#print(item)
			#print(dic)
			list_tu_name_itemid.append(dic)		
			dic={}
		else:
			continue	
		#print(list_tu_name_itemid)	
	values = values_trends_uints(cursor,list_tu_name_itemid,start_time,end_time)


	for element in trends_values:
		values.append(element)

	#print(values)
	return values




def close(conn):
    conn.close()


def main(start_time, end_time, itemid_list, user, password, host, database='zabbix'):
    conn, cursor = connect(user, host, password, database)
    value_list = execute(cursor, itemid_list, start_time, end_time)
    close(conn)
    return value_list


#start_time="21/12/2018"
#st=datetime.timestamp(datetime.strptime(start_time,'%d/%m/%Y'))
#end_time="18/12/2018"
#et=datetime.timestamp(datetime.strptime(end_time,"%d/%m/%Y"))
#get_service_values('SqStat','10201',st,et,'zabbixinfo','10.8.6.164','1234','zabbix')

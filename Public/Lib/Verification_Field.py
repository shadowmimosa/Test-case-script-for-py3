#coding=utf-8
#脚本作用：公共json数据校验方法，遍历data数据，判断指定的字段是否在实际的返回中存在。



import logging
import json
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')


#logging.basicConfig(level=logging.INFO)


def CheckField(data,checkfeild,ignore=None):
	'''
	1、验证传入data 中没有包括checkfeild中必须存在的字段；
	2、data可以为列表 字符串、字典；checkfeild为字符串表示要检查的字段名，多个字段名用逗号分隔,如fid,sid
	3、ignore 参数当为非空时，在验证不通过时不会报错，会返回0，ignore为空时，验证不通过会失败报错！
	3、入参格式: CheckField 	${data}	  field1,field2    1
	4、field1,field2 的值不为空;即要满足字符串不为空，int>=0,list不为空，字典不空；
	'''
	# print "传入data的类型为:%s"%type(data)

	if type(data)==list:
		pass
	elif type(data)==dict:
		pass
	else:
		data=json.loads(data)

	if type(checkfeild)!=list:
		checkfeild=unicodeConvList(checkfeild)
		logging.info('checkfeild={}'.format(checkfeild))
	list2= []
	list2= Sub_Isnotempty(data,None,None,checkfeild,list2)
	logging.info(checkfeild)
	logging.info(list2)
	yesNo=listContain(checkfeild,list2)
	for c in checkfeild:
		if '-Invalid' not in c:
			logging.info('[#{}] appears [#{}] times'.format(c,list2.count(c)))
	if yesNo:
		logging.info('Oh,yes! This is PASS!!')
		return  yesNo
	else:
		if ignore:
			return  yesNo
		raise AssertionError("my god! It is Fail !!")
	
	

	

def listContain(listx,listd):
	'''
	#判断listx中的值list2中，且不在的值打印出来
	#listx的所有值都在list2中（即listx<=List2），则返回1，反之返回0
	'''
	error=[]
	ispas=1
	for i in listx:
		if i in listd:
			continue
		else:
			error.append(i)
	if error:
		ispas=0
		for i in xrange(len(error)):
			if '-Invalid' not in error[i]:
				logging.info(("非常遗憾！！在列表源中未发现待检查列表的【%s】字段！！！"%(error[i])).decode('utf-8'))
			else:
				logging.info(("非常遗憾！！在列表源【%s】字段值异常(为空)！！！"%(error[i])).decode('utf-8'))
			pass
	return  ispas




def unicodeConvList(datas):
	'''
	#将unicode字符串转换成list列表，保证从RF中传入的参数为列表
	#data为字符串,用逗号隔开,可转化为列表
	#返回的值为列表
	#例如：unicodeconvlist('a,b,c');unicodeconvlist('[a,b,c]')
	'''
	if type(datas)!=list:
		datalist=[]
		data_str=str(datas)
		data_str_list= data_str.split(',')

		for i in xrange(len(data_str_list)):

			if '[' in data_str_list[i] and ']' in data_str_list[i]:
				  datalist.append(data_str_list[i].replace('[','').replace(']',''))

			elif '[' in data_str_list[i]:
				datalist.append(data_str_list[i].replace('[',''))

			elif ']' in data_str_list[i]:
				datalist.append(data_str_list[i].replace(']',''))

			else:
				datalist.append(data_str_list[i])

		return datalist



def Sub_Isnotempty(subdata,retype=None,countnull=None,checkfeildlist=None,backfeild=None):
	'''
	#不论item为何种类型，最终还是拆解成最小单元（字符串或整型），并将所有key返回至列表，
	#并将所有拆出来的字段拼接在itemfeild列表中；
	#checkfeildlist为字段集列表，对item中checkfeildlist列表字段进行空校验
	#校验不通过，将不通的字段做一些处理（格式：字段=类型Invalid）再增加至checkfeildlist；并打印来
	#不论校验是否通过，都返回itemfeild列表，此列表为原始列表+item中字段；
	retype为空时，只对checkfeildlist中字段进行校验是否为空,并返回所有item中的字段；
	retype不为空时；对item中所有字段进行是否为空校验，返回不为空的字段个数
	'''
	if backfeild is None:
		backfeild=[]
	if countnull is None:
		countnull=0
	if retype is None:
		retype=0
	#logging.info('BackList={}'.format(backfeild))
	if isinstance(subdata,str):
		if retype:
			k=Isnotempty(subdata,1)
			print k
			if k==0:
				countnull=countnull+1
		else:
			pass
	elif isinstance(subdata,(int,long)):
		if retype:
			k=Isnotempty(subdata,1)
			if k==0:
				countnull=countnull+1
	elif isinstance(subdata,list):
		item_len=len(subdata)
		if retype:
			k=Isnotempty(subdata,1)
			if k==0:
				countnull=countnull+1
		for i in range(item_len):
			#logging.info('list={}'.format(subdata[i]))
			Sub_Isnotempty(subdata[i],retype,countnull,checkfeildlist,backfeild)

	elif isinstance(subdata,dict):
		value_dict_len=len(subdata)
		if retype:
			k=Isnotempty(subdata,1)
			if k==0:
				countnull=countnull+1
		for key,value in subdata.items():
			backfeild.append(key)
			# logging.info('dictkey={}'.format(key))  
			# logging.info('dictvalue={}'.format(value))  
			if key in checkfeildlist:
				checkrs=Isnotempty(value)
				if checkrs != 1:
					checkey=key+'='+checkrs
					checkfeildlist.append(checkey)
					logging.info('{}:#{}# check result NG'.format(key,value))
			Sub_Isnotempty(value,retype,countnull,checkfeildlist,backfeild)
	# elif subdata in ['',' ','\'\'',None,'\' \'']:
			# if retype:
				# k=Isnotempty(subdata,1)
				# if k==0:
					# countnull=countnull+1
			# else:
				
		# else:
			# subdata=str(subdata)
			# print  'unicode:{}'.format(subdata).encode('GB2312')
			# subdata=json.loads(subdata)
			# Sub_Isnotempty(subdata,retype,countnull,checkfeildlist,backfeild)
	if retype:
		return  countnull
	else:
		return   backfeild

def Isnotempty(obj=None,backtype=None):
	'''
	#检查对象是否不为空
	#对字符类型："",空,空格时会返回Str-Invalid
	#对Int类型：<0时会返回Int-Invalid
	#对list类型：为空时会返回List-Invalid
	#对Dict类型：为空时会返回Dict-Invalid
	#其他值返回1
	#如retype有值，则对象为空返回0，不为空返回1
	'''
	rs=1
	if obj in ['',None]:
		rs='None-Invalid'
	elif isinstance(obj,str):
		if obj in ['\"\"',' ','\'\'',' \'\'']:
			rs='Str-Invalid'
	elif isinstance(obj,(int,long)):
		if int(obj)<0:
			rs='Int-Invalid'
	elif isinstance(obj,list):
		obj_len=len(obj)
		if  obj_len<=0:
			rs='List-Invalid'
	elif isinstance(obj,dict):
		value_dict_len=len(obj)
		if  value_dict_len<=0:
			rs='Dict-Invalid'		
	else:
		obj=str(obj)
		rs=Isnotempty(obj)
	if backtype:
		if rs!=1:
			rs=0		
	return rs
		



if __name__ == '__main__':
	data1 = [{"songId": 8269,
			 "singerId": 5785,
			 "hash": "A31F9FBFC5E73AA93CBF7EC1C6247A98",
			 "recomflag": 5,
			 "singerName": "1",
			 "singerImg": "20140117151145992387.jpg",
			 "startTime": 75000,
			 "climaxHash": "B349729F8E040F849C532C904B2A4C22",
			 "krc": "jj"},

			[{"songId": 8269,
			  "singerId": 5785,
			  "hash": "A31F9FBFC5E73AA93CBF7EC1C6247A98",
			  "recomflag": 5,
			  "singerName": "1",
			  "singerImg": "20140117151145992387.jpg",
			  "startTime": 75000,
			  "climaxHash": "B349729F8E040F849C532C904B2A4C22",
			  "krc": "jj"}]]

	test1 = ['songId', 'hash', 'singerId']
	CheckField(data1,test1)


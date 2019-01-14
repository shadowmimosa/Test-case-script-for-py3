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
	list2= analysis_subItem(data,checkfeild,list2)
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
	
	

	

def listContain(list1,list2):
	'''
	#判断list1中的值list2中，且不在的值打印出来
	#list1的所有值都在list2中，则返回1，反之返回0
	'''
	error=[]
	ispas=1
	for i in list1:
		if i in list2:
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




def unicodeConvList(data):
	'''
	#将unicode字符串转换成list列表，保证从RF中传入的参数为列表
	#data为字符串,用逗号隔开,可转化为列表
	#返回的值为列表
	#例如：unicodeconvlist('a,b,c');unicodeconvlist('[a,b,c]')
	'''
	if type(data)!=list:
		datalist=[]
		data_str=str(data)
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


#判断value值对应的类型，从而进行相应的处理，嵌入递归函数
def analysis_subItem(item,checkfeild,itemfeild=None):
	'''
	1、不管value值取出如何，最终还是拆解成最小单元，字符串或者是整型来进行判断
	:return:
	'''
	if itemfeild is None:
		itemfeild=[]
	if isinstance(item,str):
		pass
	elif isinstance(item,int):
		if int(item)<0:
			raise AssertionError("int <0")

	elif isinstance(item,list):
		item_len=len(item)
		for i in range(item_len):
			analysis_subItem(item[i],checkfeild,itemfeild)

	elif isinstance(item,dict):
		value_dict_len=len(item)
		for key,value in item.items():
			itemfeild.append(key)
			if key in checkfeild:
				checkrs=checkobj(value)
				if checkrs != 1:
					checkey=key+'='+checkrs
					checkfeild.append(checkey)
					logging.info('{}:#{}# check result NG'.format(key,value))
			analysis_subItem(value,checkfeild,itemfeild)
	return   itemfeild

def checkobj(obj):
	'''
	#检查对象是否为空
	#对字符类型："",空,空格时会返回Str-Invalid
	#对Int类型：<0时会返回Int-Invalid
	#对list类型：为空时会返回List-Invalid
	#对Dict类型：为空时会返回Dict-Invalid
	#其他值返回1
	'''
	rs=1
	# logging.info(type(obj))	
	if isinstance(obj,str):
		if obj in ['','\"\"',' ']:
			rs='Str-Invalid'
	elif isinstance(obj,int):
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
		obj=obj.encode('utf-8')
		rs=checkobj(obj)
	return rs
		
#计算字符串长度
def get_length(item):
		length = _get_length(item)
		return length

def _get_length(item):
		try:
			return len(item)

		except:
			raise RuntimeError("Could not get length of '%s'." % item)



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


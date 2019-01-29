import sys,os,platform
import time,traceback,logging
import subprocess,random,re

# run.py  test  api,advertapi   e:/log   JoyrunEvn:Beta
# system discrimination
ostype = sys.platform   
copycmd='cp'
copyoption='-r'
cpoption='/.'
print('os type is:[{}]'.format(ostype))   
if  ostype=='win32'  or  ostype=='win64':
	pwd=os.popen('cd').readlines()[0]
	copycmd='copy'
	copyoption='/y'
	cpoption=''
else:
    pwd=os.popen('pwd').readlines()[0]


	
home=pwd.replace('\n','')
print ('Home=={}'.format(home))
print ('copycmd=={}'.format(copycmd))

#Environmental discrimination
pyvs=sys.version_info.major
py3path=os.path.join(os.path.join(home,'Public_PY3'),'Public')
print('PY3 Public path=={}'.format(py3path))
RunPublic=os.path.join(home,'Public')
print('Run Public path=={}'.format(RunPublic))
if pyvs==3:
	print('python version is  3')
	copyrz=os.popen('{}  {}   {}{}    {}'.format(copycmd,copyoption,py3path,cpoption,RunPublic)).readlines()[0]
	print(copyrz)
elif pyvs==2:
	print('python version is  2')
else:
	AssertionError("Python Environmental anomaly") 
	
#Run Environmental
cmdpamlen=len(sys.argv)
print('Input argvLen is [{}]'.format(cmdpamlen))
for i in range(0,cmdpamlen):
	print('Script parameter[{}] is {}'.format(i,sys.argv[i]))
# Environmental= raw_input("please Enter Environmental:[Test/Beta/Online]")
Label='Test'
Env='Beta'
if cmdpamlen>=2:
	Env=sys.argv[1]
print('Input Env is [{}]'.format(Env))
if Env in  ['Test','test','0',0]:
	Label='Test'
	Vfile=os.path.join(os.path.join(home,'Public'),'JoyrunTestEnv_var.py')	
elif Env in  ['Beta','beta','BeataEnv','betaenv','1',1,None]:
	Label='Test'
	Vfile=os.path.join(os.path.join(home,'Public'),'JoyrunBetaEnv_var.py')
else:
	Label='Online'
	Vfile=os.path.join(os.path.join(home,'Public'),'JoyrunOnline_var.py')
print('Run Env is [{}]'.format(Env))
print('Run Label is [{}]'.format(Label))
print('Run Vfile is [{}]'.format(Vfile))


# reportpath=  raw_input("please robot_cmd  report path  -d:[JoyrunEvn:Online]")
Runpath=home
if cmdpamlen>=3:
	rpath=sys.argv[2]
	if rpath  not in ['Home','home','All','all']:
		if ',' not in rpath:
			Runpath=os.path.join(home,rpath)
		else:
			rplist=rpath.split(',')
			for paths in rplist:
				if Runpath==home:
					Runpath=os.path.join(home,paths)
				else:
					path_n=os.path.join(home,paths)
					Runpath=Runpath + '  ' + path_n
	print('Run Script Path is {}'.format(Runpath))

reportpath=0
if cmdpamlen>=4:
	reportpath=  sys.argv[3]
	
Varpam=0	
if cmdpamlen>=5:
	# Varpam=  raw_input("please robot_cmd  --variable:[JoyrunEvn:Online]")
	Varpam=  sys.argv[4]
	if ':' not in Varpam:
		Varpam='JoyrunEvn:Beta'
	print('robot_cmd  --variable is  [{}]'.format(Varpam))

# cmd    --variable  JoyrunEvn:Online   -d /var/lib/jenkins/Report/$1  
robot_cmd='pybot --include {}    -V   {}     {}'.format(Label,Vfile,Runpath)
if reportpath!=0 and Varpam!=0:
	robot_cmd='pybot --include {}   --variable  {}  -V   {}  -d  {}   {}'.format(Label,Varpam,Vfile,reportpath,Runpath)
elif reportpath!=0 and Varpam==0:
	robot_cmd='pybot --include {}   -V   {}  -d  {}   {}'.format(Label,Vfile,reportpath,Runpath)
else:
	pass
print(robot_cmd)
print('*********************      Script  Running ...      *********************')
results=os.popen(robot_cmd).readlines(-1)
if pyvs==3:
	print(results)
elif pyvs==2:
	print('py2:{}'.format(results).encode('UTF-8'))
print('*********************     Script The End!!!         *********************')



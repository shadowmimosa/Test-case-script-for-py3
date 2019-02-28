import  os,sys,time,random

########config####################
copytimes=3
#Internal circulation:0   Running N times with the same parameter, one report
##external circulation:1  Running N times with different parameters, more report
runtype=0

userword='13829744552/67889911'

# is or no time desc copy 
isdesc=1
#2014-1-1   1388505600
starttime=1388505600
##Nowtime
Endtime=long(str(time.time())[0:10])


#step time 7days-5min
step=7*24*3600-300
runtime=3600*2

##Run Env
env='Test'

##copy runrecord id #test
fidlistTest=[99176582,99124547] 

###Beta
fidlistBeta=[99111037,99110934] 

fidlistOnline=[278080494,278033486]


##################################
i=0
runtext='integrate\Copyrunrecord.txt '
runtext2='integrate\Copyrunrecord.txt,'
Gpampexternal='{\'po.aspx\':{\'lasttime\':int-startime,\'starttime\':0000000000,\'dateline\':1111111111},\'Run/GetInfo.aspx\':{\'fid\':\'int-9999999999\'},\'userpass\':\'username/password\'}'
GpampInternal='{\'Run/GetInfo.aspx\':{\'fid\':\'int-9999999999\'},\'userpass\':\'username/password\'}'
if runtype==0:
	cmd='python  Run.py  Env_cmd  '+runtext+ ' Home   SRPam:'+ GpampInternal.replace('username/password',userword)
else:
	cmd='python  Run.py  Env_cmd  '+runtext+ ' Home   SRPam:'+ Gpampexternal.replace('username/password',userword)

if env in ['Test','TEST','test']:
	fidlist=fidlistTest
elif env in ['Online','ONLINE','online','ON']:
	fidlist=fidlistOnline
else:
	fidlist=fidlistBeta


try:
	if runtype==1:
		while i<=copytimes-1:
			print('######RunTimes:{}#########'.format(i+1))
			if isdesc==1:
				time=str(Endtime-i*step)
				timestart=str(Endtime-i*step-runtime)
				dateline=str(Endtime-i*step-runtime+120)
			else:
				time=str(starttime+i*step)
				timestart=str(starttime+i*step-runtime)
				dateline=str(starttime+i*step-runtime+120)
			cmd=cmd.replace('int-startime',time)
			cmd=cmd.replace('0000000000',timestart)
			cmd=cmd.replace('1111111111',dateline)
			cmd=cmd.replace('Env_cmd',env)
			fid=random.choice(fidlist)
			fid=str(fid)
			cmd=cmd.replace('int-9999999999',fid)
			rz = os.popen(cmd)
			cmd=cmd.replace(time,'int-startime')
			cmd=cmd.replace(timestart,'0000000000')
			cmd=cmd.replace(dateline,'1111111111')
			i=i+1
			rzline=rz.readline()
			while rzline:
				print(rzline)
				rzline=rz.readline()
			rz.close()
	else:
		cmd=cmd.replace('Env_cmd',env)
		fid=random.choice(fidlist)
		fid=str(fid)
		cmd=cmd.replace('int-9999999999',fid)
		if copytimes>1:
			runtextn=runtext2*(copytimes-1)
			runtextn=runtextn+runtext
			cmd=cmd.replace(runtext,runtextn)
		rz = os.popen(cmd)
		rzline=rz.readline()
		while rzline:
			print(rzline)
			rzline=rz.readline()
		rz.close()
except Exception as exc:
	print(exc)
import sys, os, platform
import time, traceback, logging
import subprocess, random, re

# run.py  test  api,advertapi   e:/log   JoyrunEvn:Beta
# system discrimination
ostype = sys.platform

home = os.path.dirname(os.path.abspath(__file__))

print('Home=={}'.format(home))

#Environmental discrimination
pyvs = sys.version_info.major

if pyvs == 3:
    print('python version is  V3.x')

    # On python3, rename folder.
    if not os.path.exists(os.path.join(home, 'Public_PY2')):
        try:
            os.rename(
                os.path.join(home, 'Public'), os.path.join(home, 'Public_PY2'))
            os.rename(
                os.path.join(home, 'Public_PY3'), os.path.join(home, 'Public'))
        except Exception as exc:
            print('Rename folder NOT successful!!! Please check it.')
            print('The exception is {}'.format(exc))
    else:
        print('Public_PY2 is existed.')

elif pyvs == 2:
    print('python version is  V2.x')

    if os.path.exists(os.path.join(home, 'Public_PY2')):
        try:
            os.rename(
                os.path.join(home, 'Public'), os.path.join(home, 'Public_PY3'))
            os.rename(
                os.path.join(home, 'Public_PY2'), os.path.join(home, 'Public'))
        except Exception as exc:
            print('Rename folder NOT successful!!! Please check it.')
            print('The exception is {}'.format(exc))

else:
    AssertionError("Python Environmental anomaly")

#Run Environmental
variablelist=sys.argv
cmdpamlen = len(variablelist)
print('Input argvLen is [{}]'.format(cmdpamlen))
for i in range(0, cmdpamlen):
    print('Script parameter[{}] is {}'.format(i, sys.argv[i]))
# Environmental= raw_input("please Enter Environmental:[Test/Beta/Online]")
Label = 'Test'
Env = 'Beta'
if cmdpamlen >= 2:
    Env = sys.argv[1]

if Env in ['Test', 'test', '0', 0,'TEST','DEV','Dev']:
    Label = 'Test'
    Vfile = os.path.join(os.path.join(home, 'Public'), 'JoyrunTestEnv_var.py')
elif Env in ['Beta', 'beta', 'BeataEnv', 'betaenv', '1', 1, None,'']:
    Label = 'Test'
    Vfile = os.path.join(os.path.join(home, 'Public'), 'JoyrunBetaEnv_var.py')
elif Env in ['Online', 'online', 'OnLine', 'ONLINE', '2', 2, 'ON','on']:
    Label = 'Online'
    Vfile = os.path.join(os.path.join(home, 'Public'), 'JoyrunOnline_var.py')
else:
    Label = 'All'
    Vfile = os.path.join(os.path.join(home, 'Public'), 'JoyrunBetaEnv_var.py')
print('Run Env is [{}]'.format(Env))
print('Run Label is [{}]'.format(Label))
print('Run Vfile is [{}]'.format(Vfile))

# reportpath=  raw_input("please robot_cmd  report path  -d:[JoyrunEvn:Online]")
Runpath = home
if cmdpamlen >= 3:
    rpath = sys.argv[2]
    if rpath not in ['Home', 'home', 'All', 'all','ALL','HOME',0,'0']:
        if ',' not in rpath:
            Runpath = os.path.join(home, rpath)
        else:
            rplist = rpath.split(',')
            for paths in rplist:
                if Runpath == home:
                    Runpath = os.path.join(home, paths)
                else:
                    path_n = os.path.join(home, paths)
                    Runpath = Runpath + '  ' + path_n
print('Run Script Path is {}'.format(Runpath))

reportpath = 0
if cmdpamlen >= 4:
    reportpath = sys.argv[3]
    if not os.path.exists(reportpath):
        reportpath=home
    else:
        pass
print('Report Path {}'.format(reportpath))

Varpam = 0
if cmdpamlen >= 5:
    # Varpam=  raw_input("please robot_cmd  --variable:[JoyrunEvn:Online]")
    Varpam = sys.argv[4]
    if ':' not in Varpam:
        Varpam = 'JoyrunEvn:Beta'
print('robot_cmd  --variable is  [{}]'.format(Varpam))

# cmd    --variable  JoyrunEvn:Online   -d /var/lib/jenkins/Report/$1

if Label == 'All':
    robot_cmd1 = 'robot  -V  {}  '.format(Vfile)
else:
    robot_cmd1 = 'robot --include {}  -V  {}  '.format(Label, Vfile )


if  reportpath == 0 and Varpam == 0:
    robot_cmd = '{}  {}'.format(robot_cmd1, Runpath)
elif reportpath != 0 and Varpam != 0:
    robot_cmd = '{}  --variable  {}  -d  {}  {}'.format(robot_cmd1, Varpam, reportpath, Runpath)
elif reportpath != 0 and Varpam == 0:
    robot_cmd = '{}  -d  {}  {}'.format(robot_cmd1, reportpath, Runpath)
else:
    pass
print(robot_cmd)

print(
    '*********************      Script  Run   start ...      *********************'
)
# rzlist = os.popen(robot_cmd).read().split('\n')
rz = os.popen(robot_cmd)
rzline=rz.readline()
while rzline:
    print(rzline)
    rzline=rz.readline()
rz.close()


# Check folder name, and rename again.
if os.path.exists(os.path.join(home, 'Public_PY2')):
    try:
        os.rename(
            os.path.join(home, 'Public'), os.path.join(home, 'Public_PY3'))
        os.rename(
            os.path.join(home, 'Public_PY2'), os.path.join(home, 'Public'))
    except Exception as exc:
        print('Rename folder NOT successful!!! Please check it.')
        print('The exception is {}'.format(exc))

print(
    '*********************     Script   The    End!!!        *********************'
)

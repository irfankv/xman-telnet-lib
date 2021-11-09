import telnetlib
import socket
import sys
import re
import time
import threading
import logging
#import thread


class mydevice(telnetlib.Telnet):
    list = []

    def __init__(s, username, password, prompt='#', devicetype='acli',
                 host=None, port=23, monitor=True,
                 hostnamestring=None,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        s.username = username
        s.password = password
        s.prompt = prompt
        s.initprompt = prompt
        s.host=host
        s.hostnamestring=hostnamestring
        s.port=port
        s.devicetype=devicetype
        s.monitorsecs = 60
        s.monitor = monitor
        s.timeout=timeout
        s.isconnected = False
        mydevice.list.append(s)
        s.reconnect()
        s.myname = str(id(s))

    def reconnect(s):
        s.isconnected = False
        s.prompt = s.initprompt
        print("Connecting " + s.host + " .....")
        try:
            telnetlib.Telnet.__init__(s, s.host, s.port, s.timeout)
        except:
            print("Not able to Connect")
            return
        print("Telnet Connection OPened")
        s.isconnected = True
        s.dlogin(s.username, s.password, s.prompt)

    def dlogin(s, username, password, prompt):
        #print("i am here baba")
        #print(s.devicetype)
        if s.devicetype=="acli":
            #print("hehhe")
            s.write(b"\n")
            s.read_until(b"ogin: ",timeout=60)
            print("login promt received")
            s.write(str(username).encode('utf8'))
            s.write(b"\n")
            s.read_until(b"assword: ")
            print("password prompt received")
            s.write(str(password).encode('utf8'))
            s.write(b"\n")
            print("Password Provided")
            #s.read_until(b">")
            s.expect([b'#', b'>'])
            print("Password accepted")
        else:
            s.write(b"\x19\n")
        s.write(b"en\n")
        s.read_until(prompt.encode('utf8'), 10)
        #print(s.extracthostname())
        if s.hostnamestring==None:
            s.hostname = s.extracthostname()
        else:
            s.hostname=s.hostnamestring
        newprompt = s.hostname+"[\w:\(\)-\.]*"+s.prompt
        s.prompt=newprompt
        print("new prompt is "+s.prompt)
        s.flush()
        print("disabling terminal more")
        print(s.run('conf t'))
        if s.devicetype=="acli":
            print(s.run('terminal more disable'))
        else:
            print(s.run('terminal length 0'))
        print(s.run('logging screen'))
        print(s.run('exit'))
        s.flush()
        print('done')

    def extracthostname(s):
        s.write('show sys-info'.encode('utf8'))
        s.write(b'\n')
        time.sleep(5)
        mystring = ''
        mysearch = None
        while mysearch==None:
            (whichregex,mymatch,mystring) = s.expect([b'SysUpTime',b'nothing'],1)
            print(mystring)
            print(mymatch)
            print(whichregex)
            mysearch = re.search("SysName[\s]*: ([\w-]+)", str(mystring))

        return mysearch.groups(0)[0]
    def flush(s, timeout=0):
        print("flushing start")
        mymatch = None
        (whichregex,mymatch,mystring) = s.expect([s.prompt.encode('utf8'),], 1)
        while mymatch==None:
            s.write(b' \n')
            (whichregex,mymatch,mystring) = s.expect([s.prompt.encode('utf8'),], 1)
            #print("mujko bachao")
            #print(mystring)
        return mystring.decode()

    def run(s, cmd):
        if s.isconnected:
            #print("I am running command " + cmd)
            s._writewithexception(cmd)
            #s.write(str(cmd).encode('utf8'))
            if re.match('.*\?$', str(cmd))==None:
                #print("running nnn")
                s.write(b"\n")
            (whichregex,mymatch,mystring) = s.toolong()
            if re.match('.*\?$', str(cmd))!=None:
                #print("found question mark")
                onconsole = s.read_very_eager().decode('ascii')
                print(mystring.decode('ascii')+onconsole, end="")
                #s.write(input().encode('utf8'))
                #s.write(b"\n")
                return s.run(input())
                #(whichregex,mymatch,mystring) = s.toolong()
            return mystring.decode('ascii')
        else:
            print("Not Connected")
            print("Trying to reconnect")
            s.reconnect()
            if s.isconnected:
                return s.run(cmd)
            return "Not Connected"

    def toolong(s):
        #print("toolong")
        mymatch = None
        myendstring = ''
        while mymatch==None:
            #print("taking toolong")
            (whichregex,mymatch,mystring) = s.expect([s.prompt.encode('utf8'),'\(y/n\) \?'.encode('utf8')], 60)
        return (whichregex,mymatch,mystring)

    def _writewithexception(s,cmdstr):
        try:
            s.write(str(cmdstr).encode('utf8'))
        except (ConnectionResetError, EOFError):
            print("Connection lost. Please reconnect")
            s.isconnected=False
        if not s.isconnected:
            s.reconnect()
            if s.isconnected:
                s._writewithexception(cmdstr)

    def clone(s):
        return mydevice(s.username,s.password,host=s.host)

    def disconnect(s):
        telnetlib.Telnet.close(s)
        s.isconnected = False

    def xmaninteract(s):
        print("in xman interact")

    def xmanreadkeyboardinputthread(s):
        print("in xman read input thread")

    def xmanprinttelnetscreen(s):
        print("in xman print telnet screen")


class monitordevice(mydevice):
    list = []
    mytimetuple = time.localtime(time.time())
    filenametime = str(mytimetuple.tm_year)+str(mytimetuple.tm_mon)+str(mytimetuple.tm_mday)+str(mytimetuple.tm_hour)+str(mytimetuple.tm_min)
    mfileloghandler= logging.FileHandler("monitorlog"+filenametime+".log")
    mconsolehandler= logging.StreamHandler()
    mconsolehandler.setLevel('DEBUG')
    mfileloghandler.setLevel('DEBUG')
    mlogengine = logging.getLogger('Monitordevice')
    mlogengine.setLevel('DEBUG')
    mlogengine.addHandler(mfileloghandler)
    mlogengine.addHandler(mconsolehandler)
    mlogengine.debug('Logging Started')

    def __init__(s, username, password, prompt='#', devicetype='acli',
                 host=None, port=23,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        mydevice.__init__(s, username, password, prompt=prompt, devicetype=devicetype,
                 host=host, port=port,
                 timeout=timeout)
        s.monitorsecs = 60
        
        monitordevice.list.append(s)
        s.mythread = threading.Thread(target=s.every60secthread)
        s.mythread.daemon = True
        s.mythread.start()
    def readconsoleoutputifany(s):
        #print('Reading console on '+s.hostname)
        onconsole = s.read_very_eager().decode()
        if onconsole!='':
            #print("on "+s.hostname+":"+onconsole)
            #monitordevice.logengine.debug(time.asctime())
            monitordevice.mlogengine.debug(time.asctime()+" : on "+s.hostname+":"+onconsole)
    def every60secthread(s):
        while True:
            time.sleep(s.monitorsecs)
            s.readconsoleoutputifany()
            s.checkcpu()
            s.checkmemory()
            s.checkcore()              
            #print("ending 60 sec thread on "+s.hostname)
    def checkcpu(s):
        myoutput = s.run('show khi performance cpu')
        mysearch = re.search("Current utilization: ([0-9]+)", str(myoutput))
        if mysearch != None:
            if int(mysearch.groups(0)[0]) > 50:
                #print("CPU is at "+mysearch.groups(0)[0]+" on "+s.hostname)
                #monitordevice.logengine.debug(time.asctime())
                monitordevice.mlogengine.debug(time.asctime()+" : CPU is at "+mysearch.groups(0)[0]+" on "+s.hostname)

    def checkmemory(s):
        myoutput = s.run('show khi performance mem')
        mysearch = re.search("Current utilization: ([0-9]+)", str(myoutput))
        if mysearch != None:
            if int(mysearch.groups(0)[0]) > 50:
                #print("Memory is at "+mysearch.groups(0)[0]+" on "+s.hostname)
                #monitordevice.logengine.debug(time.asctime())
                monitordevice.mlogengine.debug(time.asctime()+" : Memory is at "+mysearch.groups(0)[0]+" on "+s.hostname)
    def checkcore(s):
        myoutput = s.run('dir /intflash/coreFiles/1')
        mysearch = re.search("/intflash/coreFiles/1/core.", str(myoutput))
        if mysearch != None:
            print("crash on "+s.hostname)
            print(myoutput)


            
def setmonitorsecs(mysecs):
    print("monitoring thread timer changing")
    for dev in monitordevice.list:
        dev.monitorsecs = mysecs
                
                
        

if __name__ == "__main__":
    myfirstswitch = mydevice('rwa','rwa', host='10.133.130.158')
    print(myfirstswitch.run('show sys power'))
    print(globals()['myfirstswitch'].run('show sys power'))
  



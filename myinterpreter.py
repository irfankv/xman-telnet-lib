import time
import logging
import re
from mydevice import *
from newtelnet import *
import threading
from multiprocessing import Process, Queue
import sys
import select
import os
from myutilities import *
from io import StringIO
from confighelp import *
from myupgrade import *
#from checkhelp import *

mytimetuple = time.localtime(time.time())
filenametime = str(mytimetuple.tm_year)+str(mytimetuple.tm_mon)+str(mytimetuple.tm_mday)+str(mytimetuple.tm_hour)+str(mytimetuple.tm_min)
print(filenametime)
fileloghandler= logging.FileHandler("mylog"+filenametime+".log")
consolehandler= logging.StreamHandler()
fileloghandler.setLevel('DEBUG')
consolehandler.setLevel('DEBUG')
logengine = logging.getLogger('Myinterpreter')
logengine.setLevel('DEBUG')
logengine.addHandler(consolehandler)
logengine.addHandler(fileloghandler)
logengine.debug('Logging Started')
defaultdevice = ""

def periodic(interval,count,command):
    tempmythread = threading.Thread(target=periodicthread, args=(interval,count,command))
    tempmythread.daemon = True
    tempmythread.start()

def periodicthread(interval,count,command):
    for i in range(count):
        print(i)
        runcmdstring(command)
        time.sleep(interval)


def showdevice():
    print('printing connected devices')
    for mykey, dev in globals().items():
        #print(mykey)
        #print(dev.__class__.__name__)
        if dev.__class__.__name__ == 'mydevice':
            print(mykey+'-'+dev.host+'-'+dev.hostname)

def theloop(q,qtoc):
    global defaultdevice
    print("starting the loop on process id"+str(os.getpid()))
    sys.stdin = open('CON', 'r')
    #sys.stdout.reset()
    #sys.stdout = open('CON', 'w')
    mycmd = ''
    while 1:
        try:
            mysignal = qtoc.get()
            mycmd = input('XMAN-'+str(os.getpid())+"-"+mysignal+">")
            q.put(mycmd)
        except (KeyboardInterrupt,EOFError):
            q.put("")
            print('Reconnect the device')
        except Exception as e:
            #print("I am here")
            q.put("")
            print(e)

def grep(cmd, searchstring):
    runoutput = internalruncmd(cmd)
    grepoutput = ""
    if runoutput == "":
        return
    print("grepstart for "+searchstring)
    for line in runoutput.split("\n",):
        if re.search(searchstring, line)!= None:
            grepoutput = grepoutput+line+"\n"
    print(grepoutput)
    return grepoutput


def runcmd(mycmd):
    global logengine
    output = ""
    cmdlist= mycmd.split()
    if cmdlist != []:
        if cmdlist[0] in globals():
            #if len(cmdlist)==1:
            if globals()[cmdlist[0]].__class__.__name__ == 'mydevice':
                geton.run(cmdlist[0])
                if len(cmdlist)==1:
                    return
    onnameerror=False
    #print("here")
    try:
        logengine.debug(mycmd)
        exec(mycmd, globals())
    except (NameError, SyntaxError, AttributeError):
        onnameerror=True
        #print("exception 1")
    except (KeyboardInterrupt):
        print("exception 2")
        pass
    except Exception as e:
        print(e)

    if onnameerror:
        #print("nameerror")
        try:
            #print("trying")
            if mycmd.split()[0] in globals():
                if globals()[cmdlist[0]].__class__.__name__ == 'list':
                    #print("list found")
                    myoutput = ''
                    mylist = globals()[cmdlist[0]]
                    if len(mylist) !=0:
                        if mylist[0].__class__.__name__ == 'mydevice':
                            for onedevice in mylist:
                                myoutput = myoutput+str(runcmdonmydevice(onedevice,subst(cmdlist[1:])))
                            logengine.debug(myoutput)
                            return myoutput
                else:
                    #print("found in globals")
                    output = globals()[mycmd.split()[0]].run(subst(mycmd.split()[1:]))
            elif defaultdevice in globals():
                #print("running defaultdevice")
                output = globals()[defaultdevice].run(subst(mycmd.split()))
            else:
                print('runcmd:Object Not found in globals')
                print("Unexpected error: "+str(sys.exc_info()[0]))
            #print("end try")
            logengine.debug(output)
        except (KeyboardInterrupt):
            print("keyboardinterrupt in myinterpreter")
            pass
        except Exception as e:
            print(e)
    return output

def internalruncmd(mycmd):
    output=""
    cmdlist=mycmd.split()
    if cmdlist[0] in globals():
        if globals()[cmdlist[0]].__class__.__name__ == 'list':
            print("internalruncmd:list found")
            myoutput = ''
            mylist = globals()[cmdlist[0]]
            if len(mylist) !=0:
                if mylist[0].__class__.__name__ == 'mydevice':
                    for onedevice in mylist:
                        myoutput = myoutput+str(runcmdonmydevice(onedevice,subst(cmdlist[1:])))
                    logengine.debug(myoutput)
                    return myoutput
        else:
            output = globals()[cmdlist[0]].run(subst(cmdlist[1:]))
    elif defaultdevice in globals():
        output = globals()[defaultdevice].run(subst(cmdlist))
    else:
        print('internalruncmd:Object Not found in globals')
    return output

def runcmdonmydevice(onedevice,mycmd):
    global logengine
    output = onedevice.run(mycmd)
    return output
            
def subst(mycmd):
    myoutput = ''
    tospace = False
    for cmd in mycmd:
        if cmd not in globals():
            if tospace:
                myoutput=myoutput+" "+cmd
            else:
                myoutput=myoutput+cmd
                tospace=True
        elif type(globals()[cmd]) == str:
            if tospace:
                myoutput=myoutput+" "+globals()[cmd]
            else:
                myoutput=myoutput+globals()[cmd]
                tospace=True
        else:
            if tospace:
                myoutput=myoutput+" "+cmd
            else:
                myoutput=myoutput+cmd
                tospace=True
    return myoutput

    
class loadfile:
    def __init__(s):
        print("'load' command loaded")
    def run(s, cmd):
        global logengine
        print("I am in loadfile run")
        try:
            myfile = open(cmd, 'r')
        except Exception as e:
            print(e)
            return
        for mycmd in myfile:
            runcmd(mycmd)
            time.sleep(1)

def runcmdstring(mystr):
    s = StringIO(mystr)
    for mycmd in s:
        runcmd(mycmd)

class getoncmd:
    def __init__(s):
        print("'geton' command loaded")
    def run(s, cmd):
        global defaultdevice
        print("getting on ")
        defaultdevice=cmd
class runonallmydevice:
    def __init__(s):
        print("'onall' command loaded")
        #print(mydevice.list)
    def run(s, cmd):
        #print(mydevice.list)
        output = ''
        for onedevice in mydevice.list:
            output = output + runcmdonmydevice(onedevice,cmd)
        return output
class loadpycmd:
    def __init__(s):
        print("'loadpy' command loaded")
    def run(s, cmd):
        print("Loading "+cmd)
        try:
            exec(open(cmd).read(), globals())
        except Exception as e:
            print(e)
        print("Loading "+cmd+" complete.")
            
class runonmydevicelist:
    def __init__(s):
        print("'onlist' command loaded")
        #print(mydevice.list)
    def run(s, cmd):
        print("in runobmydevicelist")
        myoutput = ''
        listcmd = 'mylist = '+cmd.split()[0]
        print(listcmd)
        exec(listcmd, globals())
        global mylist
        for onedevice in mylist:
            myoutput = myoutput+str(runcmdonmydevice(onedevice,subst(cmd.split()[1:])))
        return myoutput


        
#onall = runonallmydevice()
#onlist = runonmydevicelist()
load = loadfile()       
geton = getoncmd()
loadpy = loadpycmd()
loadpy.run("checkhelp.py")
loadpy.run("confighelp.py")


class myinterpreter:
    def __init__(s):
        print('Starting Myinterpreter on process ehhe id'+str(os.getpid()))
        s.testcasefilehandler= logging.FileHandler("testcase"+filenametime+".log")
        s.testcasefilehandler.setLevel('DEBUG')
        s.testcaseengine = logging.getLogger('testcase')
        s.testcaseengine.setLevel('DEBUG')
        s.testcaseengine.addHandler(s.testcasefilehandler)
        s.testcaseengine.debug('Logging Started---')
    def startmyloop(s):
        global defaultdevice
        print('startmyloop')
        q = Queue()
        qtoc = Queue()
        p = Process(target=theloop, args=(q,qtoc))
        p.daemon = True
        p.name = 'theloopprocess'
        p.start()
        mycmd = ''
        while mycmd != 'quit':
            qtoc.put(defaultdevice)
            try:
                mycmd=q.get()
                s.testcaseengine.debug(mycmd)
                runcmd(mycmd)
            except KeyboardInterrupt:
                pass
        

if __name__ == "__main__":
    i = myinterpreter()
    i.startmyloop()

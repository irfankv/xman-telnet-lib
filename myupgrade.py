import time
import datetime
import threading

#imagename = 'VSP4K.vsp4k_4.0.0.0int040'
#imagepath = '/home/adharmshaktu/'
#print("Image is "+imagename)


#listify(configboot,a4,fnm='fv26mar15.cfg')
def listify(myfunction,myobjectlist,**kwargs):
    for myobject in myobjectlist:
        myfunction(myobject,**kwargs)

def copyimage(onedev, server, myimage, mypath):
    tempprompt = server.prompt
    print("prompt is "+tempprompt)
    server.prompt="ftp>"
    print("prompt is "+server.prompt)
    cmd = 'ftp '+onedev.host+'\n'
    print(cmd)
    server.write(cmd.encode('utf8'))
    print("----")
    server.expect([b'.*:',], 60)
    print(server.read_eager())
    print("2-"+onedev.host)
    cmd = onedev.username+'\n'
    server.write(cmd.encode('utf8'))
    server.expect([b'word:',], 60)
    cmd = onedev.password+'\n'
    print(server.run(cmd))
    print(server.run('binary'))
    print(datetime.datetime.now().time())
    #print(server.run('ls'))
    print(server.run('put '+mypath+myimage+'.tgz ./'+myimage+'.tgz'))
    print(datetime.datetime.now().time())
    server.prompt=tempprompt
    print(server.run('bye'))
    print("copy image complete.")
def savereset(onedev):
    print(onedev.run('save config'))
    onedev.write(b'reset\n')
    onedev.expect([b'\(y\/n\) \?',])
    onedev.write(b'y\n')
    onedev.isconnected = False
def configboot(onedev,fnm):
    #print(onedev.run('save config'))
    print(onedev.run('conf t'))
    print(onedev.run('exit'))
    bootcfg = 'boot config '+fnm+' -y'
    onedev.write(bootcfg.encode('utf8'))
    onedev.write(b'\n')
    onedev.isconnected = False
def onlyreset(onedev):
    onedev.write(b'reset\n')
    onedev.expect([b'\(y\/n\) \?',])
    onedev.write(b'y\n')
    onedev.isconnected = False
def onlyresetlist(devicelist):
    for onedev in devicelist:
        onlyreset(onedev)
def reconnectlist(devicelist):
    for onedev in devicelist:
        onedev.reconnect()
def saveresetlist(devicelist):
    for onedev in devicelist:
        savereset(onedev)

#using with list example command
#listify(imageactivate,my4k,server=onedev,imagenamenotgz=imagenamenotgz)

def imageactivate(onedev,imagenamenotgz):
    print(onedev.run('conf t'))
    print(onedev.run('software add ./'+imagenamenotgz+'.tgz'))
    onedev.flush()
    print(onedev.run('software activate '+imagenamenotgz))
    onedev.flush()
    #onedev.destroy()

def mtcopyimage(mydevicelist,s1,imagenamenotgz,imagepath):
    print("inside")
    mythreadactivatelist = []
    print("inside3")
    for dev in mydevicelist:
        print("inside2")
        temps1 = s1.clone()
        print("inside4")
        tempmythread = threading.Thread(target=copyimage, args=(dev, temps1, imagenamenotgz, imagepath))
        tempmythread.daemon = True
        tempmythread.start()
        mythreadactivatelist.append(tempmythread)


#def mtimageactivate(mydevicelist,imagenamenotgz):
#    print("inside")
#    mythreadactivatelist = []
#    print("inside3")
#    for dev in mydevicelist:
#        print("inside2")
#        tempdev=dev.clone()
#        tempmythread = threading.Thread(target=myupgrade, args=(tempdev,imagenamenotgz))
#        tempmythread.daemon = True
#        tempmythread.start()
#        mythreadactivatelist.append(tempmythread)

def actthr():
    print(str(threading.activeCount()))

#using with list example command
#listify(completeupgrade,my4k,server=s1,imagenamenotgz=imagenamenotgz,imagepath=imagepath)
def completeupgrade(onedev,server,imagenamenotgz,imagepath):
    tempserver=server.clone()
    tempdev=onedev.clone()
    def internalupgrade(onedev,server,imagenamenotgz,imagepath):
        copyimage(onedev,server,imagenamenotgz,imagepath)
        imageactivate(onedev,imagenamenotgz)
        savereset(onedev)
    tempmythread = threading.Thread(target=internalupgrade, args=(tempdev,tempserver,imagenamenotgz,imagepath))
    tempmythread.daemon = True
    tempmythread.start()

    
#for onedev in mydevice.list:
    #copyimage(onedev, s1, imagename, imagepath)
    #myupgrade(onedev)
    #savereset(onedev)

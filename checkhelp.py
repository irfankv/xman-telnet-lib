import re
#checklinkup('b125','1/25')
def checklinkup(devicename,link):
    if grep(devicename+' show int gi '+link,'up     up')!='':
        print('Pass')
        return True
    else:
        print('Fail')
        return False

#checklinkdown('b125','1/25')
def checklinkdown(devicename,link):
    if grep(devicename+' show int gi '+link,'up     up')!='':
        print('Fail')
        return False
    else:
        print('Pass')
        return True

#checklinkingressbps('b125','1/48',interval=30)
#checklinkingressbps('b125','1/48')
def checklinkingressbps(devicename,link,interval=10):
    myoutputpre=runcmd(devicename+' show int gi statis '+link)
    mymatchpre=re.search(link+'\s+(\d+)',str(myoutputpre))
    preoctet=mymatchpre.group(1)
    time.sleep(interval)
    myoutputpost=runcmd(devicename+' show int gi statis '+link)
    mymatchpost=re.search(link+'\s+(\d+)',str(myoutputpost))
    postoctet=mymatchpost.group(1)
    octetreceived=int(postoctet)-int(preoctet)
    print("Ingress bps = "+str(octetreceived*8/interval))

#checklinkegressbps('b125','1/48',interval=30)
#checklinkegressbps('b125','1/48')
def checklinkegressbps(devicename,link,interval=10):
    myoutputpre=runcmd(devicename+' show int gi statis '+link)
    mymatchpre=re.search(link+'\s+(\d+)\s+(\d+)',str(myoutputpre))
    preoctet=mymatchpre.group(2)
    time.sleep(interval)
    myoutputpost=runcmd(devicename+' show int gi statis '+link)
    mymatchpost=re.search(link+'\s+(\d+)\s+(\d+)',str(myoutputpost))
    postoctet=mymatchpost.group(2)
    octetsent=int(postoctet)-int(preoctet)
    print("Egress bps = "+str(octetsent*8/interval))

#checklinkbps('b125','1/48',interval=30)
#checklinkbps('b125','1/48')
def checklinkbps(devicename,link,interval=10):
    myoutputpre=runcmd(devicename+' show int gi statis '+link)
    mymatchpre=re.search(link+'\s+(\d+)\s+(\d+)',str(myoutputpre))
    preoctetegress=mymatchpre.group(2)
    preoctetingress=mymatchpre.group(1)
    time.sleep(interval)
    myoutputpost=runcmd(devicename+' show int gi statis '+link)
    mymatchpost=re.search(link+'\s+(\d+)\s+(\d+)',str(myoutputpost))
    postoctetegress=mymatchpost.group(2)
    postoctetingress=mymatchpost.group(1)
    octetsent=int(postoctetegress)-int(preoctetegress)
    octetreceived=int(postoctetingress)-int(preoctetingress)
    ingressbps = octetreceived*8/interval
    egressbps= octetsent*8/interval
    print("Egress bps = "+str(egressbps))
    print("Ingress bps = "+str(ingressbps))
    print("Egress Mbps = "+str(egressbps/1048576))
    print("Ingress Mbps = "+str(ingressbps/1048576))

#print("checkhelp loadied")



mydevice='b192'
myip4thoctet='192'
myip1stoctet=194
basevlan=1700

for myvrf in range(10):
    runcmdstring(createl3vsn.format(devicename=mydevice, vrfname=str(myvrf), vrfisid=myvrf))
    for myvlan in range(5):
        vid=str(basevlan+(myvrf*5)+myvlan)
        secoct=vid[0]+vid[1]
        thoct=vid[2]+vid[3]
        myip=str(myip1stoctet+myvrf)+'.'+secoct+'.'+thoct+'.'+myip4thoctet+'/24'
        runcmdstring(cfgl3vsnvlan.format(devicename=mydevice, vlanid=vid,vrfname=str(myvrf),ipprefix=myip))


mydevice='b207'
myip4thoctet='207'
myip1stoctet=194
basevlan=1700

for myvrf in range(10):
    runcmdstring(createl3vsn.format(devicename=mydevice, vrfname=str(myvrf), vrfisid=myvrf))
    for myvlan in range(5):
        vid=str(basevlan+(myvrf*5)+myvlan)
        secoct=vid[0]+vid[1]
        thoct=vid[2]+vid[3]
        myip=str(myip1stoctet+myvrf)+'.'+secoct+'.'+thoct+'.'+myip4thoctet+'/24'
        runcmdstring(cfgl3vsnvlan.format(devicename=mydevice, vlanid=vid,vrfname=str(myvrf),ipprefix=myip))



mydevice='b41'
myip4thoctet='41'
myip1stoctet=192
basevlan=1899


for myvlan in range(1900,1905):
    runcmdstring(createvlanstr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/9', stpinstance='33'))


for myvrf in range(1,2):
    runcmdstring(createl3vsn.format(devicename=mydevice, vrfname=str(myvrf), vrfisid=myvrf))
    for myvlan in range(5):
        vid=str(basevlan+(myvrf)+myvlan)
        secoct=vid[0]+vid[1]
        thoct=vid[2]+vid[3]
        myip=str(myip1stoctet)+'.'+secoct+'.'+thoct+'.'+myip4thoctet+'/24'
        runcmdstring(cfgl3vsnvlan.format(devicename=mydevice, vlanid=vid,vrfname=str(myvrf),ipprefix=myip))




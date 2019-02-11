
a4 = [b45,b46,b44,b41]

mydevice='b47'
for myvlan in range(1900,1905):
    runcmdstring(createvlanstr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/11,1/34', stpinstance='33'))
    ###runcmdstring('{devicename} vlan i-sid {vlanid} 3{vlanid}'.format(devicename=mydevice, vlanid=str(myvlan)))


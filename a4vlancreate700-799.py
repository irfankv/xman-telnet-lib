
a4 = [b192,b207]

mydevice='a4'
for myvlan in range(700,750):
    runcmdstring(createvlanstr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/13,1/15', stpinstance='33'))
    runcmdstring('{devicename} vlan i-sid {vlanid} 3{vlanid}'.format(devicename=mydevice, vlanid=str(myvlan)))

for myvlan in range(750,800):
    runcmdstring(createvlanstr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/14,1/16', stpinstance='33'))
    runcmdstring('{devicename} vlan i-sid {vlanid} 3{vlanid}'.format(devicename=mydevice, vlanid=str(myvlan)))

for myvlan in range(1700,1725):
    runcmdstring(createvlanstr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/13,1/15', stpinstance='33'))
    runcmdstring('{devicename} vlan i-sid {vlanid} 3{vlanid}'.format(devicename=mydevice, vlanid=str(myvlan)))

for myvlan in range(1725,1750):
    runcmdstring(createvlanstr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/14,1/16', stpinstance='33'))
    runcmdstring('{devicename} vlan i-sid {vlanid} 3{vlanid}'.format(devicename=mydevice, vlanid=str(myvlan)))


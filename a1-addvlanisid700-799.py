
a1 = [b218,b222]

mystr="""
{devicename} conf t
{devicename} vlan i-sid {vlanid} 3{vlanid}
{devicename} vlan members add {vlanid} {portliststr}
"""


mydevice='b218'
for myvlan in range(700,800):
    runcmdstring(mystr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/4'))

mydevice='b222'
for myvlan in range(700,800):
    runcmdstring(mystr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/3'))



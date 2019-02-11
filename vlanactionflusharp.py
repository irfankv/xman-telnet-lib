
mystring="""
{devicename} vlan action {vlanid} flushArp
"""

mydevice="a4"


for myvlan in range(700,1000):
    runcmdstring(mystring.format(devicename=mydevice,vlanid=str(myvlan)))

for myvlan in range(1700,1750):
    runcmdstring(mystring.format(devicename=mydevice,vlanid=str(myvlan)))

import time

disablersmlt="""
{devicename} conf t
{devicename} int vlan {vlanid}
{devicename} no ip rsmlt
"""
enablersmlt="""
{devicename} conf t
{devicename} int vlan {vlanid}
{devicename} ip rsmlt
"""

mydevice='b207'
myvrrpvlanlist=['1705','1706','1707','1708','1709']

for i in range(len(myvrrpvlanlist)):
    runcmdstring(disablersmlt.format(devicename=mydevice,
                           vlanid=myvrrpvlanlist[i]))

time.sleep(200)


for i in range(len(myvrrpvlanlist)):
    runcmdstring(enablersmlt.format(devicename=mydevice,
                           vlanid=myvrrpvlanlist[i]))

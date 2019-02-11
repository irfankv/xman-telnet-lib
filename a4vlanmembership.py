a4 = [b192,b207]

mydevice='a4'

mystr="""
{devicename} vlan members {vlanid} {portliststr}
"""
runcmdstring("""
a4 int gi 1/13,1/14,1/15,1/16
a4 no isis
a4 no lacp
a4 encap dot
""")

for myvlan in range(700,750):
    runcmdstring(mystr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/13,1/15'))

for myvlan in range(750,800):
    runcmdstring(mystr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/14,1/16'))

for myvlan in range(1700,1725):
    runcmdstring(mystr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/13,1/15'))

for myvlan in range(1725,1750):
    runcmdstring(mystr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/14,1/16'))



a4 = [b192,b207]

mystr="""
{devicename} vlan members {vlanid} {portliststr}
"""


mydevice='a4'
for myvlan in range(1700,1725):
    runcmdstring(mystr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/13,1/15'))

for myvlan in range(1725,1750):
    runcmdstring(mystr.format(devicename=mydevice, vlanid=str(myvlan),portliststr='1/14,1/16'))



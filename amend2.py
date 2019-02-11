mydevice='b192'
myip4thoctet='192'
myip1stoctet=194
basevlan=1700

mystr="""
{devicename} conf t
{devicename} int vlan {vlanid}
{devicename} no ip vrf 0
{devicename} conf t
"""

for myvlan in range(5):
    vid=str(basevlan+myvlan)
    secoct=vid[0]+vid[1]
    thoct=vid[2]+vid[3]
    myip=str(myip1stoctet)+'.'+secoct+'.'+thoct+'.'+myip4thoctet+'/24'
    runcmdstring(mystr.format(devicename=mydevice, vlanid=vid))
    runcmdstring(cfgl3vlangrt.format(devicename=mydevice, vlanid=vid,ipprefix=myip))


mydevice='b207'
myip4thoctet='207'
myip1stoctet=194
basevlan=1700

for myvlan in range(5):
    vid=str(basevlan+myvlan)
    secoct=vid[0]+vid[1]
    thoct=vid[2]+vid[3]
    myip=str(myip1stoctet)+'.'+secoct+'.'+thoct+'.'+myip4thoctet+'/24'
    runcmdstring(mystr.format(devicename=mydevice, vlanid=vid))
    runcmdstring(cfgl3vlangrt.format(devicename=mydevice, vlanid=vid,ipprefix=myip))

a4 = [b192,b207]

mydevice='a4'

mystring="""
{devicename} int vlan {vlanid}
{devicename} ip rsmlt
"""


for myvlan in range(1700,1750):
    runcmdstring(mystring.format(devicename=mydevice,vlanid=str(myvlan)))





mystring="""
{devicename} int vlan {vlanid}
{devicename} ip vrrp address {instanceid} {ipprefix}
{devicename} ip vrrp {instanceid} enable
{devicename} ip vrrp {instanceid} backup-master enable
"""


mydevice='b192'
myip4thoctet='1'
myip1stoctet=194
basevlan=1700



for myvrf in range(1,10):
    for myvlan in range(5):
        vid=str(basevlan+(myvrf*5)+myvlan)
        secoct=vid[0]+vid[1]
        thoct=vid[2]+vid[3]
        myip=str(myip1stoctet+myvrf)+'.'+secoct+'.'+thoct+'.'+myip4thoctet
        runcmdstring(mystring.format(devicename=mydevice, vlanid=vid,instanceid=thoct,ipprefix=myip))


mydevice='b207'
myip4thoctet='1'
myip1stoctet=194
basevlan=1700


for myvrf in range(1,10):
    for myvlan in range(5):
        vid=str(basevlan+(myvrf*5)+myvlan)
        secoct=vid[0]+vid[1]
        thoct=vid[2]+vid[3]
        myip=str(myip1stoctet+myvrf)+'.'+secoct+'.'+thoct+'.'+myip4thoctet
        runcmdstring(mystring.format(devicename=mydevice, vlanid=vid,instanceid=thoct,ipprefix=myip))



import time

mydevice='b192'
myvrrpvlanlist=['1700','1701','1702','1703','1704',
                '1705','1706','1707','1708','1709',
                '1725','1726','1727','1728','1729']
myvrrpidlist=['55','1','2','3','4',
              '5','6','7','8','9',
              '25','26','27','28','29']

for i in range(len(myvrrpvlanlist)):
    runcmdstring(disablevrrpvlan.format(devicename=mydevice,
                           vrrpid=myvrrpidlist[i],
                           vlanid=myvrrpvlanlist[i]))

time.sleep(200)


for i in range(len(myvrrpvlanlist)):
    runcmdstring(enablevrrpvlan.format(devicename=mydevice,
                           vrrpid=myvrrpidlist[i],
                           vlanid=myvrrpvlanlist[i]))

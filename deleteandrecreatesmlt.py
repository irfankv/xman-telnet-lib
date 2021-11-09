import time

mydevice1="b218"
mydevice2="b222"
mysmltid="27"
myifacelist1="1/4,1/7"
myifacelist2="1/3,1/11"
myvistvlan='4000'
myvistisid='4000'
myvistip1='40.40.40.2'
myvistip2='40.40.40.1'
myvistipprefixlength='22'
mysmltbmac1='00:49:b4:00:00:00'
mysmltbmac2='00:49:b4:00:00:00'
mysmltpeerid1='0049.0002.2200'
mysmltpeerid2='0049.0002.1800'
myvistpeerip1='40.40.40.1'
myvistpeerip2='40.40.40.2'

removesmlt="""
{devicename} conf t
{devicename} int gi {ifacelist}
{devicename} shut
{devicename} int mlt {mltid}
{devicename} no smlt
{devicename} int gi {ifacelist}
{devicename} no shut
"""

addsmlt="""
{devicename} conf t
{devicename} int gi {ifacelist}
{devicename} shut
{devicename} int mlt {mltid}
{devicename} smlt
{devicename} int gi {ifacelist}
{devicename} no shut
"""

runcmdstring(removesmlt.format(devicename=mydevice2,
                            mltid=mysmltid,
                            ifacelist=myifacelist2))
print("sleeping 20 seconds....")
time.sleep(20)
runcmdstring(vistcfgremove.format(devicename=mydevice2,
                            vistvlan=myvistvlan,
                            isid=myvistisid))

print("sleeping 200 seconds....")
time.sleep(200)


runcmdstring(vistcfg.format(devicename=mydevice2,
                            vistvlan=myvistvlan,
                            isid=myvistisid,
                            vistip=myvistip2,
                            prefixlength=myvistipprefixlength,
                            smltbmac=mysmltbmac2,
                            smltpeerid=mysmltpeerid2,
                            vistpeerip=myvistip1))
print("sleeping 200 seconds....")
time.sleep(200)

runcmdstring(addsmlt.format(devicename=mydevice2,
                            mltid=mysmltid,
                            ifacelist=myifacelist2))



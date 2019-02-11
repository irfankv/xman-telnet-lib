import time

mydevice1="b218"
mydevice2="b222"
mysmltid="27"
myifacelist1=[]
myifacelist2=[]
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
{devicename} int mlt {mltid}
{devicename} no smlt
"""

addsmlt="""
{devicename} conf t
{devicename} int mlt {mltid}
{devicename} smlt
"""

for i in range(15):
    runcmdstring(removesmlt.format(devicename=mydevice1,
                            mltid=mysmltid))
    print("sleeping 20 seconds....iteration "+str(i))
    time.sleep(20)
    runcmdstring(vistcfgremove.format(devicename=mydevice1,
                            vistvlan=myvistvlan,
                            isid=myvistisid))

    print("sleeping 200 seconds....iteration "+str(i))
    time.sleep(200)
    runcmdstring(vistcfg.format(devicename=mydevice1,
                            vistvlan=myvistvlan,
                            isid=myvistisid,
                            vistip=myvistip1,
                            prefixlength=myvistipprefixlength,
                            smltbmac=mysmltbmac1,
                            smltpeerid=mysmltpeerid1,
                            vistpeerip=myvistip2))
    print("sleeping 200 seconds....iteration "+str(i))
    time.sleep(200)
    runcmdstring(addsmlt.format(devicename=mydevice1,
                            mltid=mysmltid))
    print("sleeping 200 seconds....iteration "+str(i))
    time.sleep(200)

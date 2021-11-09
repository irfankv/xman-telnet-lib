import time

mydevice1="b192"
mydevice2="b207"

myvistvlan='70'
myvistisid='70'
myvistip1='70.1.1.1'
myvistip2='70.1.1.2'
myvistipprefixlength='24'
mysmltbmac1='aa:bb:cc:dd:ee:ff'
mysmltbmac2='aa:bb:cc:dd:ee:ff'
mysmltpeerid1='7254.beb1.0207'
mysmltpeerid2='7254.beb1.0192'
myvistpeerip1='70.1.1.2'
myvistpeerip2='70.1.1.1'

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

###############

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
                            mltid='13',
                            ifacelist='1/13'))

runcmdstring(addsmlt.format(devicename=mydevice2,
                            mltid='14',
                            ifacelist='1/14'))


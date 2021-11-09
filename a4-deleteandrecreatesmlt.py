import time

vist={'device1':'b192',
      'device2':'b207',
      'device1vistip':'70.1.1.1',
      'device2vistip':'70.1.1.2',
      'vistipprefixlength':'22',
      'device1systemid':'7254.beb1.0192',
      'device2systemid':'7254.beb1.0207',
      'smltbmac':'aa:bb:cc:dd:ee:ff',
      'vistvlan':'70',
      'vistisid':'70'}

mlt13={'device':'b192',
     'mltid':'13',
     'interfacelist':'1/15',
     'static':False,
     'smlt':True}

mlt14={'device':'b192',
     'mltid':'14',
     'interfacelist':'1/16,1/18',
     'static':True,
     'smlt':True}


smlt1={'device1':'',
      'device2':'',
     'mltid':'',
     'device1interfacelist':'',
     'device2interfacelist':'',
     'static':True}



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

shutandremovesmlt="""
{devicename} conf t
{devicename} int gi {ifacelist}
{devicename} shut
{devicename} int mlt {mltid}
{devicename} no smlt
"""

addsmltandnoshut="""
{devicename} conf t
{devicename} int mlt {mltid}
{devicename} smlt
{devicename} int gi {ifacelist}
{devicename} no shut
"""

def xsleep(interval):
    print("sleeping "+str(interval)+" secs")
    time.sleep(interval)

def removesmlt(mlt):
    runcmdstring(shutandremovesmlt.format(devicename=mlt['device'],
                            mltid=mlt['mltid'],
                            ifacelist=mlt['interfacelist']))
def addsmlt(mlt):
    runcmdstring(addsmltandnoshut.format(devicename=mlt['device'],
                            mltid=mlt['mltid'],
                            ifacelist=mlt['interfacelist']))

def configvistdevice1(vist):
    runcmdstring(vistcfg.format(devicename=vist['device1'],
                            vistvlan=vist['vistvlan'],
                            isid=vist['vistisid'],
                            vistip=vist['device1vistip'],
                            prefixlength=vist['vistipprefixlength'],
                            smltbmac=vist['smltbmac'],
                            smltpeerid=vist['device2systemid'],
                            vistpeerip=vist['device2vistip']))

def removevistconfigdevice1(vist):
    runcmdstring(vistcfgremove.format(devicename=vist['device1'],
                            vistvlan=vist['vistvlan'],
                            isid=vist['vistisid']))


##### Start Of Testcase ############
removesmlt(mlt13)
removesmlt(mlt14)
xsleep(20)
removevistconfigdevice1(vist)
xsleep(200)
configvistdevice1(vist)
xsleep(200)
addsmlt(mlt13)
addsmlt(mlt14)


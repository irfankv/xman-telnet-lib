mydevice1="b192"
myvistip1='70.1.1.1'
oldsmltsysid1='7254.beb1.0192'
newsmltsysid1='7254.beb2.0192'
oldnickname1='0.01.92'
newnickname1='0.11.92'

mydevice2="b207"
myvistip2='70.1.1.2'
oldsmltsysid2='7254.beb1.0207'
newsmltsysid2='7254.beb2.0207'
oldnickname2='0.02.07'
newnickname2='0.12.07'


myvistvlan='70'
myvistisid='70'
myvistipprefixlength='24'
oldsmltbmac='aa:bb:cc:dd:ee:ff'
newsmltbmac='aa:01:92:02:07:ff'

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
#runcmdstring(mystring.format(dn=mydevice1,isissystemid=newsmltsysid1,nickname=newnickname1,smltbmac=newsmltbmac,smltpeerid=newsmltsysid2))
mystring="""
{dn} conf t
{dn} no router isis enable
{dn} y
{dn} router isis
{dn} system-id {isissystemid}
{dn} spbm 1 nick-name {nickname}
{dn} spbm 1 smlt-virtual-bmac {smltbmac}
{dn} spbm 1 smlt-peer-system-id {smltpeerid}
{dn} router isis enable
"""

runcmdstring(mystring.format(dn=mydevice1,isissystemid=oldsmltsysid1,nickname=oldnickname1,smltbmac=oldsmltbmac,smltpeerid=oldsmltsysid2))
runcmdstring(mystring.format(dn=mydevice2,isissystemid=oldsmltsysid2,nickname=oldnickname2,smltbmac=oldsmltbmac,smltpeerid=oldsmltsysid1))





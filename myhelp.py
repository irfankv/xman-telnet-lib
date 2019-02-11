
b41=mydevice('rwa','rwa',host='10.139.149.41')
b42=mydevice('rwa','rwa',host='10.139.149.42')
b43=mydevice('rwa','rwa',host='10.139.149.43')
b44=mydevice('rwa','rwa',host='10.139.149.44')

b45=mydevice('rwa','rwa',host='10.139.149.45')
b46=mydevice('rwa','rwa',host='10.139.149.46')
b47=mydevice('rwa','rwa',host='10.139.149.47')


b49=mydevice('rwa','rwa',host='47.17.120.11',port=5039,devicetype="ers",hostnamestring="ERS-4850-2")
b50=mydevice('rwa','rwa',host='47.17.120.11',port=5038,devicetype="ers",hostnamestring="ERS-4850-1")
b51=mydevice('rwa','rwa',host='10.139.120.29',port=5046,devicetype="ers",hostnamestring="ERS4850-3")


allacli=[b45,b46,b47,b41,b42,b43,b44]
allers=[b49,b50,b51]
allbox=[b45,b46,b47,b41,b42,b43,b44,b49,b50,b51]



b45=mydevice('rwa','rwa',host='47.17.120.11',port=5069)
b46=mydevice('rwa','rwa',host='47.17.120.11',port=5072)
b47=mydevice('rwa','rwa',host='47.17.120.11',port=5068)


b49=mydevice('rwa','rwa',host='10.139.149.49')
b50=mydevice('rwa','rwa',host='10.139.149.50')
b51=mydevice('rwa','rwa',host='10.139.149.51')

runcmdstring(createvlanstr.format(devicename='b106', vlanid=str(2709), portliststr='1/25', stpinstance='33'))
runcmdstring('b106 vlan i-sid 2700 72700')

for myvlan in range(700,704):
    runcmd('b1 vlan i-sid {} 77{}'.format(myvlan,myvlan))

runcmdstring(createvlanstr.format(devicename='b1', vlanid=str(600),
                                  portliststr='1/3', stpinstance='33'))


addvlanlisttoport('b46','1/13-1/14',1381,1390)
addvlanlisttoport('b45','1/9-1/10',1381,1390)
addvlanlisttoport('b41','1/13-1/14',1381,1390)
addvlanlisttoport('b46','3/15-3/16',1371,1380)
addvlanlisttoport('b45','1/17-1/18',1371,1380)
addvlanlisttoport('b44','1/10',1371,1380)

addvlanlisttoport('b46','1/13-3/14',1381,1390)
addvlanlisttoport('b46','1/13-3/14',1381,1390)

addvlanlisttoport('b','1/24',850,900)



addvlanlisttoport('b207',portlist,startvlan,stopvlan)
addvlanlisttoport('b128','1/11',800,850)
addvlanlisttoport('b128','1/24',850,900)
addvlanlisttoport('b250','1/12',800,850)
addvlanlisttoport('b250','2/23',850,900)
addvlanlisttoport('b207','1/2',700,800)
addvlanlisttoport('b207','1/2',1700,1750)
addvlanlisttoport('b192','1/1',700,800)
addvlanlisttoport('b192','1/1',1700,1750)



remvlanlistfromport('b207','1/2',700,800)
remvlanlistfromport('b207','1/2',1700,1750)
remvlanlistfromport('b192','1/18',750,800)
remvlanlistfromport('b192','1/18',1725,1750)

remvlanlistfromport('b207','1/13',700,750)
remvlanlistfromport('b207','1/13',1700,1725)
remvlanlistfromport('b192','1/15',700,750)
remvlanlistfromport('b192','1/15',1700,1725)

remvlanlistfromport('b218','1/4',700,1000)
remvlanlistfromport('b218','1/4',1400,1465)
remvlanlistfromport('b222','1/3',700,1000)
remvlanlistfromport('b222','1/3',1400,1465)


#### UPgrade
imagenamenotgz='VOSS4K.4.2.1.0int009'
imagenamenotgz6k='VOSS8K.4.2.1.0int009'
imagenamenotgz7k='VOSS7K.4.2.1.0int009'
imagepath='/opt/corp/projects/baystack01/formal/voss_4.2.1.0/int009/'
s1 = mybasictelnet('dsushrut','Avaya123',prompt='\%',host='135.55.40.198')
mtcopyimage(mydevicelist,s1,imagenamenotgz,imagepath)
mtcopyimage(my4k,s1,imagenamenotgz,imagepath)
mtcopyimage(my8k,s1,imagenamenotgz6k,imagepath)
mtcopyimage(mysf,s1,imagenamenotgz7k,imagepath)

mtimageactivate(my4k,imagenamenotgz)
mtimageactivate(my8k,imagenamenotgz6k)
mtimageactivate(mysf,imagenamenotgz7k)


completeupgrade(b128,s1,imagenamenotgz,imagepath)

my4k2=[b218,b222,b129,b125,b106]
listify(completeupgrade,my4k,server=s1,imagenamenotgz=imagenamenotgz,imagepath=imagepath)
listify(completeupgrade,my8k,server=s1,imagenamenotgz=imagenamenotgz6k,imagepath=imagepath)
listify(completeupgrade,my7k,server=s1,imagenamenotgz=imagenamenotgz7k,imagepath=imagepath)

listify(imageactivate,b250,imagenamenotgz=imagenamenotgz6k)
listify(imageactivate,[b250,b251],imagenamenotgz=imagenamenotgz6k)
listify(imageactivate,[b222],imagenamenotgz=imagenamenotgz)
listify(imageactivate,b218,imagenamenotgz=imagenamenotgz)


runcmdstring(disableservicesgrt.format(devicename='b207'))
runcmdstring(disableservicesvrf.format(devicename='b207', vrfname='1'))
runcmdstring(disableservicesvrf.format(devicename='b207', vrfname='5'))

runcmdstring(enableservicesgrt.format(devicename='b207'))
runcmdstring(enableservicesvrf.format(devicename='b207', vrfname='1'))
runcmdstring(enableservicesvrf.format(devicename='b207', vrfname='5'))


imagenamenotgz='shashih_4k_noopt'
imagenamenotgz6k='shashih_8k_noopt'
imagepath='/home/shashih/images/'
s1 = mybasictelnet('dsushrut','Avaya123',host='135.55.40.198')
mtcopyimage([b218],s1,imagenamenotgz,imagepath)

mtimageactivate([b218],imagenamenotgz)

runcmdstring(savecfg.format(filename='sv2jan15.cfg'))
onlyresetlist([b125,b106])



imagenamenotgz='VSP4K.4.1.0.0int026'
imagenamenotgz6k='VSP8K.4.1.0.0int026'
imagepath='/opt/corp/projects/baystack01/formal/voss_4100/int026/'
s1 = mybasictelnet('dsushrut','Avaya123',prompt='\%',host='135.55.40.198')
mtcopyimage(my4k,s1,imagenamenotgz,imagepath)
mtcopyimage(my8k,s1,imagenamenotgz6k,imagepath)
mtimageactivate(my4k,imagenamenotgz)
mtimageactivate(my8k,imagenamenotgz6k)

runcmdstring(savecfg.format(filename='sv22jan15.cfg'))
onlyresetlist(all8)



mtcopyimage([b125],s1,imagenamenotgz,imagepath)

loadpy conhelp.py
imagenamenotgz='VSP4K.4.1.0.0int023'
imagenamenotgz6k='VSP8K.4.1.0.0int023'
mtimageactivate(my4k,imagenamenotgz)
mtimageactivate(my8k,imagenamenotgz6k)

runcmdstring(savecfg.format(filename='sv16jan15.cfg'))

onlyresetlist(my4k)
onlyresetlist(my8k)


mtimageactivate([b222,b128,b129,b125,b106],imagenamenotgz)

b131=mydevice('rwa','rwa',host='10.133.130.131')
b160=mydevice('rwa','rwa',host='10.133.130.160')


configboot(b218,'ssd-001.cfg')
configboot(b222,'ssd-001.cfg')
configboot(b128,'ssd-001.cfg')
configboot(b129,'ssd-001.cfg')
configboot(b125,'ssd-001.cfg')
configboot(b251,'ssd-001.cfg')
configboot(b250,'ssd-001.cfg')
configboot(b106,'ssd-001.cfg')

runcmdstring(cfgaccessmlt.format(devicename='b129', mltid='27', portlist='1/3,1/4,1/7,1/11'))

runcmdstring(cfgaccessmlt.format(devicename='b218', mltid='27', portlist='1/4,1/7'))
runcmdstring(cfgaccessmlt.format(devicename='b222', mltid='27', portlist='1/3,1/11'))
runcmdstring(cfgtrunkmlt.format(devicename='b129', mltid='27', portlist='1/3,1/4,1/7,1/11', vlanlist='2700-2709'))

mtimageactivate(['b250'],imagenamenotgz6k)

runcmdstring(vistcfg.format(devicename='b106',vistvlan='4001', isid='54001', vistip='40.40.41.1', prefixlength='22', smltbmac='00:49:b4:66:00:00', smltpeerid='0049.0001.2500', vistpeerip='40.40.41.2'))
runcmdstring(vistcfg.format(devicename='b125',vistvlan='4001', isid='54001', vistip='40.40.41.2', prefixlength='22', smltbmac='00:49:b4:66:00:00', smltpeerid='0049.0001.0600', vistpeerip='40.40.41.1'))
runcmdstring(vistcfgremove.format(devicename='b106', vistvlan='4001', isid='54001'))


runcmdstring(porttuniadd.format(devicename='b218', isid='77700', portlist='1/9'))
runcmdstring(porttuniadd.format(devicename='b106', isid='77700', portlist='1/6'))
runcmdstring(porttuniadd.format(devicename='b222', isid='77701', portlist='1/12'))
runcmdstring(porttuniadd.format(devicename='b125', isid='77701', portlist='1/7'))
runcmdstring(cfgtrunkmlt.format(devicename='b129', mltid='77', portlist='1/9,1/12', vlanlist='2710-2719'))
runcmdstring(cfgtrunkmlt.format(devicename='b203', mltid='77', portlist='4/6,4/7', vlanlist='2710-2719'))

onlist [b128,b250] conf t
onlist [b128,b250] int gi 1/33,1/34
onlist [b128,b250] no shut
runcmdstring(cfgaccessmlt.format(devicename='b128', mltid='33', portlist='1/34'))
runcmdstring(cfgaccessmlt.format(devicename='b250', mltid='33', portlist='1/33'))
onlist [b128,b250] conf t
onlist [b128,b250] int mlt 33
onlist [b128,b250] smlt
runcmdstring(cfgtrunkmlt.format(devicename='b129', mltid='33', portlist='1/33,1/34', vlanlist='2700-2709'))



checklinkup('b125','1/25')
checklinkdown('b125','1/25')
checklinkbps('b203','4/25')

runcmdstring(mlttuniadd.format(devicename='b218', isid='62700', mltid='27'))
runcmdstring(mlttuniadd.format(devicename='b222', isid='62700', mltid='27'))

runcmdstring(cfgtrunkmlt.format(devicename='b218', mltid='37', portlist='1/37,1/38', vlanlist=''))
runcmdstring(cfgtrunkmlt.format(devicename='b222', mltid='37', portlist='1/37,1/38', vlanlist=''))
runcmdstring(mltspbmcfg.format(devicename='b218', mltid='37'))
runcmdstring(mltspbmcfg.format(devicename='b222', mltid='37'))

runcmdstring(cfgtrunkmltlacp.format(devicename='b129', mltid='77', portlist='1/9,1/12', lacpkey='77'))

b129
conf t
no mlt 27
b218
conf t
i-sid 62700
no mlt 27
b218 exit
no mlt 27
b222
conf t
i-sid 62700
no mlt 27
b222 exit
no mlt 27
runcmdstring(cfgtrunkmltlacp.format(devicename='b129', mltid='27', portlist='1/3-1/4,1/7,1/11', lacpkey='27'))
runcmdstring(cfgtrunkmltlacp.format(devicename='b218', mltid='27', portlist='1/4,1/7', lacpkey='27'))
runcmdstring(cfgtrunkmltlacp.format(devicename='b222', mltid='27', portlist='1/3,1/11', lacpkey='27'))
b218
conf t
int mlt 27
smlt
b222
conf t
int mlt 27
smlt

runcmdstring(cfgtrunkmltlacp.format(devicename='b129', mltid='27', portlist='1/3-1/4,1/7,1/11', lacpkey='27'))
runcmdstring(cfgtrunkmltlacp.format(devicename='b218', mltid='27', portlist='1/4,1/7', lacpkey='27'))
runcmdstring(cfgtrunkmltlacp.format(devicename='b222', mltid='27', portlist='1/3,1/11', lacpkey='27'))
b218
conf t
int mlt 27
smlt
b222
conf t
int mlt 27
smlt

################ Bug Steps
b129
conf t
no mlt 27
b218
conf t
i-sid 62700
no mlt 27
b218 exit
no mlt 27
b222
conf t
i-sid 62700
no mlt 27
b222 exit
no mlt 27



runcmdstring(cfgtrunkmltlacp.format(devicename='b129', mltid='27', portlist='1/3-1/4,1/7,1/11', lacpkey='27'))
runcmdstring(cfgtrunkmltlacp.format(devicename='b218', mltid='27', portlist='1/4,1/7', lacpkey='27'))
runcmdstring(cfgtrunkmltlacp.format(devicename='b222', mltid='27', portlist='1/3,1/11', lacpkey='27'))

runcmdstring(cfgtrunkmltlacp.format(devicename='b250', mltid='5', portlist='2/3,1/23', lacpkey='5'))
runcmdstring(cfgtrunkmltlacp.format(devicename='b251', mltid='5', portlist='2/3,1/23', lacpkey='5'))


runcmdstring(macsecportrem.format(devicename='b250', portlist='2/3,1/23', cakname='sush2'))
runcmdstring(macsecdeletekey.format(devicename='b250', thekeyname='sush2'))

runcmdstring(macsecportrem.format(devicename='b251', portlist='2/3,1/23', cakname='sush2'))
runcmdstring(macsecdeletekey.format(devicename='b251', thekeyname='sush2'))


runcmdstring(macseccreatekey.format(devicename='b250', thekeyname='sush2', thekey='0123456789'))
runcmdstring(macsecencryptcfg.format(devicename='b250', portlist='2/3,1/23', cakname='sush2'))

runcmdstring(macseccreatekey.format(devicename='b251', thekeyname='sush2', thekey='0123456789'))
runcmdstring(macsecencryptcfg.format(devicename='b251', portlist='2/3,1/23', cakname='sush2'))


onlist [b222,b218] mlt 27 vlan 3000 

runcmdstring(mlttuniadd.format(devicename='b218', isid='62700', mltid='27'))
runcmdstring(mlttuniadd.format(devicename='b222', isid='62700', mltid='27'))

b218
conf t
int mlt 27
smlt
b222
conf t
int mlt 27
smlt

#######################


b129
conf t
no mlt 27
b218
conf t
no mlt 27
b222
conf t
no mlt 27



################# IST_PEER bug ##################

b129
conf t
no mlt 27

runcmdstring(cfgtrunkmlt.format(devicename='b129', mltid='27', portlist='1/3-1/4,1/7,1/11', vlanlist=''))

b129 mlt 27 vlan 2700-2709



onlist [b218,b222] conf t
onlist [b218,b222] i-sid 62700
onlist [b218,b222] no mlt 27

onlist [b218,b222] conf t
onlist [b218,b222] i-sid 62700
onlist [b218,b222] mlt 27
onlist [b218,b222] y

b57=mydevice('rwa','rwa',host='10.133.136.57')

runcmdstring(cfgtrunkmltlacp.format(devicename='b129', mltid='27', portlist='1/3-1/4,1/7,1/11', lacpkey='27'))

b129 mlt 27 vlan 2700-2709

onlist [b129,b218,b222] int gi 1/3-1/4,1/7,1/11
onlist [b129,b218,b222] no lacp
runcmdstring(cfgtrunkmlt.format(devicename='b129', mltid='27', portlist='1/3-1/4,1/7,1/11', vlanlist=''))
runcmdstring(cfgtrunkmlt.format(devicename='b192', mltid='14', portlist='1/16', vlanlist='750-799,1725-1749'))
runcmdstring(cfgtrunkmlt.format(devicename='b207', mltid='14', portlist='1/14', vlanlist='750-799,1725-1749'))



runcmdstring(cfgtrunkmltlacp.format(devicename='b2', mltid='23', portlist='4/23,4/24', lacpkey='23'))
runcmdstring(cfgtrunkmltlacp.format(devicename='b192', mltid='13', portlist='1/15', lacpkey='13'))
runcmdstring(cfgtrunkmltlacp.format(devicename='b207', mltid='13', portlist='1/13', lacpkey='13'))


runcmdstring(interfacespbmcfgstr.format(devicename='b250', ifid='1/9'))

a4 vlan action 1800 flusharp
a4 vlan action 1900 flusharp
a4 vlan action 1800 flushMacFdb
a4 vlan action 1900 flushMacFdb



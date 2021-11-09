# runcmdstring(vistcfg.format(devicename='b1',vistvlan='4000', isid='62700', vistip='40.40.40.2', prefixlength='22', smltbmac='00:49:b4:00:00:00', smltpeerid='0049.0002.2200', vistpeerip='40.40.40.1')
vistcfg = """
{devicename} conf t
{devicename} vlan create {vistvlan} type port-mstprstp 0
{devicename} vlan i-sid {vistvlan} {isid}
{devicename} interface Vlan {vistvlan}
{devicename} no ip address
{devicename} ip address {vistip}/{prefixlength}
{devicename} no router isis enable
{devicename} y
{devicename} router isis
{devicename} spbm 1 smlt-virtual-bmac {smltbmac}
{devicename} spbm 1 smlt-peer-system-id {smltpeerid}
{devicename} virtual-ist  peer-ip {vistpeerip} vlan {vistvlan}
{devicename} router isis enable
"""


# runcmdstring(vistcfgremove.format(devicename='b1', vistvlan='4000', isid='62700')
vistcfgremove = """
{devicename} conf t
{devicename} no router isis enable
{devicename} y
{devicename} no virtual-ist peer-ip
{devicename} router isis
{devicename} spbm 1 smlt-peer-system-id 0000.0000.0000
{devicename} spbm 1 smlt-virtual-bmac 00:00:00:00:00:00
{devicename} interface Vlan {vistvlan}
{devicename} no ip address
{devicename} no vlan i-sid {vistvlan} {isid}
{devicename} no vlan {vistvlan}
{devicename} router isis enable
{devicename} y
"""


# runcmdstring(porttuniadd.format(devicename='b1', isid='62700', portlist='1/30')
porttuniadd = """
{devicename} conf t
{devicename} i-sid {isid} elan-transparent
{devicename} i-sid {isid}
{devicename} port {portlist}
{devicename} y
"""

# runcmdstring(porttuniremove.format(devicename='b1', isid='62700', portlist='1/30')
porttuniremove = """
{devicename} conf t
{devicename} i-sid {isid} elan-transparent
{devicename} i-sid {isid}
{devicename} no port {portlist}
{devicename} y
"""

# runcmdstring(mlttuniadd.format(devicename='b1', isid='62700', mltid='27')
mlttuniadd = """
{devicename} conf t
{devicename} i-sid {isid} elan-transparent
{devicename} i-sid {isid}
{devicename} mlt {mltid}
{devicename} y
"""

# runcmdstring(mlttuniremove.format(devicename='b1', isid='62700', mltid='27')
mlttuniremove = """
{devicename} conf t
{devicename} i-sid {isid} elan-transparent
{devicename} i-sid {isid}
{devicename} no mlt {mltid}
{devicename} y
"""


# runcmdstring(macsecencryptcfg.format(devicename='b224', portlist='1/49,1/50', cakname='ssd224'))
macsecencryptcfg = """
{devicename} conf t
{devicename} int gi {portlist}
{devicename} no macsec enable
{devicename} no macsec connectivity-association
{devicename} macsec connectivity-association {cakname}
{devicename} macsec encryption enable
{devicename} macsec enable
"""

# runcmdstring(macsecportrem.format(devicename='b224', portlist='1/49,1/50', cakname='ssd224'))
macsecportrem = """
{devicename} conf t
{devicename} int gi {portlist}
{devicename} no macsec enable
{devicename} no macsec connectivity-association
"""


# runcmdstring(macseccreatekey.format(devicename='b1', thekeyname='sush1', thekey='mykeyname')
macseccreatekey = """
{devicename} conf t
{devicename} macsec connectivity-association {thekeyname} connectivity-association-key {thekey}
"""

# runcmdstring(macsecdeletekey.format(devicename='b1', thekeyname='sush1')
macsecdeletekey = """
{devicename} conf t
{devicename} no macsec connectivity-association {thekeyname}

"""


# cfg = configmodestr
# cfg.format(devicename='')
# runcmdstring(configmodestr.format(devicename='b1'))
configmodestr = """
{devicename} conf t
"""


# cfg = enableisisstr
# cfg.format(devicename='', systemname='',
#                       isissrcadd='159.0.0.224',
#                       isissystemid='0000.0000.0224',
#                       isisarea='', nickname='',
#                       bvidrange='3000-3001', primarybvid='',
#                       secondarybvid='')
# runcmdstring(enableisisstr.format(devicename='b3', systemname='vsp222',isissrcadd='159.0.0.222',isissystemid='0001.0000.0222',isisarea='49.0000', nickname='0.02.22',bvidrange='3000-3001', primarybvid='3000',secondarybvid='3001'))
enableisisstr = """
{devicename} conf t
{devicename} spbm
{devicename} router isis
{devicename} sys-name {systemname}
{devicename} ip-source-address {isissrcadd}
{devicename} is-type l1
{devicename} system-id {isissystemid}
{devicename} manual-area {isisarea}
{devicename} spbm 1
{devicename} spbm 1 nick-name {nickname}
{devicename} spbm 1 b-vid {bvidrange} primary {primarybvid}
{devicename} spbm 1 ip enable
{devicename} exit
{devicename} vlan create {primarybvid} type spbm-bvlan
{devicename} vlan create {secondarybvid} type spbm-bvlan
{devicename} router isis enable
"""

# cfg = interfacespbmcfgstr
# cfg.format(devicename='', ifid='')
# runcmdstring(interfacespbmcfgstr.format(devicename='b1', ifid='1/50'))
interfacespbmcfgstr = """
{devicename} conf t
{devicename} interface GigabitEthernet {ifid}
{devicename} no shutdown
{devicename} isis
{devicename} isis spbm 1
{devicename} isis enable
"""

# runcmdstring(interfacenospbmcfgstr.format(devicename='b1', ifid='1/50'))
interfacenospbmcfgstr = """
{devicename} conf t
{devicename} interface GigabitEthernet {ifid}
{devicename} no isis
"""

# runcmdstring(mltspbmcfg.format(devicename='onall', mltid='77'))
mltspbmcfg = """
{devicename} conf t
{devicename} interface mlt {mltid}
{devicename} no shutdown
{devicename} isis
{devicename} isis spbm 1
{devicename} isis enable
"""



# cfg =createvlanstr
# runcmdstring(createvlanstr.format(devicename='b5', vlanid='555',portliststr='1/49,1/50', stpinstance='33'))
createvlanstr = """
{devicename} conf t
{devicename} vlan create {vlanid} type port-mstprstp {stpinstance}
{devicename} vlan members {vlanid} {portliststr}
"""

deletevlanstr = """
{devicename} conf t
{devicename} no vlan {vlanid}
"""


# runcmdstring(createl2vsn.format(devicename='b5', vlanid='555',visid='33'))
createl2vsn = """
{devicename} conf t
{devicename} vlan i-sid {vlanid} {visid}
"""


# cfg = createl3vsn
# runcmdstring(createl3vsn.format(devicename='', vrfname='', vrfisid=''))
createl3vsn = """
{devicename} conf t
{devicename} ip vrf {vrfname}
{devicename} router vrf {vrfname}
{devicename} ipvpn
{devicename} i-sid {vrfisid}
{devicename} ipvpn enable
{devicename} isis redistribute direct
{devicename} isis redistribute direct metric 1
{devicename} isis redistribute direct enable
{devicename} isis redistribute ospf
{devicename} isis redistribute ospf metric 1
{devicename} isis redistribute ospf enable
{devicename} exit
{devicename} isis apply redistribute direct vrf {vrfname}
{devicename} isis apply redistribute ospf vrf {vrfname}
"""

# runcmdstring(disableservicesvrf.format(devicename='', vrfname=''))
disableservicesvrf = """
{devicename} conf t
{devicename} router vrf {vrfname}
{devicename} no ipvpn enable
{devicename} no isis redistribute direct enable
{devicename} no isis redistribute ospf enable
{devicename} no isis redistribute bgp enable
{devicename} no isis redistribute static enable
{devicename} no isis redistribute rip enable
{devicename} exit
{devicename} no isis apply redistribute direct vrf {vrfname}
{devicename} no isis apply redistribute ospf vrf {vrfname}
{devicename} no isis apply redistribute bgp vrf {vrfname}
{devicename} no isis apply redistribute static vrf {vrfname}
{devicename} no isis apply redistribute rip vrf {vrfname}
"""

# runcmdstring(disableservicesgrt.format(devicename=''))
disableservicesgrt = """
{devicename} conf t
{devicename} router isis
{devicename} no spbm 1 ip enable
{devicename} no isis redistribute direct enable
{devicename} no isis redistribute ospf enable
{devicename} no isis redistribute bgp enable
{devicename} no isis redistribute static enable
{devicename} no isis redistribute rip enable
{devicename} exit
{devicename} no isis apply redistribute direct
{devicename} no isis apply redistribute ospf
{devicename} no isis apply redistribute bgp
{devicename} no isis apply redistribute static
{devicename} no isis apply redistribute rip
"""

# runcmdstring(enableservicesvrf.format(devicename='', vrfname=''))
enableservicesvrf = """
{devicename} conf t
{devicename} router vrf {vrfname}
{devicename} ipvpn enable
{devicename} isis redistribute direct enable
{devicename} isis redistribute ospf enable
{devicename} isis redistribute bgp enable
{devicename} isis redistribute static enable
{devicename} isis redistribute rip enable
{devicename} exit
{devicename} isis apply redistribute direct vrf {vrfname}
{devicename} isis apply redistribute ospf vrf {vrfname}
{devicename} isis apply redistribute bgp vrf {vrfname}
{devicename} isis apply redistribute static vrf {vrfname}
{devicename} isis apply redistribute rip vrf {vrfname}
"""

# runcmdstring(enableservicesgrt.format(devicename=''))
enableservicesgrt = """
{devicename} conf t
{devicename} router isis
{devicename} spbm 1 ip enable
{devicename} isis redistribute direct enable
{devicename} isis redistribute ospf enable
{devicename} isis redistribute bgp enable
{devicename} isis redistribute static enable
{devicename} isis redistribute rip enable
{devicename} exit
{devicename} isis apply redistribute direct
{devicename} isis apply redistribute ospf
{devicename} isis apply redistribute bgp
{devicename} isis apply redistribute static
{devicename} isis apply redistribute rip
"""


# cfg = cfgl3vsnvlan
# runcmdstring(cfgl3vsnvlan.format(devicename='', vlanid='705',vrfname='v705',
#            ipprefix='10.10.10.10/24'))
cfgl3vsnvlan = """
{devicename} conf t
{devicename} ip vrf {vrfname}
{devicename} int vlan {vlanid}
{devicename} vrf {vrfname}
{devicename} ip address {ipprefix}
"""

# cfg = cfgl3vlangrt
# runcmdstring(cfgl3vlangrt.format(devicename='', vlanid='705',
#            ipprefix='10.10.10.10/24'))
cfgl3vlangrt = """
{devicename} conf t
{devicename} int vlan {vlanid}
{devicename} ip address {ipprefix}
"""


# runcmdstring(cfgaccessmlt.format(devicename='b2', mltid='77', portlist='1/49,1/50'))
cfgaccessmlt = """
{devicename} conf t
{devicename} int gi {portlist}
{devicename} no isis
{devicename} exit
{devicename} mlt {mltid}
{devicename} mlt {mltid} enable
{devicename} mlt {mltid} member {portlist}
"""

# runcmdstring(cfgtrunkmlt.format(devicename='b1', mltid='77', portlist='1/49,1/50', vlanlist='2700-2709'))
cfgtrunkmlt = """
{devicename} conf t
{devicename} int gi {portlist}
{devicename} no lacp
{devicename} no isis
{devicename} exit
{devicename} mlt {mltid}
{devicename} mlt {mltid} encap dot
{devicename} mlt {mltid} enable
{devicename} mlt {mltid} member {portlist}
{devicename} mlt {mltid} vlan {vlanlist}
"""

# runcmdstring(cfgtrunkmltlacp.format(devicename='onall', mltid='77', portlist='1/49,1/50', lacpkey='77'))
cfgtrunkmltlacp = """
{devicename} conf t
{devicename} lacp enable
{devicename} int gi {portlist}
{devicename} shut
{devicename} no isis
{devicename} encap dot
{devicename} lacp key {lacpkey}
{devicename} lacp mode active
{devicename} lacp aggregation enable
{devicename} lacp enable
{devicename} no shut
{devicename} mlt {mltid}
{devicename} mlt {mltid} encap dot
{devicename} mlt {mltid} enable
{devicename} int mlt {mltid}
{devicename} lacp key {lacpkey}
{devicename} lacp enable
{devicename} mlt {mltid} member {portlist}
"""

# runcmdstring(cfgaddtolacpmlt.format(devicename='onall', portlist='1/49,1/50', lacpkey='77'))
cfgaddtolacpmlt = """
{devicename} conf t
{devicename} int gi {portlist}
{devicename} lacp key {lacpkey}
{devicename} lacp mode active
{devicename} lacp aggregation enable
{devicename} lacp enable
"""


# runcmdstring(cfgvrrpvlan.format(devicename='', vrrpip='', vlanid='', vrrpid=''))
cfgvrrpvlan = """
{devicename} conf t
{devicename} int vlan {vlanid}
{devicename} ip vrrp  address {vrrpid} {vrrpip}
{devicename} ip vrrp {vrrpid} enable
"""


# runcmdstring(disablevrrpvlan.format(devicename='',  vlanid='', vrrpid=''))
disablevrrpvlan = """
{devicename} conf t
{devicename} int vlan {vlanid}
{devicename} no ip vrrp {vrrpid} enable
"""


# runcmdstring(enablevrrpvlan.format(devicename='',  vlanid='', vrrpid=''))
enablevrrpvlan = """
{devicename} conf t
{devicename} int vlan {vlanid}
{devicename} ip vrrp {vrrpid} enable
"""

def addvlanlisttoport(devicename,portlist,startvlan,stopvlan):
    runcmdstring("{devicename} conf t".format(devicename=devicename))
    for myvlan in range(startvlan,stopvlan):
        runcmdstring("{devicename} vlan member add {vlanid} {portlist} ".format(devicename=devicename,portlist=portlist,vlanid=myvlan))
    

def remvlanlistfromport(devicename,portlist,startvlan,stopvlan):
    runcmdstring("{devicename} conf t".format(devicename=devicename))
    for myvlan in range(startvlan,stopvlan):
        runcmdstring("{devicename} vlan member rem {vlanid} {portlist} ".format(devicename=devicename,portlist=portlist,vlanid=myvlan))


def cfgvrrponvlan(devicename,vrrpip,vlanid,vrrpid):
    runcmdstring(cfgvrrpvlan.format(devicename=devicename, vrrpip=vrrpip, vlanid=vlanid, vrrpid=vrrpid))


iprsmltholddownstr="""
b207 int vlan {vlanid}
b207 ip rsmlt holddown 180
"""
#runstringwithfor(iprsmltholddownstr,1705,1710)
def runstringwithfor(mystring,startvlan,stopvlan):
    for myvlan in range(startvlan,stopvlan):
        runcmdstring(mystring.format(vlanid=myvlan))


runcmdstring("b203 conf t")

for i in range(700,1564):
    runcmdstring("b203 vlan mem add {vlanid} 4/23,4/24".format(vlanid=str(i)))



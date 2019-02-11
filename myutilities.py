
def deletevlanrange(mydev, startvlan, endvlan):
    mydev.run('conf t')
    for delvlan in range(startvlan, endvlan):
        print(mydev.run("vlan delete "+str(delvlan)))

#configstring ='vlan create {} type port-mstprstp 10'
def configrange(mydev, configstring, startofrange, endofrange):
    for myrange in range(startofrange, endofrange):
        cmd = configstring.format(str(myrange))
        print(cmd)
        print(mydev.run(cmd))

def configlistrange(mydev, configstringlist, startofrange, endofrange):
    for myrange in range(startofrange, endofrange):
        for configstring in configstringlist:
            cmd = configstring.format(str(myrange),str(myrange),str(myrange))
            print(cmd)
            print(mydev.run(cmd))


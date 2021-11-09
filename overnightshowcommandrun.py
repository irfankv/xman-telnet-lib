mystring1="""
{devicename} show khi perf cpu
"""
mystring2="""
{devicename} show khi perf mem
"""
mystring3="""
{devicename} show isis adjac
"""
mystring4="""
{devicename} show isis lsdb detail
"""
mystring5="""
{devicename} show tech
"""
mystring6="""
{devicename} show khi perf cpu
"""
mystring7="""
{devicename} show khi perf mem
"""

mydevice4k="a1"
mydevice8k="a4"


for mycount in range(0,50):
    runcmdstring(mystring1.format(devicename="a1"))
    runcmdstring(mystring1.format(devicename="a4"))
    time.sleep(60)
    runcmdstring(mystring2.format(devicename="a1"))
    runcmdstring(mystring2.format(devicename="a4"))
    time.sleep(60)
    runcmdstring(mystring3.format(devicename="a1"))
    runcmdstring(mystring3.format(devicename="a4"))
    time.sleep(60)
    runcmdstring(mystring4.format(devicename="a1"))
    runcmdstring(mystring4.format(devicename="a4"))
    time.sleep(60)
    runcmdstring(mystring5.format(devicename="a1"))
    runcmdstring(mystring5.format(devicename="a4"))
    time.sleep(60)
    runcmdstring(mystring6.format(devicename="a1"))
    runcmdstring(mystring6.format(devicename="a4"))
    time.sleep(60)
    runcmdstring(mystring7.format(devicename="a1"))
    runcmdstring(mystring7.format(devicename="a4"))
    time.sleep(60)


runcmdstring("b222 show clock")

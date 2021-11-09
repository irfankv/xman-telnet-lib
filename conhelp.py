#runcmdstring(shutb222)
shutb222="""
b129 conf t
b129 int gi 1/34
b129 shut
"""

#runcmdstring(noshutb222)
noshutb222="""
b129 conf t
b129 int gi 1/34
b129 no shut
"""

#runcmdstring(shutb218)
shutb218="""
b129 conf t
b129 int gi 1/33
b129 shut
"""

#runcmdstring(noshutb218)
noshutb218="""
b129 conf t
b129 int gi 1/33
b129 no shut
"""

#runcmdstring(savecfg.format(filename='sv27may15.cfg'))
savecfg="""
my4k save config file {filename}
my4k y
my4k save config file ssd-001.cfg
my4k y
my8k save config file {filename}
my8k y
my8k save config file config.cfg
my8k y
my7k save config file {filename}
my7k y
my7k save config file config.cfg
my7k y

b203 save config file {filename}
b203 y
b203 save config
"""



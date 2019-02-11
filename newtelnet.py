import telnetlib
import socket
import sys
import re
import time
import threading


class mybasictelnet(telnetlib.Telnet):
    def __init__(s, username, password, prompt='\$', devicetype='acli',
                 host=None, port=23,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        s.username = username
        s.password = password
        s.prompt = prompt
        s.host=host
        s.port=port
        s.timeout=timeout
        s.isconnected = False
        print("Connecting " + host + " .....")
        try:
            telnetlib.Telnet.__init__(s, host, port, timeout,)
        except:
            print("Not able to Connect")
            return
        print("Telnet Connection OPened")
        s.isconnected = True
        s.dlogin(s.username, s.password, s.prompt)
    def dlogin(s, username, password, prompt):
        s.read_until(b"ogin: ")
        s.write(str(username).encode('utf8'))
        s.write(b"\n")
        s.read_until(b"assword: ")
        s.write(str(password).encode('utf8'))
        s.write(b"\n")
        print("Password Provided")
        #s.read_until(b">")
        s.expect([b'$',])
        s.hostname = s.extracthostname()
        print("new prompt is "+s.prompt)
        s.flush()
        print('done')
    def extracthostname(s):
        return s.host
    def flush(s):
        mymatch = None
        (whichregex,mymatch,mystring) = s.expect([s.prompt.encode('utf8'),], 1)
        while mymatch==None:
            s.write(b' \n')
            (whichregex,mymatch,mystring) = s.expect([s.prompt.encode('utf8'),], 1)
            print(mystring.decode())
        return mystring.decode()
    def run(s, cmd):
        if s.isconnected:
            #print("I am running command " + cmd)
            s.write(str(cmd).encode('utf8'))
            if not re.match('\?$', str(cmd)):
                s.write(b"\n")
            (whichregex,mymatch,mystring) = s.expect([s.prompt.encode('utf8'),])
            if re.match('\?$', str(cmd)):
                for i in range(len(cmd) - 1):
                    print("sending backspace")
                    s.write(b"\b")
            return mystring.decode()
        else:
            print("Not Connected")
            return "Not Connected"
    def clone(s):
        return mybasictelnet(s.username,s.password,host=s.host,prompt=s.prompt)





#if __name__ == "__main__":
    #myfirstswitch = mydevice('rwa','rwa', host='10.133.130.158')
    #print(myfirstswitch.run('show sys power'))
    #print(globals()['myfirstswitch'].run('show sys power'))

import socket
from webosint.cmsdetect import CMSdetect
from webosint.nslookup import nsLookup
from webosint.portscan import DefaultPort,Customrange
from webosint.reverseip import ReverseIP
from webosint.subdomain import SubDomain
from webvuln.bruteforce import ssh,ftp
from webvuln.clickjacking import ClickJacking
from webvuln.cors import Cors
from webvuln.hostheader import HostHeader
from webosint.header import header
from webosint.crawler import crawler
from webosint.who.whoami import whoami

host = None
port = None

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

# Checking whether the target host is alive or dead
def CheckTarget():

    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))

    if  result == 0:
        return True
    else:
        return False

# Main Method
def domain():

    global host
    host = input("Enter the Target Host : ")
    global port
    port = int(input("Enter the Target port : "))
    print ( W + '[+]' + G + 'Checking whether the Target is reachable ...' + '\n')
    # calling CheckTarget method
    if CheckTarget()==True:
        print("Target Alive \n")
        print("Host : " + host)
        print("Port : %s" % port)
        Menu()
    else:
        print("The Host is Unreachable \n")
        exit()


NmapFunctions = {
    1: DefaultPort,
    2: Customrange,
}


def nmaprec(host,port):

    Choice = 1
    while True:
        print("1. Scan Default Ports (22-443)")
        print("2. Enter Custom Range")
        print("3. Back to Main Menu")
        print('')
        Choice = int(input(">> "))
        if (Choice >= 0) and (Choice < 3):
            NmapFunctions[Choice](host, port)
        elif Choice == 3:
            Menu()
        else:
            print("Please choose an Appropriate option")

BruteFunctions = {
        1: ssh,
        2: ftp
    }

def BruteForce(host, port):
    Selection = 1
    while True:
        print('')
        print("1. SSH")
        print("2. FTP")
        print("3. Main Menu")
        print('')
        Selection = int(input("root@osint:~/Domain/BruteForce# "))
        print('')
        if (Selection >= 0) and (Selection < 3):
            BruteFunctions[Selection](host, port)
        elif Selection == 3:
            Menu()
        else:
            print("Please choose an Appropriate option")


MainFunctions = {
 1: ReverseIP,
 2: SubDomain,
 3: nsLookup,
 4: CMSdetect,
 5: nmaprec,
 6: BruteForce,
 7: ClickJacking,
 8: Cors,
 9: HostHeader,
 10:header,
 11:crawler,
 12:whoami
}

def Menu():
    Selection = 1
    while True:
        print('')
        print(C+"1."+W+" ReverseIP")
        print(C+"2."+W+" SubDomain")
        print(C+"3."+W+" nsLookup")
        print(C+"4."+W+" CMSDetect")
        print(C+"5."+W+" PortScan")
        print(C+"6."+W+" Bruteforce")
        print(C+"7."+W+" ClickJacking")
        print(C+"8."+W+" CORS")
        print(C+"9."+W+" Host Header Injection")
        print(C+"10."+W+" Header")
        print(C+"11."+W+" Crawler")
        print(C+"12."+W+" Whoami")
        print(C+"99."+W+" Exit")
        print('')
        Selection = int(input(C+"root@osint:"+W+"~/Domain# "))
        if (Selection >= 0) and (Selection <=12):
            MainFunctions[Selection](host, port)
        elif Selection == 99:
            exit()
        else:
            print(R+"Error: Please choose an Appropriate option")
        print(W+'')

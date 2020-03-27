import os
from Phonenumber import *
from proxy import *
from macaddress import *
from ipaddress import *
from reverseimagesearch import *
from metadata import *
from domain import *
from Username import *
from torrent import *
from maildb import *
from src.banner import *

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

switcher={1:username,
2:Phonenumber,
3:maildb,
4:domain,
5:metadata,
6:reverseimagesearch,
7:IPHeatmap,
8:MacAddressLookup,
9:ip2Proxy,
10:torrent,
99:exit
}

def main():
    os.system("clear")
    banner()
    print("\n\nWelcome To Osint Tool\n")
    while True:
        print(C+"\n1." +W+ "Username")
        print(C+"2."+W+"Phone number")
        print(C+"3."+W+"Email Data Breach")
        print(C+"4."+W+"Domain")
        print(C+"5."+W+"Metadata")
        print(C+"6."+W+"Reverse Image Search")
        print(C+"7."+W+"IP Heatmap")
        print(C+"8."+W+"Mac Address Lookup")
        print(C+"9."+W+"IP2Proxy")
        print(C+"10."+W+"Torrent")
        print(C+"99."+W+"Exit\n")

        ch=int(input(C+"root@osint#"+W))
        if ch not in switcher.keys():
            print(R+"Error : "+W+"Invalid Input")
        else:
            switcher[ch]()
if __name__ == '__main__':
    main()

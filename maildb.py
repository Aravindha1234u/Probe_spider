import os

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def maildb():
    emailaddress=input(C+"Enter the Email Address (Eg:test@gmail.com): "+W)
    if  ("@" and ".com") or ("@" and ".in") in emailaddress:
        print ( W + '[+]' + G + "Data Breaching....." + '\n'+W)
        os.system("h8mail -t "+emailaddress+" -o /root/Downloads/osint/src/output.csv > /root/Downloads/osint/src/log")
        f=open("/root/Downloads/osint/src/output.csv","r")
        line=f.readlines()
        if len(line) > 1:
            for i in line:
            	print(i)
        else:
            print(G+"Data breached is Not Compromised")
    else:
        print(R+"Error: Invalid Email Address")

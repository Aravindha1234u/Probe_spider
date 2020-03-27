from src.api import phoneapis
import requests
import json

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def Phonenumber():
    print ( W + '[+]' + G + ' Fetching Phonenumber Details...' + '\n')
    ph=int(input(C+"\nroot@osint:"+W+"~/Phonenumber:Enter the Phonenumber (Eg:919451237895) :"))
    api_key=phoneapis()
    url = ("http://apilayer.net/api/validate?access_key="+api_key+"&number="+str(ph))
    response=requests.get(url)
    if "91" not in str(ph):
        print(R+"Error: CountryCode is missing")
    else:
        if response.status_code ==200:
            get=response.json()
            print(G+"Number: "+W+get['number'])
            print(G+"Type: "+W+get['line_type'])
            print(G+"CountryCode: "+W+get['country_code'])
            print(G+"Country: "+W+get['country_name'])
            print(G+"Location: "+W+get['location'])
            print(G+"Carrier: "+W+get['carrier'])
            ch=input("Want to Redo (Y/N):")
            if ch=="y" or ch=="Y":
                Phonenumber()
            print("")
        else:
            print(R+"Invalid Mobile Number")

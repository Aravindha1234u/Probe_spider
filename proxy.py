import IP2Proxy
import re
import requests
from src.api import *
from webosint.who.whois import *

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def ip2Proxy():
    IP=input(C+"\nroot@osint:"+W+"~/IP2Proxy# Enter the IP Address:")
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",IP):
        db = IP2Proxy.IP2Proxy()
        db.open("/root/Downloads/osint/src/IP2PROXY-IP-PROXYTYPE-COUNTRY-REGION-CITY-ISP-DOMAIN-USAGETYPE-ASN-LASTSEEN.BIN")
        print ( W + '[+]' + G + "Processing....." + '\n')
        record = db.get_all(IP)
        db.close()
        if record['is_proxy']!=0:
            #print(record)
            print(C+"Proxy: " + "Enabled")
            print(C+"Proxy Type:" + W+record['proxy_type'])
            print(C+"Country Code:" + W+record['country_short'])
            print(C+"Country:" +W+ record['country_long'])
            print(C+"Region Name:" + W+record['region'])
            print(C+"City:" +W+ record['city'])
            print(C+"Isp:" +W+ record['isp'])
            print(C+"Domain:" +W+ record['domain'])
            print(C+"Usage:" +W+ record['usage_type'])
            print(C+"ASN:" +W+ record['asn'])
            print(C+"Name:" +W+ record['as_name'])
            api_key = ipstack()
            if api_key == "":
                print("Add you ipstack api key to src/api.py")
                exit()
            r = requests.get("http://api.IPstack.com/" + IP + "?access_key=" + api_key)
            response = r.json()
            print(C+"Latitude :"+W+" {latitude}".format(**response))
            print(C+"Longitude :"+W+" {longitude}".format(**response))
            if input(C+"Want More Whois Details (Y/N): "+W):
                whois_more(IP)
            if response['latitude'] and response['longitude']:
                lats = response['latitude']
                lons = response['longitude']
                url = "https://maps.google.com/maps?q=%s,+%s" % (lats, lons)
                print(C+"Google Map Link :" +W+ url)
        else:
            print(G+"IP does not use any Proxy or VPN")
    else:
        print(R+"\nEnter a Valid IP Address")
        ip2Proxy()
    ch=input(C+"Want to Redo (Y/N):"+W)
    if ch=="y" or ch=="Y":
        ip2Proxy()
    print("")

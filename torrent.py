import requests
import json

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def torrent():
    IP = str(input(C+"Enter the IP Address:"+W))
    r = requests.get("https://api.antitor.com/history/peer/?ip="+ IP +"&key=3cd6463b477d46b79e9eeec21342e4c7")
    res = r.json()
    print ( W + '[+]' + G + "Processing Torrent....." + '\n')
    if len(res)>4:
        print(C+"IP Address: "+W+res['ip'])
        print(C+"ISP: "+W+res['isp'])
        print(C+"Country: "+W+res['geoData']['country'])
        print(C+"Latitude: "+W+str(res['geoData']['latitude']))
        print(C+"Longitude: "+W+str(res['geoData']['longitude'])+"\n")
        for i in res['contents']:
        	print(C+"Category:"+W+i['category'])
        	print(C+"Name:"+W+i['name'])
        	print(C+"Start:" + W+i['startDate'])
        	print(C+"End:" + W+i['endDate'])
        	print(C+"Size:"+W+str(i['torrent']['size']))
        	print("")
    else:
        print(R+"Error: Something Went Wrong")

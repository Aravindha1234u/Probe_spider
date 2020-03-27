import requests

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def MacAddressLookup():
    mac = input(C+"Enter the MAC Address (Eg:08:00:69:02:01:FC):"+W)
    print ( W + '[+]' + G + "Processing Mac Address..." + '\n')
    url = ("https://macvendors.co/api/" + mac)
    response=requests.get(url)
    result=response.json()
    if result["result"]:
        final=result['result']
        print(C+"Company:" + W+final["company"])
        print(C+"Address:" + W+final["address"])
        print(C+"Country:" + W+final["country"])
        ch=input(C+"Want to Redo (Y/N):"+W)
        if ch=="y" or ch=="Y":
            MacAddressLookup()
        print("")
    else:
        print(R+"Error: Something Went Wrong")

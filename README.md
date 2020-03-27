# Recon_Spider  :mag:
  This is a Open Source Intelligence Tool made complete out of Python.
  
## Overview of the tool:

* Tool has module involved to scrape social media account details from Instagram, Facebook and Twitter
* It can find details about Phone number
* Email data Breach
* Domain module has various scans for domain check for vulneribility and spider crawlers
* Metadata Analyser
* Reverse Image Search 
* IP Heatmap generator
* Mac Address finder of manufacturer
* IP2Proxy checks whether provided ip uses any kind of Proxy/VPN if any then check for DNSLeaks
* Torrent Download History
* Tool is currently available only in Command Line Interface (CLI)

![Tool UI](https://drive.google.com/uc?export=view&id=12pJcN7J20XfzdY16sMKs0ddSaja5-lMn)

**Creators:**  :bust_in_silhouette:
> [Aravindha Hariharan M](https://github.com/Aravindha1234u)  
  Mail ID: aravindha1234u@gmail.com

### Prerequisites  :package:
1.Python 3.X with pip3 Installed  
If not then, pip3 installation  
```
apt install python3-pip
```  
To Check pip versioon  
```
pip3 --version
```
2.Geolite & IP2Proxy Databases  
**Geolite2 City Database**
```
https://github.com/texnikru/GeoLite2-Database/blob/master/GeoLite2-City.mmdb.gz
```

**IP2Proxy Database**
```
https://lite.ip2location.com/database/px8-ip-proxytype-country-region-city-isp-domain-usagetype-asn-lastseen
```
Download both database and move it to Recon_Spider/src/.

### Installation  :floppy_disk:
Open Terminal and type
```
git clone https://github.com/Aravindha1234u/Recon_Spider

cd Recon_Spider
```

To Install required Python package

```
pip3 install -r requirements.txt
```
or
```
python3 -m pip install -r requirements.txt
```

### Execution  :+1:
**Before Executing, Change api keys in file src/api.py file for full version of the tool**  
To Run Recon_Spider
```
python3 main.py
```

### Important Message  :warning:

>This tool is for research purposes only. Hence, the developers of this tool won't be responsible for any misuse of data collected using this tool. Used by many researchers and open source intelligence (OSINT) analysts.

### License  :page_facing_up:
Recon_Spider is licensed under GNU General Public License v3.0. Take a look at the [License](https://github.com/Aravindha1234u/Recon_Spider/blob/master/LICENSE)

## Special Thanks 
[Adithyan AK](https://github.com/adithyan-ak)  
[Gowtham G](https://github.com/Gowtham-18)

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def username():
    print(C+"1."+W+" Facebook "+C+"\n2."+W+" Twitter "+C+"\n3."+W+" Instagram")
    choice = input(C+"root@osint:"+W+"~/Username# Enter the Options: ")
    if choice == '1':
        pass
    elif choice == '2':
        ScrapTweets()
        return()
    elif choice == '3':
        Instagram()
        return()
    else:
        exit()
    print ( W + '[+]' + G + ' Fetching Data From Facebook...' + '\n')
    username= input(C+"root@osint:"+W+"~/Username# Enter the Username : ")
    search_string = "https://en-gb.facebook.com/" + username

    #response is stored after request is made
    response = requests.get(search_string)

    #Response is stored and parsed to implement beautifulsoup
    soup = BeautifulSoup(response.text, 'html.parser')

    #List that will store the data that is to be fetched
    data = {'Name': "null",
            'Photo_link': "null",
            'Work':{'Company': "null", 'Position': "null", 'time_period': "null", 'Location': "null"},
            'Education': {'Institute': "null", 'time_period': "null", 'Location': "null"},
            'Address': {'Current_city': "null", 'Home_town': "null"},
            'Favouriate': {},
            'Contact_info': {}
            }

    ###Finding Name of the user
    #Min div element is found which contains all the information
    main_div = soup.div.find(id="globalContainer")

    #finding name of the user
    def find_name():
        name = main_div.find(id="fb-timeline-cover-name").get_text()
        print("\n"+G+"Name:"+W+name)

    ###Finding About the user details
    #finding work details of the user
    def find_eduwork_details():
        education = soup.find(id="pagelet_eduwork")
        apple=education.find(attrs={"class":"_4qm1"})
        if (apple.get_text() != " "):
            for category in education.find_all(attrs={"class":"_4qm1"}):
                print(G+category.find('span').get_text() + " : "+W)
                for company in category.find_all(attrs={"class":"_2tdc"}):
                    if (company.get_text() != " "):
                        print(company.get_text())
                    else:
                        continue
        else:
            print("No work details found")

    #finding home details of the user
    def find_home_details():
        if(soup.find(id="pagelet_hometown") !=" "):
                home = soup.find(id="pagelet_hometown")
                for category in home.find_all(attrs={"class":"_4qm1"}):
                    print(G+category.find('span').get_text() + " : "+W)
                    for company in category.find_all(attrs={"class":"_42ef"}):
                        if (company.get_text() != " "):
                            print(company.get_text())
                        else:
                            continue
        else:
            print("No Home details found")

    #finding contact details of the user
    def find_contact_details():
        contact = soup.find(id="pagelet_contact")
        orange = contact.find(attrs={"class":"_4qm1"})
        if (orange.get_text() !=" "):
            for category in contact.find_all(attrs={"class":"_4qm1"}):
                print(G+category.find('span').get_text() + " : "+W)
                for company in category.find_all(attrs={"class":"_2iem"}):
                    if (company.get_text() != " "):
                        print(company.get_text())
                    else:
                        continue
        else:
             print("No Contact details found")

    ###Logic for finding the status of the response
    if ("200" in str(response)):
        find_name()
        find_eduwork_details()
        find_home_details()

    elif ("404" in str(response)):
        print(R+"Error: Profile not found")
    else:
        print(R+"Error: some other response")
    return()

def Instagram():
    print ('\n' + W + '[+]' + G + ' Fetching Data From Instagram...' + '\n')
    username = input(C+"root@osint:"+W+"~/Username# Enter the Username:")
    r = requests.get("https://www.instagram.com/"+ username +"/?__a=1")
    if r.status_code == 200:
        res = r.json()['graphql']['user']
        print(G+"\nUsername: " + W+res['username'])
        print(G+"Full Name: "+W+res['full_name'])
        try:
            print(G+"Business Category: "+W+res['edge_follow']['business_category_name'])
        except:
            print(G+"Account :"+W+" Private")
        finally:
            print(G+"Biograph: " + W+res['biography'])
            print(G+"URL: "+ W+str(res['external_url']))
            print(G+"Followers: "+W+str(res['edge_followed_by']['count']))
            print(G+"Following: "+W+str(res['edge_follow']['count']))
            print(G+"Profile Picture HD: " + W+res['profile_pic_url_hd'])
    elif r.status_code == 404:
        print(R+"Error: Profile Not Found")
    else:
        print(R+"Error: Something Went Wrong")

def ScrapTweets():
    print (W + '[+]' + G + ' Fetching Data From Twitter...' + '\n')
    username = input(C+"root@osint:"+W+"~/Username# Enter the Username : ")
    link = "https://twitter.com/" + username
    the_client = uReq(link)
    page_html = the_client.read()
    the_client.close()

    soup = BeautifulSoup(page_html, 'html.parser')

    try:
        full_name = soup.find('a', attrs={"class": "ProfileHeaderCard-nameLink u-textInheritColor js-nav"})
        print(G+"User Name --> " +W+ full_name.text)
    except:
        print("User Name -->"+R+" Not Found")
    print()

    try:
        user_id = soup.find('b', attrs={"class": "u-linkComplex-target"})
        print(G+"User Id --> "+W + user_id.text)
    except:
        print("User Id --> "+R+"Not Found")
    print()

    try:
        decription = soup.find('p', attrs={"class": "ProfileHeaderCard-bio u-dir"})
        print(G+"Description --> "+W + decription.text)
    except:
        print(R+"Decription not provided by the user")
    print()

    try:
        user_location = soup.find('span', attrs={"class": "ProfileHeaderCard-locationText u-dir"})
        print(G+"Location -->  " + W+user_location.text.strip())
    except:
        print(R+"Location not provided by the user")
    print()

    try:
        connectivity = soup.find('span', attrs={"class": "ProfileHeaderCard-urlText u-dir"})
        tittle = connectivity.a["title"]
        print(G+"Link provided by the user --> " +W+ tittle)
    except:
        print(R+"No contact link is provided by the user")
    print()

    try:
        join_date = soup.find('span', attrs={"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"})
        print(G+"The user joined twitter on --> " +W+ join_date.text)
    except:
        print(R+"The joined date is not provided by the user")
    print()

    try:
        birth = soup.find('span', attrs={"class": "ProfileHeaderCard-birthdateText u-dir"})
        birth_date = birth.span.text
        print(G+"Date of Birth:"+W+birth_date.strip())
    except:
        print(R+"Birth Date not provided by the user")
    print()

    try:
        span_box = soup.findAll('span', attrs={"class": "ProfileNav-value"})
        print(G+"Total tweets --> " + W+span_box[0].text)
    except:
        print(R+"Total Tweets --> Zero")
    print()

    try:
        print(G+"Following --> " +W+span_box[1].text)
    except:
        print(R+"Following --> Zero")
    print()

    try:
        print(G+"Followers --> " +W+ span_box[2].text)
    except:
        print(R+"Followers --> Zero")
    print()

    try:
        print(G+"Likes send by him --> " + W+span_box[3].text)
    except:
        print(R"Likes send by him --> Zero")
    print()

    try:
        if span_box[4].text != "More ":
            print(G+"No. of parties he is Subscribed to --> " + W+span_box[4].text)
        else:
            print(G+"No. of parties he is Subscribed to --> Zero")
    except:
        print("No. of parties he is Subscribed to --> Zero")
    print(W)

    spana = soup.findAll('span', attrs={"class": "ProfileNav-value"})

    print(G+"Tweets by "+W+ username + " are --> ")
    # TweetTextSize TweetTextSize--normal js-tweet-text tweet-text
    for tweets in soup.findAll('p', attrs={"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
        print(tweets.text)
        print()

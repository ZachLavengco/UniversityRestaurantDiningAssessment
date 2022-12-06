
import pandas as pd
import requests
from bs4 import BeautifulSoup

def colleges():
    # this part retrieves the addresses of the first 22 colleges on this webpage
    url = "https://www.studypoint.com/admissions/category/size/15000-25000-students/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    address = []
    colleges = []

    # gets the link to page with all the college links to individual websites
    for a in soup.select('.list-result a'):
        slink = a['href']
        home = 'https://www.studypoint.com'
        page = home.strip() + slink.strip()
        #print(page)
    #     # concatenates link for each college link
        req2 = requests.get(page)
        soup2 = BeautifulSoup(req2.text, "html.parser")
        # parses through tables and retrieves address and student population
        for sibling in soup2.find_all('table')[0].children:
            for tbody in sibling:
                for tr in tbody:
                    if tr == '\n' or tr == '\xa0' or tr is None: # gets rid of weird values
                        continue
                    address.append(tr.get_text(strip=True))


    # retrieves the names of the first 22 colleges
    for a in soup.findAll(class_ ='result-title'):
        colleges.append(a.get_text(strip=True))

    # had to add empty strings to get correct format of addresses
    address.insert(address.index('One Shields AvenueDavis, CA 95616'), '')
    address.insert(address.index('(530) 752-1011'), '')
    address.insert(address.index('www.ucdavis.edu'), '')
    addy = address[1::9]

    # this part retrieves the next 22 college addresses on a separate webpage
    url2 = 'https://www.studypoint.com/admissions/category/size/more-than-25000-students/'
    req3 = requests.get(url2)
    soup3 = BeautifulSoup(req3.text, "html.parser")

    address2 = []

    for a in soup3.select('.list-result a'):
        slink = a['href']
        home = 'https://www.studypoint.com'
        # concatenates link for each college link
        page = home.strip() + slink.strip()
        req4 = requests.get(page)
        soup4 = BeautifulSoup(req4.text, "html.parser")
        # parses through tables and retrieves address and student population
        for sibling in soup4.find_all('table')[0].children:
            for tbody in sibling:
                for tr in tbody:
                    if tr == '\n' or tr == '\xa0' or tr is None: # gets rid of weird values
                        continue
                    address2.append(tr.get_text(strip=True))

    # retrieves the next 22 colleges on separate webpage
    for a in soup3.findAll(class_ ='result-title'):
        colleges.append(a.get_text(strip=True))

    # cleans up the colleges list names
    complete_colleges = [sub.replace(' Admissions Information', '') for sub in colleges]


    # adds all the addresses to one list called complete_list
    address2 = address2[1::9]
    complete_addresses = addy + address2
    complete_list = []

    if(len(complete_colleges) == len(complete_addresses)):
        for idx, x in enumerate(complete_colleges):
            dict = {
                "college": complete_colleges[idx],
                "location": complete_addresses[idx]
            }
            complete_list.append(dict)

    print(complete_list)
    # print(complete_colleges)
    # print(complete_addresses
    return complete_list
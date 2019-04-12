from bs4 import BeautifulSoup
import urllib3
import re


def FetchPassword(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)

    username = "freevpn" + url[19:21]

    content = response.data

    soup = BeautifulSoup(content, "lxml")
    pt = soup.find_all('div', class_='plan')

    temp = re.search("Password:</b> .*<span", str(pt[-1]))
    password = str(pt[-1])

    print('OpenVPN - ' + url)
    print('Username: ' + username)
    print('Password: ' + password[(temp.span()[0]+14):(temp.span()[1]-5)])
    return

FetchPassword("http://www.freevpn.me/accounts")
FetchPassword("http://www.freevpn.se/accounts")
FetchPassword("http://www.freevpn.it/accounts")
FetchPassword("http://www.freevpn.be/accounts")
FetchPassword("http://www.freevpn.im/accounts")
FetchPassword("http://www.freevpn.co.uk/accounts")


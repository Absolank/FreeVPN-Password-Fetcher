from bs4 import BeautifulSoup
import urllib3
import re
import sys

url_link = {
    "-me": "http://www.freevpn.me/accounts",
    "-se": "http://www.freevpn.se/accounts",
    "-it": "http://www.freevpn.it/accounts",
    "-be": "http://www.freevpn.be/accounts",
    "-im": "http://www.freevpn.im/accounts",
    "-ck": "http://www.freevpn.co.uk/accounts"
}

http = urllib3.PoolManager()


def fetch_password(url):
    try:
        response = http.request('GET', url)
    except urllib3.exceptions.MaxRetryError:
        print("Internet connection error!!!!")
        sys.exit(1)
    ul = url.split('/')
    username = ul[2][4:]

    content = response.data

    soup = BeautifulSoup(content, "lxml")

    pt = soup.find_all('div', class_='pricing-table')
    if pt is None or pt.__len__() < 1:
        return

    span4 = pt[0].find_all('div', class_="span4")
    if span4 is None or span4.__len__() < 1:
        return

    li = span4[0].find_all('li')
    if li is None or li.__len__() < 3:
        return

    password = re.findall("> .*<", str(li[2]))
    if password is None or password.__len__() < 1:
        return

    print('OpenVPN - ' + url)
    print('Username: ' + username)
    print('Password: ' + password[0][1:-1])
    return



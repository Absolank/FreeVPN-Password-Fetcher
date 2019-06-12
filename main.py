#!/usr/bin/python3

import freevpn
import sys

help_string = """ 
    main.py  [options]

        -me                   http://www.freevpn.me/
        
        -se                   http://www.freevpn.se/
        
        -it                   http://www.freevpn.it/
        
        -be                   http://www.freevpn.be/
        
        -im                   http://www.freevpn.im/
        
        -ck                   http://www.freevpn.co.uk/
        
        -all                  For fetching all passwords
        
        --help                For help
"""



def main():
    args = sys.argv
    if args.__len__() < 2:
        print("No arguments specified")
    if args.__len__() == 2 and "--help" in args:
        print(help_string)
    elif "-all" in args:
        for url in freevpn.url_link.values():
            freevpn.fetch_password(url)
    else:
        for arg in args:
            if arg in freevpn.url_link.keys():
                freevpn.fetch_password(freevpn.url_link[arg])


if __name__ == "__main__":
    main()

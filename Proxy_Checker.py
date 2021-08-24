import urllib.request , socket
import os

socket.setdefaulttimeout(180)

proxyList = []

path = str(input("Your Proxy file Path: "))

file = open(path, "r")

for line in file:
    proxyList.append(line)


def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
        #sock=urllib.urlopen(req)
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print( "ERROR:", detail)
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        print ("Bad Proxy", item)
    else:
        file = open("Proxys.txt", "w") 
        file.write(item)
        print (item, "is working")
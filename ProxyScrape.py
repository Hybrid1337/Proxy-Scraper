import requests
Proxy = open('Proxies.txt', 'a')
print(" US | DE | ZA | ES | CN | RU | FR | GB | RO | BR | SG | KH")
Country = input("Country : ")
print("HTTP | SOCKS4 | SOCKS5")
Type = input("Proxy Type: ")
if Type == 'HTTP':
    Update = f'https://api.proxyscrape.com?request=lastupdated&proxytype=http'
    Api = f'https://api.proxyscrape.com?request=displayproxies&proxytype=http&anonymity=all&ssl=all'
    Update1 = requests.get(Update)
    print("Updated : " + Update1.text)
    Api1 = requests.get(Api)
    print(Api1.text)
    Proxy.write(Api1.text)
elif Type == 'SOCKS4':
    Update1 = f'https://api.proxyscrape.com?request=lastupdated&proxytype=socks4'
    Api1 = f'https://api.proxyscrape.com?request=displayproxies&proxytype=socks4'
    Update2 = requests.get(Update1)
    print("Updated : " + Update2.text)
    Api2 = requests.get(Api1)
    print(Api2.text)
    Proxy.write(Api2.text)
elif Type == 'SOCKS5':
    Update2 = f'https://api.proxyscrape.com?request=lastupdated&proxytype=socks5'
    Api2 = f'https://api.proxyscrape.com?request=displayproxies&proxytype=socks5'
    Update3 = requests.get(Update2) 
    print("Updated : " + Update3.text)
    Api3 = requests.get(Api2)
    print(Api3.text)
    Proxy.write(Api3.text)
else:
    print("Incorrect Input.")

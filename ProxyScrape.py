import requests
Proxy = open('Proxies.txt', 'a')
TimeOut = input("TimeOut : ")
print("Example : US")
Country = input("Country : ")
print("1. Http , 2. Https , 3. All")
Type = input(": ")
if Type == '1':
    Update = f'https://api.proxyscrape.com?request=lastupdated&proxytype=http'
    Api = f'https://api.proxyscrape.com?request=displayproxies&proxytype=http&timeout={TimeOut}&country={Country}&anonymity=elite&ssl=no'
    Update1 = requests.get(Update)
    print("Updated : " + Update1.text)
    Api1 = requests.get(Api)
    print(Api1.text)
    Proxy.write(Api1.text)
elif Type == '2':
    Update1 = f'https://api.proxyscrape.com?request=lastupdated&proxytype=http'
    Api1 = f'https://api.proxyscrape.com?request=displayproxies&proxytype=https&timeout={TimeOut}&country={Country}&anonymity=elite&ssl=no'
    Update2 = requests.get(Update1)
    print("Updated : " + Update2.text)
    Api2 = requests.get(Api1)
    print(Api2.text)
    Proxy.write(Api2.text)
elif Type == '3':
    Update2 = f'https://api.proxyscrape.com?request=lastupdated&proxytype=all'
    Api2 = f'https://api.proxyscrape.com?request=displayproxies&proxytype=all&timeout={TimeOut}&country={Country}&anonymity=elite&ssl=no'
    Update3 = requests.get(Update2) 
    print("Updated : " + Update3.text)
    Api3 = requests.get(Api2)
    print(Api3.text)
    Proxy.write(Api3.text)
else:
    print("Incorrect Input.")
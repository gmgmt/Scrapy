import requests
from lxml import etree
import re
import random
import time

# def get_ip():
#     ip_req = requests.get("http://mp.pachongdaili.com/api.php?order=d1546865289")
#     ip_text = ip_req.text
#     # print(ip_text.split('</br>'))
#     ip_list = re.sub(r'\d+s', "",
#                      ip_text.replace('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />',
#                                      "")).replace("\r\n", "").replace("-", "").replace(" ", "").replace(
#         "</body></html>", "").replace("<html><body>", "").split('</br>')
#     # print(ip[i])
#     # print("20", len(ip_list) - 1)
#     # print(type(ip_list))
#     # print(ip_proxies)
#     # print(ip_list)
#     # i = random.choice(range(len(ip_list) - 1))#在这里不能随机ip
#     ip_proxies=[]
#     for i in ip_list[:-1]:
#         # ip_proxies = 'http://dtip123456:dtip123456@' + ip_list[i] + ':888'
#         ip_proxie = 'http://dtip123456:dtip123456@' +i+ ':888'
#         ip_proxies.append(ip_proxie)
#     return ip_proxies
headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
# 'Cookie': 'UM_distinctid=1682c128555128-0f7e7cd0177148-671b1b7c-1fa400-1682c12855610c; CNZZDATA1262639445=1753030362-1546924484-%7C1547002574; Hm_lvt_eee540744c3b30c74bc273b168ccec21=1546927641,1547002580; Hm_lpvt_eee540744c3b30c74bc273b168ccec21=1547002580',
'Host': 'mp.pachongdaili.com',
# 'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',}

def get_ip():
    ip_req = requests.get("http://mp.pachongdaili.com/api.php?order=d1546865289",headers=headers)
    # print("1",ip_req.text)

    html = etree.HTML(ip_req.text)
    ip_list= html.xpath("//body/text()")[0].split("    ")
    # print("2", ip_list)
    ip_list2=[]
    ip_list3=[]
    ip_list4=[]
    for ip in ip_list:
        new_ip=ip.strip().split("s")
        # print(new_ip)
        ip_list2.append(new_ip)
        for i in new_ip:
            ip_list3.append(i)
    # print("3", ip_list3)
    for k in range(1,len(ip_list3),2):
        # print(k)
        if int(ip_list3[k])>30:
            ip_list4.append(ip_list3[k-1])
    # print("4", ip_list4)
    ip_proxies = []
    for i in ip_list4:
        # ip_proxies = 'http://dtip123456:dtip123456@' + ip_list[i] + ':888'
        ip_proxie = 'http://dtip123456:dtip123456@' + i + ':888'
        ip_proxies.append(ip_proxie)
    print('ip1_list',ip_proxies)
    if ip_proxies == [] or ip_proxies ==None:
        time.sleep(1.5)
        # get_ip()
        return get_ip()
    else:
        return ip_proxies

def get_ip2():
    ip_req = requests.get("http://mp.pachongdaili.com/api.php?order=d1546865289",headers=headers)
    # print("1",ip_req.text)

    html = etree.HTML(ip_req.text)
    ip_list= html.xpath("//body/text()")[0].split("    ")
    # print("2", ip_list)
    ip_list2=[]
    ip_list3=[]
    ip_list4=[]
    for ip in ip_list:
        new_ip=ip.strip().split("s")
        # print(new_ip)
        ip_list2.append(new_ip)
        for i in new_ip:
            ip_list3.append(i)
    # print("3", ip_list3)
    for k in range(1,len(ip_list3),2):
        # print(k)
        if int(ip_list3[k])>30:
            ip_list4.append(ip_list3[k-1])
    # print("4", ip_list4)
    ip_proxies = []
    for i in ip_list4:
        # ip_proxies = 'http://dtip123456:dtip123456@' + ip_list[i] + ':888'
        ip_proxie = 'http://dtip123456:dtip123456@' + i + ':888'
        ip_proxies.append(ip_proxie)
    print('ip1_list',ip_proxies)
    if ip_proxies == [] or ip_proxies == None:
        time.sleep(1.5)
        return get_ip2()
    else:
        return ip_proxies

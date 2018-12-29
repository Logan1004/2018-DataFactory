import requests
from bs4 import BeautifulSoup
import random
import urllib.request
import time
import lxml
import re
import threading
from fake_useragent import UserAgent
lock = threading.Lock()
successNum = 1
ips = []
ipPrevious = ""
fp = open("/Users/logan/Desktop/DataFactory/Homework1/Final/Data.txt", 'w+')
fp2 = open("/Users/logan/Desktop/DataFactory/Homework1/Final/Except.txt",'w+')

# 通过自动开线程的爬虫(伪多线程)，当一个线程被阻挡的时候，自动开启新的线程

def get_ip():
    """获取代理IP"""
    url = "http://www.xicidaili.com/nn"
    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
                "Accept-Encoding":"gzip, deflate, sdch",
                "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                "Referer":"http://www.xicidaili.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                }
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.table.find_all("td")
    ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
    port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
    ip = re.findall(ip_compile,str(data))       # 获取所有IP
    port = re.findall(port_compile,str(data))   # 获取所有端口
    return [":".join(i) for i in zip(ip,port)]  # 组合IP+端口，如：115.112.88.23:8080
# 设置 user-agent列表，每次请求时，可在此列表中随机挑选一个user-agnet


#生成随机头
def randHeader():
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']

    ua = UserAgent()

    header = {
        #'Connection': head_connection[0],
        #'Accept': head_accept[0],
        #'Accept-Language': head_accept_language[1],
        'User-Agent': ua.random
        #'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36"
    }
    #"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36"
    return header

def crawl(url):
    s = requests.session()
    headers = randHeader()
    global successNum
    global ipPrevious
    if (successNum==1):
        ip = random.choice(ips)
        ipPrevious = ip
        successNum=0
    else:
        ip = ipPrevious
    #1:failure 0:success
    proxies = {
            "http":ip,
        }

    try:
        response = s.get(url, headers=headers, proxies = proxies, timeout=30)
        if response.status_code == 200:
            text = response.text
            return text
    except:
        return False

def loadexcept(line,num):
    # 提取异常网页的信息
    global fp
    global fp2
    html = crawl(line)
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        soup = ""
    soup_texts = ""
    if (soup != ""):

        # 根据不同的页面爬取不同位置的信息

        try:
            soup_texts = soup.body.find(class_='avu-content avu-section').find('div',
                                                                               class_='av-dp-container').find(
                'div', class_='avu-page-container avu-clearfix').find('section').find(
                class_='avu-full-width').string
        except:
            try:
                soup_texts = soup.body.find('div', id='a-page').find('div', class_='a-container', role='main').find(
                    'div', class_='centerColAlign', id='centerCol').find('div', id='title_feature_div').find('div',
                                                                                                             id='titleSection'). \
                    find('h1', id='title').find('span').string
            except:
                try:
                    soup_texts = soup.body.find('div', id='a-page').find('div', id='dp').find('div',
                                                                                              id='dp-container').find(
                        'div', class_='centerColAlign', id='centerCol').find('div',
                                                                             id='title_feature_div').find('div',
                                                                                                          id='titleSection'). \
                        find('h1', id='title').find('span').string
                except:
                    try:
                        soup_texts = soup.find('title').string
                    except:
                        soup_texts = ""
    if (soup_texts != ""):
        if (soup_texts.strip() == 'Robot Check'):
            t1 = threading.Thread(target=loadexcept, args=(line,num))
            print("Thread: Robot Check")
            t1.start()
        # 当一个进程被组织时，新开一个进程继续尝试
        else:
            print("Thread"+" "+line + " " + str(num) + " " + soup_texts.strip())
            with lock:
                print("lock")
                fp.write(soup_texts.strip() + "\n")


def loadData(fileName,num):
    global fp
    global fp2
    with open(fileName) as txtData:
        lines=txtData.readlines()
        for line in lines:
            if num % 200 == 0:
                ips.extend(get_ip())
            line.replace("\n","")

            num = num + 1
            if (num % 500==0):
                print("rest!")
                time.sleep(300)

            line = "https://www."+ line
            html = crawl(line)
            try:
               soup = BeautifulSoup(html, "lxml")
            except:
                soup = ""
            if (soup != ""):
                try:
                    soup_texts = soup.body.find(class_='avu-content avu-section').find('div',
                                                                                   class_='av-dp-container').find(
                        'div', class_='avu-page-container avu-clearfix').find('section').find(
                        class_='avu-full-width').string
                except:
                    try:
                        soup_texts = soup.body.find('div', id='a-page').find('div', class_='a-container', role='main').find(
                            'div', class_='centerColAlign', id='centerCol').find('div', id='title_feature_div').find('div',id='titleSection'). \
                            find('h1', id='title').find('span').string
                    except:
                        try:
                            soup_texts = soup.body.find('div', id='a-page').find('div', id='dp').find('div',id='dp-container').find(
                                'div', class_='centerColAlign', id='centerCol').find('div',
                                                                                 id='title_feature_div').find('div',id='titleSection'). \
                                find('h1', id='title').find('span').string
                        except:
                            try:
                                soup_texts = soup.find('title').string
                            except:
                                 soup_texts=""
                                 fp2.write(line)
                global successNum
                if (soup_texts!=""):
                    if (soup_texts.strip()=='Robot Check'):

                        fp2.write(str(num)+" "+line)
                        t1 = threading.Thread(target=loadexcept, args=(line,num))
                        print("Robot Check")
                        successNum=1
                        t1.start()
                    else:
                        print(line+" "+str(num)+" "+soup_texts.strip())
                        successNum=0
                        with lock:
                            print("lock")
                            fp.write(soup_texts.strip()+"\n")

    return num

if __name__ == '__main__':
    num = loadData("/Users/logan/Desktop/DataFactory/Homework1/Final/Data.txt",0)
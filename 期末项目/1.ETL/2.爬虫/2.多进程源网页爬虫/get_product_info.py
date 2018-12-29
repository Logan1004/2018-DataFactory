
import readurls
import requests
import fcntl
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent
import random
import os
import threading
import multiprocessing
from time import sleep
import time

starttime = time.time()
def check_runtime():
    now = time.time()
    global starttime
    return now - starttime
    

def get_header():
    ua = UserAgent()
    user_agent = ua.random
    head = {}
    head['User_Agent'] = user_agent
    # head['Connection'] = 'keep-alive'
    head['Accept'] = "text/html,application/xhtml+xml,application/xml"
    head['Accept-Language'] = "zh-CN,zh;q=0.9,en;q=0.8"

    # head["Referer"] = "https://www.amazon.com"
    # head['Host'] = "https://www.amazon.com"
    return head

def get_proxy():
    global lock
    global proxies
    if len(proxies) == 0:
        with lock:
            proxies = get_ips()
    ip = random.sample(proxies, 1)
    ip = ip[0]
    with lock:
        proxies.remove(ip)
    print(ip)
    proxy = {'https': ip}
    return proxy

def get_cookies():
    with open('cookies') as file:
        cookie = file.readlines()

        lines = random.sample(cookie, 1)
        lines = lines[0]
        lines = lines.split(';')
        cookie = {}
        for line in lines:  # 按照字符：进行划分读取
            # 其设置为1就会把字符串拆分成2份
            name, value = line.strip().split('=', 1)
            cookie[name] = value
        print(cookie)
        return cookie
def write_fail_url(url):

    with open('fail_url.csv', 'a') as log:
        fcntl.flock(log.fileno(), fcntl.LOCK_EX)
        log.write(url+'\n')


def check_info(text):
    soup = BeautifulSoup(text, 'lxml')
    if soup.title.string == "Sorry! Something went wrong!":
        print("Dog")
        return False
    if soup.title.string == "Robot Check":
        print("Robot")
        return False
    if soup.title.string == "Page Not Found":
        print("404")
        return False
    print(soup.title.string)
    return True



def access_url(start, end, proxy, head):
    count = 0
    cookie = get_cookies()
    time = 0
    while start < end:
        url = urls[start]
        id = get_id(url)
        if os.path.exists("data/%s.html"%id):
            start = start + 1
            continue
        try:
            result = requests.get(url, headers=head, proxies=proxy, cookies=cookie)
            id = get_id(url)
            if check_info(result.text):
                store_pages('data/'+id+'.html', result.text)
                count = 0
                time = 0
                print('Success %s' % url)
            else:
                count = count + 1  # 处理多次无法访问的情况
                if count >= 5:
                    print('Fail %s  <<recorded>>' % url)
                    write_fail_url(url)
                    count = 0
                    time = time + 1
                    if time > 10:
                        head = get_header()
                        proxy = get_proxy()
                        cookie = get_cookies()
                        time = 0
                else:
                    print('Fail %s  %d time(s)' % (url, count))
                    start = start - 1

        except:
            print("open_fail")
            count = count + 1                       # 处理多次无法访问的情况
            if count >= 5:
                print('Fail %s  <<recorded>>' % url)
                write_fail_url(url)
                count = 0
                time = time+1
                if time > 10:
                    head = get_header()
                    proxy = get_proxy()
                    cookie = get_cookies()
                    time = 0
            else:
                print('Fail %s  %d time(s)' % (url, count))
                start = start - 1

        finally:
            start = start + 1
            sleep_time = random.random()
            sleep(sleep_time)

#for test
def access(url, proxy, head, cookie):
    count = 0
    try:
        result = requests.get(url, headers=head, cookies=cookie, proxies=proxy)
        print(result.text)
        id = get_id(url)
        if check_info(result.text):
            store_pages('data/' + id + '.html', result.text)
            print('Success %s' % url)
        else:
            count = count + 1  # 处理多次无法访问的情况
            if count >= 10:
                print('Fail %s  <<recorded>>' % url)
                write_fail_url(url)
                count = 0
            else:
                print('Fail %s  %d time(s)' % (url, count))

    except:
        print("open_fail")
        count = count + 1  # 处理多次无法访问的情况
        if count >= 10:
            print('Fail %s  <<recorded>>' % url)
            write_fail_url(url)

            count = 0
        else:
            print('Fail %s  %d time(s)' % (url, count))
            head = get_header()
            proxy = get_proxy()

    finally:
        sleep_time = random.random() * 3
        sleep(sleep_time)


def store_pages(filename, text):
    with open(filename, 'w') as file:
        try:
            soup = BeautifulSoup(text, 'lxml')
            [s.extract() for s in soup('script')]
            [s.extract() for s in soup('style')]
            [s.extract() for s in soup('link')]
            [s.extract() for s in soup('img')]
            [s.extract() for s in soup.select(".navFooterVerticalColumn")]
            [s.extract() for s in soup.select(".navFooterDescLine")]


            file.write(soup.prettify())

        except:
            print('Fail to write %s' % filename)

        finally:
            pass



# def get_ip():
#     """获取代理IP"""
#     url = "http://www.xicidaili.com/nn"
#     headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
#                 "Accept-Encoding": "gzip, deflate, sdch",
#                 "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
#                 "Referer": "http://www.xicidaili.com",
#                 "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
#                 }
#     proxy = {"https": "121.225.27.0:3128"}
#     r = requests.get(url, headers=headers, proxies=proxy)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     data = soup.table.find_all("td")
#     ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
#     port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
#     ip = re.findall(ip_compile, str(data))       # 获取所有IP
#     port = re.findall(port_compile, str(data))   # 获取所有端口
#     return [":".join(i) for i in zip(ip, port)]  # 组合IP+端口，如：115.112.88.23:8080

def get_ips():
    proxy = []
    if check_runtime() > 1200 :
        with open("pick.txt", 'r') as file:
            url = "http://webapi.http.zhimacangku.com/getip?num=10&type=1&pro=0&city=0&yys=100017&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=2&regions="
            result = requests.get(url)
            file.write(result.text.strip())
        starttime = time.time()
    with open('pick.txt', 'r') as file:

        while 1:
            line = file.readline()
            if not line:
                break
            line = line.strip('\n')
            proxy.append(line)
    return proxy

def get_id(url):
    pattern = re.compile(r'https://www\.amazon\.com/dp/([a-zA-Z0-9]+)')
    group = pattern.match(url)
    id = group.group(1)
    return id



soup = BeautifulSoup(open('robot.html'), 'lxml')
robot = soup.title.string
proxies = get_ips()
print(proxies)
urls = readurls.load()
mutex = threading.Lock()
lock = multiprocessing.Lock()

if __name__ == "__main__":

    step = int(len(urls)/20)
    start = 0
    pool = multiprocessing.Pool(20)
    for i in range(19):
        pool.apply_async(access_url, args=(start, start + step, get_proxy(), get_header()))
        start = start + step + 1
    pool.apply_async(access_url, args=(start, len(urls) - 1, get_proxy(), get_header()))
    pool.close()
    pool.join()
    print("Done ")
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)





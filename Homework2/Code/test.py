#coding=utf8
import sys

import requests
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent
def randHeader():
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']

    ua = UserAgent()

    header = {
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36"
    }
    # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36"
    return header

def crawl(url):
    headers = randHeader()
    try:
        response = requests.get("https://www.amazon.com/dp/B003AI2VGA", headers=headers,  timeout=30)
        if response.status_code == 200:
            text = response.text
            return text
    except:
        return False


# html = crawl("http://www.amazon.com/dp/B003AI2VGA")
# html = crawl("https://www.amazon.com/dp/6305508569")
# html = crawl("https://www.amazon.com/dp/B002LSIAQU")

# fp.write(html)

# soup_texts = soup.find('div', id = 'a-page').find('div', class_ ='avu-content avu-section').find('div',class_='av-dp-container').find('div',class_='avu-page-container avu-clearfix').find_next('div')
# soup_texts = soup.findAll('div', id = 'a-page')

# soup_texts = soup.findAll(attrs={'class':'avu-content'})


# .find('div',id='title').find('span').string
#f = open("/Users/logan/Desktop/temp.html",'w')
#html = crawl("amazon.com/dp/B003AI2VGA")
#html = crawl("www.baidu.com")
#f.write(html)
#try:
#    soup = BeautifulSoup(html, "lxml")
#except:
#    soup = ""
#soup_texts = ""
#print(soup)


#path = '/Users/logan/Desktop/temp.html'
for i in range(1,139088):
    path = '/Users/logan/Desktop/data/data/example'+str(i)+'.html'
    print(i)
    #path = '/Users/logan/Desktop/temp.html'
    #path = '/Users/logan/Desktop/data/example2738.html'
#htmlf=open('/Users/logan/Desktop/temp.html','r',encoding="utf-8")
    form = 0
    with open(path, 'r') as f:
        Soup = BeautifulSoup(f.read(), 'lxml')
    #print(Soup.prettify())
        titles = Soup.select('tr > td > div > ul > li')
        if (titles==[]):
            titles = Soup.select('dd')
            form = 1
        #titles = Soup.findAll('span')
        #print(titles)
    if len(titles)>=3:
        try:
            directors = []
            actors = []
            num=0
            for title in titles:
                if ('Actors' in title.text):
                    actors = title.text.split(',')
                if ('Directors' in title.text):
                    directors = title.text.split(',')
            #if (form==0):
            #    directors = titles[1].text.split(',')
            #    actors = titles[0].text.split(',')
            #else:
            #    directors = titles[1].text.split(',')
            #    actors = titles[2].text.split(',')

#写入具体内容
            if (directors!=[] and actors!=[]):
                with open("XXX.csv","a",newline="") as datacsv:
                    csvwriter = csv.writer(datacsv,dialect = ("excel"))
                    for director in directors:
                        for actor in actors:
                            if ('Actors:' in actor):
                                actor = actor.replace('Actors:', '')
                            if ('Directors:' in director):
                                director = director.replace('Directors:', '')
                            print(director.strip(),actor.strip())
                            csvwriter.writerow([director.strip(),actor.strip()])
        except:
            print(num)
#with open(path,'wb') as f:
#    csv_write = csv.writer(f, dialect='excel')
#    csv_head = ["good", "bad"]
#    csv_write.writerow(csv_head)
#    csv_write.writerow(str(director))
#    csv_write.writerow(str(actor))

print ("write over")
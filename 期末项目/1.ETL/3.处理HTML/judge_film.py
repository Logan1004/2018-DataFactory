import os
from bs4 import BeautifulSoup
# 提取
class ProcessInfo():
# 判断是否是电影 通过imdb 和 时间 做初步的判断
    def check_imdb(self, imdb):
        pass


    def check_duration(self, length):
        pass

    def check_rate(self, rate):
        pass

    def check_introduction(self, comment):
        pass

    def check(self, info):
        if info['imdb'] != "None":
            return True
        elif float(info['time']) > 60 and float(info['time']) < 160:
            return True
        elif info['rate'] != "Not Rated":
            return True
        else:
            return False
               

class GetMovieDetail():
    # 提取不同电影格式的信息
    def get_movie_name_1(self, soup):
        # Extract the movie IMDB and Rate
        name = soup.h1.text
        name = name.strip()
        name = name.strip(' VHS')
        # Extract the movie duration
        tag = 'min'
        time = '0'
        bange = soup.select(".av-badge-text")
        #p = soup.select(".avu-page-section")
        for item in bange:
            text = item.text.strip()
            if tag in text:
                time = text.strip(' min')
                # print(type(time))
                # print(time)
                break
        info = soup.select('span[data-automation-id]')
        rate = "not"
        imdb = "None"
        directors = []
        actors = []
        genres = []
        starrings = []
        studio = "None"
        language = "None"
        format = "None"
        subtitle = "None"
        # 提取 rate imdb directors actors genres starring studio language format suntitle

        p = soup.select_one("table")
        details = p.select("tr")
        for item in details:
            if item.th and item.th.text.strip() == "Genres":
                genre = item.select("a")
                for g in genre:
                    genres.append(g.text.strip())
                #print(genres)
            if item.th and item.th.text.strip() == "Starring":
                starring = item.select("a")
                for s in starring:
                    starrings.append(s.text.strip())
                #print(starrings)

            if item.th and item.th.text.strip() == "Supporting actors":
                actor = item.select("a")
                for a in actor:
                    actors.append(a.text.strip())
                #print(actors)

            if item.th and item.th.text.strip() == "Director":
                director = item.select("a")
                for d in director:
                    directors.append(d.text.strip())
                #print(directors)
            #print("sss")
            if item.th and item.th.text.strip() == "MPAA rating":
                rate = item.td.text.strip()
                #print(rate)

            if item.th and item.th.text.strip() == "Studio":
                studio = item.td.text.strip()
                #print(studio)

            if item.th and item.th.text.strip() == "Format":
                format = item.td.text.strip()
                #print(studio)

            if item.th and item.th.text.strip() == "Audio":
                language = item.td.text.strip()
                #print(language)

            if item.th and item.th.text.strip() == "Captions and subtitles":
                subtitle = item.td.text.strip()
                subtitle = subtitle.strip('Details').strip()
                #print(subtitle)

        for item in bange:
            text = item.text.strip()
            if tag in text:
                time = text.strip(' min')
                # print(type(time))
                # print(time)
                break

        if not info:
            imdb = "None"   
        else:
            for item in info:
                if item['data-automation-id'] == "imdb-rating-badge":
                    imdb = item.text.strip()
                if item['data-automation-id'] == "maturity-rating-badge":
                    rate = item.text.strip()
        #return {'name': name, 'time': time, 'imdb': imdb, 'rate': rate, 'directors': directors, 'actors':actors, 'genres':genres}

        return {'name': name, 'genre':genres,'time': time, 'imdb': imdb, 'rate': rate, 'directors': directors,'starring':starrings, 'actors': actors,
                'writers': "None"
            , 'producers': "None", 'format': format, "language": language, "date": "None", "subtitle": subtitle,'studio':studio}
        
    def get_movie_name_2(self, soup):
        # soup = BeautifulSoup(open('aaa.html'), 'lxml')
        # extract the movie name
        # print(soup.h1.span)
        name = soup.select_one("#productTitle")
        name = name.text.strip()
        name = name.strip(' VHS')

        # extract the movie run time and rate

        time = "0"
        format = "None"
        rate = "Not Rated"
        imdb = "None"
        directors = []
        actors = []
        writers = []
        producers = []
        language = "None"
        date = "None"
        asin = "None"
        subtitle = "None"
        details = soup.select('.bucket')
        detail = None
        # 提取 rate imdb directors actors writers producers language asin date subtitle details
        for item in details:
            if item.h2 and "Product" in item.h2.text.strip():
                detail = item
                break
        
        if detail:
            detail = detail.select_one('.content')
        else:
            return {'name': name, 'time': time, 'imdb': imdb, 'rate': rate}
        detail = detail.select('li')
        
        for item in detail:
            if item.b and item.b.text.strip() == "Format:":
                if item.b:
                    item.b.extract()
                if item.div:
                    item.div.extract()
                if item.span:
                    item.span.extract()
                format = item.text.strip()


            if item.b and item.b.text.strip() == "Run Time:":
                if item.b:
                    item.b.extract()
                if item.div:
                    item.div.extract()
                if item.span:
                    item.span.extract()
                if 'seconds' in item.text:
                    time = item.text.strip().strip(' seconds')
                    time = str(float(time)/60)
                else:
                    time = item.text.strip().strip(" minutes")


            if item.b and item.b.text.strip() == "Rated:":
                if item.b:
                    item.b.extract()
                if item.div:
                    item.div.extract()
                if item.span:
                    item.span.extract()
                rate = item.text.strip()

            if item.b and item.b.text.strip() == "Actors:":
                actor = item.select('a')
                for a in actor:
                    actors.append(a.text.strip())
            if item.b and item.b.text.strip() == "Directors:":
                director = item.select('a')
                for d in director:
                    directors.append(d.text.strip())

            if item.b and item.b.text.strip() == "Writers:":
                writer = item.select('a')
                for w in writer:
                    writers.append(w.text.strip())

            if item.b and item.b.text.strip() == "Producers:":
                producer = item.select('a')
                for p in producer:
                    producers.append(p.text.strip())

            if item.b and item.b.text.strip() == "Language:":
                if item.b:
                    item.b.extract()
                if item.div:
                    item.div.extract()
                if item.span:
                    item.span.extract()
                language = item.text.strip()

            if item.b and item.b.text.strip().find("Date")!=-1:
                if item.b:
                    item.b.extract()
                if item.div:
                    item.div.extract()
                if item.span:
                    item.span.extract()
                date = item.text.strip()

            if item.b and item.b.text.strip() == "Subtitles:":
                if item.b:
                    item.b.extract()
                if item.div:
                    item.div.extract()
                if item.span:
                    item.span.extract()
                subtitle = item.text.strip()

            if item.b and item.b.text.strip() == "ASIN:":
                if item.b:
                    item.b.extract()
                if item.div:
                    item.div.extract()
                if item.span:
                    item.span.extract()
                asin = item.text.strip()

        return {'name': name, 'genre': "None",'time': time, 'imdb': imdb, 'rate': rate, 'directors': directors, 'starring': "None",'actors': actors,'writers':writers
                ,'producers':producers,'format':format,"language":language,"date":date,"subtitle":subtitle,'studio': "None"}



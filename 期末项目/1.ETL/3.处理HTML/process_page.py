from judge_film import GetMovieDetail
from bs4 import BeautifulSoup
from judge_film import ProcessInfo
import csv
import os

# 基于电影判断 爬得网页不同的信息 写入csv
def load(filename):
    result = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            result.append(item['url'])
    return result

def loadmin(filename):
    result = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            result.append(item['id'])
    return result

def get_exist(filename):
    result = []
    with open(filename, 'r') as file:
        while 1:
            line = file.readline()
            if line:
                result.append(line.strip())
            else:
                break
    return result

def write_exist(filename, filelist):
    with open(filename, 'w') as file:
        for item in filelist:
            file.write(item+'\n')
        
    
def writeheader(filename, file):
    fileheader = ['name', 'genre','time', 'imdb', 'rate', 'directors','starring', 'actors', 'writers', 'producers', 'format', 'language',
                  'date', 'subtitle', 'studio', 'id']
    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fileheader)
        writer.writeheader()


def write(filename, file):
    fileheader = ['name', 'genre', 'time', 'imdb', 'rate', 'directors', 'starring', 'actors', 'writers', 'producers',
                  'format', 'language',
                  'date', 'subtitle', 'studio', 'id']
    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fileheader)
        for item in file:
            writer.writerow(item)

def writerelation(filename, file):
    fileheader = ['director', 'actor']
    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fileheader)
        for item in file:
            writer.writerow(item)


if __name__=="__main__":
    open_path = "movieList.csv"
    open_path_min = "detail.csv"
    judge_path = "judge.csv"
    save_path = "detail.csv"
    all_save_path = "movie_all.csv"
    error_path = "error.log"
    relation_path = "relation.csv"
    movies = loadmin(open_path_min)
    exist_list = get_exist(judge_path)
    result = []
    all_result = []
    error_list = []
    relation = []
    count = 0
    all = 0
    for item in movies:
        filename = '/Users/logan/Desktop/DataAll/data_all/'+item+".html"
        if os.path.exists(filename):
            if item in exist_list:
                continue
            exist_list.append(item)
            print("start %s"%item)
            processor = GetMovieDetail()
            soup = BeautifulSoup(open(filename), "lxml")
            info = []
            try:
                if not soup.h1:
                    continue
                if not soup.h1.span:
                    info = processor.get_movie_name_1(soup)
                else:
                    info = processor.get_movie_name_2(soup)
                check = ProcessInfo()
                info['id'] = item.strip('.html')
                print(info)
                count += 1
                result.append(info)
            except:
                error_list.append(item.strip('.html'))
                continue
            finally:
                if count % 500 == 0:
                    if all==0:
                        writeheader(relation_path,result)
                        all=1
                    write(relation_path, result)
                    result = []
                # if all % 500 == 0:
                #     write(all_save_path, all_result)
                #     all_result = []
    
    write_exist(judge_path, exist_list) 
    write_exist(error_path, error_list)               
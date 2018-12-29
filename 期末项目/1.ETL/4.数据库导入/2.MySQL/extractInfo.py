import csv


movieDict = {}
directorDict = {}
actorDict = {}
formatDict = {}
writerDict = {}
subtitleDict = {}
studioDict = {}
producerDict = {}
languageDict = {}
genreDict = {}
def loadFromCsv(filepath):
    result = []
    with open(filepath) as file:
        reader = csv.DictReader(file)
        for item in reader:
            result.append(item)

    return result

def stringToList(string):
    string = string.replace("\"", "")
    return [i.strip("\"").strip("\'").strip("['").strip("']").strip(" '") for i in string.strip("None").strip("\"").strip("[").strip("]").strip().split(",")]

def seperateString(string):
    return [i.strip("\"").lstrip().rstrip() for i in string.strip("None").split(",")]

def writeToFile(filename, data, header):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

    print("Success to save file %s"%filename)
# TODO: Extract the entity set data
# TODO: to create the movie table
movieList = []
def movieTable(id, date, rate, imdb, name, time):
    if imdb == "None":
        imdb = "0"
    if rate == "":
        rate = "Not Rated"
    temp = {}
    temp["id"] = id
    temp["date"] = date
    temp["imdb"] = imdb
    temp["rate"] = rate
    temp["name"] = name
    temp["time"] = time
    movieList.append(temp)


directorList = []
def directorsTable(name, id):
    temp = {}
    temp["name"] = name
    temp["id"] = id
    directorList.append(temp)

actorList = []
def actorTable(name, id):
    temp = {}
    temp["name"] = name
    temp["id"] = id
    actorList.append(temp)

languageList = []
def languageTable(type, id):
    temp = {}
    temp["type"] = type
    temp["id"] = id
    languageList.append(temp)

writerList = []
def writerTable(name, id):
    temp = {}
    temp["name"] = name
    temp["id"]  = id
    writerList.append(temp)

formatList = []
def formatTable(type, id):
    temp = {}
    temp["type"] = type
    temp["id"] = id
    formatList.append(temp)

producerList = []
def producerTable(name, id):
    temp = {}
    temp["name"] = name
    temp["id"] = id 
    producerList.append(temp)

subtitleList = []
def subtitleTable(language, id):
    temp = {}
    temp["language"] = language
    temp["id"] = id
    subtitleList.append(temp)

#TODO: contribute need to be modified
commentList = []
def commentTable(movieId, content, id):
    temp = {}
    temp["movieId"] = movieId
    temp["content"] = content
    temp["id"] = id
    commentList.append(temp)

    
studioList = []
def studioTable(name, id):
    temp = {}
    temp["name"] = name
    temp["id"] = id 
    studioList.append(temp)

# TODO: genre table
genreList = []
def genreTable(type, id):
    temp = {}
    temp["type"] = type
    temp["id"] = id
    genreList.append(temp)



# TODO: Extract the relation set

directorDirectMovieList = []
def directorDirectMovie(movieId, directorId):
    temp = {}
    temp["movie_id"] = movieId
    temp["director_id"] = directorId
    directorDirectMovieList.append(temp)

movieHasSubtitleList = []
def movieHasSubtitle(movieId, subtitleId):
    temp = {}
    temp["movie_id"] = movieId
    temp["subtitle_id"] = subtitleId
    movieHasSubtitleList.append(temp)

producerProduceMovieList = []
def producerProduceMovie(movieId, producerId):
    temp = {}
    temp["movie_id"] = movieId
    temp["producer_id"] = producerId
    producerProduceMovieList.append(temp)

writerWriteMovieList = []
def writerWriteMovie(movieId, writerId):
    temp = {}
    temp["movie_id"] = movieId
    temp["write_id"] = writerId
    writerWriteMovieList.append(temp)

actorActMovieList = []
def actorActMovie(movieId, actorId):
    temp = {}
    temp["movie_id"] = movieId
    temp["actor_id"] = actorId
    actorActMovieList.append(temp)

movieHasLanguageList = []
def movieHasLanguage(movieId, languageId):
    temp = {}
    temp["movie_id"] = movieId
    temp["language_id"] = languageId
    movieHasLanguageList.append(temp)

movieHasFormatList = []
def movieHasFormat(movieId, formatId):
    temp = {}
    temp["movie_id"] = movieId
    temp["format_id"]  = formatId
    movieHasFormatList.append(temp)

studioSponsorMovieList = []
def studioSponsorMovie(movieId, studioId):
    temp = {}
    temp["movie_id"] = movieId
    temp["studio_id"] = studioId
    studioSponsorMovieList.append(temp)

starStarringMovieList = []
def starStarringMovie(movieId, actorId):
    temp = {}
    temp["movie_id"] = movieId
    temp["actor_id"] = actorId
    starStarringMovieList.append(temp)

movieHasGenreList = []
def movieHasGenre(movieId, genreId):
    temp = {}
    temp["movie_id"] = movieId
    temp["genre_id"] = genreId
    movieHasGenreList.append(temp)





idList = []
def extract(datalist):
    # for entity set
    for data in datalist:
        # Get Meta Data
        id = data["id"]
        name = data["name"]
        time = data["time"]
        imdb = data["imdb"]
        rate = data["rate"]
        directors = stringToList(data["directors"])
        actors = stringToList(data["actors"]) 
        writers = stringToList(data["writers"])
        producers = stringToList(data["producers"])
        format_ = seperateString(data["format"])
        language = seperateString(data["language"])
        date = data["date"]
        genre = stringToList(data["genre"]) 
        subtitle = seperateString(data["subtitle"])
        studio = data["studio"]
        stars = stringToList(data["starring"])



        ### HEADERS
        movieHeader = ["id",  "date", "imdb", "rate","name", "time"]
        directorHeader = ["id", "name"]
        actorHeader = ["id", "name"]
        writerHeader = ["id", "name"]
        producerHeader = ["id", "name"]
        languageHeader = ["id", "type"]
        formatHeader = ["id", "type"]
        genreHeader = ["id", "type"]
        subtitleHeader = ["id", "language"]
        directorDirectMovieHeader = [ "movie_id", "director_id"]
        movieHasSubtitleHeader = ["movie_id","subtitle_id"]
        producerProduceMovieHeader = [ "movie_id","producer_id"]
        writerWriteMovieHeader = [ "movie_id", "write_id"]
        actorActMovieHeader = [ "movie_id" , "actor_id"]
        movieHasLanguageHeader = ["movie_id" ,"language_id"]
        movieHasFormatHeader = [ "movie_id", "format_id"]
        studioSponsorMovieHeader = ["movie_id","studio_id"]
        movieHasGenreHeader = [ "movie_id", "genre_id"]
        starStarringMovieHeader = ["movie_id","actor_id"]

        if time == "":
            time = "0"
        if len(date) > 15:
            date = "None"
        if name == "" or id == "":
            continue
        # Deduplicate movie
        if name in movieDict:
            id = movieDict[name]
        else:
            movieDict[name] = id
            movieTable(id, date, rate, imdb, name, time)

        # Deduplicate director
        for director in directors:
            if director == "":
                continue
            if director not in directorDict:
                tempId = len(directorDict) + 1
                directorDict[director] = tempId
                directorsTable(director, tempId)

        # Deduplicate actor

        for actor in actors:
            if actor == "":
                continue
            if actor not in actorDict:
                tempId = len(actorDict) + 1
                actorDict[actor] = tempId
                actorTable(actor, tempId)
        
        # Deduplicate language
        for lan in language:
            if lan == "":
                continue
            if lan not in languageDict:
                tempId = len(languageDict) + 1
                languageDict[lan] = tempId
                languageTable(lan, tempId)

        # Deduplicate writer
        for writer in writers:
            if writer == "":
                continue
            if writer not in writerDict:
                tempId = len(writerDict) + 1
                writerDict[writer] = tempId
                writerTable(writer, tempId)
        
        # Deduplicate format
        for fo in format_:
            if fo == "":
                continue
            if fo not in formatDict:
                tempId = len(formatDict)+ 1
                formatDict[fo] = tempId
                formatTable(fo, tempId)

        for producer in producers:
            if producer == "":
                continue
            if producer not in producerDict:
                tempId = len(producerDict) + 1
                producerDict[producer] = tempId
                producerTable(producer, tempId)

        # Deduplicate subtitle
        for sub in subtitle:
            if sub == "":
                continue
            if sub not in subtitleDict:
                tempId = len(subtitleDict) + 1
                subtitleDict[sub] = tempId
                subtitleTable(sub, tempId)


        # Deduplicate comment
        # pass
        ###
        ###
        ###

        # Deduplicate studio
        for sto in studio:
            if sto == "":
                continue
            if sto not in studioDict:
                tempId = len(studioDict) + 1
                studioDict[sto] = tempId
                studioTable(sto, tempId)


        # Deduplicate genre
        for gen in genre:
            if gen == "":
                continue
            if gen not in genreDict:
                tempId = len(genreDict) + 1
                genreDict[gen] = tempId
                genreTable(gen, tempId)

        # Deduplicate star
        for star in stars:
            if star == "":
                continue
            if star not in actorDict:
                tempId = len(actorDict)  + 1
                actorDict[star] = tempId
                actorTable(star, tempId)
        
        ####
        ####
        ####
        ####
        ####
        ####
        # For relation set 
    idList = []
    for data in datalist:
        # Get Meta Data
        id = data["id"]
        name = data["name"]
        time = data["time"]
        imdb = data["imdb"]
        rate = data["rate"]
        genre = stringToList(data["genre"]) 
        directors = stringToList(data["directors"])
        actors = stringToList(data["actors"]) 
        writers = stringToList(data["writers"])
        producers = stringToList(data["producers"])
        format_ = seperateString(data["format"])
        language = seperateString(data["language"])
        date = data["date"]
        subtitle = seperateString(data["subtitle"])
        studio = data["studio"]
        stars = stringToList(data["starring"])
        if name == "" or id == "":
            print("getOne")
            continue
        id = movieDict[name]
        if id in idList:
            continue
        idList.append(id)


        # director and movie
        temp = []
        for director in directors:
            if director == "" or director in temp:
                continue
            directorId = directorDict[director]
            directorDirectMovie(id, directorId)
            temp.append(director)
        
        # actor and movie
        temp = []
        for actor in actors:
            if actor == "" or actor in temp:
                continue
            actorId = actorDict[actor]
            actorActMovie(id, actorId)
            temp.append(actor)
        
        # subtitle and movie 
        temp = []
        for su in subtitle:
            if su == "" or su in temp:
                continue
            subtitleId = subtitleDict[su]   
            movieHasSubtitle(id, subtitleId)
            temp.append(su)

        # producer and movie
        temp = []
        for producer in producers:
            if producer == "" or producer in temp:
                continue
            producerId = producerDict[producer]
            producerProduceMovie(id, producerId)
            temp.append(producer)

        # writer and movie 
        temp = []
        for writer in writers:
            if writer == "" or writer in temp:
                continue
            writerId = writerDict[writer]
            writerWriteMovie(id, writerId)
            temp.append(writer)

        # language and movie
        temp = []
        for lan in language :
            if lan == "" or lan in temp:
                continue
            languageId = languageDict[lan]
            movieHasLanguage(id, languageId)
            temp.append(lan)

        # format and movie
        temp = []
        for fo in format_:
            if fo == "" or fo in temp:
                continue
            formatId = formatDict[fo]
            movieHasFormat(id, formatId)
            temp.append(fo)

        # studio and movie
        temp = []
        for sto in studio:
            if sto == "" or sto in temp:
                continue
            studioId = studioDict[sto]
            studioSponsorMovie(id, studioId)
            temp.append(sto)

        # star and movie
        temp = []
        for star in stars:
            if star=="" or star in temp:
                continue
            starId = actorDict[star]
            starStarringMovie(id, starId)
            temp.append(star)

        # movie and genre

        temp = []
        for gen in genre:
            if gen=="" or gen in temp:
                continue
            genreId = genreDict[gen]
            movieHasGenre(id, genreId)
            temp.append(gen)


    path = "/Users/LYC/Desktop/2018Fall/DataWarehouse/CsvData/"
    # Entity Table
    writeToFile(path+"movie.csv", movieList, movieHeader)
    writeToFile(path+"actor.csv", actorList, actorHeader)
    writeToFile(path+"director.csv", directorList, directorHeader)
    writeToFile(path+"writer.csv", writerList, writerHeader)
    writeToFile(path+"producer.csv", producerList, producerHeader)
    writeToFile(path+"language.csv", languageList, languageHeader)
    writeToFile(path+"subtitle.csv", subtitleList, subtitleHeader)
    writeToFile(path+"format.csv", formatList, formatHeader)
    writeToFile(path+"genre.csv", genreList, genreHeader)

    writeToFile(path+"direct_direct_movie.csv", directorDirectMovieList, directorDirectMovieHeader)
    writeToFile(path+"movie_has_subtitle.csv", movieHasSubtitleList, movieHasSubtitleHeader)
    writeToFile(path+"producer_produce_movie.csv", producerProduceMovieList, producerProduceMovieHeader)
    writeToFile(path+"writerWriteMovie.csv", writerWriteMovieList, writerWriteMovieHeader)
    writeToFile(path+"actor_act_movie.csv", actorActMovieList, actorActMovieHeader)
    writeToFile(path+"movie_has_language.csv", movieHasLanguageList, movieHasLanguageHeader)
    writeToFile(path+"movie_has_format.csv", movieHasFormatList, movieHasFormatHeader)
    writeToFile(path+"studio_sponsor_movie.csv", studioSponsorMovieList, studioSponsorMovieHeader)
    writeToFile(path+"movie_has_genre.csv", movieHasGenreList, movieHasGenreHeader)
    writeToFile(path+"star_starring_movie.csv", starStarringMovieList, starStarringMovieHeader)
    print(actorList[1])



data = loadFromCsv("/Users/LYC/Desktop/2018Fall/DataWarehouse/relation.csv")
dicStr = data[73]["actors"]
print(dicStr)
print(dicStr.replace("\"",""))
list = [i.strip("\'").strip("\"\"").strip("['").strip("']").strip(" '").strip(' "') for i in dicStr.strip(" \"\"").strip("[").strip("]").split(",")]
print(list)
extract(data)


from py2neo import Graph, Node, Relationship,NodeMatcher
import csv
#提取合作信息 创建times关系
graph = Graph("http://localhost:7474", username="neo4j", password='1234')
graph.delete_all()
i=-1
with open("relation.csv","r",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        i=i+1
        if (i>0):
            movieName = line[0]
            time = line[2]
            imdb = line[3]
            rate = line[4]
            date = line[12]
            subtitle = line[13]
            id = line[15]

            movieName = movieName.replace("\"", "")
            movieName = movieName.strip(" ")
            matcher = NodeMatcher(graph)
            movie = matcher.match("Movie", name=movieName).first()

            if (movie == None):
                movie = Node('Movie', name=movieName, time = time, imdb = imdb, rate = rate, date = date, subtitle = subtitle, id = id )
                #graph.create(movie)


            temp = line[1].replace("[","")
            temp = temp.replace("]","")
            list = temp.split(",")
            genres = []
            for name in list:
                if name != "None" and name != "":
                    name = name.replace("\"", "")
                    name = name.replace("'", "")
                    name = name.strip(" ")
                    genre = matcher.match("Genre",name = name.replace("'","")).first()
                    if (genre==None):
                        genre = Node('Genre',name = name.replace("'",""))
                    #graph.create(genre)
                    genres.append(genre)


            temp = line[5].replace("[", "")
            temp = temp.replace("]", "")
            list = temp.split(",")
            directors = []
            for name in list:
                if name != "None" and name != "":
                    name = name.replace("\"", "")
                    name = name.replace("'", "")
                    name = name.strip(" ")
                    director = matcher.match("Director", name=name.replace("'","")).first()
                    if (director == None):
                        director = Node('Director', name=name.replace("'",""))
                    #graph.create(director)
                    directors.append(director)


            temp = line[6].replace("[", "")
            temp = temp.replace("]", "")
            list = temp.split(",")
            starrings = []
            for name in list:
                if name != "None" and name != "":
                    name = name.replace("\"", "")
                    name = name.replace("'", "")
                    name = name.strip(" ")
                    starring = matcher.match("Starring", name=name.replace("'", "")).first()
                    if (starring == None):
                        starring = Node('Starring', name=name.replace("'", ""))
                    #graph.create(starring)
                    starrings.append(starring)


            temp = line[7].replace("[", "")
            temp = temp.replace("]", "")
            list = temp.split(",")
            actors = []
            for name in list:
                if name != "None" and name != "":
                    name = name.replace("\"", "")
                    name = name.replace("'", "")
                    name = name.strip(" ")
                    actor = matcher.match("Actor", name=name.replace("'", "")).first()
                    if (actor == None):
                        actor = Node('Actor', name=name.replace("'", ""))
                    #graph.create(actor)
                    actors.append(actor)


            temp = line[8].replace("[", "")
            temp = temp.replace("]", "")
            list = temp.split(",")
            writers = []
            for name in list:
                if name != "None" and name != "":
                    name = name.replace("\"", "")
                    name = name.replace("'", "")
                    name = name.strip(" ")
                    writer = matcher.match("Writer", name=name.replace("'", "")).first()
                    if (writer == None):
                        writer = Node('Writer', name=name.replace("'", ""))
                    #graph.create(writer)
                    writers.append(writer)


            temp = line[9].replace("[", "")
            temp = temp.replace("]", "")
            list = temp.split(",")
            producers = []
            for name in list:
                if name != "None" and name != "":
                    name = name.replace("\"","")
                    name = name.replace("'", "")
                    name = name.strip(" ")
                    producer = matcher.match("Producer", name=name.replace("'", "")).first()
                    if (producer == None):
                        producer = Node('Producer', name=name.replace("'", ""))
                    #graph.create(producer)
                    producers.append(producer)

            temp = line[10].replace("[", "")
            temp = temp.replace("]", "")
            list = temp.split(",")
            formats = []
            for name in list:
                if name != "None" and name != "":
                    name = name.replace("\"", "")
                    name = name.replace("'", "")
                    name = name.strip(" ")
                    format = matcher.match("Format", name=name.replace("'", "")).first()
                    if (format == None):
                        format = Node('Format', name=name.replace("'", ""))
                    #graph.create(format)
                    formats.append(format)

            temp = line[11].replace("[", "")
            temp = temp.replace("]", "")
            list = temp.split(",")
            languages = []
            for name in list:
                if name != "None" and name != "" :
                    name = name.replace("'", "").split("(")[0]
                    name = name.replace("\"", "")
                    name = name.strip(" ")
                    if name != "Unknown":
                        language = matcher.match("Language", name=name.replace(",","")).first()
                        if (language == None):
                            language = Node('Language', name=name.replace(",",""))
                        #graph.create(language)
                        languages.append(language)

            temp = line[14].replace("[", "")
            temp = temp.replace("]", "")
            list = temp.split(",")
            studios = []
            for name in list:
                if name != "None" and name != "":
                    name = name.replace("\"", "")
                    name = name.replace("'", "")
                    name = name.strip(" ")
                    studio = matcher.match("Studio", name=name.replace(",", "")).first()
                    if (studio == None):
                        studio = Node('Studio', name=name.replace(",", ""))
                    #graph.create(studio)
                    studios.append(studio)

            #movie genres directors starrings actors writers producers formats languages studios
            relation = []
            for actor in actors:
                r = Relationship(actor,"acts",movie)
                s = actor | movie | r
                relation.append(s)

            for director in directors:
                r = Relationship(director,'directs',movie)
                s = director | movie | r
                relation.append(s)

            for starring in starrings:
                r = Relationship(starring,'stars',movie)
                s = starring | movie | r
                relation.append(s)

            for writer in writers:
                r = Relationship(writer,'writes',movie)
                s = writer | movie | r
                relation.append(s)

            for producer in producers:
                r = Relationship(producer, 'produces', movie)
                s = producer | movie | r
                relation.append(s)

            # for starring in starrings:
            #     for starring2 in starrings:
            #         if starring!=starring2:
            #             r = Relationship(starring, 'cooperates', starring2)
            #             s = starring | starring2 | r
            #             relation.append(s)
            #
            #     for actor in actors:
            #         r = Relationship(starring, 'cooperates', actor)
            #         s = starring | actor | r
            #         relation.append(s)
            #
            #     for director in directors:
            #         r = Relationship(starring, 'cooperates', director)
            #         s = starring | director | r
            #         relation.append(s)
            #
            # for actor in actors:
            #     for actor2 in actors:
            #         if actor != actor2:
            #             r = Relationship(actor, 'cooperates', actor2)
            #             s = actor | actor2 | r
            #             relation.append(s)
            #
            #     for starring in starrings:
            #         r = Relationship(actor, 'cooperates', starring)
            #         s = actor | starring | r
            #         relation.append(s)
            #
            #     for director in directors:
            #         r = Relationship(actor, 'cooperates', director)
            #         s = actor | director | r
            #         relation.append(s)
            #
            # for director in directors:
            #     for director2 in directors:
            #         if director != director2:
            #             r = Relationship(director, 'cooperates', director2)
            #             s = director | director2 | r
            #             relation.append(s)
            #
            #     for starring in starrings:
            #         r = Relationship(director, 'cooperates', starring)
            #         s = director | starring | r
            #         relation.append(s)
            #
            #     for actor in actors:
            #         r = Relationship(director, 'cooperates', actor)
            #         s = director | actor | r
            #         relation.append(s)

            for format in formats:
                r = Relationship(movie,'format',format)
                s = movie | format | r
                relation.append(s)

            for language in languages:
                r = Relationship(movie,'language',language)
                s = movie | language | r
                relation.append(s)

            for studio in studios:
                r = Relationship(studio,'makes',movie)
                s = studio | movie | r
                relation.append(s)

            for genre in genres:
                r = Relationship(movie,'style',genre)
                s = movie | genre | r
                relation.append(r)
                # for director in directors:
                #     r = Relationship(director,'directingstyle',genre)
                #     s = director | genre | r
                #     relation.append(r)
            print(str(i)+"  "+movieName)

            for r in relation:
                graph.create(r)




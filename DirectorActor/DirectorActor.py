from py2neo import Graph, Node, Relationship,NodeMatcher
import csv


graph = Graph("http://localhost:7474", username="neo4j", password='1234')

graph.delete_all()
num=-1
with open("relation.csv","r",encoding="utf-8") as csvfile:
     #读取csv文件，返回的是迭代类型

     reader = csv.reader(csvfile)
     for line in reader:
           #node = graph.data('MATCH (p:Person) return p')
           num = num + 1
           if (num > 0):
                print(num)
                matcher = NodeMatcher(graph)
                temp = line[1].replace("[", "")
                temp = temp.replace("]", "")
                list = temp.split(",")
                genres = []
                for name in list:
                    if name != "None" and name != "":
                        name = name.replace("\"", "")
                        name = name.replace("'", "")
                        name = name.strip(" ")
                        genre = matcher.match("Genre", name=name.replace("'", "")).first()
                        if (genre == None):
                            genre = Node('Genre', name=name.replace("'", ""))
                        graph.create(genre)
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
                        director = matcher.match("Director", name=name.replace("'", "")).first()
                        if (director == None):
                            director = Node('Director', name=name.replace("'", ""))
                        graph.create(director)
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
                        graph.create(starring)
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
                        graph.create(actor)
                        actors.append(actor)

                for a in genres:
                    for b in directors:
                        relation = graph.match_one([b, a])
                        if (relation == None):
                            r = Relationship(b, 'directingstyle', a)
                            r['times'] = 1
                            s = b | a | r
                            graph.create(s)
                        else:
                            relation['times'] += 1
                            graph.push(relation)

                for a in directors:
                    for b in actors:
                        relation = graph.match_one([a, b])
                        if (relation == None):
                            r = Relationship(a, 'cooperates', b)
                            r['times'] = 1
                            s = a | b | r
                            graph.create(s)
                        else:
                            relation['times'] += 1
                            graph.push(relation)

                for a in directors:
                    for b in starrings:
                        relation = graph.match_one([a, b])
                        if (relation == None):
                            r = Relationship(a, 'cooperates', b)
                            r['times'] = 1
                            s = a | b | r
                            graph.create(s)
                        else:
                            relation['times'] += 1
                            graph.push(relation)

                for a in starrings:
                    for b in actors:
                        relation = graph.match_one([a, b])
                        if (relation == None):
                            r = Relationship(a, 'cooperates', b)
                            r['times'] = 1
                            s = a | b | r
                            graph.create(s)
                        else:
                            relation['times'] += 1
                            graph.push(relation)

                for i in range(0,len(directors)-2):
                    for j in range(i+1,len(directors)-1):
                        a = directors[i]
                        b = directors[j]
                        relation = graph.match_one([a, b])
                        if (relation == None):
                            r = Relationship(a, 'cooperates', b)
                            r['times'] = 1
                            s = a | b | r
                            graph.create(s)
                        else:
                            relation['times'] += 1
                            graph.push(relation)

                for i in range(0,len(starrings)-2):
                    for j in range(i+1,len(starrings)-1):
                        a = starrings[i]
                        b = starrings[j]
                        relation = graph.match_one([a, b])
                        if (relation == None):
                            r = Relationship(a, 'cooperates', b)
                            r['times'] = 1
                            s = a | b | r
                            graph.create(s)
                        else:
                            relation['times'] += 1
                            graph.push(relation)

                for i in range(0,len(actors)-2):
                    for j in range(i+1,len(actors)-1):
                        a = actors[i]
                        b = actors[j]
                        relation = graph.match_one([a, b])
                        if (relation == None):
                            r = Relationship(a, 'cooperates', b)
                            r['times'] = 1
                            s = a | b | r
                            graph.create(s)
                        else:
                            relation['times'] += 1
                            graph.push(relation)











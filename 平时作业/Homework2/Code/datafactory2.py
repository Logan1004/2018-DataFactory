from py2neo import Graph, Node, Relationship,NodeMatcher
import csv

graph = Graph("http://localhost:7474", username="neo4j", password='1234')
i=0

with open("paperinfo.csv","r",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        try:
            temp = line[0].split('\t')
            matcher = NodeMatcher(graph)
            a = matcher.match('Essay', name=temp[0]).first()
            if (a==None):
                a = Node('Essay', name = temp[0])
                graph.create(a)
            b = matcher.match('Essay', name=temp[1]).first()
            if (b==None):
                b = Node('Essay', name = temp[1])
                graph.create(b)

            a = matcher.match('Essay', name=temp[0]).first()
            b = matcher.match('Essay', name=temp[1]).first()
            print(i)
            i=i+1
            relation = Relationship(a, 'Uses', b)
            s = a | b | relation
            graph.create(s)
        except:
            print("!!!!!")




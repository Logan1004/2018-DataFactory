from py2neo import Graph, Node, Relationship,NodeMatcher
import csv

graph = Graph("http://localhost:7474", username="neo4j", password='1234')
graph.delete_all()
i=0
with open("cit-HepPh-dates.csv","r",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        temp = line[0].split('\t')
        print(i)
        i=i+1
        a = Node('Essay', name=temp[0], date = temp[1])
        graph.create(a)



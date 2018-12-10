from py2neo import Graph, Node, Relationship,NodeMatcher
import csv


graph = Graph("http://localhost:7474", username="neo4j", password='1234')

graph.delete_all()
with open("XXX.csv","r",encoding="utf-8") as csvfile:
     #读取csv文件，返回的是迭代类型
     reader = csv.reader(csvfile)
     for line in reader:
           #node = graph.data('MATCH (p:Person) return p')
           flag=0
           matcher = NodeMatcher(graph)
           a = matcher.match("Director",name=line[0]).first()
           b = matcher.match("Actor",name=line[1]).first()
           if (a==None):
               flag=1
               a = Node('Director', name=line[0])
           if (b==None):
               flag=1
               b = Node('Actor', name = line[1])
           if (flag==1):
               r = Relationship(a, 'Cooperate', b)
               r['times'] = 1
               s = a | b | r
               print(s)
               graph.create(s)
           if (flag==0):
               relation = graph.match_one([a,b])
               print(a)
               print(b)
               if (relation==None):
                   r = Relationship(a, 'Cooperate', b)
                   r['times'] = 1
                   s = a | b | r
                   print(s)
                   graph.create(s)
               else:
                   relation['times']+=1
                   graph.push(relation)




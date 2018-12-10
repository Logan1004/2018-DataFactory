from py2neo import Graph, Node, Relationship,NodeMatcher
graph = Graph("http://localhost:7474", username="neo4j", password='1234')
num=0

for line in open("graph2.txt","r"):
    num = num+1
    line = line[:-1]
    if (num==2):
        data = line.split(',')
        for node_name in data:
            node = Node('Param',name = node_name)
            graph.create(node)
    if (num>=5):
        data = line.split(' ')
        relation = ''
        matcher = NodeMatcher(graph)
        a = matcher.match("Param", name=data[1]).first()
        b = matcher.match("Param", name=data[3]).first()
        r = ''
        s = ''
        if (data[2]=='-->' or data[2]=='o->'):
            r = Relationship(a, 'Cause', b)
        elif data[2]=='o-o':
            r = Relationship(a, 'Not_exact', b)
        elif data[2]=='<->':
            r = Relationship(b, 'Cause', a)
            s = a | b | r
            graph.create(s)
            r = Relationship(a, 'Cause', b)
        s = a | b | r
        graph.create(s)




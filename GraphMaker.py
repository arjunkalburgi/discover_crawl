from py2neo import authenticate, Graph, Node, Relationship, Path
from vis import draw

class GraphMaker(object):
    '''

        neo4j: (https://10-0-1-111-33931.neo4jsandbox.com/browser/)
            Entire triple: 
                CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})-[:ACTED_IN {roles:['Neo']}]->(TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})
                MATCH(N) RETURN N

            Create node: 
                CREATE (n:Page {title:'Finance', url:'https://en.wikipedia.org/wiki/Finance'})

            Get node (as "n")
                match(n:Page {title: "Finance"})

    '''

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "ece406")
        self.graph = Graph("http://localhost:7474/db/data/")
        self.graph.delete_all()



    def appendNode(self, node): 
        self.graph.create(node)

    def appendNodes(self, *nodes): 
        for node in nodes: 
            self.graph.create(node)



    def makeRelationship(self, subjectnode, propertystring, objectnode): 
        self.graph.create(Relationship(subjectnode, propertystring, objectnode))



    def drawGraph(self): 
        options = {"Page": "title", "Section": "title"}
        draw(self.graph, options)

    def printData(self, querystring=None): 
        if querystring is None: 
            querystring = "match (n) return n"
        data = self.graph.run(querystring)
        for d in data:
            print(d)


    
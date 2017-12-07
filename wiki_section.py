from py2neo import Node

class wiki_section(object):
	"""docstring for WikiParse"""
	def __init__(self, graph, node):
		self._graph = graph
		self._section = node

	def run(): 
		self.sectionParse()

        print("Explore: ")
        self.getSubtopics()



	def sectionParse(self): 
        main_ideas = [] #self._page.sections

        for idea in main_ideas: 

            p = self.makeWikiPoint(idea)
            self._graph.makeRelationship(self._section, "HASSUBTOPIC", p)



	def makeWikiPoint(self, idea): 
		return Node("Point", title=idea)



	def getSubtopics(self): 
        p = self._graph.getData("MATCH (fin:Section {title:'" + self._section["title"] + "'})-[:HASSUBTOPIC]->(point) RETURN point.title")
        return [el.values()[0] for el in p]

		
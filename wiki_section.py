from py2neo import Node
from pntl.tools import Annotator

from hiddenkeys import username, password

from watson_developer_cloud import NaturalLanguageUnderstandingV1 as watson
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


class wiki_section(object):
	"""docstring for WikiParse
		
		# set up watson obj
		watson_obj = watson(
		  username=username,
		  password=password,
		  version='2017-02-27')

		# make request 
		response = watson_obj.analyze(
		  text='IBM is an American multinational technology company headquartered in Armonk, New York, United States, with operations in over 170 countries.',
		  features=Features(
		    concepts=ConceptsOptions(limit=3),
		    entities=EntitiesOptions(limit=3), 
		    KeywordsOptions(limit=5),
		    relations=RelationsOptions(), 
		    semantic_roles=SemanticRolesOptions()
		    )
		  )

	"""
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

		
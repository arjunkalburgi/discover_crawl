"""The main command for asking questions"""

# from .base import Base
import re, requests, json, inquirer, unicodedata, Algorithmia, wikipedia
import GraphMaker
from py2neo import Node

full_api = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=" 
# description_api = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=" 
        

class WikiTripleMaker():
    """

    """

    def __init__(self):
        # user = neo4j 
        # pw = ece406
        uri = "bolt://127.0.0.1:7687/browser/"
        user = 'neo4j'
        password = 'ece406'
        self._graph = GraphMaker.GraphMaker()
        

    def run(self, topic): 
        self.getTopic(topic)

        self.setTopicAsSubject()

        self.parseWikiPage()

        # self.pushTriple()


    def getTopic(self, topic): 
        # if match 
        if topic in wikipedia.search(topic): 
            print("Pulling from wiki page on " + topic + ".")
            self._topic = topic
        # if close match
        elif wikipedia.suggest(topic) is not None: 
            print("Pulling from " + wikipedia.suggest(topic) + ", if this isn't correct please exit and specify a different query.")
            self._topic = wikipedia.suggest(topic)
        # no matches
        else:
            print("That topic didn't work, please try again")
            exit()

    def setTopicAsSubject(self): 
        # CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})
        self._page = wikipedia.WikipediaPage(self._topic)

        self.subjectnode = Node("Page", title=self._page.title, 
                                        url=self._page.url,
                                        abstract=self._page.summary)

        self._graph.appendNode(self.subjectnode)


    def parseWikiPage(self): 
        sections = self._page.sections

        for section in sections: 
            if len(self._page.section(section)): 
                
                s = self.makeWikiSection(section)
                self._graph.makeRelationship(self.subjectnode, "HASSUBTOPIC", s)

                # self.parseWikiSection(s)

    def makeWikiSection(self, sectiontitle): 

        if sectiontitle in wikipedia.search(sectiontitle) and sectiontitle is not "See also": 
            return Node("Section", title=sectiontitle, 
                                   content=self._page.section(sectiontitle), 
                                   mainarticleurl=wikipedia.page(self._topic).url)

        return Node("Section", title=sectiontitle, content=self._page.section(sectiontitle))



    def dump(self): 
        self._graph.printData()

    def view(self): 
        self._graph.drawGraph()

    '''

        def findsections(self, data): 
            # get actual title 
            title = data[u'query'][u'pages'][data[u'query'][u'pages'].keys()[0]][u'title'] # sorry
            # print(title)

            # query wikidata for sections
            level = 1
            sections = self.narrow(title, level)

            # TODO no sections

            # make user select from sections
            print("\nWhat about " + title + " would you like to learn?")
            self.selectnext(sections, title)


        def selectnext(self, sections, title): 
            questions = [
                    inquirer.List('size',
                                    message="Check these",
                                    choices=[sec["name"] for sec in sections],
                    ),
                ]
            answers = inquirer.prompt(questions)

            nextt = sections[[sec["name"] for sec in sections].index(answers["size"])]
            # give me resources 
            if [sec['name'] for sec in sections].index(answers["size"]) is 0: 
                res = self.getres(title)
                if (len(res) > 0): 
                    print("Saving resources...")
                    print([item['title'] for item in res])
                    print("Above has been saved to your library")
                else: 
                    print("resource lookup error")
                quit()
            # go back
            elif (answers["size"] is "Back"): 
                self.selectnext(nextt["sections"], nextt["title"])
            # subcategories 
            elif ("more" in nextt): 
                print("There are subcategories!")
                nextt["more"].append({"name": "Back", "title": title, "sections": sections})
                self.selectnext(nextt["more"], nextt["name"])
            # search new
            else: 
                self.getdesc(nextt["name"], description_api + nextt["title"])


        def narrow(self, title, level):
            
            # query wikidata for inner sections
            api_url = "https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=sections&page=" + title
            response = requests.get(api_url)
            if (response.status_code is not 200): 
                print("fail")
                quit()
                
            data = json.loads(response.content)

            moretopics = []
            moretopics.append({"name": "Give me resources about " + title, "title": title})
            for i, section in enumerate(data[u'parse'][u'sections']): 
                if (int(section[u'level']) is (level+1)): 
                    moretopics.append({"name": unicodedata.normalize('NFKD', section[u'line']).encode('ascii','ignore'), "title": unicodedata.normalize('NFKD', section[u'anchor']).encode('ascii','ignore')})
                elif (int(section[u'level']) is (level+2)):
                    if "more" in moretopics[-1]: 
                        moretopics[-1]["more"].append({"name": unicodedata.normalize('NFKD', section[u'line']).encode('ascii','ignore'), "title": unicodedata.normalize('NFKD', section[u'anchor']).encode('ascii','ignore')})
                    else:
                        moretopics[-1]["more"] = [{"name": unicodedata.normalize('NFKD', section[u'line']).encode('ascii','ignore'), "title": unicodedata.normalize('NFKD', section[u'anchor']).encode('ascii','ignore')}]

            return moretopics[0:4]


        def getres(self, title): 
        response = requests.get("https://learn-anything.xyz/api/maps/?q=" + title.replace(" ", "+"))
        if (response.status_code is not 200): 
            print("fail")
            quit()
            
        data = json.loads(response.content)
        dataa = [item for item in data if item.get('key') == title.lower()]
        if len(dataa) is not 0: 
            response = requests.get("https://learn-anything.xyz/api/maps/" + dataa[0]['id'])
            if (response.status_code is not 200): 
                print("fail")
                quit()
                
            data = json.loads(response.content)['nodes']
            dataaa = [{"title": item.get('nodes')[0]['text'], "url": item.get('nodes')[0]['url']} for item in data if len(item.get('nodes')) > 0]
            return dataaa
        else: 
            print("error in learn-anything")
            return []
    '''

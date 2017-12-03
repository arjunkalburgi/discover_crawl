## db setup 
neo4j community 3.3 https://neo4j.com/download/community-edition/
Just start the server and then these scripts will work :) 


## db structure 

Wiki Page strucutre nodes: 
- :Page 
- :Section
- ? :Table ? 

## wikipedia lib 
Version with working "wikipedia.WikipediaPage().sections": 
>>> sudo pip install git+https://github.com/lucasdnd/Wikipedia.git

	Basically the main lib doesn't have this working rn, so you have to "--upgrade" the package

## wikipedia page object 
	page.__class__(                        page._parent_id                       
	page.__delattr__(                      page._references                      
	page.__dict__                          page._revision_id                     
	page.__doc__                           page._sections                        
	page.__eq__(                           page._summary                         
	page.__format__(                       page._WikipediaPage__continued_query( 
	page.__getattribute__(                 page._WikipediaPage__load(            
	page.__hash__(                         page._WikipediaPage__title_query_param
	page.__init__(                         page.categories                       
	page.__module__                        page.content                          
	page.__new__(                          page.html(                            
	page.__reduce__(                       page.images                           
	page.__reduce_ex__(                    page.links                            
	page.__repr__(                         page.original_title                   
	page.__setattr__(                      page.pageid                           
	page.__sizeof__(                       page.parent_id                        
	page.__str__(                          page.references                       
	page.__subclasshook__(                 page.revision_id                      
	page.__weakref__                       page.section(                         
	page._categories                       page.sections                         
	page._content                          page.summary                          
	page._images                           page.title                            
	page._links                            page.url




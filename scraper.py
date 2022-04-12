import scrapy



SEARCH_URL = "https://www.agriculture.com/search?search_api_views_fulltext="

def question_search(search : str = "cow feeding"):
    list_search = search.split(' ')
    new_search = '+'.join(list_search)
    return "https://www.agriculture.com/search?search_api_views_fulltext=" + new_search + "&sort_by=search_api_relevance&sort_by=search_api_relevance"
    
question_search()
class AgroSpider(scrapy.Spider):
    name = "agro_spider"
    start_urls = {
        question_search()
    }
    
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.start_urls = {
            question_search(kwargs.get("search", "goat feed"))
        }
    
    def parse(self, response, **kwargs):
        for article in response.css(".public-search-result"):
            yield {
                "title" : article.css(".content h2 a::text").get(),
                "text" : article.css(".content .field-body p::text").get(),
                "author": article.css(".content .content-footer .field-byline a::text").get()
            }
        
        
        return super().parse(response, **kwargs)
    

        
    
"""
title = response.css(".content h2 a::text").get()
text = response.css(".content .field-body p::text").get()
date = response.css(".content .content-footer::text").get()

"""


    
    
    
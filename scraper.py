import scrapy
from scrapy import signals
from scrapy.signalmanager import dispatcher
from config import crochet
from scrapy.crawler import CrawlerRunner


SEARCH_URL = "https://www.agriculture.com/search?search_api_views_fulltext="
output_data = []

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
            question_search(kwargs.get("data", "goat feed"))
        }

    
    def parse(self, response, **kwargs):
        for article in response.css(".public-search-result"):
            
            # the initial methods brings a null cause not all the text are in the paragraph tag
            scraped_text = article.css(".content .field-body p::text").get()
            if not scraped_text:
                scraped_text = article.css(".content .field-body::text").get().strip('\n').strip(' ')
                
            yield {
                "image" : article.css(".field-image picture img::attr(data-srcset)").get(),
                "title" : article.css(".content h2 a::text").get(),
                "text" : scraped_text, 
                "author": article.css(".content .content-footer .field-byline a::text").get(), 
                "link": article.css(".content h2 a::attr(href)").get()
            }
        
        
        return super().parse(response, **kwargs)
    

class AgroDetailSpider(scrapy.Spider):
    name = "detail_spider"
    
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.start_urls = {
            kwargs.get("data", None)
        }
    
    def parse(self, response, **kwargs):
        yield {
            "title" : response.css(".page-primary-content h1::text").get(),
            "author" : response.css('.page-primary-content .field-byline a::text').get(),
            "date" : response.css('.page-primary-content .byline-date::text').get(),
            "text" : response.css("section article .field-body p::text").getall()
        }
        
        return super().parse(response, **kwargs)
        


def _crawler_result(item, response, spider):
    output_data.append(dict(item)) 

@crochet.run_in_reactor
def scrape_with_crochet(search_str : str, spider : scrapy.Spider):
    output_data.clear()
    # This will connect to the dispatcher that will kind of loop the code between these two functions.
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    
    # This will connect to the ReviewspiderSpider function in our scrapy file and after each yield will pass to the crawler_result function.
    eventual = CrawlerRunner().crawl(spider, data = search_str)
    return eventual


    



    
    
    
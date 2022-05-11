from crypt import methods
from random import Random
from flask import jsonify, request
import time
from scraper import scrape_with_crochet, output_data, AgroSpider, AgroDetailSpider
from config import app, crochet



@app.route("/", methods=['GET'])
def home():
    return jsonify({
        "/recommend/" : {
            "GET" : {
                'url' : request.base_url + "recommend/",
                'description' : "get random recommendations to display in the home screen",
                'returns' : {
                    "title" : 'String',
                    "image" : "String",
                    "text" : "String",
                    "author" : "String",
                    "link" : "String"
                }
            }
        },
        "/question/" : {    
            "POST" : {
                'url' : request.base_url + "question/",
                'description' :"data to be searched",
                'data' : "String",
                'returns' : {
                    "title" : 'String',
                    "image" : "String",
                    "text" : "String",
                    "author" : "String",
                    "link" : "String"
                }
            }
        },
        "/detail/" : {
            "POST" : {
                'url' : request.base_url + "detail/",
                'description' : "gets the detail of a single page",
                "data" : "detail page to be scraped",
                'returns' : {
                    "title" : "String",
                    "author" : "String",
                    "date" : "String",
                    "text" : "String"
                }
            }
        },
    })

@crochet.run_in_reactor
@app.route('/recommend/', methods=['GET'])
def requestForData():
    recommendation_list : list[str] = [
        'goat feeds',
        'cow feeds',
        'farming technology',
        'farm management',
        'livestock technology',
        'planting',
        'farm market',
        'crop news',
        'conservation',
        'poultry',
        'soil health',
        'poultry health'
    ] 
    scrape_with_crochet(recommendation_list[Random().randint(0, recommendation_list.__len__() - 1)], AgroSpider)
    time.sleep(10)
    return jsonify(output_data)

@app.route('/question/', methods=['POST'])
def scrapeData():
    data  = dict(request.get_json())
    search_data = data.get('data')
    scrape_with_crochet(search_data, AgroSpider)
    time.sleep(10)
    return jsonify(output_data)

@app.route('/detail/', methods=['POST'])
def detail(): 
    data  = dict(request.get_json())
    link = data.get('data')
    scrape_with_crochet(link, AgroDetailSpider)
    time.sleep(5)
    return jsonify(output_data)


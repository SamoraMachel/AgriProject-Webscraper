from crypt import methods
from random import Random
from flask import jsonify, request
import time
from scraper import scrape_with_crochet, output_data, AgroSpider, AgroDetailSpider
from config import app, crochet



@app.route("/", methods=['GET'])
def home():
    return jsonify({
        "/recommend/" : "get random recommendations to display in the home screen",
        "/question/" : {    
            "POST" : {
                "data" : "data to be searched"
            }
        },
        "/detail/" : {
            "POST" : {
                "data" : "detail page to be scraped"
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
    time.sleep(5)
    return jsonify(output_data)

@app.route('/question/', methods=['POST'])
def scrapeData():
    data  = dict(request.get_json())
    search_data = data.get('data')
    scrape_with_crochet(search_data, AgroSpider)
    time.sleep(5)
    return jsonify(output_data)

@app.route('/detail/', methods=['POST'])
def detail(): 
    data  = dict(request.get_json())
    link = data.get('data')
    scrape_with_crochet(link, AgroDetailSpider)
    time.sleep(3)
    return jsonify(output_data)


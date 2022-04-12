from random import Random
from flask import jsonify
from scraper import AgroSpider
from config import app

@app.route("/", methods=['GET'])
def home():
    return jsonify({
        "/recommendations" : "gets general data users display",
        "/farmerQuestion" : "posts farmers question"
    })

@app.route('/recommendations', methods=['GET'])
def requestForData():
    recommendation_list : list[str] = [
        'goat feeds',
        'cow feeds'
    ] 
    spider : AgroSpider = AgroSpider(search=recommendation_list[Random.randint(0, recommendation_list.__len__())])
    return jsonify(spider.parse)

@app.route('/farmerQuestion', methods=['POST'])
def scrapeData():
    pass


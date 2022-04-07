from bs4 import BeautifulSoup
from flask import Response
import requests


SEARCH_URL = "https://www.agriculture.com/search?search_api_views_fulltext="

def getThePage(question : str) : 
    formatted_question = "+".join(question)
    page = requests.get(SEARCH_URL + formatted_question)
    return page

def parsePage(page : Response) :                                            
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)


    
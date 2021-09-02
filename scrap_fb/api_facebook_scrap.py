# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:15:11 2020

@author: Asus

"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from script_scrap_fb import Scrap_facebook
from configuration_file import m_file
from configurations_MongoDb.insert_posts_mongoDB import insert_posts

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
api = Api(app)
nb_scroll = 10
list_urls=["https://www.facebook.com/DiwanFM"]
class scrapy(Resource):
    def get(self):
        urls = m_file(list_urls)
        for url_page in urls:
            data=Scrap_facebook(url_page,nb_scroll)
            insert_posts(data)
        return " insertion terminé"


     
api.add_resource(scrapy, '/api/scraping')
if __name__ == '__main__':
    app.run(port=5000, debug=False)


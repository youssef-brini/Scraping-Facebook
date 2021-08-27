from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from script_scrap_post import Scrap_post
import csv
from configurations_MongoDb.insert_posts_mongoDB import insert_post
from configuration_file import read_file,m_file
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
api = Api(app)
with_comment = True
datas = []
list_urls=["https://m.facebook.com/WeviooGroup/posts/776040973025375","https://m.facebook.com/WeviooGroup/posts/811620116134127"]
class scrapy(Resource):
    def get(self):
        urls = read_file()
        urls = m_file(urls)
        for url_post in urls:
            
            data=Scrap_post(url_post,with_comment)
            datas.append(data)
            # insert_post(data)
        return jsonify(datas)


     
api.add_resource(scrapy, '/api/scrapingPost')

if __name__ == '__main__':
    app.run(port=5000, debug=False)


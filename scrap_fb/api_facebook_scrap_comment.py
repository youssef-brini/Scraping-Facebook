from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from script_scrap_comment import Scrap_comment

from configurations_MongoDb.insert_posts_mongoDB import insert_comment

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
api = Api(app)
nb_click = 5
list_urls=["https://m.facebook.com/santetunisie.rns.tn/posts/4408535059185564"]
class scrapy(Resource):
    def get(self):
        for url_post in list_urls:
            data=Scrap_comment(url_post)
            insert_comment(data)
        return " insertion terminé"


     
api.add_resource(scrapy, '/api/scrapingComment')
if __name__ == '__main__':
    app.run(port=5000, debug=False)


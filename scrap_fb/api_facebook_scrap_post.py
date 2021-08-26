from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from script_scrap_post import Scrap_post
import csv
from configurations_MongoDb.insert_posts_mongoDB import insert_post
def read_file():
    list_urls = []
    with open('C:/Users/Youssef/Desktop/mCode/scrap_fb/test.csv','r',encoding="utf-8-sig") as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        
        for row in csvReader:
            
            list_urls.append(str(row[0]))

    return list_urls

def m_file(list_urls):
    new_urls = []
    for x in list_urls:
        m_url = x.split(".facebook")
        m_url[1] = "https://m.facebook"+ str(m_url[1])
        new_urls.append(m_url[1])
    print(new_urls)
    return new_urls

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


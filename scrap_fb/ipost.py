from time import sleep
import pymongo
from pymongo import results
from pymongo.message import delete
from script_scrap_post import Scrap_post
from configurations_MongoDb.insert_posts_mongoDB import insert_post
from bson.objectid import ObjectId
from script_scrap_comment import *
import requests
connection = pymongo.MongoClient("localhost", 27017)
import csv
#import datetime
database = connection['Posts_facebook']
#collection Posts
Posts=database['Posts']
Post=database['Post']
Comment = database['Comments']

datas = []
class iPost ():
    def __init__(self,Posts,Post,Comment):
        self.Posts = Posts
        self.Post = Post
        self.Comment = Comment

    def scrap(self):
        
        BASE = "http://127.0.0.1:5000/"
        value = requests.get(BASE+"api/scrapingPost")
        datas = value.json()
        # print(value)
        # datas.append(value)
        return datas
    #insertion des posts extraits
    def insert_post(self,datas):
        for data in datas:
            
            Post.insert_one(data)

    #insertion des posts extraits
    def insert_posts(data):

        Posts.insert_one(data)


    
    def afficher_Post(self,id):
        results = self.Post.find({"_id": id})
        for result in results:
            print(result)

    def update_Post(self, id,key,value):
        self.Post.update_one({"_id":id},{"$set":{key:value}})
    def delete_Post(self,id):
        self.Post.delete_one({"_id": id})

    def add_Comment(self , id):
        url_post = ""
        results = self.Post.find({"_id": id})
        for result in results:
            url_post = result["url"]
        data=Scrap_comment(url_post)
        self.Post.update_one({"_id":id},{"$set":{"Comment":data}})
        

    def afficher_Posts(self,url_Page):
        results = self.Post.find({"url": url_Page})
        for result in results:
            print(result)

    def update_Posts(self, url_Page):
        self.Posts.update_one({"url":url_Page},{"$set":{"change":"yes"}})

    def delete_Posts(self,url_Page):
        self.Post.delete_one({"url": url_Page})
    
p1 = iPost(Posts,Post,Comment)
# p1.add_Comment(ObjectId("6118cf92c065f724c107b3cb"))
datas = p1.scrap()
p1.insert_post(datas)
# p1.update_Post(ObjectId("6122e389989adbffd20bfc1f"),"hello", "world")
# p1.afficher_Post(ObjectId("6122e389989adbffd20bfc1f"))









"""    
#insertion du nouveau dossier avec ch est le nom de dossier "topic"    
def insert_dossier(ch):
    d=dict()
    h=hachage(ch)
    d['_id']= h
    d['name']=ch
    d['active']= True
    d['date']= datetime.datetime.now()
    d['nbr_dossiers']= 1
    d['urls'] = [{'url' : 'https://www.facebook.com/Test-632171700752966/' , 'is_scraped' : False, 'type' : 'facebook'} ]
    document = Dossier.insert_one(d)
    return document.inserted_id  
"""


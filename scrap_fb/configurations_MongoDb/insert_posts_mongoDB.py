
import pymongo
connection = pymongo.MongoClient("localhost", 27017)
#import datetime
database = connection['Posts_facebook']
#collection Posts
Posts=database['Posts']
Post=database['Post']
Comment = database['Comments']



#insertion des posts extraits
def insert_posts(data):

    Posts.insert_one(data)

#insertion des posts extraits
def insert_post(data):

    Post.insert_one(data)

#insertion des posts extraits
def insert_comment(data):

    Comment.insert_one(data)
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


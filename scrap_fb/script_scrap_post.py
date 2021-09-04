import pymongo
import datetime
import time
import hashlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from configurations_MongoDb.insert_posts_mongoDB import insert_post
from selenium.webdriver.common.action_chains import ActionChains
from script_scrap_comment import extract_commentaires,scroll_comment
from script_scrap_fb import _login
import random
import json

PATH = "C:\Program Files (x86)\chromedriver.exe"

def extract_url_post (post):
    '''
    This function allow you to extract the URL post .
    :param post : this is a html container
    
    '''
    urls = post.find("a",class_= "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw")

    return urls["href"]


def extract_nbr_react(post):
    '''
    This function allow you to extract the number of reaction in  post .
    :param post : this is a html container
    
    '''
    try :
        postShares = post.find("div",class_="_1g06")
        
        if postShares:
            return (postShares.text)  
        
        
        else:
            return "0"
    except :
        return "0"



# extraire le nombre de partages
def extract_nbr_shares(post):
    '''
    This function allow you to extract the number of shares in  post .
    :param post : this is a html container
    
    '''
    try:
        postShares = post.find("div",class_="_43lx _55wr")
        shares = ""
        if postShares:
            return (postShares.text)  

        
        else:
            return "0"
    except :
        return "0"

#extraire la la date du poste
def extract_post_date(post):
    '''
    This function allow you to extract the post date  .
    :param post : this is a html container
    
    '''
    try : 
        
        paragraphs = post.find_all('abbr')
                    
        par = paragraphs[0].text
        return(par)
    except :
        return ""

#focntion pour extraire et retourner le contenue du titre du post   
def extract_text(post):
    
      '''
    This function allow you to extract the post text.
    :param post : this is a html container
    
      '''
      text = ""
      try:
        actualPosts = post.find_all(class_="story_body_container")
        
        
        if len(actualPosts) >= 1:
                
                try:
                    
                    x=actualPosts[0].find('p').text
                    
                    text=x
                except:
                    None
      except :
        return text
      return(text)


def extract_src_post(post):
      '''
    This function allow you to extract the sources images in  post .
    :param post : this is a html container
    
      '''
      src = []
      try :
        postPictures = post.find(class_="_5rgu _7dc9 _27x0")      
        images_links = postPictures.find_all('a')
        
        for img in images_links:
            try :
                
                print(img['href'])
                src.append("https://m.facebook.com" +img['href'])
                
            except:
                None
      except:
          return src

      return src
def extract_video_url(post):
        '''
    This function allow you to extract the source video in  post .
    :param browser : this is an instance of webdriver
    :param url_post : this is the URL post 

        '''
        try:
            video_div = post.find('div', class_="_53mw")
            if video_div != None:
    
                src = json.loads(video_div.attrs['data-store'])['src']
                return src   
        except :
            return []

def who_share(browser,url_post):
    '''
    This function takes two parameters and return a html instance contain persons names who shares post
    :param browser : this is an instance of webdriver
    :param url_post : this is the URL post 
    
    '''
    time.sleep(random.randint(1,4))
    try:
            person_share = browser.find_element_by_xpath("//div[@class='_43lx _55wr']//a")
            person_share = person_share.get_attribute('href')
            
            browser.get(person_share)
            try:
                time.sleep(random.randint(3,7))
                but= browser.find_element_by_xpath("//div[@class='title mfsm fcl']")
                while but:
                    
                    ActionChains(browser).move_to_element(but)
                    time.sleep(random.randint(3,7))
                    ActionChains(browser).click(but).perform()
                    time.sleep(random.randint(3,7))
                    
                    browser.execute_script("document.getElementsByClassName('_i3g _5n09 _55wp')[0].scrollTo(0,document.getElementsByClassName('_i3g _5n09 _55wp')[0].scrollHeight);")
                    time.sleep(random.randint(2,5))
                    
                    but= browser.find_element_by_xpath("//div[@class='title mfsm fcl']")
            except:
                pass
            
                        
           
    except:
        # do nothing right heree
            pass
    source_data = browser.page_source
    share_data = bs(source_data, 'html.parser')
    
    time.sleep(random.randint(2,4))
    browser.get(url_post)
    
    return share_data
    
def who_react(browser,url_post):
    '''
    This function takes two parameters and return a html instance contain persons names who react in post
    :param post : this is a html container
    
    '''
    time.sleep(random.randint(1,4))
    try:
            person_react = browser.find_element_by_xpath("//div[@class='_52jh _5ton _45m7']//a")
            person_react = person_react.get_attribute('href')
            
            browser.get(person_react)
            try:
                time.sleep(random.randint(5,9))
                but= browser.find_element_by_xpath("//div[@class='title mfsm fcl']")
                while but:
                    
                    ActionChains(browser).move_to_element(but)
                    time.sleep(random.randint(5,9))
                    ActionChains(browser).click(but).perform()
                    time.sleep(random.randint(5,9))
                    
                    browser.execute_script("document.getElementsByClassName('_5p-o')[0].scrollTo(0,document.getElementsByClassName('_5p-o')[0].scrollHeight);")
                    time.sleep(random.randint(2,5))
                    
                    but= browser.find_element_by_xpath("//div[@class='title mfsm fcl']")
            except:
                pass     
           
    except:
        # do nothing right heree
            pass
    source_data = browser.page_source
    react_data = bs(source_data, 'html.parser')
    
    time.sleep(random.randint(2,4))
    browser.get(url_post)
    return react_data

def extract_who_react(post):
    '''
    This function allow you to extract the names persons who react in  post .
    :param post : this is a html container
    
    '''
    persons_name = []
    try :
        persons = post.find_all(class_="_4mo")
        
        
        for person in persons:
            name = person.text
            persons_name.append(name)
    except :
        pass
    return persons_name
def extract_who_share(post):
    '''
    This function allow you to extract the names persons who share the post .
    :param post : this is a html container
    
    '''
    persons_name = []
    try : 
        persons = post.find_all(class_="_4mo")
        
        
        for person in persons:
            name = person.text
            
            persons_name.append(name)
    except :
        pass
    return persons_name
def Scrap_post(post_url,with_comment):
    '''
    This function takes two parameters the post_url and the option with_comment, it return datas with different details
    :param url_post : this is the URL post 
    :param with_comment : this is an option to scrap your post with comments or Not
    '''
    with open("C:/Users/Youssef/Documents/MyCode/scrap_fb/Configurations_fb.txt") as file:
        EMAIL = file.readline().split('"')[1]
        PASSWORD = file.readline().split('"')[1] 

    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")


    option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1}) 
    browser = webdriver.Chrome(PATH, options=option)
    browser.get("https://www.facebook.com/")
    url_post = post_url 
    
    _login(browser, EMAIL, PASSWORD)
    time.sleep(random.randint(9,16))
    browser.get(url_post)
    time.sleep(random.randint(4,8))
    react_data = who_react(browser,url_post) # contient une parametre !!!!!!!!!!!!!!
    time.sleep(random.randint(4,7))
    share_data = who_share(browser,url_post) # contient une parametre !!!!!!!!!!!!!!
    time.sleep(random.randint(4,7))
    
    with open('./react.html',"w", encoding="utf-8") as file:
            file.write(str(react_data.prettify()))
    react_html = react_data.find(class_="_5p-o")


    with open('./share.html',"w", encoding="utf-8") as file:
            file.write(str(share_data.prettify()))
    share_html = share_data.find('div',class_="_i3g _5n09 _55wp")

    if with_comment :
        scroll_comment(browser)

    source_data = browser.page_source
    post_data = bs(source_data, 'html.parser')
    with open('./post.html',"w", encoding="utf-8") as file:
        file.write(str(post_data.prettify()))
    list_html = post_data.find(class_="_59e9")


    data=dict()
    data['url']=url_post
    data['scraping_date'] = datetime.datetime.now()
    
    data["titre"]=extract_text(list_html);
    data["src_img"]=extract_src_post(list_html);
    data["video_src"]=extract_video_url(list_html);
    
    data["nbr_de_partage"]= extract_nbr_shares(list_html);
    data["post_date"]=extract_post_date(list_html);
    data["nbr_de_react"]=extract_nbr_react(list_html);
    data["who_react"] =extract_who_react(react_html);
    data["who_share"] =extract_who_share(share_html);
    if with_comment :
        data["comments"]=extract_commentaires(list_html);
        data["nb_comment"]=len(extract_commentaires(list_html))
    return (data)

    
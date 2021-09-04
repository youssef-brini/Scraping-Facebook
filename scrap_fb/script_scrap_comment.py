import pymongo
import datetime
import time
import hashlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains
from script_scrap_fb import _login
import random
PATH = "C:\Program Files (x86)\chromedriver.exe"

def scroll_comment(browser):
    time.sleep(random.randint(1,3))
    nb_click = 0
    moreComments = browser.find_elements_by_class_name('_108_')
    while moreComments:
        nb_click +=1
        time.sleep(random.randint(1,3))
        action = webdriver.common.action_chains.ActionChains(browser)
        time.sleep(random.randint(1,3))
        try:
        # move to where the comment button is
            action.move_to_element_with_offset(moreComments[0], 5, 5)
            action.perform()
            moreComments[0].click()
            time.sleep(random.randint(2,5))
            if nb_click > 10 :
                break
            moreComments = browser.find_elements_by_class_name('_108_')
        except:
        # do nothing right heree
            pass
   
#extraire les commentaires
def extract_commentaires(post):
    try : 
        postComments = post.find_all(class_="_2b04")
        comments = []
        
        for comment in postComments:
            com=dict()
            person = comment.find("div",class_="_2b05").text
            com['person'] = person

            comment_text = comment.find_all("div")
                    
            com['comment'] = comment_text[3].text
            
            comments.append(com)
            
        return comments
    except :
            return ""

def Scrap_comment(post_url):
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
    time.sleep(random.randint(12,17))
    browser.get(url_post)
    time.sleep(random.randint(4,9))
    scroll_comment(browser) 
    source_data = browser.page_source
    post_data = bs(source_data, 'html.parser')

    with open('./post.html',"w", encoding="utf-8") as file:
        file.write(str(post_data.prettify()))

    list_html = post_data.find(class_="_59e9")
    data=dict()
    data["comments"]=extract_commentaires(list_html);
    return (data)









    
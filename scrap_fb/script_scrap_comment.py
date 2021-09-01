import pymongo
import datetime
import time
import hashlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains
import random
PATH = "C:\Program Files (x86)\chromedriver.exe"

def _login(browser, email, password):
    random.randint(3,7)
    #browser.maximize_window()
    browser.find_element_by_id("email").send_keys(email)
    time.sleep(random.randint(3,7))
    browser.find_element_by_name("pass").send_keys(password)
    time.sleep(random.randint(3,7))
    browser.find_element_by_name("login").click()
    time.sleep(random.randint(3,7))
def extract_url_post (post):
    urls = post.find("a",class_= "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw")
    
    return urls["href"]

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

def extract_nbr_commantaire(post):
    postShares = post.find_all("span",class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh m9osqain")
    shares = ""
    if postShares:
     for postShare in postShares:
        
        x = postShare.string
        if x is not None:
            x = x.split(" ", 1)
            shares = x
            return shares[0]     
    else:
        return "0"


def extract_post_date(post):
    div = post.find_all(class_="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw")
    if div :
            paragraphs = div[0].find('span')
            
            return(paragraphs.text)
# --------------------------------------------------------------------------------------------------
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
    scroll_comment(browser) # contient une parametre !!!!!!!!!!!!!!
    source_data = browser.page_source
    post_data = bs(source_data, 'html.parser')
    with open('./post.html',"w", encoding="utf-8") as file:
        file.write(str(post_data.prettify()))
    list_html = post_data.find(class_="_59e9")


    data=dict()
    # data['url']=url_post
    # data['scraping_date'] = datetime.datetime.now()
    # data["post_url"] =extract_url_post(list_html);
    # data["post_date"]=extract_post_date(list_html);
    # data["nbr_de_comments"]=extract_nbr_commantaire(list_html);
    data["comments"]=extract_commentaires(list_html);
    return (data)









    
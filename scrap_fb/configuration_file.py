import csv
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

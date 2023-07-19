import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
import json
import csv
import bs4


mrtlist2={}
mrtname={}

url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with req.urlopen(url) as reponse:
    data=reponse.read().decode("utf-8")

data=json.loads(data)
list=data["result"]['results']

with open("attraction.csv","w",newline="")as file:
    for i in list:
        name=i['stitle']
        address=i['address'].split(" ")[2][0:3]
        longitude=i['longitude']
        latitude=i["latitude"]
        pic=(i["file"].lower().split("jpg"))[0]+"jpg"
        mrt=i["MRT"]
     
        if mrt in mrtname:
            mrtname[mrt].append(name)
        else:
            mrtname[mrt] = [name]
        
        ww=csv.writer(file)
        ww.writerow([name,address,longitude,latitude,pic])
        
        with open("mrt.csv","w",newline="")as file2:
            for k,v in mrtname.items():
                row = [k] + v 
                writer2=csv.writer(file2)
                writer2.writerow(row)


#----------------------- task1-2 ----------------------------

def getData(url):   
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
    })

    with req.urlopen(request) as reponse:
        data=reponse.read()
    a=[]
    b=[]
    c=[]
    data=bs4.BeautifulSoup(data,"html.parser")
    titles=data.find_all("div",class_="title")
    counts=data.find_all("div",class_="nrec")

    for i in titles:
        if i.a!=None:
            title=i.a.string

        else:
            title=0
        
        a.append(title)
        titleurls=data.find_all("a",string=title)
        
        
        for i in titleurls:
            titleurl="https://www.ptt.cc"+i["href"]
            url2=titleurl
       
   
        request=req.Request(url2,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
    })

        with req.urlopen(request) as reponse2:
            data2=reponse2.read()

        data2=bs4.BeautifulSoup(data2,"html.parser")
        times=data2.find_all("span",class_="article-meta-value")
        b.append(times[3].string)
        
    for i in counts:
        if i.span!=None:
            count=i.span.string
        else:
            count=0
        c.append(count)

    merged_list=[f"{x}, {y}, {z}" for x, y, z in zip(a, c, b)]
    
    with open("movie.txt","a",newline="") as file:
        result ="\n".join(merged_list)
        file.write(result)
    
    nextlinks=data.find("a",string="‹ 上頁")
    nextlink="https://www.ptt.cc"+nextlinks["href"]
  
    return nextlink


PageUrl="https://www.ptt.cc/bbs/movie/index.html"
i=0
while i<=3:
    PageUrl=getData(PageUrl)
    i+=1

    
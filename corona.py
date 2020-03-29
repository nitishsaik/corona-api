from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ur
import requests
import json
import pycountry

URL='https://www.worldometers.info/coronavirus/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page=requests.get(URL,headers=headers)
soup=bs(page.content,'html.parser')
table_body=soup.find('table')
rows = table_body.find_all('tr')
l=[]
d={
    "Corona":[]
    }
f={
    "Main":[]
}
#to find the Main Header
ss=[]
mains=soup.findAll("div", {"id": "maincounter-wrap"} )


for i in mains:
    ss.append(i.find("span").text)
temp=soup.find_all("div",{"class":"panel_flip"})
data1=[]
data2=[]
for k in temp:
   x=k.findAll("div",{"class":"number-table-main"})
   for i in x:
     data1.append(i.text.strip())
   m=k.findAll("span")
   for j in m:
     data2.append(j.text.strip())

 
#print(temp1)
cuinf,cloc=data1
mild,seri,dis,dea=data2
coc,cocd,rec=ss
f["Main"].append({
    "CoronaCases":coc,
    "CoronaCurrent":cuinf,
    "CoronaClose":cloc,
    "CoronaMild":mild,
    "CoronaCritical":seri,
    "CoronaDischarged":dis,
    "CoronaDeaths":dea,
    "CoronaDeaths":cocd,
    "Recoverd":rec
})

#To get table data

#To get table data
mapping = {country.name: country.alpha_2 for country in pycountry.countries}
for row in rows:
    cols=row.find_all('td')
    z=['0' if v.text.strip() == "" else v.text.strip() for v in cols]

    #print(z)
    if len(z)!=0:
        c,totc,newc,totd,newd,totrecv,Actcases,seri,avg,Avgd,date=z
    
        d['Corona'].append({
            "Country":c,
            "Code":str(mapping.get(c)).lower(),
            "TotalCases":totc,
            "FirstDate":date,
            "NewCases":newc,
            "TotalDeaths":totd,
            "NewDeaths":newd,
            "TotalRecoverd":totrecv,
            "ActiveCases":Actcases,
            "Serious":seri,
            "Average":avg,
            "AverageDeaths":Avgd

        })

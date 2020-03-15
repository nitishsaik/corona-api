from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ur
import requests
import json

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
coc,cocd,rec=ss
f["Main"].append({
    "CoronaCases":coc,
    "CoronaDeaths":cocd,
    "Recoverd":rec
})

#To get table data

for row in rows:
    cols=row.find_all('td')
    z=['0' if v.text.strip() == "" else v.text.strip() for v in cols]

    #print(z)
    if len(z)!=0:
        c,totc,newc,totd,newd,totrecv,Actcases,seri,avg=z
        d['Corona'].append({
            "Country":c,
            "TotalCases":totc,
            "NewCases":newc,
            "TotalDeaths":totd,
            "NewDeaths":newd,
            "TotalRecoverd":totrecv,
            "ActiveCases":Actcases,
            "Serious":seri,
            "Average":avg

        })


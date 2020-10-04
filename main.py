import requests
from bs4 import BeautifulSoup
q_id=input("Enter Q Id:")
name= input("Enter User Name:")
url="https://atcoder.jp/contests/dp/submissions?f.Task={0}&f.LanguageName=&f.Status=&f.User={1}".format(q_id,name)
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
status=soup.find_all('span', class_='label')
ans="NO"
for x in status:
    if(x.get_text()=="AC"):
        ans="YES"
        break
print(ans)
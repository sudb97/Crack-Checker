}

#build 3 daily gamelist included
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import pytz
def hrs_now():
  tz_NY = pytz.timezone('Asia/Kolkata') 
  datetime_NY = datetime.now(tz_NY)
  return ((datetime_NY.strftime("%H")))  

def crack_checker():
  URL='https://www.skidrowreloaded.com/'
  headers= {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
  page= requests.get(URL, headers=headers)
  soup= BeautifulSoup(page.content,'html.parser')
  game_list=[]
  for foo in soup.find_all('div', attrs={'class': 'post'}):
      game_list.append(foo.get_text().split('\n')[1])
      
  for j in game_list:
    if j.find('Fifa')!= -1 or j.find('FIFA')!= -1 or j.find('fifa')!= -1   :
      server=smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.ehlo()

      server.login('yourmail@domainname.com','password')

      subject=' FIFA 20 Crack status'
      body='Fifa 20 has been CRACKED!!!!! PLAY!!! PLAY!!! PLAY!!!'
  
      msg= f"Subject: {subject}\n\n{body}"
      server.sendmail('crackwatch11@gmail.com','sudb97@gmail.com',msg)
      server.quit()
      return 1

  if int(hrs_now())==12:
      server=smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.ehlo()

      server.login('yourmail@domainname.com','password')

      subject='Latest Games Cracked List'
      body=''
      for g in game_list:
        body=body+g+'\n'
  
      msg= f"Subject: {subject}\n\n{body}"
      server.sendmail('yourmail@domainname.com','sendermai@domainname.com',msg)
      server.quit()
      

while True:
  sts=crack_checker()
  if sts==1:
    break
  time.sleep(3600)

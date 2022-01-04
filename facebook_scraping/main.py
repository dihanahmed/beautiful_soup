from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text=requests.get('https://www.facebook.com/').text
    #print(html_text)

    soup =BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('div',class_='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0')

    print(jobs)
    

    Profile_name=jobs.find('span', class_='nc684nl6').text

        #skills= job.find('span',class_='srp-skills').text.replace(' ','')
        #
        #more_info=job.header.h2.a['href']


    print(Profile_name)

        # print(skills)

       


        
                    
                
      
    



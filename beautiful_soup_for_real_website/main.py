from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)

    print('put some skills you are not familiar with')
    unfamiliar_skill=input('>')
    print(f'Filtering out:{unfamiliar_skill}')

    soup =BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    #print(jobs)
    for job in jobs:

        job_published_date=job.find('span',class_='sim-posted').text
        if 'few' in job_published_date:
            company_name=job.find('h3', class_='joblist-comp-name').text

            skills= job.find('span',class_='srp-skills').text.replace(' ','')
            
            more_info=job.header.h2.a['href']


            # print(company_name)

            # print(skills)

            if unfamiliar_skill not in skills:

                print(f"Company name:{company_name.strip()}")
                print(f"Required Skills:{skills.strip()}")
                print(f"Released Date:{job_published_date.strip()}")
            
                print(f'More Info:{more_info}')
                print('')

if __name__== '__main__':
    while True:
        find_jobs()
        time_wait=15
        print(f'Waiting {time_wait} seconds ...')
        time.sleep(time_wait)

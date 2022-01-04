from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)

soup =BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

#print(jobs)
for job in jobs:

    job_published_date=job.find('span',class_='sim-posted').text
    if 'few' in job_published_date:
        company_name=job.find('h3', class_='joblist-comp-name').text

        skills= job.find('span',class_='srp-skills').text.replace(' ','')



        # print(company_name)

        # print(skills)

        
        print(f"Company name:{company_name.strip()}")
        print(f"Required Skills:{skills.strip()}")
        print(f"Released Date:{job_published_date.strip()}")
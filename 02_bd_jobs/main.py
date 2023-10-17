import requests
from bs4 import BeautifulSoup
import time, os

def find_job_from_bdjob():
    get_url = requests.get('https://jobs.bdjobs.com/jobsearch.asp?fcatId=8&icatId=').text
    
    soup = BeautifulSoup(get_url, 'lxml')
    
    jobs = soup.find_all('div', class_="norm-jobs-wrapper")
    
    for index, job in enumerate(jobs):
        job_n = job.find('div', class_ ="job-title-text").a.text.replace(' ','')
        company_n = job.find('div', class_ = 'comp-name-text').text.replace(' ','')
        education_matched = job.ul
        location = job.find('div', class_ = "locon-text-d").text.replace(' ','')
        experience = job.find('div', class_ = "exp-text-d").text
        last_date = job.find('div', class_ = "dead-text-d").strong.text
        
        print(education_matched)
        
        if education_matched:
            education = education_matched.li.text
        else:
            education = "Not Spacified"
        
        print(f"""
            Job Name : {job_n.strip()} \n
            Company Name : {company_n.strip()} \n
            Education : {education.strip()} \n
            Location : {location.strip()} \n
            Experience : {experience.strip()} \n
            Last Date : {last_date.strip()} \n               
    
        """)
        
        # page = f"all_jobs/page_{page_num}"
        # if not os.path.exists(page):
        #     os.makedirs(page)
        
        # with open(f'{page}/{index+1}_job.txt', 'w') as f:
        #     f.write(f"""
        #             Job Name : {job_n.strip()} \n
        #             Company Name : {company_n.strip()} \n
        #             Education : {education.strip()} \n
        #             Location : {location.strip()} \n
        #             Experience : {experience.strip()} \n
        #             Last Date : {last_date.strip()} \n               
                
        #         """)
        # print(f'File Save {index+1}')
    

if __name__ == "__main__":
    find_job_from_bdjob()
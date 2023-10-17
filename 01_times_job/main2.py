from bs4 import BeautifulSoup
import requests
import time


# Filter the skill that i'm not familiyer 
unfamiliyer_skill = input(str('Enter your unfamilier skill : '))
print(f'Unfamilyer skill filtered', {unfamiliyer_skill})


def find_job():
     
    get_data = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(get_data, 'lxml') # will show all the data from only one page

    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx") # rap class

    for job in jobs:
        company_name = job.find('h3', class_ ="joblist-comp-name").text.replace(' ','') # will see only company name
        # print(company_name)
        skills = job.find('span', class_="srp-skills").text.replace(' ','')

        job_post_date = job.find('span', class_ = 'sim-posted').span.text # span er vitore span ke target kora holo

        more_info_link = job.header.h2.a['href']
        
        job_des = job.find('ul', class_ = 'list-job-dtl clearfix').li.text
        
        if unfamiliyer_skill not in skills:
            print(f"""
                    Company Name : {company_name.strip()}
                    Skill : {skills.strip()}
                    Job Published Date : {job_post_date.strip()}
                    More Info Link : {more_info_link}
                
                """)
            
if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 3  # second
        print(f'Wait for {time_wait} Second..')
        total_wait = time.sleep(time_wait * 3)
        
    

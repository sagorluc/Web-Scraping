from bs4 import BeautifulSoup
import requests
import time
import os


# Filter the skill that i'm not familiyer 
unfamiliyer_skill = input(str('Enter your unfamilier skill : '))
print(f'Unfamilyer skill filtered', {unfamiliyer_skill})


def find_job(page_num):
     
    get_data = requests.get('https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=python&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&pDate=I&sequence={page_num}&startPage={page_num}').text

    soup = BeautifulSoup(get_data, 'lxml') # will show all the data from only one page
    
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx") # rap class

    
    for index, job in enumerate(jobs):
             
        company_name = job.find('h3', class_ ="joblist-comp-name").text.replace(' ','') # will see only company name
        # print(company_name)
        skills = job.find('span', class_="srp-skills").text.replace(' ','')

        job_post_date = job.find('span', class_ = 'sim-posted').span.text # span er vitore span ke target kora holo

        more_info_link = job.header.h2.a['href']
        
        job_des = job.find('ul', class_ = 'list-job-dtl clearfix').li.text
        
        if unfamiliyer_skill not in skills:
            
            page_dir = f'posts_job/page_{page_num}'
            if not os.path.exists(page_dir):
                os.makedirs(page_dir)
            
            with open(f'{page_dir}/{index+1}.txt', 'w') as post: 
                post.write(f'Company Name : {company_name.strip()} \n')
                post.write(f'Skill : {skills.strip()} \n')
                post.write(f'Job Published Date : {job_post_date.strip()} \n')
                post.write(f'More Info Link : {more_info_link} \n')
            print(f'File Save {index}')
            
            
# if __name__ == '__main__':
#     while True:
#         find_job()
#         time_wait = 3  # second
#         print(f'Wait for {time_wait} Second..')
#         total_wait = time.sleep(time_wait * 3)
        
if __name__ == '__main__':
    num_pages = 5  # Change this to the number of pages you want to scrape
    for page_num in range(1, num_pages + 1):
        find_job(page_num)
        time_wait = 3  # second
        print(f'Wait for {time_wait} Second..')
        total_wait = time.sleep(time_wait)
    

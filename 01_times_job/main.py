from bs4 import BeautifulSoup
import requests

get_data = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(get_data)
soup = BeautifulSoup(get_data, 'lxml') # will show all the data from only one page
# print(soup)
job = soup.find('li', class_ = "clearfix job-bx wht-shd-bx") # rap class
# print(jobs)


company_name = job.find('h3', class_ ="joblist-comp-name").text.replace(' ','') # will see only company name
# print(company_name)

# remove_space = company_name.replace(' ', '') # replace diye space ke remove kora holo
# # print(remove_space)


skill = job.find('span', class_="srp-skills").text.replace(' ','')
# print(skill)

job_post_date = job.find('span', class_ = 'sim-posted').span.text # span er vitore span ke target kora holo
# print(job_post)

job_des = job.find('ul', class_ = 'list-job-dtl clearfix').li.text
# print(job_des)

# change the class name

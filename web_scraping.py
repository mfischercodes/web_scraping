from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests #used for online web access alternatively use selenium
import re

'''
#region ONLINE WEBSITE SELF
url = 'https://www.amazon.ca/0-5meter-Lead-Snowkids-Compatible-Ethernet-Function/dp/B0839CBWBR/ref=br_msw_pdt-4?_encoding=UTF8&smid=A3M67XBJECTJN0&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=&pf_rd_r=B0DJT26VPXYR82JWH3SP&pf_rd_t=36701&pf_rd_p=4500e888-b5b9-4e64-8bd4-fc15289d25f6&pf_rd_i=desktop'
#ONLINE ACCESS
chrome_options = Options()
chrome_options.add_argument("--headless") #option don't open browser to the user run in background

driver=webdriver.Chrome("C:/Users/Work/chromedriver", chrome_options=chrome_options) #opens browser
get = driver.get(url) #loads/gets a webpage
html = driver.page_source #gets the page source for html
soup = BeautifulSoup(html, 'lxml') #variable beautiful soup accessing the html source with html.praser or lxml
#soup = BeautifulSoup(html, 'html.parser')

tags = soup.find(id ="productTitle").text.strip('\n') #run find or find_all, etc... to find information you like
#endregion

#region OFFLINE WEBSITE
with open('start.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text
        pattern = r"\d+"
        digits = ''.join(re.findall(pattern, course_price))

        print(course_name + ' costs: $' + digits)

    
    #tags = soup.find_all('h5')
    #for i in tags:
        #print(i.text)
    
#endregion

#region ONLINE WEBSITE
url = 'https://ca.indeed.com/jobs?q=junior+software+developer&l=Vancouver%2C+BC'

chrome_options = Options()
chrome_options.add_argument("--headless")
#driver=webdriver.Chrome("C:/Users/Work/chromedriver", chrome_options=chrome_options)
driver=webdriver.Chrome("C:/Users/LenovoAdmin/chromedriver", chrome_options=chrome_options)
get=driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')


#html_text = requests.get(url)
#soup = BeautifulSoup(html_text, 'lxml')

job = soup.find('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')
job_title = job.find_all('b')
job_title = ' '.join([job.text for job in job_title])
company_name = job.find(class_='company').text.strip('\n')
days_ago = job.find('span', class_='date').text
link = job.find('h2', class_='title').a['href']

print(f"""
Job Title: {job_title}
Company Name: {company_name}
Days Ago: {days_ago}
Link: https://ca.indeed.com/{link} doesnt really work
""")

#endregion
''' 
#region Price Tracker
url = 'https://www.amazon.ca/s?k='

user_input = '+'.join(input("What would you like to check the price of? ").split(' '))
url += user_input
print(url)

chrome_options = Options()
chrome_options.add_argument("--headless")
#driver=webdriver.Chrome("C:/Users/Work/chromedriver", chrome_options=chrome_options)
driver=webdriver.Chrome("C:/Users/LenovoAdmin/chromedriver", chrome_options=chrome_options)
#driver=webdriver.Chrome("C:/Users/LenovoAdmin/chromedriver")
get=driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')


product = soup.find('div', class_='a-section a-spacing-medium')
title = product.find('div', class_='a-section aok-relative s-image-square-aspect').img['alt']
link = 'null'
price_whole = product.find('span', class_='a-price-whole').text
price_sub = product.find('span', class_='a-price-fraction')
price = str(price_whole) + '.' + str(price_sub)
print()
print(title)
print(price)

#html_text = requests.get(url)
#soup = BeautifulSoup(html_text, 'lxml')
'''
job = soup.find('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')
job_title = job.find_all('b')
job_title = ' '.join([job.text for job in job_title])
company_name = job.find(class_='company').text.strip('\n')
days_ago = job.find('span', class_='date').text
link = job.find('h2', class_='title').a['href']
'''




























#endregion






















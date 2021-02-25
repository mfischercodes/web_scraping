from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
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
'''



with open('start.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h5')
    for i in tags:
        print(i.text)




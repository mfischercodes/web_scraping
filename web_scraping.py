#region imports
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests 
import re
#endregion

websites = {'amazon.ca': 'https://www.amazon.ca/s?k=', 'bestbuy.ca': 'https://www.bestbuy.ca/en-ca/search?search='}
lowest = {'website': None, 'title': 'No Title', 'price': 100000, 'link': 'no link'}




url = websites['amazon.ca']

user_input = input("What would you like to check the price of? ")
url_input = '+'.join(user_input.split(' '))
url += url_input
print(url)
#TODO: FOR EACH WEBSITE KEY USE AS URL BASE THEN ADD URL_INPUT

def open_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver=webdriver.Chrome("C:/Users/Work/chromedriver", chrome_options=chrome_options)
    #driver=webdriver.Chrome("C:/Users/LenovoAdmin/chromedriver", chrome_options=chrome_options)
    get=driver.get(url)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    return soup

soup = open_browser()

ran_once = False
wrong_product = False

lowest_location = 'No Website'
lowest_title = 'Error'
lowest_price = 100000
lowest_link = 'No Link'

#TODO: Refactor code

product = soup.find_all('div', class_='a-section a-spacing-medium')
for i in range(5):

    try: title = product[i].find('a', class_='a-link-normal a-text-normal').span.text
    except: pass
    
    if 'case' in title.lower() and 'case' not in user_input.lower():
        no_product = True

    if re.search(user_input.lower(), title.lower()):
        wrong_product = True
    else:
        wrong_product = False

    if wrong_product == True:
        try: price_whole = product[i].find('span', class_='a-price-whole').text
        except AttributeError: price_whole = 100000
        
        try: price_sub = product[i].find('span', class_='a-price-fraction').text
        except AttributeError: price_sub = '00'

        try: link = product[i].find('span', class_='rush-component').a['href']
        except: pass

        if price_whole == 100000:
            price = 100000
        else:
            price = price_whole + price_sub
        
        if float(price) < float(lowest_price):
            lowest['website'] = 'Amazon.ca'
            lowest['title'] = title
            lowest['price'] = price
            lowest['link'] = 'https://www.amazon.ca/' + link

        def price_printer(website = 'amazon.ca'):
            print()
            if website in url: print(website)
            print(title)
            if price == 100000:
                print("Out of Stock")
            else:
                print(price)

        ran_once = True
        
        price_printer()   
    
    

if not ran_once:
    print("We did not find the product you were looking for.\
        \nPlease make sure you typed in the correct name")
    
def lowest_price_func():
    print(f"""
Website: {lowest['website']}
Title: {lowest['title']}
Price: ${lowest['price']}
Link: {lowest['link']} 
""")

lowest_price_func()




























#endregion





















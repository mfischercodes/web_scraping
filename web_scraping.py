#region imports
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests 
import re
import time
#endregion

websites = {'amazon.ca': 'https://www.amazon.ca/s?k=', 'bestbuy.ca': 'https://www.bestbuy.ca/en-ca/search?search=',
 'canadacomputers.com': 'https://www.canadacomputers.com/search/results_details.php?language=en&keywords='}
lowest = {'website': None, 'title': 'No Title', 'price': 100000, 'link': 'no link'}

#url = websites['amazon.ca']
url = websites['canadacomputers.com']

user_input = input("What would you like to check the price of? ")
url_input = '+'.join(user_input.split(' '))
url += url_input
print(url)
#TODO: FOR EACH WEBSITE KEY USE AS URL BASE THEN ADD URL_INPUT

def open_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver=webdriver.Chrome("C:/Users/Work/chromedriver", chrome_options=chrome_options)
    #driver=webdriver.Chrome("C:/Users/Work/chromedriver")
    #driver=webdriver.Chrome("C:/Users/LenovoAdmin/chromedriver", chrome_options=chrome_options)

    get=driver.get(url)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    return soup
#TODO: BEST BUY FUNCTION WORKING COPY FROM GET PRODUCT INFO
#TODO: BEST BUY NO MARKETPLACE SELLERS
#TODO: SEE IF YOU CAN COMBINE THE TWO INPUTTING 'div' or span if differ from default + inputing id name all the time. 
#add ending as input parameter to add the .span.text etc...

#product_bestbuy = soup.find_all('div', class_='col-xs-12_198le col-sm-4_13E9O col-lg-3_ECF8k x-productListItem productLine_2N9kG')
#title_bb = product[i].find('div', class_='productItemName_3IZ3c').text
#price = product[i].find('span', class_='screenReaderOnly_3anTj large_3aP7Z')[1:]
#def price_whole(ending, addition):
#   return (product[i].find('span', class_=''a-price-whole')ending)
#   additional
#def price_whole([1:0], additional line here?)

def get_product_info_bb():
    time.sleep(5)
    product = soup.find_all('div', class_='col-xs-12_198le col-sm-4_13E9O col-lg-3_ECF8k x-productListItem productLine_2N9kG')

    for i in range(5):
        title = product[i].find('div', class_='productItemName_3IZ3c').text

        def input_in_title():
            return re.search(user_input.lower(), title.lower())            
        
        if input_in_title():
            def price_whole():
                try: 
                    # need to remove $ from this and change to a float
                    return (product[i].find('span', class_='screenReaderOnly_3anTj large_3aP7Z').text)
                except AttributeError: 
                    return '100000'
            
            print(price_whole())
            '''
            def price_sub():
                try: 
                    return (product[i].find('span', class_='a-price-fraction').text)
                except AttributeError: 
                    return '00'

            def price():
                if price_whole() == '100000':
                    return 100000
                else:
                    return price_whole() + price_sub()

            def set_lowest_variables():
                if float(price) < float(lowest['price']):
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

            price = price()
            link = product[i].find('span', class_='rush-component').a['href']
            
            set_lowest_variables()
            #price_printer()   
    '''

def get_product_info_cc():
    
    product = soup.find_all('div', class_='col-xl-3 col-lg-4 col-6 mt-0_5 px-0_5 toggleBox mb-1')
    #TODO: wrap for loops in a try since only 2 products on this page
    for i in range(2):
        title = product[i].find('a', class_='text-dark text-truncate_3').text
        
        def input_in_title():
            return re.search(user_input.lower(), title.lower())            
        
        if input_in_title():
            def price():
                price = product[i].find('span', class_='d-block mb-0 pq-hdr-product_price line-height').strong.text
                price = price[1:]
                return price

            #TODO: CHECK each page if in stock
            
            def set_lowest_variables():
                if float(price) < float(lowest['price']):
                    lowest['website'] = 'canadacomputers.com'
                    lowest['title'] = title
                    lowest['price'] = price
                    lowest['link'] = link

            def price_printer(website = 'amazon.ca'):
                print()
                if website in url: print(website)
                print(title)
                if price == 100000:
                    print("Out of Stock")
                else:
                    print(price)

            price = price()
            link = product[i].find('div', class_='productImageSearch pt-2 pt-sm-0 w-100').a['href']
            
            set_lowest_variables()
            #price_printer()   
        

def get_product_info():
    product = soup.find_all('div', class_='a-section a-spacing-medium')

    for i in range(5):
        title = product[i].find('a', class_='a-link-normal a-text-normal').span.text

        def input_in_title():
            return re.search(user_input.lower(), title.lower())            
        
        if input_in_title():
            def price_whole():
                try: 
                    return (product[i].find('span', class_='a-price-whole').text)
                except AttributeError: 
                    return '100000'
            
            def price_sub():
                try: 
                    return (product[i].find('span', class_='a-price-fraction').text)
                except AttributeError: 
                    return '00'

            def price():
                if price_whole() == '100000':
                    return 100000
                else:
                    return price_whole() + price_sub()

            def set_lowest_variables():
                if float(price) < float(lowest['price']):
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

            price = price()
            link = product[i].find('span', class_='rush-component').a['href']
            
            set_lowest_variables()
            #price_printer()   

def print_lowest_price():
    if lowest['website'] == None:
        print("\nWe did not find the product you were looking for.\
        \nPlease make sure you typed in the correct name")
    else:
        print(f"\nWebsite: {lowest['website']} \
        \nTitle: {lowest['title']}\
        \nPrice: ${lowest['price']}\
        \nLink: {lowest['link']}\n")

#TODO: FOR EACH WEBSITE IN WEBSITES DO BELOW
#PRINT LOWEST PRICE SHOULD BE ONLY RAN ONCE
soup = open_browser()
get_product_info_cc()    
print_lowest_price()






















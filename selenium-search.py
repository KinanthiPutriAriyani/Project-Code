from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
query = 'Soekarno'
n_pages = 10

for page in range(1, n_pages):
    url = "http://www.google.com/search?q=" + query + "&start" + str((page - 1) * 10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    search = soup.find_all('div', class_="yuRUbf")
    for h in search:
        print(h.a.text)
        print(h.a.get('href'))
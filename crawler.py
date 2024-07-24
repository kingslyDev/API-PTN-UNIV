from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def get_ptn_list():
   
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    url = 'https://sidata-ptn-snpmb.bppp.kemdikbud.go.id/ptn_sb.php'
    driver.get(url)
    
   
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    ptn_list = []

  
    rows = soup.select('table.table.table-striped tbody tr')
    
    print(f"Found {len(rows)} rows in the table")  

    for row in rows:
        cells = row.find_all('td')
        print(f"Found {len(cells)} cells in the row") 
        if len(cells) >= 3:
            ptn_name = cells[1].find('a').get_text().strip() 
            ptn_list.append(ptn_name)
            print(f"Added PTN: {ptn_name}") 

    return ptn_list

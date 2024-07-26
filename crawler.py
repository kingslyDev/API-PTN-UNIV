from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json

def get_ptn_list():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    url = 'https://sidata-ptn-snpmb.bppp.kemdikbud.go.id/ptn_sb.php'
    
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'table.table.table-striped tbody tr'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    finally:
        driver.quit()

    ptn_list = []

    rows = soup.select('table.table.table-striped tbody tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:
            ptn_name = cells[2].find('a').get_text().strip()
            ptn_id = cells[2].find('a')['href'].split('=')[-1]
            ptn_list.append({'name': ptn_name, 'id': ptn_id})

    return ptn_list

def get_prodi_list(ptn_id):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    url = f'https://sidata-ptn-snpmb.bppp.kemdikbud.go.id/ptn_sb.php?ptn={ptn_id}'
    
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'table.table.table-striped tbody tr'))
        )
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    finally:
        driver.quit()

    prodi_list = []

    rows = soup.select('table.table.table-striped tbody tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:
            prodi_name = cells[2].find('a').get_text().strip()
            prodi_jenjang = cells[3].get_text().strip()
            prodi_list.append({'name': prodi_name, 'jenjang': prodi_jenjang})

    return prodi_list

# Scrape data and store it in a JSON file
def scrape_and_store_data():
    ptn_data = get_ptn_list()
    all_data = []

    for ptn in ptn_data:
        ptn_id = ptn['id']
        prodi_list = get_prodi_list(ptn_id)
        all_data.append({
            'ptn_name': ptn['name'],
            'ptn_id': ptn_id,
            'prodi_list': prodi_list
        })

    with open('ptn_data.json', 'w') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

scrape_and_store_data()

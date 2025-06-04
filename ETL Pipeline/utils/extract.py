import time
import logging
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

# Setup logging untuk mencatat error
logging.basicConfig(
    filename="etl_log.log", level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def get_html_content(url):
    try:
        with requests.Session() as session:
            res = session.get(url, headers=HEADERS)
            res.raise_for_status()
            return res.text
    except requests.exceptions.RequestException as err:
        logging.error(f"Gagal mengakses {url}: {err}")
        return None

def parse_fashion_info(element):
    if not element:
        return None
    
    try:
        if isinstance(element, dict):
            name = element.get('Title', '').strip()
            price = element.get('Price', '').strip()
            rating = element.get('Rating', '').strip()
            colors = element.get('Colors', '').strip()
            size = element.get('Size', '').strip()
            gender = element.get('Gender', '').strip()
            
            return {
                "Title": name,
                "Price": price,
                "Rating": rating,
                "Colors": colors,
                "Size": size,
                "Gender": gender,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        
        name = element.find('h3').text.strip()
        price = element.find('span', class_='price').text.strip() if element.find('span', class_='price') else None
        
        rating_text = element.find('p', string=lambda t: t and "Rating:" in t).text.strip().replace("Rating:", "").strip() if element.find('p', string=lambda t: t and "Rating:" in t) else None
        rating = float(re.search(r"(\d+(\.\d+)?)", rating_text).group(1)) if rating_text and re.search(r"(\d+(\.\d+)?)", rating_text) else None
        
        colors_text = element.find('p', string=lambda t: t and "Colors:" in t).text.strip() if element.find('p', string=lambda t: t and "Colors:" in t) else None
        colors = re.search(r'(\d+)', colors_text).group(1) if colors_text and re.search(r'(\d+)', colors_text) else None
        
        if colors is None:
            details = {
                p.text.split(': ')[0].strip(): p.text.split(': ')[1].strip()
                for p in element.find_all('p') if ': ' in p.text
            }
            colors = details.get('Colors', None)
        
        if colors is None:
            colors_p = element.find('p', string=lambda t: t and "Colors" in t)
            if colors_p:
                colors = colors_p.text.replace('Colors:', '').strip()
                match = re.search(r'(\d+)', colors)
                colors = match.group(1) if match else None
        
        details = {
            p.text.split(': ')[0].strip(): p.text.split(': ')[1].strip()
            for p in element.find_all('p') if ': ' in p.text
        }
        
        size = details.get('Size', None)
        gender = details.get('Gender', None)
        
        return {
            "Title": name,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as error:
        logging.error(f"Gagal parsing data produk: {error}")
        return None

def scrape_fashion(base_url, start=1, delay_sec=2):
    result = []
    current_page = start
    while True:
        page_url = f"{base_url}/page{current_page}" if current_page > 1 else base_url
        print(f"Mengambil data dari: {page_url}")
        html = get_html_content(page_url)
        if not html:
            break
        try:
            soup = BeautifulSoup(html, "html.parser")
            products = soup.find_all('div', class_='product-details')
            if not products:
                break
            for product in products:
                record = parse_fashion_info(product)
                if record:
                    result.append(record)
            current_page += 1
            time.sleep(delay_sec)
        except Exception as err:
            logging.error(f"Error saat proses scraping halaman {current_page}: {err}")
            break
    return result
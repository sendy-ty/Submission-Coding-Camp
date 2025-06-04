import pandas as pd
import logging
import re

# Konfigurasi logging
logging.basicConfig(
    filename="etl_log.log", level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_price(price_str):
    if not price_str:
        return None
    try:
        price_str = re.sub(r'[^\d.]', '', price_str)
        return float(price_str) if price_str else None
    except Exception as e:
        logging.error(f"Error parsing harga: {price_str} - {e}")
        return None

def parse_rating(value):
    if value is None:
        return None
    try:
        match = re.findall(r"\d+\.\d+|\d+", str(value))
        if match:
            return float(match[0])
        return None
    except Exception as e:
        logging.error(f"Error parsing rating: {value} - {e}")
        return None

def parse_colors(color_data):
    try:
        if not color_data:
            return None
        match = re.search(r'\d+', str(color_data))
        if match:
            return int(match.group(0))
        default_colors = {
            'None': None,
            '': None
        }
        return default_colors.get(color_data, None)
    except (ValueError, TypeError) as e:
        logging.error(f"Gagal parsing warna: {color_data} - {e}")
        return None

def normalize_size(size_data):
    return str(size_data).strip() if size_data is not None else None

def normalize_gender(gender_data):
    return str(gender_data).strip() if gender_data is not None else None

def clean_price(price_str):
    return parse_price(price_str)

def clean_rating(value):
    return parse_rating(value)

def transform_data(data, exchange_rate=16000):
    if isinstance(data, list) and len(data) == 0:
        return pd.DataFrame()
    
    df = pd.DataFrame(data) if not isinstance(data, pd.DataFrame) else data.copy()
    df = df[~df['Title'].isin([None, "", "Unknown Product"])]

    df['Price'] = df['Price'].apply(clean_price)
    df['Rating'] = df['Rating'].apply(clean_rating)
    df['Colors'] = df['Colors'].apply(parse_colors)
    df['Size'] = df['Size'].apply(normalize_size)
    df['Gender'] = df['Gender'].apply(normalize_gender)

    df['Price'] = df['Price'] * exchange_rate
    df = df.dropna(subset=['Price'])
    df['Price'] = df['Price'].astype(float)
    df = df.drop_duplicates()

    return df

def clean_and_transform(data, exchange_rate=16000):
    return transform_data(data, exchange_rate)
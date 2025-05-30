import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from utils.transform import (
    clean_price, clean_rating, transform_data, clean_and_transform,
    parse_price, parse_rating, parse_colors, normalize_size, normalize_gender
)
from utils.extract import parse_fashion_info

def test_price_cleaning_usd():
    assert clean_price('$100.00') == 100.0
    assert clean_price('$1,000.00') == 1000.0

def test_price_cleaning_invalid():
    assert clean_price('invalid-text') is None
    assert clean_price(None) is None

def test_rating_conversion_basic():
    assert clean_rating('4.5') == 4.5
    assert clean_rating('4.5/5') == 4.5

def test_rating_with_text_format():
    assert clean_rating('Rating: 3⭐/5') == 3.0

def test_rating_invalid_input():
    assert clean_rating('text-only') is None

def test_empty_data_transformation():
    df = transform_data([])
    assert isinstance(df, pd.DataFrame)
    assert df.empty

def test_data_transformation_logic():
    sample_data = [({
        'Title': 'Sample',
        'Price': '$1.00',
        'Rating': '4.0',
        'Colors': '3 Colors',
        'Size': 'M',
        'Gender': 'Unisex',
        'Timestamp': '2025-01-01 00:00:00'
    })]
    df = transform_data(sample_data, exchange_rate=16000)
    assert df.iloc[0]['Price'] == 16000.0
    assert df.iloc[0]['Rating'] == 4.0
    assert df.iloc[0]['Colors'] == 3
    assert df.iloc[0]['Size'] == 'M'
    assert df.iloc[0]['Gender'] == 'Unisex'

def test_data_transformation_with_special_characters():
    sample_data = [({
        'Title': 'Sample',
        'Price': '$1,000.00',
        'Rating': '4.5/5',
        'Colors': '3 Colors',
        'Size': 'M',
        'Gender': 'Unisex',
        'Timestamp': '2025-01-01 00:00:00'
    })]
    df = transform_data(sample_data, exchange_rate=16000)
    assert df.iloc[0]['Price'] == 16000000.0
    assert df.iloc[0]['Rating'] == 4.5

def test_clean_and_transform_function():
    sample_data = [({
        'Title': 'Sample',
        'Price': '$1.00',
        'Rating': '4.0',
        'Colors': '2 Colors',
        'Size': 'L',
        'Gender': 'Men',
        'Timestamp': '2025-01-01 00:00:00'
    })]
    df = clean_and_transform(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.iloc[0]['Price'] == 16000.0

# 🔼 Tambahan test untuk fungsi utilitas langsung:

def test_parse_price():
    assert parse_price('$1,234.56') == 1234.56
    assert parse_price(None) is None
    assert parse_price('') is None

def test_parse_rating():
    assert parse_rating('4.2') == 4.2
    assert parse_rating('Rating: 5⭐') == 5.0
    assert parse_rating('invalid') is None

def test_parse_colors():
    assert parse_colors('4 Colors') == 4
    assert parse_colors('No Colors') is None
    assert parse_colors(None) is None

def test_normalize_size():
    assert normalize_size(' L ') == 'L'
    assert normalize_size(None) is None

def test_normalize_gender():
    assert normalize_gender(' Female ') == 'Female'
    assert normalize_gender(None) is None

def test_parse_fashion_info():
    element_dict = {
        'Title': 'Sample',
        'Price': '$1.00',
        'Rating': '4.0',
        'Colors': '3 Colors',
        'Size': 'M',
        'Gender': 'Unisex',
    }
    result_dict = parse_fashion_info(element_dict)
    assert result_dict is not None

    from bs4 import BeautifulSoup
    html = """
    <div class="product-details">
        <h3>Sample</h3>
        <div class="price-container">
            <span class="price">$1.00</span>
        </div>
        <p>Rating: 4.0</p>
        <p>Colors: 3 Colors</p>
        <p>Size: M</p>
        <p>Gender: Unisex</p>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    element_bs = soup.find('div', class_='product-details')
    result_bs = parse_fashion_info(element_bs)
    assert result_bs is not None
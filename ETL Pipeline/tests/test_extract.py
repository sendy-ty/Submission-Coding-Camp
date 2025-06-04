import pytest
from bs4 import BeautifulSoup
from utils.extract import get_html_content, parse_fashion_info, scrape_fashion

def test_valid_get_html_content():
    content = get_html_content('https://fashion-studio.dicoding.dev')
    assert content is not None
    assert '<html' in content.lower()

def test_invalid_get_html_content():
    assert get_html_content('invalid-url') is None

def test_valid_parse_fashion_info():
    html_snippet = '''
    <div class="product-details">
        <h3>Example</h3>
        <div class="price-container"><span class="price">$1.00</span></div>
        <p>Rating: 4.0⭐/5</p>
        <p>Colors: 3 Colors</p>
        <p>Size: M</p>
        <p>Gender: Unisex</p>
    </div>
    '''
    soup_tag = BeautifulSoup(html_snippet, 'html.parser').find('div', class_='product-details')
    result = parse_fashion_info(soup_tag)
    assert isinstance(result, dict)
    assert result['Title'] == 'Example'
    assert result['Price'] == '$1.00'
    assert result['Rating'] == 4.0
    assert result['Colors'] == '3'
    assert result['Size'] == 'M'
    assert result['Gender'] == 'Unisex'
    assert 'Timestamp' in result

def test_invalid_parse_fashion_info():
    assert parse_fashion_info(None) is None
    empty = BeautifulSoup('<div></div>', 'html.parser').find('div')
    assert parse_fashion_info(empty) is None

def test_empty_scrape_result(monkeypatch):
    monkeypatch.setattr('utils.extract.get_html_content', lambda url: '<html></html>')
    result = scrape_fashion('http://dummy-url', start=1, delay_sec=0)
    assert result == []
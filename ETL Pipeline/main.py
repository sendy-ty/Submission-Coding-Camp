import pandas as pd
from utils.extract import scrape_fashion
from utils.transform import clean_and_transform
from utils.load import export_to_csv, export_to_postgres, export_to_gsheet

def run_etl():
    BASE_URL = 'https://fashion-studio.dicoding.dev'
    RATE = 16000
    POSTGRE_URL = 'postgresql+psycopg2://sandytirtayudha:sandy123@localhost:5432/fashions_db'
    SPREADSHEET_NAME = "products.csv"
    SERVICE_ACCOUNT = "google-sheets-api.json"

    print("="*10, "Memulai proses pengambilan data fashion", "="*10)
    raw_data = scrape_fashion(BASE_URL)

    if raw_data:
        print(f"{'.'*10} Total produk ditemukan: {len(raw_data)}. Mulai transformasi... {'.'*10}")
        df = pd.DataFrame(raw_data)
        df = clean_and_transform(df, RATE)

        print("="*10, "Menyimpan ke file dan database", "="*10)
        export_to_csv(df, 'products.csv')
        export_to_postgres(df, POSTGRE_URL)

        print(f">>> Dimensi data: {df.shape}")
        print(df.head())

        print("="*10, "Menyimpan ke Google Sheets", "="*10)
        export_to_gsheet(df, SPREADSHEET_NAME, SERVICE_ACCOUNT)
        print(f"{'.'*10} Sukses menyimpan ke Google Sheets! {'.'*10}")
    else:
        print("Tidak ada data yang berhasil diambil dari website.")

if __name__ == '__main__':
    run_etl()
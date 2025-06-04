import pandas as pd
import logging
from sqlalchemy import create_engine
import gspread
from google.oauth2.service_account import Credentials

# Logging untuk mencatat error
logging.basicConfig(
    filename="etl_log.log", level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def export_to_csv(df, filename="produk.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Data berhasil diekspor ke file CSV: {filename}")
    except Exception as err:
        logging.error(f"Kesalahan saat menyimpan CSV {filename}: {err}")

def export_to_postgres(df, conn_url):
    db_engine = None
    try:
        db_engine = create_engine(conn_url)
        df.to_sql("data_fashion", db_engine, if_exists="replace", index=False)
        print("Data sukses dimasukkan ke PostgreSQL.")
    except Exception as err:
        logging.error(f"Error saat menyimpan ke PostgreSQL: {err}")
    finally:
        if db_engine:
            db_engine.dispose()

def export_to_gsheet(df, sheet_title, credentials_path):
    try:
        creds = Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        )
        gc = gspread.authorize(creds)
        try:
            worksheet = gc.open(sheet_title).sheet1
        except Exception:
            worksheet = gc.create(sheet_title).sheet1
        worksheet.clear()
        worksheet.update([df.columns.tolist()] + df.values.tolist())
        print(f"Data berhasil ditulis ke Google Sheets: {sheet_title}")
    except Exception as err:
        logging.error(f"Error saat menulis ke Google Sheets: {err}")
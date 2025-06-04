import os
import pandas as pd
import pytest
from unittest.mock import MagicMock, patch
from utils.load import export_to_csv, export_to_postgres, export_to_gsheet

def test_csv_storage(tmp_path):
    df = pd.DataFrame({'Col': [1]})
    file_path = tmp_path / "output.csv"
    export_to_csv(df, str(file_path))
    assert file_path.exists()
    data_loaded = pd.read_csv(str(file_path))
    assert data_loaded['Col'][0] == 1

def test_postgres_storage(monkeypatch):
    df = pd.DataFrame({'Col': [1]})
    mock_engine = MagicMock()
    monkeypatch.setattr('utils.load.create_engine', lambda url: mock_engine)
    df.to_sql = MagicMock()
    export_to_postgres(df, 'dummy_connection_url')
    mock_engine.dispose.assert_called_once()

@patch('utils.load.Credentials.from_service_account_file')
@patch('utils.load.gspread')
def test_gsheet_open_update(mock_gspread, mock_creds):
    df = pd.DataFrame({'Col': [1]})
    mock_creds.return_value = object()
    client = MagicMock()
    mock_gspread.authorize.return_value = client
    mock_sheet = MagicMock()
    client.open.return_value.sheet1 = mock_sheet

    export_to_gsheet(df, 'TestSheet', 'dummy_creds.json')
    mock_sheet.clear.assert_called_once()
    mock_sheet.update.assert_called_once()

@patch('utils.load.Credentials.from_service_account_file')
@patch('utils.load.gspread')
def test_gsheet_create_update(mock_gspread, mock_creds):
    df = pd.DataFrame({'Col': [1]})
    mock_creds.return_value = object()
    client = MagicMock()
    mock_gspread.authorize.return_value = client
    client.open.side_effect = Exception("SheetNotFound")
    mock_sheet = MagicMock()
    client.create.return_value.sheet1 = mock_sheet

    export_to_gsheet(df, 'NewSheet', 'dummy_creds.json')
    mock_sheet.clear.assert_called_once()
    mock_sheet.update.assert_called_once()
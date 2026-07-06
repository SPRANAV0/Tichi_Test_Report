import os
import openpyxl

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "test_data.xlsx")


def get_test_data(sheet_name):
    
    workbook = openpyxl.load_workbook(DATA_FILE, data_only=True)
    sheet = workbook[sheet_name]

    rows = list(sheet.iter_rows(values_only=True))
    headers = rows[0]
    data_rows = rows[1:]

    records = []
    for row in data_rows:
        record = dict(zip(headers, row))
        records.append(record)

    return records

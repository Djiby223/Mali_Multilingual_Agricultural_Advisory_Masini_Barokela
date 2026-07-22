from pathlib import Path
from openpyxl import load_workbook
import zipfile

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXCEL_FILE = PROJECT_ROOT / "data" / "Test.xlsx"

print("File:", EXCEL_FILE)
print("Exists:", EXCEL_FILE.exists())
print("ZIP:", zipfile.is_zipfile(EXCEL_FILE))

wb = load_workbook(EXCEL_FILE)

print("SUCCESS!")
print("Sheets:", wb.sheetnames)
import csv
import json
from pathlib import Path


def read_json(file_path: str):
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_csv(file_path: str):
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [row for row in reader]


def read_excel(file_path: str):
    try:
        import openpyxl
    except ImportError as exc:
        raise ImportError("openpyxl is required to read Excel files. Install it with 'pip install openpyxl'.") from exc

    path = Path(file_path)
    workbook = openpyxl.load_workbook(path, data_only=True)
    sheet = workbook.active
    rows = list(sheet.rows)
    headers = [cell.value for cell in rows[0]]
    data = []
    for row in rows[1:]:
        entry = {headers[idx]: cell.value for idx, cell in enumerate(row)}
        data.append(entry)
    return data


def read_test_data(file_path: str):
    path = Path(file_path)
    suffix = path.suffix.lower()
    if suffix == ".json":
        return read_json(file_path)
    if suffix == ".csv":
        return read_csv(file_path)
    if suffix in {".xlsx", ".xlsm", ".xltx", ".xltm"}:
        return read_excel(file_path)
    raise ValueError(f"Unsupported test data format: {suffix}")

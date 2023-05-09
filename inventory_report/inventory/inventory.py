from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def import_data(file_path, extension):
    if extension == "csv":
        data = CsvImporter.import_data(file_path)
    elif extension == "json":
        data = JsonImporter.import_data(file_path)
    elif extension == "xml":
        data = XmlImporter.import_data(file_path)
    else:
        raise ValueError("Formato inválido")
    return data

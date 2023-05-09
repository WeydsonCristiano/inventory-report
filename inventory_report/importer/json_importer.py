import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if not file_path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(file_path, "r") as file:
            data = json.load(file)
            return data

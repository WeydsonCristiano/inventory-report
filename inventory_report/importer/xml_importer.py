import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []
        for product in root.findall("record"):
            item = {}
            for child in product:
                item[child.tag] = child.text
            data.append(item)
        return data

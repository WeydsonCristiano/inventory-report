import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    REPORT_CLASSES = {"simples": SimpleReport, "completo": CompleteReport}

    @classmethod
    def import_data(cls, file_path, report_type):
        file_extension = file_path.split(".")[-1]
        if file_extension == "csv":
            data = cls._read_csv(file_path)
        elif file_extension == "json":
            data = cls._read_json(file_path)
        elif file_extension == "xml":
            data = cls._read_xml(file_path)
        else:
            raise ValueError("Formato de arquivo inválido")

        report_class = cls.REPORT_CLASSES.get(report_type)
        if not report_class:
            raise ValueError("Tipo de relatório inválido")

        report = report_class.generate(data)
        return report

    @staticmethod
    def _read_csv(file_path):
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        return data

    @staticmethod
    def _read_json(file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def _read_xml(file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []
        for item in root:
            row = {}
            for field in item:
                row[field.tag] = field.text
            data.append(row)
        return data

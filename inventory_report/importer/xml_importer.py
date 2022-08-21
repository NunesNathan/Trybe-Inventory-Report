from xml.etree import ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        with open(path) as file:
            root = ET.parse(file).getroot()
            return [XmlImporter._build_dict(child) for child in root]

    @staticmethod
    def _build_dict(child):
        return {grandchild.tag: grandchild.text for grandchild in child}

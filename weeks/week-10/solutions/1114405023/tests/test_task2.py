import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from task2_json_to_xml import build_xml_tree, read_json, write_xml


class TestTask2(unittest.TestCase):
    def sample_data(self):
        return {
            "來源": "113年新生資料庫",
            "總人數": 2,
            "學生清單": [
                {
                    "學號": "1131234001",
                    "系所名稱": "資訊工程系",
                    "畢業學校": "國立馬公高中",
                    "郵遞區號": "880",
                },
                {
                    "學號": "1131234002",
                    "系所名稱": "電機工程系",
                    "畢業學校": "國立澎湖海事",
                    "郵遞區號": "880",
                },
            ],
        }

    def test_root_tag_and_attrs(self):
        root = build_xml_tree(self.sample_data())

        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib["source"], "113年新生資料庫")
        self.assertEqual(root.attrib["total"], "2")

    def test_student_count_matches(self):
        root = build_xml_tree(self.sample_data())

        students = root.findall("student")

        self.assertEqual(len(students), 2)

    def test_student_attrs_exist(self):
        root = build_xml_tree(self.sample_data())

        for student in root.findall("student"):
            self.assertIn("id", student.attrib)
            self.assertIn("dept", student.attrib)
            self.assertIn("school", student.attrib)
            self.assertIn("zip", student.attrib)

    def test_empty_student_list(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 0,
            "學生清單": [],
        }

        root = build_xml_tree(data)

        self.assertEqual(root.attrib["total"], "0")
        self.assertEqual(len(root.findall("student")), 0)

    def test_xml_is_valid(self):
        root = build_xml_tree(self.sample_data())
        xml_bytes = ET.tostring(root, encoding="utf-8")

        parsed = ET.fromstring(xml_bytes)

        self.assertEqual(parsed.tag, "students")

    def test_write_xml_file_can_be_read_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            xml_path = Path(tmp) / "output" / "students.xml"

            write_xml(self.sample_data(), xml_path)
            parsed = ET.parse(xml_path).getroot()

            self.assertEqual(parsed.tag, "students")
            self.assertEqual(parsed.attrib["total"], "2")

    def test_read_json_rejects_non_object_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            json_path = Path(tmp) / "bad.json"
            json_path.write_text("[]", encoding="utf-8")

            with self.assertRaises(ValueError):
                read_json(json_path)


if __name__ == "__main__":
    unittest.main()

import json
import tempfile
import unittest
from pathlib import Path

from task1_csv_to_json import (
    build_output_data,
    count_by_dept,
    filter_by_admission,
    read_csv,
    write_json,
)


class TestTask1(unittest.TestCase):
    def test_filter_keeps_correct_rows(self):
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "資訊工程系"},
            {"入學方式": "繁星推甄", "系所名稱": "電機工程系"},
        ]

        result = filter_by_admission(rows, "聯合登記分發")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["入學方式"], "聯合登記分發")

    def test_filter_removes_others(self):
        rows = [
            {"入學方式": "聯合登記分發", "學號": "1130001"},
            {"入學方式": "個人申請", "學號": "1130002"},
            {"入學方式": "分科測驗", "學號": "1130003"},
        ]

        result = filter_by_admission(rows, "聯合登記分發")
        ids = [row["學號"] for row in result]

        self.assertEqual(ids, ["1130001"])
        self.assertNotIn("1130002", ids)
        self.assertNotIn("1130003", ids)

    def test_filter_empty_input(self):
        self.assertEqual(filter_by_admission([], "聯合登記分發"), [])

    def test_count_by_dept_correct(self):
        rows = [
            {"系所名稱": "資訊工程系"},
            {"系所名稱": "資訊工程系"},
            {"系所名稱": "電機工程系"},
        ]

        result = count_by_dept(rows)

        self.assertEqual(result["資訊工程系"], 2)
        self.assertEqual(result["電機工程系"], 1)

    def test_count_by_dept_empty(self):
        self.assertEqual(count_by_dept([]), {})

    def test_build_output_data_format(self):
        rows = [
            {
                "學號": "1131234001",
                "系所名稱": "資訊工程系",
                "入學方式": "聯合登記分發",
                "畢業學校": "國立馬公高中",
                "郵遞區號": "880",
            }
        ]

        data = build_output_data(rows, "聯合登記分發")

        self.assertEqual(data["來源"], "113年新生資料庫")
        self.assertEqual(data["總人數"], 1)
        self.assertEqual(data["系所統計"], {"資訊工程系": 1})
        self.assertEqual(data["學生清單"][0]["學號"], "1131234001")

    def test_read_csv_and_write_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            csv_path = tmp_path / "students.csv"
            json_path = tmp_path / "output" / "students.json"

            csv_path.write_text(
                "學號,系所名稱,入學方式,郵遞區號,畢業學校,前畢業科系\n"
                "1130001,資訊工程系,聯合登記分發,880,國立馬公高中,普通科\n",
                encoding="utf-8-sig",
            )

            rows = read_csv(csv_path)
            data = build_output_data(rows, "聯合登記分發")
            write_json(data, json_path)

            loaded = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(loaded["總人數"], 1)
            self.assertEqual(loaded["學生清單"][0]["系所名稱"], "資訊工程系")


if __name__ == "__main__":
    unittest.main()

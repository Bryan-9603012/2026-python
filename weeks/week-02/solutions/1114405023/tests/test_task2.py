import unittest
from task2_student_ranking import student_ranking


class TestStudentRanking(unittest.TestCase):

    def test_normal(self):
        students = [
            ("amy",88,20),
            ("bob",88,19),
            ("zoe",92,21),
            ("ian",88,19),
            ("leo",75,20),
            ("eva",92,20)
        ]

        result = student_ranking(students,3)

        self.assertEqual(result,[
            ("eva",92,20),
            ("zoe",92,21),
            ("bob",88,19)
        ])

    def test_k_limit(self):
        students = [("a",90,20),("b",80,21)]
        result = student_ranking(students,1)

        self.assertEqual(len(result),1)

    def test_tie_score(self):
        students = [
            ("a",90,21),
            ("b",90,20)
        ]

        result = student_ranking(students,2)

        self.assertEqual(result[0][0],"b")
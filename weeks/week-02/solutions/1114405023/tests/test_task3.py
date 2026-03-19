import unittest
from task3_log_summary import log_summary


class TestLogSummary(unittest.TestCase):

    def test_normal(self):

        records = [
            ("alice","login"),
            ("bob","login"),
            ("alice","view"),
            ("alice","logout"),
            ("bob","view"),
            ("bob","view"),
            ("chris","login"),
            ("bob","logout")
        ]

        users, top = log_summary(records)

        self.assertEqual(users[0],("bob",4))
        self.assertEqual(top,("login",3))

    def test_empty(self):
        users, top = log_summary([])

        self.assertEqual(users,[])
        self.assertEqual(top,None)

    def test_single_user(self):

        records = [
            ("alice","login"),
            ("alice","view")
        ]

        users, top = log_summary(records)

        self.assertEqual(users[0],("alice",2))
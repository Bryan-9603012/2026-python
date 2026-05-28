import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch

def url_print(host, domain):
    print(f'https://{host}.{domain}')

def parse_int(s):
    if not s:
        raise ValueError('空字串無法轉成整數')
    return int(s)

def fetch_user(api, user_id):
    return api.get(f'/users/{user_id}')

class TestStdout(unittest.TestCase):

    def test_url_print(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            url_print('www', 'example.com')
        self.assertEqual(buf.getvalue().strip(), 'https://www.example.com')

class TestPatch(unittest.TestCase):

    def test_fetch_user_with_mock(self):
        fake_api = MagicMock()
        fake_api.get.return_value = {'id': 1, 'name': 'Alice'}
        result = fetch_user(fake_api, 1)
        self.assertEqual(result['name'], 'Alice')
        fake_api.get.assert_called_once_with('/users/1')

    @patch('builtins.print')
    def test_url_print_via_patch(self, mock_print):
        url_print('api', 'example.com')
        mock_print.assert_called_once_with('https://api.example.com')

class TestExceptions(unittest.TestCase):

    def test_raises(self):
        with self.assertRaises(ValueError):
            parse_int('')

    def test_raises_with_message(self):
        with self.assertRaisesRegex(ValueError, '空字串'):
            parse_int('')

    def test_normal_case(self):
        self.assertEqual(parse_int('42'), 42)
if __name__ == '__main__':
    unittest.main()

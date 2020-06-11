from src.common import Common
import unittest


class DemoTest(unittest.TestCase):

    def setUp(self):
        self.host_url = r'http://127.0.0.1:12356'
        self.comm = Common(self.host_url)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_index(self):
        uri_index = '/'
        respanse_index_test = self.comm.get(uri_index)
        self.assertEqual(respanse_index_test.text, 'please input your username(your english name) and password(your english name)')

    def test_login(self):
        uri = r'/login'
        username = 'criss'
        password = 'criss'

        payload = 'username=' + username + '&password=' + password
        res_login = self.comm.post(uri, payload)
        self.assertEqual(res_login.text, 'please select One Equipment:\n10001:Knife\n10002:Big Sword\n10003:KuiHuaBaoDian')


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
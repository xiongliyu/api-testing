from src.common import Common
import unittest


class SampleTest(unittest.TestCase):
    def setUp(self):
        self.host_url = r'http://127.0.0.1:12356'
        self.comm = Common(self.host_url)


    def test_selectEq(self):
        uri_selectEq = r'/selectEq'
        equipmentid = '10003'
        payload_selectEq = 'equipmentid=' + equipmentid
        res_selectEq = self.comm.post(uri_selectEq, payload_selectEq)
        self.assertEqual(res_selectEq.text, '{"equipmentid": "10003", "Message": "your pick up equipmentid:10003 please select your  enemyid:\\n20001:Terran\\n20002:ORC\\n20003:Undead"}')

    def test_kill(self):
        equipmentid = '10003'
        enmyid = '20001'
        uri_kill = '/kill'
        payload_enmyid = 'enmyid=' + enmyid + '&equipmentid=' + equipmentid
        res_enmyid = self.comm.post(uri_kill, payload_enmyid)
        self.assertEqual(res_enmyid.text, 'Error 9904: Your kill yourself!!')


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
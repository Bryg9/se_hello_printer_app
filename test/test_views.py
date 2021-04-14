import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        strFirstPart1 = b'{"imie": "Brygida", '
        strSecondPart1 = b'"msg": "Hello World!"}'
        self.assertEqual(strFirstPart1 + strSecondPart1, rv.data)

    def test_msg_with_output2(self):
        rv = self.app.get('/?output=xml')
        strFirstPart2 = b'<greetings><name>Brygida</name> '
        '<msg>Hello World!</msg></greetings>'
        self.assertEqual(strFirstPart2, rv.data)

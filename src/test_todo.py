
from app import app
import unittest


class TodoTestCase(unittest.TestCase):
    def setUp(self):
        tester = app.test_client(self)
        self.tester = tester


    def test_get_list(self):
        response = self.tester.get('/tasks')

        self.assertEqual(response.status_code, 200)

    def test_content(self):
        data = {
            "title": "flask",
            "description": "lern flak"
        }
        response = self.tester.post('/tasks', json=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], data['title'])
        self.assertEqual(response.json['description'], data['description'])

    def test_get_by_id(self):
        id = 3
        response = self.tester.get(f'/tasks/{id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["id"], id)

    def test_put_by_id(self):
        id = 3
        data = {
            "title": "fastApi",
            "description": "lern fastApi"
        }
        response = self.tester.put(f'/tasks/{id}', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], data['title'])
        self.assertEqual(response.json['description'], data['description'])





if __name__ == '__main__':
    unittest.main()
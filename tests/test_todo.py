from src.factories import TodoFactory
# from apps.todo.models import Todo, db
from src.settings import test_user, test_host, test_database, test_password
from src.app import app, db
import unittest

class TestTodoCase(unittest.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{test_user}:{test_password}@{test_host}/{test_database}'


    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_list(self):
        task = TodoFactory.create_batch(5)
        response = self.app.get('/tasks')
        assert(response.status_code == 200)
        # assert('todos' in response.data)
        assert(len(response.data) == 5)
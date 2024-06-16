import unittest

from bson import ObjectId

from models.user import User
from services.database.repositories.user_repository import UserRepository
from services.implemented.auth_service import AuthService
from utils.auth import get_hashed_password


class UserRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository()
        self.auth_service = AuthService()
        self.user = User(_id=ObjectId("665a15efd8e36d760d1fbc96"), username="test", password=get_hashed_password("123"))
        self.user_update = User(_id=ObjectId("665a15efd8e36d760d1fbc96"), username="test",
                                password=get_hashed_password("121"))

    def test_register(self):
        self.assertIsNotNone(self.auth_service.register(self.user))

    def test_login(self):
        self.assertIsNotNone(self.auth_service.login("test", "123"))

    def test_update(self):
        self.assertIsNotNone(
            self.user_repository.update(str(self.user.id), self.user_update))

    def test_read(self):
        self.assertTrue(len(self.user_repository.get_all()) > 0)

    def test_delete(self):
        self.assertTrue(self.user_repository.delete(str(self.user.id)))


if __name__ == '__main__':
    unittest.main()

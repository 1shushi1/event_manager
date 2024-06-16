from bson import ObjectId

from models.user import User
from services.database.repositories.user_repository import UserRepository
from services.interfaces.auth_service import IAuthService
from utils.auth import check_password


class AuthService(IAuthService):

    def __init__(self):
        self.user_repository = UserRepository()

    def login(self, username: str, password: str) -> User or None:
        """
        Method to login
        :param username:
        :param password:
        :return:
        """
        user = self.user_repository.get_by_username(username)
        if user is not None:
            if check_password(password, user.password):
                return user
        return None

    def register(self, user: User) -> User or None:
        """
        Method to register
        :param user:
        :return:
        """
        if self.user_repository.get_by_username(user.username) is None:
            user_id: ObjectId = self.user_repository.create(user)
            if user_id is not None:
                return self.user_repository.get_by_id(str(user_id))
        else:
            return self.user_repository.get_by_username(user.username)

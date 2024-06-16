import abc

from models.user import User


class IAuthService(abc.ABC):

    @abc.abstractmethod
    def login(self, username: str, password: str) -> User or None:
        """
        Login a user
        :param username: str
        :param password: str
        :return: User or None
        """
    @abc.abstractmethod
    def register(self, user: User) -> User or None:
        """
        Register a user
        :param user: User
        :return: User or None
        """

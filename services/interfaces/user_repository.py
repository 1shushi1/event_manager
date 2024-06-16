from abc import ABC, abstractmethod
from typing import List

from bson import ObjectId

from models.user import User


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> ObjectId:
        """
        Creates a new user.
        :param user:
        :return: str or ObjectId
        """

    @abstractmethod
    def get_all(self) -> List[User]:
        """
        Gets all users.
        :return: List[User]
        """

    @abstractmethod
    def get_by_id(self, user_id: str or ObjectId) -> User:
        """
        Gets a user by id.
        :param user_id:
        :return: User
        """

    @abstractmethod
    def update(self, user_id: str or ObjectId, user: User) -> str or ObjectId:
        """
        Updates a user.
        :param user_id:
        :param user:
        :return: str or ObjectId
        """

    @abstractmethod
    def delete(self, user_id: str or ObjectId) -> bool:
        """
        Deletes a user.
        :param user_id:
        :return: str or ObjectId
        """

    @abstractmethod
    def get_by_username(self, username: str) -> User:
        """
        Gets a user by username.
        :param username:
        :return: User
        """

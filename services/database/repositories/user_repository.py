from abc import ABC
from typing import List

from bson import ObjectId
from pymongo.collection import Collection

from models.user import User
from services.database.client import database
from services.interfaces.user_repository import IUserRepository


class UserRepository(IUserRepository, ABC):
    users: Collection

    def __init__(self):
        self.users = database.users

    def create(self, user: User) -> ObjectId:
        """
        Create a new user
        :param user:
        :return:
        """

        insert_body = user.dict()
        if "id" in insert_body:
            if insert_body['id'] is not None:
                insert_body["_id"] = insert_body['id']
            del insert_body["id"]
        return self.users.insert_one(insert_body).inserted_id

    def get_all(self) -> List[User]:
        """
        Get all users
        :return:
        """
        return list(map(User.model_validate, self.users.find()))

    def get_by_id(self, user_id: str or ObjectId) -> User:
        """
        Get a user by id
        :param user_id:
        :return:
        """
        record = self.users.find_one({"_id": ObjectId(user_id)})
        return User.model_validate(record) if record is not None else None

    def update(self, user_id: str or ObjectId, user: User) -> ObjectId:
        """
        Update a user
        :param user_id:
        :param user:
        :return:
        """
        user_dict = user.dict()
        user_dict["_id"] = user.id
        del user_dict["id"]
        record = self.users.update_one({"_id": ObjectId(user_id)}, {"$set": user_dict}, upsert=True)
        if record.upserted_id is not None:
            return record.upserted_id
        else:
            return ObjectId(user_id)

    def delete(self, user_id: str or ObjectId) -> bool:
        """
        Delete a user
        :param user_id:
        :return:
        """
        return self.users.delete_one({"_id": ObjectId(user_id)}).deleted_count > 0

    def get_by_username(self, username: str) -> User:
        """
        Get a user by username
        :param username:
        :return:
        """
        record = self.users.find_one({"username": username})
        return User.model_validate(record) if record is not None else None

import abc
from typing import List

from bson import ObjectId

from models.event import Event


class IEventRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, event: Event) -> ObjectId:
        """
        Create a new event
        :param event:
        :return:
        """

    @abc.abstractmethod
    def get_by_id(self, event_id: str or ObjectId) -> Event:
        """
        Get an event by id
        :param event_id:
        :return:
        """

    @abc.abstractmethod
    def get_all(self) -> List[Event]:
        """
        Get all events
        :return:
        """


    @abc.abstractmethod
    def update(self, event_id: str, event: Event) -> ObjectId:
        """
        Update an event
        :param event_id:
        :param event:
        :return:
        """

    @abc.abstractmethod
    def delete(self, event_id: str or ObjectId) -> bool:
        """
        Delete an event
        :param event_id:
        :return:
        """

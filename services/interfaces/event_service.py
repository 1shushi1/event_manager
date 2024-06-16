import abc
from typing import List

from bson import ObjectId

from models.event import Event


class IEventService(abc.ABC):

    @abc.abstractmethod
    def create(self, event: Event) -> ObjectId:
        """
        Create a new event
        :param event:
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
    def read(self) -> List[Event]:
        """
        Get all events
        :return: List of events
        """
    @abc.abstractmethod
    def delete(self, event_id: str) -> bool:
        """
        Delete an event
        :param event_id:
        :return:
        """

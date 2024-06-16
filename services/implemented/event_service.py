from typing import List

from bson import ObjectId

from models.event import Event
from services.database.repositories.event_repository import EventRepository
from services.interfaces.event_service import IEventService


class EventService(IEventService):
    event_repository = EventRepository()

    def create(self, event: Event) -> ObjectId:
        """
        Create a new event
        :param event:
        :return:
        """
        return self.event_repository.create(event)

    def update(self, event_id: str, event: Event) -> ObjectId:
        """
        Update an event
        :param event_id:
        :param event:
        :return:
        """
        return self.event_repository.update(event_id, event)

    def read(self) -> List[Event]:
        """
        Get all events
        :return: List of events
        """
        return self.event_repository.get_all()

    def delete(self, event_id: str) -> bool:
        """
        Delete an event
        :param event_id:
        :return:
        """
        return self.event_repository.delete(event_id)

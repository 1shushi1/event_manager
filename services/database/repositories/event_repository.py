from abc import ABC
from typing import List

from bson import ObjectId
from pymongo.collection import Collection
from pymongo.results import InsertOneResult

from models.event import Event
from services.database.client import database
from services.interfaces.event_repository import IEventRepository


class EventRepository(IEventRepository, ABC):
    events: Collection

    def __init__(self):
        self.events = database.events

    def create(self, event: Event) -> ObjectId:
        """
        Create event in database
        :param event:
        :return:
        """
        insert_body = event.dict()
        if "id" in insert_body:
            if insert_body['id'] is not None:
                insert_body["_id"] = insert_body['id']
            del insert_body["id"]
        inserted: InsertOneResult = self.events.insert_one(insert_body)
        return inserted.inserted_id

    def get_by_id(self, event_id: str or ObjectId) -> Event:
        """
        Get an event by id
        :param event_id:
        :return:
        """
        return Event.model_validate(self.events.find_one({"_id": ObjectId(event_id)}))

    def get_all(self) -> List[Event]:
        """
        Get all events
        :return:
        """
        return list(map(Event.model_validate, self.events.find()))

    def update(self, event_id: str, event: Event) -> ObjectId:
        """
        Update an event
        :param event_id:
        :param event:
        :return:
        """
        update_dict = event.dict()
        update_dict["_id"] = ObjectId(event_id)
        del update_dict["id"]
        record = self.events.update_one({"_id": ObjectId(event_id)}, {"$set": update_dict}, upsert=True)
        if record.upserted_id is not None:
            return record.upserted_id
        else:
            return ObjectId(event_id)

    def delete(self, event_id: str or ObjectId) -> bool:
        """
        Delete an event
        :param event_id:
        :return:
        """
        return self.events.delete_one({"_id": ObjectId(event_id)}).deleted_count > 0

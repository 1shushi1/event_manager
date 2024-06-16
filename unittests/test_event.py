import unittest

from bson import ObjectId

from models.event import Event
from services.database.repositories.event_repository import EventRepository


class EventRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.event_repository = EventRepository()
        self.event = Event(_id=ObjectId("665a10951e826db434aaaf5b"), name="Test Event", date="2024-10-16",
                           description="Empty", organizator=None)
        self.event_update = Event(_id=ObjectId("665a10951e826db434aaaf5b"), name="Test Event Updated",
                                  date="2024-10-16", description="Empty", organizator=None)
        self.event_id: ObjectId = ObjectId("665a10951e826db434aaaf5b")

    def test_create(self):
        self.event_id = self.event_repository.create(event=self.event)
        self.event = self.event.model_copy(update={"_id": self.event_id})
        self.assertTrue(self.event_id is not None)

    def test_get_all(self):
        self.assertTrue(len(self.event_repository.get_all()) > 0)

    def test_get_by_id(self):
        self.assertIsNotNone(self.event_repository.get_by_id(str(self.event_id)))

    def test_update(self):
        self.assertIsNotNone(self.event_repository.update(str(self.event_id), self.event_update))

    def test_delete(self):
        self.assertTrue(self.event_repository.delete(str(self.event_id)))


if __name__ == '__main__':
    unittest.main()

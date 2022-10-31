from abc import ABC
from typing import Type

from bson import ObjectId, DBRef
from pymongo import MongoClient

from models.abstract import AbstractModel, ElementDoesNotExist

MONGO_STRING_CONNECTION = "mongodb+srv://samuel:samuel@cluster0.qsk8qkx.mongodb.net/?retryWrites=true&w=majority"
DATABASE = "g28database"

class AbstractRepository(ABC):
    def __init__(self, model: Type[AbstractModel], does_not_exist: Type[ElementDoesNotExist]):
        self._client = MongoClient(MONGO_STRING_CONNECTION)
        self.database = self._client.get_database(DATABASE)
        self.collection = self.database.get_collection(model.COLLECTION)
        self.model = model
        self.does_not_exist = does_not_exist

    def create(self, element: AbstractModel):
        if element.is_new():
            inserted = self.collection.insert_one(
                element.prepare_to_save()
            )
            element._id = str(inserted.inserted_id)
        else:
            self.collection.update_one({
                "_id": ObjectId(element._id)
            }, {
                "$set": element.prepare_to_save()
            })
        return element

    def delete(self, element: AbstractModel):
        response = self.collection.delete_one({
            "_id": ObjectId(element._id)
        })
        return {
            "deleted_count": response.deleted_count
        }

    def get_all(self):
        elements = []
        for element in self.collection.find():
            self._fill_db_ref(element)
            elements.append(self.model.create(element))
        return elements

    def get_by_id(self, id_item):
        element = self.collection.find_one({
            "_id": ObjectId(id_item)
        })
        if not element:
            raise self.does_not_exist
        self._fill_db_ref(element)
        return self.model.create(element)

    def count(self):
        return self.collection.count_documents({})

    def _fill_db_ref(self, document):
        for key, value in document.items():
            if value and isinstance(value, DBRef):
                collection = self.database.get_collection(value.collection)
                related = collection.find_one({
                    "_id": value.id
                })
                document[key] = related
                if related and isinstance(related, dict):
                    self._fill_db_ref(related)

    def find_by_query(self, query):
        elements = []
        for element in self.collection.find(query):
            self._fill_db_ref(element)
            elements.append(self.model.create(element))
        return elements


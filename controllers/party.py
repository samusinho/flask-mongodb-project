from pyexpat import model

from controllers.abstract import AbstractController
from models.party import Party, PartyDoesNotExist
from repositories.party import PartyRepository

class PartyController(AbstractController):
    def __init__(self):
        self.repository = PartyRepository(
            model= Party,
            does_not_exist= PartyDoesNotExist
        )

    def get_all(self):
        return self.repository.get_all();

    def get_by_id(self, party_id):
        return self.repository.get_by_id(party_id)

    def create(self, content):
        created = Party(
            name=content["name"]
        )
        return self.repository.create(created)

    def update(self, id_item, content):
        pass

    def delete(self, id_item):
        pass

    def count(self):
        return self.repository.count();


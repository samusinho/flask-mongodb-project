from controllers.abstract import AbstractController
from models.party import Party, PartyDoesNotExist
from models.candidate import Candidate, CandidateDoesNotExist
from repositories.candidate import CandidateRepository
from repositories.party import PartyRepository

class CandidateController(AbstractController):
    def __init__(self):
        self.repository = CandidateRepository(
            model=Candidate,
            does_not_exist=CandidateDoesNotExist
        )
        self.partyRepository = PartyRepository(
            model=Party,
            does_not_exist=PartyDoesNotExist
        )

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, candidate_id):
        return self.repository.get_by_id(candidate_id)

    def create(self, content):
        party_object = content.get("party")
        party = self.partyRepository.get_by_id(party_object.get("id"))
        return self.repository.create(
            element= Candidate(
                name=content["name"],
                identification=content["identification"],
                party=party.to_json()
            )
        )

    def update(self, id_item, content):
        pass

    def delete(self, id_item):
        pass

    def count(self):
        return self.repository.count()
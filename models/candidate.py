from models.abstract import AbstractModel, ElementDoesNotExist
from models.party import Party
from bson import DBRef, ObjectId


class Candidate(AbstractModel):
    COLLECTION = "candidates"

    name = None
    identification = None
    party: Party = None

    def __init__(
            self,
            name,
            identification,
            party = None,
            _id = None
    ):
        super().__init__(_id)
        self.name = name
        self.identification = identification
        self.party = party

    def prepare_to_save(self):
        party_db_ref = None
        if self.party:
            party_db_ref = DBRef(
                id=ObjectId(self.party["_id"]),
                collection=Party.COLLECTION
            )
        return {
            "name": self.name,
            "identification": self.identification,
            "party": party_db_ref
        }

    def to_json(self):
        party = None
        if self.party:
            party = self.party.to_json()
        return {
            "_id": self._id,
            "name": self.name,
            "identification": self.identification,
            "party": party
        }

    @staticmethod
    def create(content):
        party = None
        if (content.get("party")):
            party = Party.create(content.get("party"))
        return Candidate(
            name=content["name"],
            identification=content["identification"],
            party=party,
            _id=str(content["_id"]) if content.get("_id") else None
        )


class CandidateDoesNotExist(ElementDoesNotExist):
    pass
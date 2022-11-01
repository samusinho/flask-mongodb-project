from models.abstract import AbstractModel, ElementDoesNotExist

from bson import DBRef, ObjectId
from models.station import Station
from models.candidate import Candidate


class Vote(AbstractModel):
    COLLECTION = "votes"

    user_id = None
    station: Station = None
    candidate: Candidate = None

    def __init__(
            self,
            user_id,
            station = None,
            candidate = None,
            _id = None
    ):
        super().__init__(_id)
        self.user_id = user_id
        self.station = station
        self.candidate = candidate

    def prepare_to_save(self):
        return {
            "station": DBRef(
                id=ObjectId(self.station["_id"]),
                collection=Station.COLLECTION
            ),
            "candidate": DBRef(
                id=ObjectId(self.candidate["_id"]),
                collection=Candidate.COLLECTION
            ),
            "user_id": self.user_id
        }

    def to_json(self):
        station = None
        candidate = None
        if self.station:
            station = self.station.to_json()
        if self.candidate:
            candidate = self.candidate.to_json()
        return {
            "_id": self._id,
            "user_id": self.user_id,
            "candidate": candidate,
            "station": station
        }

    @staticmethod
    def create(content):
        assert content.get("candidate")
        assert content.get("station")
        station = Station.create(content.get('station'))
        candidate = Candidate.create(content.get('candidate'))
        return Vote(
            user_id=content.get("user_id"),
            candidate=candidate,
            station=station,
            _id=str(content["_id"]) if content.get("_id") else None
        )


class VoteDoesNotExist(ElementDoesNotExist):
    pass
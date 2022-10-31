from controllers.abstract import AbstractController
from models.vote import Vote, VoteDoesNotExist
from models.candidate import Candidate, CandidateDoesNotExist
from models.station import Station, StationDoesNotExist
from repositories.vote import VoteRepository
from repositories.candidate import CandidateRepository
from repositories.station import StationRepository

class VoteController(AbstractController):
    def __init__(self):
        self.repository = VoteRepository(
            model=Vote,
            does_not_exist=VoteDoesNotExist
        )
        self.candidateRepository = CandidateRepository(
            model=Candidate,
            does_not_exist=CandidateDoesNotExist
        )
        self.stationRepository = StationRepository(
            model=Station,
            does_not_exist=StationDoesNotExist
        )

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, vote_id):
        return self.repository.get_by_id(vote_id)

    def create(self, content):
        station_object = content.get("station", {})
        candidate_object = content.get("candidate", {})
        station = self.stationRepository.get_by_id(station_object.get("id"))
        candidate = self.candidateRepository.get_by_id(candidate_object.get("id"))
        return self.repository.create(
            element=Vote(
                user_id=content["user_id"],
                station=station.to_json(),
                candidate=candidate.to_json()
            )
        )

    def update(self, id_item, content):
        pass

    def delete(self, id_item):
        pass

    def count(self):
        return self.repository.count()
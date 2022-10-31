from controllers.abstract import AbstractController
from models.station import Station, StationDoesNotExist
from repositories.station import StationRepository

class StationController(AbstractController):
    def __init__(self):
        self.repository = StationRepository(
            model= Station,
            does_not_exist= StationDoesNotExist
        )

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, station_id):
        return self.repository.get_by_id(station_id)

    def create(self, content):
        created = Station(
            name=content["name"],
            number=content["number"],
            location=content["location"],
            users=content["users"]
        )
        return self.repository.create(created)

    def update(self, station_id, content):
        station = self.get_by_id(station_id)
        if content["name"]:
            station.name = content["name"]
        if content["number"]:
            station.number = content["number"]
        if content["location"]:
            station.location = content["location"]
        if content["users"]:
            station.users = content["users"]
        return self.repository.create(station)

    def delete(self, station_id):
        station = self.get_by_id(station_id)
        return self.repository.delete(station)

    def count(self):
        return self.repository.count()



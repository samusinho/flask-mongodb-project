from models.abstract import AbstractModel, ElementDoesNotExist

class Station(AbstractModel):
    COLLECTION = "stations"

    name = None
    number = None
    location = None
    users = []

    def __init__(
            self,
            name,
            number,
            location,
            users,
            _id=None
    ):
        super().__init__(_id)
        self.name = name
        self.number = number
        self.location = location
        self.users = users

    def prepare_to_save(self):
        return {
            "name": self.name,
            "number": self.number,
            "location": self.location,
            "users": self.users
        }

    def to_json(self):
        return self.__dict__

    @staticmethod
    def create(content):
        return Station(
            name=content["name"],
            number=content["number"],
            location=content["location"],
            users=content["users"],
            _id=str(content["_id"]) if content.get("_id") else None
        )


class StationDoesNotExist(ElementDoesNotExist):
    pass
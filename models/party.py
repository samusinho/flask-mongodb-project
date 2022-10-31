from models.abstract import AbstractModel, ElementDoesNotExist

class Party(AbstractModel):
    COLLECTION = "parties"

    name = None

    def __init__(
            self,
            name,
            _id=None
    ):
        super().__init__(_id)
        self.name = name

    def prepare_to_save(self):
        return {
            "name": self.name
        }

    def to_json(self):
        return self.__dict__

    @staticmethod
    def create(content):
        return Party(
            name=content["name"],
            _id=str(content["_id"]) if content.get("_id") else None
        )

class PartyDoesNotExist(ElementDoesNotExist):
    pass
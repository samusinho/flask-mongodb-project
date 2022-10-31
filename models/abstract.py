from abc import ABCMeta, abstractmethod

class AbstractModel(metaclass=ABCMeta):
    _id = None
    COLLECTION = ""

    def __init__(self, _id=None):
        self._id = _id

    def is_new(self) -> bool:
        return not self._id

    @abstractmethod
    def prepare_to_save(self):
        raise NotImplemented

    @abstractmethod
    def to_json(self):
        raise NotImplemented

    @staticmethod
    def create(content):
        raise NotImplemented


class ElementDoesNotExist(Exception):
    pass

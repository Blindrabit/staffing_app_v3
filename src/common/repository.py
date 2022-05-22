import abc


class AbstractUnitOfWork(abc.ABC):
    def __init__(self):
        self.seen = set()

    @abc.abstractmethod
    def add(self):
        raise NotImplemented

    @abc.abstractmethod
    def get(self):
        raise NotImplemented

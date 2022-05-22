import abc

from src.api.users import repository


class AbstractUserUnitOfWork(abc.ABC):
    users: repository.AbstractUserRepository

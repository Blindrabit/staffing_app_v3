import abc
from uuid import UUID

from src.api.users.domain import User


class AbstractUserRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    def add(self, user: User):
        self._add(user)
        self.seen.add(user)

    def get(self, user_id: UUID) -> User:
        user = self._get(user_id)
        if user:
            self.seen.add(user)
        return user

    @abc.abstractmethod
    def _add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, user_uuid: UUID) -> User:
        raise NotImplementedError


class UserSqlAlchemyRepository(AbstractUserRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, user: User):
        self.session.add(user)

    def _get(self, user_uuid: UUID) -> User:
        return self.session.query(User).filter_by(uuid=user_uuid).first()

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, engine
from sqlalchemy.orm import mapper, sessionmaker

from core import config
from source.databases.abstractions.User import User


class InternalDB:
    def __init__(self) -> None:
        self._engine: engine = create_engine(f'sqlite:///{config.get("db_name", "zalgo.db")}', echo=False)
        self._session = sessionmaker(bind=self._engine)()

    def create(self) -> None:
        metadata: MetaData = MetaData()
        data: Table = Table('data', metadata,
                            Column('id', Integer, primary_key=True, autoincrement=True),
                            Column('user_id', Integer),
                            Column('current_mode', String, default='zalgo'),
                            Column('messages_count', Integer, default=0),
                            Column('status', String, nullable=True),
                            Column('subtype', String, default='Базовая'),
                            Column('token', String, nullable=True),
                            Column('language', String, default='ru')
                            )
        metadata.create_all(self._engine)
        mapper(User, data)

    def set_language(self, language: str) -> None:
        raise NotImplementedError

    def add_user(self, user_id: int) -> None:
        if self.user_exists(user_id):
            return
        self._session.add(User(user_id=user_id))
        self._session.commit()

    def get_user(self, user_id: int) -> dict:
        for user in self._session.query(User).filter_by(user_id=user_id):
            return dict(user)

    def messages_increment(self, user_id: int) -> None:
        for user in self._session.query(User).filter_by(user_id=user_id):
            user.messages_count += 1
        self._session.commit()

    def status_changer(self, user_id: int, status) -> None:
        for user in self._session.query(User).filter_by(user_id=user_id):
            user.status = status
        self._session.commit()

    def mode_changer(self, user_id: int, mode: str) -> None:
        for user in self._session.query(User).filter_by(user_id=user_id):
            user.current_mode = mode
        self._session.commit()

    def status_cleaner_emergency(self) -> None:
        for user in self._session.query(User):
            user.status = None
        self._session.commit()

    def update_token(self, user_id: int, token) -> None:
        for user in self._session.query(User).filter_by(user_id=user_id):
            user.token = token
        self._session.commit()

    def user_exists(self, user_id: int) -> bool:
        return bool([user for user in self._session.query(User).filter_by(user_id=user_id)])

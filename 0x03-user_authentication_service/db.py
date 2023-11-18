#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError, NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): User's email.
            hashed_password (str): Hashed password.

        Returns:
            User: Created User object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        self._session.refresh(new_user)
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database based on input arguments.

        Args:
            **kwargs: Arbitrary keyword arguments for filtering.

        Returns:
            User: Found User object.

        Raises:
            NoResultFound: If no results are found.
            InvalidRequestError: If wrong query arguments are passed.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("No user found with the specified criteria.")
        except InvalidRequestError as e:
            raise InvalidRequestError(f"Invalid request: {e}")
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes based on input arguments.

        Args:
            user_id (int): User ID to locate the user to update.
            **kwargs: Arbitrary keyword arguments for updating user attributes.

        Raises:
            ValueError: If an invalid argument is passed.
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError(f"Invalid arguement: {key}")
                self._session.commit()
        except NoResultFound:
            raise NoResultFound(f"No user found with ID {user_id}")

        return None

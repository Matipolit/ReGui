from enum import Enum


class AppState(Enum):
    LOGIN = 1
    LOGGED_IN = 2


class LoggedInState(Enum):
    PAGE = 1
    POST = 2

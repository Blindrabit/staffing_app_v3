from dataclasses import dataclass


@dataclass
class AddUser:
    username: str
    email: str
    first_name: str
    last_name: str
    password: str

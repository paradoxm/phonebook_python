from typing import TypedDict, List


class Contact(TypedDict):
    id: str
    last_name: str
    first_name: str


class PhoneNumber(TypedDict):
    id: int
    contact_id: str
    number: str


class Store(TypedDict):
    contacts: List[Contact]
    phone_numbers: List[PhoneNumber]

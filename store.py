import json
import os

from phonebook_types import Store

STORE_CACHE_KEY = "phonebook_store"
STORE_PATH = "store.json"

EMPTY_STORE: Store = {
    "contacts": [],
    "phone_numbers": []
}


def _read_data_from_file() -> Store:
    try:
        with open(STORE_PATH, "r") as f:
            return json.loads(f.read())
    except Exception:
        return EMPTY_STORE


def _write_data_to_file(value: Store) -> None:
    with open(STORE_PATH, "w") as f:
        f.write(json.dumps(value))


def _create_store_if_not_exist() -> None:
    if not os.path.exists(STORE_PATH):
        file = open(STORE_PATH, "w")
        file.write(json.dumps(EMPTY_STORE))
        file.close()


def get_store_value() -> Store:
    _create_store_if_not_exist()
    return _read_data_from_file()


def set_store_value(value: Store) -> None:
    _write_data_to_file(value)

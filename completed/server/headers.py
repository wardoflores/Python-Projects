import typing

from collections import defaultdict

class Headers:
    def __init__(self) -> None:
        self._headers = defaultdict(list)

    def add(self, name: str, value: str) -> None:
        self._headers[name.lower()].append(value)

    def get_all(self, name: str) -> typing.List[str]:
        return self._headers[name.lower()]

    def get(self, name: str, default: typing.Optional[str] = None) -> typing.Optional[str]:
        try:
            return self.get_all(name)[-1]
        except IndexError:
            return default

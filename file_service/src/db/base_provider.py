from abc import ABC, abstractmethod

from src.models.file_model import FileDbModel


class BaseProvider(ABC):
    @abstractmethod
    async def add(self, file: FileDbModel) -> None:
        pass

    @abstractmethod
    async def find_by_shortname(self, short_name: str) -> FileDbModel | None:
        pass

    @abstractmethod
    async def delete(self, file: FileDbModel) -> None:
        pass

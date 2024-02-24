from abc import ABC, abstractmethod
from pydantic import BaseModel


class AbstractItemService(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> BaseModel:
        pass

    @abstractmethod
    def create(self, data: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def update(self, data: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[BaseModel]:
        pass

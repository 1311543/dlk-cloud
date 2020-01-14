from abc import ABC, abstractmethod
from typing import Any
from typing import Iterable
from typing import Type

from dlk_cloud.repository.\
    s3_sesion_repository import AwsServiceSessionRepository
from dlk_cloud.repository.\
    s3_sesion_repository import S3Boto3SessionRepository


class S3Repository(ABC):
    @abstractmethod
    def add(self,
            s3_session: Type[AwsServiceSessionRepository],
            bucket_name) -> None:
        """Add method to be implemented."""
        pass

    @abstractmethod
    def get(self,
            s3_session: Type[AwsServiceSessionRepository],
            bucket_name) -> None:
        """Add method to be implemented."""
        pass

    @abstractmethod
    def update(self,
               s3_session: Type[AwsServiceSessionRepository],
               bucket_name) -> None:
        """Add method to be implemented."""
        pass

    @abstractmethod
    def delete(self,
               s3_session: Type[AwsServiceSessionRepository],
               bucket_name) -> None:
        """Add method to be implemented."""
        pass


# logica de negocio aplicado al servicio
class S3TaskRepository(S3Repository):
    def __init__(self) -> None:
        self.tasks = {}
        self.sequence = 1

    def get(self,
            s3_session: S3Boto3SessionRepository,
            bucket_name) -> Iterable[Any]:
        return s3_session \
            .getSession() \
            .list_objects(Bucket=bucket_name)['Contents']

    def update(self,
               s3_session: S3Boto3SessionRepository,
               bucket_name) -> None:
        pass

    def delete(self,
               s3_session: S3Boto3SessionRepository,
               bucket_name) -> None:
        pass

    def add(self,
            s3_session: S3Boto3SessionRepository,
            bucket_name) -> None:
        pass

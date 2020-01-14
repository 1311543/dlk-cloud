from abc import ABC, abstractmethod
from typing import Type

import boto3
import botocore.session
from botocore.client import BaseClient

from dlk_cloud.domain.s3 import S3


class AwsServiceSessionRepository(ABC):
    @abstractmethod
    def getSession(self) -> None:
        """Add method to be implemented."""
        pass


class S3Boto3SessionRepository(AwsServiceSessionRepository):
    def __init__(self) -> None:
        pass

    def getSession(self) -> Type[BaseClient]:
        try:
            return boto3.client(S3().getService())
        except Exception as e:
            print('\n\n>>>Error while instantiating'
                  ' s3 manager: {}'.format(e.message))


class S3BotocoreSessionRepositoryAws(AwsServiceSessionRepository):
    def __init__(self) -> None:
        session = botocore.session.get_session()
        self.s3 = session.create_client('s3',
                                        region_name='us-west-2')

    def getSession(self) -> Type[BaseClient]:
        try:
            return self.s3
        except Exception as e:
            print('\n\n>>>Error while instantiating'
                  ' s3 manager: {}'.format(e.message))

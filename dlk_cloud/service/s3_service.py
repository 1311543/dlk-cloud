from dlk_cloud.repository.\
    s3_repository import S3Repository
from dlk_cloud.repository.\
    s3_sesion_repository import S3Boto3SessionRepository
from dlk_cloud.repository.\
    s3_sesion_repository import AwsServiceSessionRepository
from typing import Type
from botocore.client import BaseClient


class S3Service:
    """ Casos de Uso
    * In this class we are using Inversión de dependencias
    * Dependency inversion
    """
    def __init__(self,
                 s3_repository: Type[S3Repository]):
        self.s3_repository = s3_repository
        self.s3_session = S3Boto3SessionRepository()

    def list_bucket_content(self, bucket_name):
        return self.s3_repository\
            .get(self.s3_session, bucket_name=bucket_name)


class ServiceAwsSession:
    def __init__(self,
                 aws_session: Type[AwsServiceSessionRepository]):
        self.session = aws_session

    def getSession(self) -> Type[BaseClient]:
        return self.session.getSession()

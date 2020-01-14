# no Business logic
from dlk_cloud.domain.service import Service


class S3(Service):
    def __init__(self):
        self.s3_client = "s3"

    def getService(self) -> str:
        return self.s3_client

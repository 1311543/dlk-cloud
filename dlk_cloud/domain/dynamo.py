from dlk_cloud.domain.service import Service


class DynamoManager(Service):
    def __init__(self):
        self.client = "dynamodb"

    def getService(self) -> str:
        return self.client

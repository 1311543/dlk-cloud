import unittest

from dlk_cloud.domain.s3 import S3
from dlk_cloud.domain.dynamo import DynamoManager


class TestDomain(unittest.TestCase):

    def test_s3_domain(self):
        self.assertEqual('s3', S3().getService())

    def test_s3_domain(self):
        self.assertEqual('dynamodb', DynamoManager().getService())

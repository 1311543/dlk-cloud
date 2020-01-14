import datetime
import logging
import os
import pickle
import zipfile
from urllib.parse import urlparse

from dlk_cloud.repository.s3_repository import S3TaskRepository
from dlk_cloud.repository.s3_sesion_repository import S3Boto3SessionRepository
from dlk_cloud.service.s3_service import S3Service
from dlk_cloud.service.s3_service import ServiceAwsSession

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler("logfile", mode='w')
formatter = logging.Formatter("%(asctime)s - %(message)s")
log.addHandler(fh)
log.info("Loaded S3 functions Belcorp Library")


# noinspection PyTypeChecker
class S3functions:
    def __init__(self):
        self.s3_client = ServiceAwsSession(S3Boto3SessionRepository)

    @classmethod
    def list_bucket_content(cls, bucket_name):
        for key in S3Service(S3TaskRepository()) \
                .list_bucket_content(bucket_name):
            print(key['Key'])

    def get_last_modified_time(self, bucket_name, key_name):
        s3_obj = self.s3_client.getSession() \
            .get_object(Bucket=bucket_name, Key=key_name)
        return s3_obj['LastModified']

    def get_count_of_object(self, bucket_name, key_name):
        self.s3_client.getSession() \
            .list_objects_v2(Bucket=bucket_name, Prefix=key_name)
        return list['KeyCount']

    def download_from_bucket(self,
                             list_files,
                             local_folder_path,
                             s3_remote_path):
        op = urlparse(s3_remote_path)
        s3_bucket = op.netloc
        remote_folder = op.path

        print("s3 bucket: ".format(s3_bucket))
        print("remote folder: ".format(remote_folder))

        try:
            for filename in list_files:
                remote_file = remote_folder + filename
                local_file = os.path.join(local_folder_path,
                                          filename)
                log_msg = 'Downloading {} from S3 bucket: {}'
                print(log_msg.format(local_file,
                                     remote_file))
                self.s3_client.getSession()\
                    .download_file(s3_bucket,
                                   remote_file,
                                   local_file)
            print('success')
        except Exception as e:
            print('exception: {}'.format(e))

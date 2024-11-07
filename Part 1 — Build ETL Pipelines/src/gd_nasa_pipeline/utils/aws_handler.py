import logging
from io import BytesIO

import boto3
import netCDF4
from botocore.handlers import disable_signing


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

BUCKET_NAME = 'power-datastore'
resource = boto3.resource('s3', region_name='us-west-2')

resource.meta.client.meta.events.register(
    'choose-signer.s3.*', disable_signing)


class S3Handler:

    def get_all_files_from_s3(self) -> list:
        """Get all file names from AWS S3."""
        prefix = 'v9/'
        objects = []
        bucket = resource.Bucket(BUCKET_NAME)
        for s3_object in bucket.objects.filter(Prefix=prefix):
            objects.append(s3_object.key)
        logger.info("Objects are: %s", objects)
        return objects

    def get_files_from_s3(self, prefix: str) -> list:
        """Get file names from AWS S3."""
        objects = []
        bucket = resource.Bucket(BUCKET_NAME)
        for s3_object in bucket.objects.filter(Prefix=prefix):
            objects.append(s3_object.key)
        logger.info("Objects are: %s", objects)
        return objects

    def get_daily_files_from_s3(
            self,
            year: int = 2024) -> list:
        """Get daily file names from AWS S3."""
        prefix = f'v9/daily/{year}'
        return self.get_files_from_s3(prefix)

    def get_climatology_files_from_s3(self) -> list:
        """Get climatology file names from AWS S3."""
        prefix = 'v9/climatology/'
        return self.get_files_from_s3(prefix)

    def read_nc_file(self, file_name: str) -> netCDF4.Dataset:
        """Read NetCDF file content from AWS without
        downloading it to a local file."""
        s3_client = resource.meta.client

        # Download the file content into a BytesIO object
        file_content = BytesIO()
        s3_client.download_fileobj(BUCKET_NAME, file_name, file_content)

        # Reset the file-like object position to the beginning
        file_content.seek(0)

        # Read the NetCDF file from the in-memory object
        nc_file = netCDF4.Dataset('dummy.nc', memory=file_content.read())
        logger.info("File content: %s", nc_file)
        return nc_file

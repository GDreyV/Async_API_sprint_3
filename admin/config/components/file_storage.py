import os

FILE_STORAGE_URL = os.environ.get("DJANGO_S3_URL")
FILE_STORAGE_BUCKET = os.environ.get("DJANGO_S3_BUCKET")

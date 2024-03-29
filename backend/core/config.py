import os


COUCHBASE_HOST = os.getenv('COUCHBASE_HOST')
COUCHBASE_PORT = os.getenv('COUCHBASE_PORT')
COUCHBASE_FULL_TEXT_PORT = os.getenv('COUCHBASE_FULL_TEXT_PORT')

COUCHBASE_MEMORY_QUOTA_MB = os.getenv('COUCHBASE_MEMORY_QUOTA_MB')
COUCHBASE_INDEX_MEMORY_QUOTA_MB = os.getenv('COUCHBASE_INDEX_MEMORY_QUOTA_MB')
COUCHBASE_FTS_MEMORY_QUOTA_MB = os.getenv('COUCHBASE_FTS_MEMORY_QUOTA_MB')
COUCHBASE_OPERATION_TIMEOUT_SECS = 10
COUCHBASE_N1QL_TIMEOUT_SECS = 10

COUCHBASE_USER = os.getenv('CLUSTER_USERNAME')
COUCHBASE_PASSWORD = os.getenv('CLUSTER_PASSWORD')

COUCHBASE_DEFAULT_DATASET = 'test'


COUCHBASE_IP = os.getenv('COUCHBASE_IP')
LOCAL_IP = os.getenv('LOCAL_IP')
AUTH_IP = os.getenv('AUTH_IP')


# DB Data
INT_COUNTER_NAME = 'id_counter'
PRODUCTS_BUCKET = 'product'
BRANDS_BUCKET = 'brand'
TAGS_BUCKET = 'tag'
ATTRIBUTE_BUCKET = 'attribute'
BUCKETS = [PRODUCTS_BUCKET, BRANDS_BUCKET, TAGS_BUCKET, ATTRIBUTE_BUCKET]

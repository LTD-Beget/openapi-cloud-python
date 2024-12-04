import typing_extensions

from beget_openapi_cloud.apis.tags import TagValues
from beget_openapi_cloud.apis.tags.cloud_service_api import CloudServiceApi
from beget_openapi_cloud.apis.tags.mysql_backup_service_api import MysqlBackupServiceApi
from beget_openapi_cloud.apis.tags.mysql_service_api import MysqlServiceApi
from beget_openapi_cloud.apis.tags.mysql_statistic_service_api import MysqlStatisticServiceApi
from beget_openapi_cloud.apis.tags.postgresql_backup_service_api import PostgresqlBackupServiceApi
from beget_openapi_cloud.apis.tags.postgresql_service_api import PostgresqlServiceApi
from beget_openapi_cloud.apis.tags.postgresql_statistic_service_api import PostgresqlStatisticServiceApi
from beget_openapi_cloud.apis.tags.s3_service_api import S3ServiceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CLOUD_SERVICE: CloudServiceApi,
        TagValues.MYSQL_BACKUP_SERVICE: MysqlBackupServiceApi,
        TagValues.MYSQL_SERVICE: MysqlServiceApi,
        TagValues.MYSQL_STATISTIC_SERVICE: MysqlStatisticServiceApi,
        TagValues.POSTGRESQL_BACKUP_SERVICE: PostgresqlBackupServiceApi,
        TagValues.POSTGRESQL_SERVICE: PostgresqlServiceApi,
        TagValues.POSTGRESQL_STATISTIC_SERVICE: PostgresqlStatisticServiceApi,
        TagValues.S3SERVICE: S3ServiceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CLOUD_SERVICE: CloudServiceApi,
        TagValues.MYSQL_BACKUP_SERVICE: MysqlBackupServiceApi,
        TagValues.MYSQL_SERVICE: MysqlServiceApi,
        TagValues.MYSQL_STATISTIC_SERVICE: MysqlStatisticServiceApi,
        TagValues.POSTGRESQL_BACKUP_SERVICE: PostgresqlBackupServiceApi,
        TagValues.POSTGRESQL_SERVICE: PostgresqlServiceApi,
        TagValues.POSTGRESQL_STATISTIC_SERVICE: PostgresqlStatisticServiceApi,
        TagValues.S3SERVICE: S3ServiceApi,
    }
)

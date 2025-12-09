import typing_extensions

from beget_openapi_cloud.apis.tags import TagValues
from beget_openapi_cloud.apis.tags.cdn_service_api import CdnServiceApi
from beget_openapi_cloud.apis.tags.cdn_statistic_service_api import CdnStatisticServiceApi
from beget_openapi_cloud.apis.tags.cloud_service_api import CloudServiceApi
from beget_openapi_cloud.apis.tags.mysql_backup_service_api import MysqlBackupServiceApi
from beget_openapi_cloud.apis.tags.mysql_service_api import MysqlServiceApi
from beget_openapi_cloud.apis.tags.mysql_statistic_service_api import MysqlStatisticServiceApi
from beget_openapi_cloud.apis.tags.postgresql_backup_service_api import PostgresqlBackupServiceApi
from beget_openapi_cloud.apis.tags.postgresql_service_api import PostgresqlServiceApi
from beget_openapi_cloud.apis.tags.postgresql_statistic_service_api import PostgresqlStatisticServiceApi
from beget_openapi_cloud.apis.tags.project_service_api import ProjectServiceApi
from beget_openapi_cloud.apis.tags.s3_service_api import S3ServiceApi
from beget_openapi_cloud.apis.tags.s3_statistic_service_api import S3StatisticServiceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CDN_SERVICE: CdnServiceApi,
        TagValues.CDN_STATISTIC_SERVICE: CdnStatisticServiceApi,
        TagValues.CLOUD_SERVICE: CloudServiceApi,
        TagValues.MYSQL_BACKUP_SERVICE: MysqlBackupServiceApi,
        TagValues.MYSQL_SERVICE: MysqlServiceApi,
        TagValues.MYSQL_STATISTIC_SERVICE: MysqlStatisticServiceApi,
        TagValues.POSTGRESQL_BACKUP_SERVICE: PostgresqlBackupServiceApi,
        TagValues.POSTGRESQL_SERVICE: PostgresqlServiceApi,
        TagValues.POSTGRESQL_STATISTIC_SERVICE: PostgresqlStatisticServiceApi,
        TagValues.PROJECT_SERVICE: ProjectServiceApi,
        TagValues.S3SERVICE: S3ServiceApi,
        TagValues.S3STATISTIC_SERVICE: S3StatisticServiceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CDN_SERVICE: CdnServiceApi,
        TagValues.CDN_STATISTIC_SERVICE: CdnStatisticServiceApi,
        TagValues.CLOUD_SERVICE: CloudServiceApi,
        TagValues.MYSQL_BACKUP_SERVICE: MysqlBackupServiceApi,
        TagValues.MYSQL_SERVICE: MysqlServiceApi,
        TagValues.MYSQL_STATISTIC_SERVICE: MysqlStatisticServiceApi,
        TagValues.POSTGRESQL_BACKUP_SERVICE: PostgresqlBackupServiceApi,
        TagValues.POSTGRESQL_SERVICE: PostgresqlServiceApi,
        TagValues.POSTGRESQL_STATISTIC_SERVICE: PostgresqlStatisticServiceApi,
        TagValues.PROJECT_SERVICE: ProjectServiceApi,
        TagValues.S3SERVICE: S3ServiceApi,
        TagValues.S3STATISTIC_SERVICE: S3StatisticServiceApi,
    }
)

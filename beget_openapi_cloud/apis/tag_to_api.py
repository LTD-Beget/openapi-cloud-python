import typing_extensions

from beget_openapi_cloud.apis.tags import TagValues
from beget_openapi_cloud.apis.tags.cloud_service_api import CloudServiceApi
from beget_openapi_cloud.apis.tags.mysql_service_api import MysqlServiceApi
from beget_openapi_cloud.apis.tags.mysql_statistic_service_api import MysqlStatisticServiceApi
from beget_openapi_cloud.apis.tags.postgresql_service_api import PostgresqlServiceApi
from beget_openapi_cloud.apis.tags.postgresql_statistic_service_api import PostgresqlStatisticServiceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CLOUD_SERVICE: CloudServiceApi,
        TagValues.MYSQL_SERVICE: MysqlServiceApi,
        TagValues.MYSQL_STATISTIC_SERVICE: MysqlStatisticServiceApi,
        TagValues.POSTGRESQL_SERVICE: PostgresqlServiceApi,
        TagValues.POSTGRESQL_STATISTIC_SERVICE: PostgresqlStatisticServiceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CLOUD_SERVICE: CloudServiceApi,
        TagValues.MYSQL_SERVICE: MysqlServiceApi,
        TagValues.MYSQL_STATISTIC_SERVICE: MysqlStatisticServiceApi,
        TagValues.POSTGRESQL_SERVICE: PostgresqlServiceApi,
        TagValues.POSTGRESQL_STATISTIC_SERVICE: PostgresqlStatisticServiceApi,
    }
)

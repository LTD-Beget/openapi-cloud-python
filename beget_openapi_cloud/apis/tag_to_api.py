import typing_extensions

from beget_openapi_cloud.apis.tags import TagValues
from beget_openapi_cloud.apis.tags.cloud_service_api import CloudServiceApi
from beget_openapi_cloud.apis.tags.mysql_service_api import MysqlServiceApi
from beget_openapi_cloud.apis.tags.mysql_statistic_service_api import MysqlStatisticServiceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CLOUD_SERVICE: CloudServiceApi,
        TagValues.MYSQL_SERVICE: MysqlServiceApi,
        TagValues.MYSQL_STATISTIC_SERVICE: MysqlStatisticServiceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CLOUD_SERVICE: CloudServiceApi,
        TagValues.MYSQL_SERVICE: MysqlServiceApi,
        TagValues.MYSQL_STATISTIC_SERVICE: MysqlStatisticServiceApi,
    }
)

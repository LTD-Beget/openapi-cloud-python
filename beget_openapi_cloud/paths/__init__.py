# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from beget_openapi_cloud.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_CLOUD = "/v1/cloud"
    V1_CLOUD_CONFIGURATION = "/v1/cloud/configuration"
    V1_CLOUD_MYSQL_SERVICE_ID_CONFIG = "/v1/cloud/mysql/{service_id}/config"
    V1_CLOUD_MYSQL_SERVICE_ID_DB = "/v1/cloud/mysql/{service_id}/db"
    V1_CLOUD_MYSQL_SERVICE_ID_DB_DB_NAME = "/v1/cloud/mysql/{service_id}/db/{db_name}"
    V1_CLOUD_MYSQL_SERVICE_ID_DB_DB_NAME_ACCESS = "/v1/cloud/mysql/{service_id}/db/{db_name}/access"
    V1_CLOUD_MYSQL_SERVICE_ID_DB_DB_NAME_ACCESS_HOST = "/v1/cloud/mysql/{service_id}/db/{db_name}/access/{host}"
    V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_CPU = "/v1/cloud/mysql/{service_id}/statistic/cpu"
    V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_CPUDETAILS = "/v1/cloud/mysql/{service_id}/statistic/cpu-details"
    V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_DISK = "/v1/cloud/mysql/{service_id}/statistic/disk"
    V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_DISKUSAGE = "/v1/cloud/mysql/{service_id}/statistic/disk-usage"
    V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_LOADAVERAGE = "/v1/cloud/mysql/{service_id}/statistic/load-average"
    V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_MEMORY = "/v1/cloud/mysql/{service_id}/statistic/memory"
    V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_NETWORK = "/v1/cloud/mysql/{service_id}/statistic/network"
    V1_CLOUD_SERVICE_ID = "/v1/cloud/{service_id}"
    V1_CLOUD_SERVICE_ID_CONFIGURATION = "/v1/cloud/{service_id}/configuration"

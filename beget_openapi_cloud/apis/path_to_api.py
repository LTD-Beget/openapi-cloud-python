import typing_extensions

from beget_openapi_cloud.paths import PathValues
from beget_openapi_cloud.apis.paths.v1_cloud import V1Cloud
from beget_openapi_cloud.apis.paths.v1_cloud_configuration import V1CloudConfiguration
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_config import V1CloudMysqlServiceIdConfig
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_db import V1CloudMysqlServiceIdDb
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_db_db_name import V1CloudMysqlServiceIdDbDbName
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_db_db_name_access import V1CloudMysqlServiceIdDbDbNameAccess
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_db_db_name_access_host import V1CloudMysqlServiceIdDbDbNameAccessHost
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_statistic_cpu import V1CloudMysqlServiceIdStatisticCpu
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_statistic_cpu_details import V1CloudMysqlServiceIdStatisticCpuDetails
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_statistic_disk import V1CloudMysqlServiceIdStatisticDisk
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_statistic_disk_usage import V1CloudMysqlServiceIdStatisticDiskUsage
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_statistic_load_average import V1CloudMysqlServiceIdStatisticLoadAverage
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_statistic_memory import V1CloudMysqlServiceIdStatisticMemory
from beget_openapi_cloud.apis.paths.v1_cloud_mysql_service_id_statistic_network import V1CloudMysqlServiceIdStatisticNetwork
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_config import V1CloudPostgresqlServiceIdConfig
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_db import V1CloudPostgresqlServiceIdDb
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_db_db_name import V1CloudPostgresqlServiceIdDbDbName
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_remote_access import V1CloudPostgresqlServiceIdRemoteAccess
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_role import V1CloudPostgresqlServiceIdRole
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_role_role_name import V1CloudPostgresqlServiceIdRoleRoleName
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_statistic_cpu import V1CloudPostgresqlServiceIdStatisticCpu
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_statistic_cpu_details import V1CloudPostgresqlServiceIdStatisticCpuDetails
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_statistic_disk import V1CloudPostgresqlServiceIdStatisticDisk
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_statistic_disk_usage import V1CloudPostgresqlServiceIdStatisticDiskUsage
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_statistic_load_average import V1CloudPostgresqlServiceIdStatisticLoadAverage
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_statistic_memory import V1CloudPostgresqlServiceIdStatisticMemory
from beget_openapi_cloud.apis.paths.v1_cloud_postgresql_service_id_statistic_network import V1CloudPostgresqlServiceIdStatisticNetwork
from beget_openapi_cloud.apis.paths.v1_cloud_service_id import V1CloudServiceId
from beget_openapi_cloud.apis.paths.v1_cloud_service_id_configuration import V1CloudServiceIdConfiguration

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_CLOUD: V1Cloud,
        PathValues.V1_CLOUD_CONFIGURATION: V1CloudConfiguration,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_CONFIG: V1CloudMysqlServiceIdConfig,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_DB: V1CloudMysqlServiceIdDb,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_DB_DB_NAME: V1CloudMysqlServiceIdDbDbName,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_DB_DB_NAME_ACCESS: V1CloudMysqlServiceIdDbDbNameAccess,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_DB_DB_NAME_ACCESS_HOST: V1CloudMysqlServiceIdDbDbNameAccessHost,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_CPU: V1CloudMysqlServiceIdStatisticCpu,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_CPUDETAILS: V1CloudMysqlServiceIdStatisticCpuDetails,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_DISK: V1CloudMysqlServiceIdStatisticDisk,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_DISKUSAGE: V1CloudMysqlServiceIdStatisticDiskUsage,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_LOADAVERAGE: V1CloudMysqlServiceIdStatisticLoadAverage,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_MEMORY: V1CloudMysqlServiceIdStatisticMemory,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_NETWORK: V1CloudMysqlServiceIdStatisticNetwork,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_CONFIG: V1CloudPostgresqlServiceIdConfig,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_DB: V1CloudPostgresqlServiceIdDb,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_DB_DB_NAME: V1CloudPostgresqlServiceIdDbDbName,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_REMOTEACCESS: V1CloudPostgresqlServiceIdRemoteAccess,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_ROLE: V1CloudPostgresqlServiceIdRole,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_ROLE_ROLE_NAME: V1CloudPostgresqlServiceIdRoleRoleName,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_CPU: V1CloudPostgresqlServiceIdStatisticCpu,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_CPUDETAILS: V1CloudPostgresqlServiceIdStatisticCpuDetails,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_DISK: V1CloudPostgresqlServiceIdStatisticDisk,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_DISKUSAGE: V1CloudPostgresqlServiceIdStatisticDiskUsage,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_LOADAVERAGE: V1CloudPostgresqlServiceIdStatisticLoadAverage,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_MEMORY: V1CloudPostgresqlServiceIdStatisticMemory,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_NETWORK: V1CloudPostgresqlServiceIdStatisticNetwork,
        PathValues.V1_CLOUD_SERVICE_ID: V1CloudServiceId,
        PathValues.V1_CLOUD_SERVICE_ID_CONFIGURATION: V1CloudServiceIdConfiguration,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_CLOUD: V1Cloud,
        PathValues.V1_CLOUD_CONFIGURATION: V1CloudConfiguration,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_CONFIG: V1CloudMysqlServiceIdConfig,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_DB: V1CloudMysqlServiceIdDb,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_DB_DB_NAME: V1CloudMysqlServiceIdDbDbName,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_DB_DB_NAME_ACCESS: V1CloudMysqlServiceIdDbDbNameAccess,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_DB_DB_NAME_ACCESS_HOST: V1CloudMysqlServiceIdDbDbNameAccessHost,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_CPU: V1CloudMysqlServiceIdStatisticCpu,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_CPUDETAILS: V1CloudMysqlServiceIdStatisticCpuDetails,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_DISK: V1CloudMysqlServiceIdStatisticDisk,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_DISKUSAGE: V1CloudMysqlServiceIdStatisticDiskUsage,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_LOADAVERAGE: V1CloudMysqlServiceIdStatisticLoadAverage,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_MEMORY: V1CloudMysqlServiceIdStatisticMemory,
        PathValues.V1_CLOUD_MYSQL_SERVICE_ID_STATISTIC_NETWORK: V1CloudMysqlServiceIdStatisticNetwork,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_CONFIG: V1CloudPostgresqlServiceIdConfig,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_DB: V1CloudPostgresqlServiceIdDb,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_DB_DB_NAME: V1CloudPostgresqlServiceIdDbDbName,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_REMOTEACCESS: V1CloudPostgresqlServiceIdRemoteAccess,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_ROLE: V1CloudPostgresqlServiceIdRole,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_ROLE_ROLE_NAME: V1CloudPostgresqlServiceIdRoleRoleName,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_CPU: V1CloudPostgresqlServiceIdStatisticCpu,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_CPUDETAILS: V1CloudPostgresqlServiceIdStatisticCpuDetails,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_DISK: V1CloudPostgresqlServiceIdStatisticDisk,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_DISKUSAGE: V1CloudPostgresqlServiceIdStatisticDiskUsage,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_LOADAVERAGE: V1CloudPostgresqlServiceIdStatisticLoadAverage,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_MEMORY: V1CloudPostgresqlServiceIdStatisticMemory,
        PathValues.V1_CLOUD_POSTGRESQL_SERVICE_ID_STATISTIC_NETWORK: V1CloudPostgresqlServiceIdStatisticNetwork,
        PathValues.V1_CLOUD_SERVICE_ID: V1CloudServiceId,
        PathValues.V1_CLOUD_SERVICE_ID_CONFIGURATION: V1CloudServiceIdConfiguration,
    }
)

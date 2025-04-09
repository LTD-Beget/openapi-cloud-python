# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from beget_openapi_cloud.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CLOUD_SERVICE = "CloudService"
    MYSQL_BACKUP_SERVICE = "MysqlBackupService"
    MYSQL_SERVICE = "MysqlService"
    MYSQL_STATISTIC_SERVICE = "MysqlStatisticService"
    POSTGRESQL_BACKUP_SERVICE = "PostgresqlBackupService"
    POSTGRESQL_SERVICE = "PostgresqlService"
    POSTGRESQL_STATISTIC_SERVICE = "PostgresqlStatisticService"
    S3SERVICE = "S3Service"
    S3STATISTIC_SERVICE = "S3StatisticService"

# coding: utf-8

"""
    API Управляемых сервисов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.1.1
    Generated by: https://openapi-generator.tech
"""

from beget_openapi_cloud.paths.v1_cloud_mysql_service_id_db_db_name_access_host.patch import MysqlServiceChangeAccessPassword
from beget_openapi_cloud.paths.v1_cloud_mysql_service_id_db_db_name_access.post import MysqlServiceCreateAccess
from beget_openapi_cloud.paths.v1_cloud_mysql_service_id_db.post import MysqlServiceCreateDb
from beget_openapi_cloud.paths.v1_cloud_mysql_service_id_config.get import MysqlServiceGetConfig
from beget_openapi_cloud.paths.v1_cloud_mysql_service_id_db.get import MysqlServiceGetDbList
from beget_openapi_cloud.paths.v1_cloud_mysql_service_id_db_db_name_access_host.delete import MysqlServiceRemoveAccess
from beget_openapi_cloud.paths.v1_cloud_mysql_service_id_db_db_name.delete import MysqlServiceRemoveDb
from beget_openapi_cloud.paths.v1_cloud_mysql_service_id_config.put import MysqlServiceSetConfig
from beget_openapi_cloud.paths.v1_cloud_mysql_service_id_db_db_name.patch import MysqlServiceUpdateDb


class MysqlServiceApi(
    MysqlServiceChangeAccessPassword,
    MysqlServiceCreateAccess,
    MysqlServiceCreateDb,
    MysqlServiceGetConfig,
    MysqlServiceGetDbList,
    MysqlServiceRemoveAccess,
    MysqlServiceRemoveDb,
    MysqlServiceSetConfig,
    MysqlServiceUpdateDb,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
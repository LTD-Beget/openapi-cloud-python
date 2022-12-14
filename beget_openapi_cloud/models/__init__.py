# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from beget_openapi_cloud.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from beget_openapi_cloud.model.cloud_change_configuration_request import CloudChangeConfigurationRequest
from beget_openapi_cloud.model.cloud_change_configuration_response import CloudChangeConfigurationResponse
from beget_openapi_cloud.model.cloud_change_configuration_response_error import CloudChangeConfigurationResponseError
from beget_openapi_cloud.model.cloud_create_request import CloudCreateRequest
from beget_openapi_cloud.model.cloud_create_response import CloudCreateResponse
from beget_openapi_cloud.model.cloud_get_configuration_list_response import CloudGetConfigurationListResponse
from beget_openapi_cloud.model.cloud_get_list_response import CloudGetListResponse
from beget_openapi_cloud.model.cloud_get_response import CloudGetResponse
from beget_openapi_cloud.model.cloud_remove_response import CloudRemoveResponse
from beget_openapi_cloud.model.cloud_service import CloudService
from beget_openapi_cloud.model.cloud_service_configuration import CloudServiceConfiguration
from beget_openapi_cloud.model.cloud_update_request import CloudUpdateRequest
from beget_openapi_cloud.model.cloud_update_response import CloudUpdateResponse
from beget_openapi_cloud.model.cloud_update_response_error import CloudUpdateResponseError
from beget_openapi_cloud.model.mysql_change_access_password_request import MysqlChangeAccessPasswordRequest
from beget_openapi_cloud.model.mysql_change_access_password_response import MysqlChangeAccessPasswordResponse
from beget_openapi_cloud.model.mysql_change_access_password_response_error import MysqlChangeAccessPasswordResponseError
from beget_openapi_cloud.model.mysql_config import MysqlConfig
from beget_openapi_cloud.model.mysql_create_access_request import MysqlCreateAccessRequest
from beget_openapi_cloud.model.mysql_create_access_response import MysqlCreateAccessResponse
from beget_openapi_cloud.model.mysql_create_access_response_error import MysqlCreateAccessResponseError
from beget_openapi_cloud.model.mysql_create_db_request import MysqlCreateDbRequest
from beget_openapi_cloud.model.mysql_create_db_response import MysqlCreateDbResponse
from beget_openapi_cloud.model.mysql_create_db_response_error import MysqlCreateDbResponseError
from beget_openapi_cloud.model.mysql_create_error import MysqlCreateError
from beget_openapi_cloud.model.mysql_create_params import MysqlCreateParams
from beget_openapi_cloud.model.mysql_db import MysqlDb
from beget_openapi_cloud.model.mysql_db_access import MysqlDbAccess
from beget_openapi_cloud.model.mysql_get_config_response import MysqlGetConfigResponse
from beget_openapi_cloud.model.mysql_get_db_list_response import MysqlGetDbListResponse
from beget_openapi_cloud.model.mysql_mysql5 import MysqlMysql5
from beget_openapi_cloud.model.mysql_mysql5_configuration import MysqlMysql5Configuration
from beget_openapi_cloud.model.mysql_mysql8 import MysqlMysql8
from beget_openapi_cloud.model.mysql_mysql8_configuration import MysqlMysql8Configuration
from beget_openapi_cloud.model.mysql_remove_access_response import MysqlRemoveAccessResponse
from beget_openapi_cloud.model.mysql_remove_access_response_error import MysqlRemoveAccessResponseError
from beget_openapi_cloud.model.mysql_remove_db_response import MysqlRemoveDbResponse
from beget_openapi_cloud.model.mysql_remove_db_response_error import MysqlRemoveDbResponseError
from beget_openapi_cloud.model.mysql_set_config_request import MysqlSetConfigRequest
from beget_openapi_cloud.model.mysql_set_config_response import MysqlSetConfigResponse
from beget_openapi_cloud.model.mysql_set_config_response_error import MysqlSetConfigResponseError
from beget_openapi_cloud.model.mysql_statistic_get_cpu_details_response import MysqlStatisticGetCpuDetailsResponse
from beget_openapi_cloud.model.mysql_statistic_get_cpu_response import MysqlStatisticGetCpuResponse
from beget_openapi_cloud.model.mysql_statistic_get_disk_response import MysqlStatisticGetDiskResponse
from beget_openapi_cloud.model.mysql_statistic_get_disk_usage_response import MysqlStatisticGetDiskUsageResponse
from beget_openapi_cloud.model.mysql_statistic_get_load_average_response import MysqlStatisticGetLoadAverageResponse
from beget_openapi_cloud.model.mysql_statistic_get_memory_response import MysqlStatisticGetMemoryResponse
from beget_openapi_cloud.model.mysql_statistic_get_network_response import MysqlStatisticGetNetworkResponse
from beget_openapi_cloud.model.mysql_update_db_request import MysqlUpdateDbRequest
from beget_openapi_cloud.model.mysql_update_db_response import MysqlUpdateDbResponse
from beget_openapi_cloud.model.mysql_update_db_response_error import MysqlUpdateDbResponseError
from beget_openapi_cloud.model.structures_address_info import StructuresAddressInfo
from beget_openapi_cloud.model.structures_address_info_private_address import StructuresAddressInfoPrivateAddress
from beget_openapi_cloud.model.structures_address_info_public_address import StructuresAddressInfoPublicAddress
from beget_openapi_cloud.model.structures_statistic_series_data import StructuresStatisticSeriesData

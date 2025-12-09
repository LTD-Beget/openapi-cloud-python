<a name="__pageTop"></a>
# beget_openapi_cloud.apis.tags.postgresql_backup_service_api.PostgresqlBackupServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postgresql_backup_service_get_list**](#postgresql_backup_service_get_list) | **get** /v1/cloud/postgresql/backup | 
[**postgresql_backup_service_get_orders**](#postgresql_backup_service_get_orders) | **get** /v1/cloud/postgresql/backup/orders | 
[**postgresql_backup_service_restore**](#postgresql_backup_service_restore) | **post** /v1/cloud/postgresql/backup/{copy_id} | 

# **postgresql_backup_service_get_list**
<a name="postgresql_backup_service_get_list"></a>
> PostgresqlBackupGetListResponse postgresql_backup_service_get_list()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_backup_service_api
from beget_openapi_cloud.model.postgresql_backup_get_list_response import PostgresqlBackupGetListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_cloud.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_cloud.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = postgresql_backup_service_api.PostgresqlBackupServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': "filter_example",
    }
    try:
        api_response = api_instance.postgresql_backup_service_get_list(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlBackupServiceApi->postgresql_backup_service_get_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter | FilterSchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_backup_service_get_list.ApiResponseFor200) | OK

#### postgresql_backup_service_get_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlBackupGetListResponse**](../../models/PostgresqlBackupGetListResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **postgresql_backup_service_get_orders**
<a name="postgresql_backup_service_get_orders"></a>
> PostgresqlBackupGetOrdersResponse postgresql_backup_service_get_orders()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_backup_service_api
from beget_openapi_cloud.model.postgresql_backup_get_orders_response import PostgresqlBackupGetOrdersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_cloud.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_cloud.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = postgresql_backup_service_api.PostgresqlBackupServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 1,
        'offset': 1,
    }
    try:
        api_response = api_instance.postgresql_backup_service_get_orders(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlBackupServiceApi->postgresql_backup_service_get_orders: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_backup_service_get_orders.ApiResponseFor200) | OK

#### postgresql_backup_service_get_orders.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlBackupGetOrdersResponse**](../../models/PostgresqlBackupGetOrdersResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **postgresql_backup_service_restore**
<a name="postgresql_backup_service_restore"></a>
> PostgresqlBackupRestoreResponse postgresql_backup_service_restore(copy_idpostgresql_backup_restore_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_backup_service_api
from beget_openapi_cloud.model.postgresql_backup_restore_request import PostgresqlBackupRestoreRequest
from beget_openapi_cloud.model.postgresql_backup_restore_response import PostgresqlBackupRestoreResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_cloud.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_cloud.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = postgresql_backup_service_api.PostgresqlBackupServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'copy_id': "copy_id_example",
    }
    body = PostgresqlBackupRestoreRequest(
        copy_id="copy_id_example",
        service_uuid="service_uuid_example",
    )
    try:
        api_response = api_instance.postgresql_backup_service_restore(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlBackupServiceApi->postgresql_backup_service_restore: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlBackupRestoreRequest**](../../models/PostgresqlBackupRestoreRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
copy_id | CopyIdSchema | | 

# CopyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_backup_service_restore.ApiResponseFor200) | OK

#### postgresql_backup_service_restore.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlBackupRestoreResponse**](../../models/PostgresqlBackupRestoreResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


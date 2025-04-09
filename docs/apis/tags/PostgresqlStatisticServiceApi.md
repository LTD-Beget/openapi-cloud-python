<a name="__pageTop"></a>
# beget_openapi_cloud.apis.tags.postgresql_statistic_service_api.PostgresqlStatisticServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postgresql_statistic_service_get_cpu**](#postgresql_statistic_service_get_cpu) | **get** /v1/cloud/postgresql/{service_id}/statistic/cpu | 
[**postgresql_statistic_service_get_cpu_details**](#postgresql_statistic_service_get_cpu_details) | **get** /v1/cloud/postgresql/{service_id}/statistic/cpu-details | 
[**postgresql_statistic_service_get_disk**](#postgresql_statistic_service_get_disk) | **get** /v1/cloud/postgresql/{service_id}/statistic/disk | 
[**postgresql_statistic_service_get_disk_usage**](#postgresql_statistic_service_get_disk_usage) | **get** /v1/cloud/postgresql/{service_id}/statistic/disk-usage | 
[**postgresql_statistic_service_get_load_average**](#postgresql_statistic_service_get_load_average) | **get** /v1/cloud/postgresql/{service_id}/statistic/load-average | 
[**postgresql_statistic_service_get_memory**](#postgresql_statistic_service_get_memory) | **get** /v1/cloud/postgresql/{service_id}/statistic/memory | 
[**postgresql_statistic_service_get_network**](#postgresql_statistic_service_get_network) | **get** /v1/cloud/postgresql/{service_id}/statistic/network | 

# **postgresql_statistic_service_get_cpu**
<a name="postgresql_statistic_service_get_cpu"></a>
> PostgresqlStatisticGetCpuResponse postgresql_statistic_service_get_cpu(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_statistic_service_api
from beget_openapi_cloud.model.postgresql_statistic_get_cpu_response import PostgresqlStatisticGetCpuResponse
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
    api_instance = postgresql_statistic_service_api.PostgresqlStatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_cpu(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_cpu: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_cpu(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_cpu: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
period | PeriodSchema | | optional


# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["UNKNOWN", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_statistic_service_get_cpu.ApiResponseFor200) | OK

#### postgresql_statistic_service_get_cpu.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlStatisticGetCpuResponse**](../../models/PostgresqlStatisticGetCpuResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **postgresql_statistic_service_get_cpu_details**
<a name="postgresql_statistic_service_get_cpu_details"></a>
> PostgresqlStatisticGetCpuDetailsResponse postgresql_statistic_service_get_cpu_details(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_statistic_service_api
from beget_openapi_cloud.model.postgresql_statistic_get_cpu_details_response import PostgresqlStatisticGetCpuDetailsResponse
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
    api_instance = postgresql_statistic_service_api.PostgresqlStatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_cpu_details(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_cpu_details: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_cpu_details(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_cpu_details: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
period | PeriodSchema | | optional


# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["UNKNOWN", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_statistic_service_get_cpu_details.ApiResponseFor200) | OK

#### postgresql_statistic_service_get_cpu_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlStatisticGetCpuDetailsResponse**](../../models/PostgresqlStatisticGetCpuDetailsResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **postgresql_statistic_service_get_disk**
<a name="postgresql_statistic_service_get_disk"></a>
> PostgresqlStatisticGetDiskResponse postgresql_statistic_service_get_disk(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_statistic_service_api
from beget_openapi_cloud.model.postgresql_statistic_get_disk_response import PostgresqlStatisticGetDiskResponse
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
    api_instance = postgresql_statistic_service_api.PostgresqlStatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_disk(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_disk: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_disk(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_disk: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
period | PeriodSchema | | optional


# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["UNKNOWN", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_statistic_service_get_disk.ApiResponseFor200) | OK

#### postgresql_statistic_service_get_disk.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlStatisticGetDiskResponse**](../../models/PostgresqlStatisticGetDiskResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **postgresql_statistic_service_get_disk_usage**
<a name="postgresql_statistic_service_get_disk_usage"></a>
> PostgresqlStatisticGetDiskUsageResponse postgresql_statistic_service_get_disk_usage(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_statistic_service_api
from beget_openapi_cloud.model.postgresql_statistic_get_disk_usage_response import PostgresqlStatisticGetDiskUsageResponse
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
    api_instance = postgresql_statistic_service_api.PostgresqlStatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_disk_usage(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_disk_usage: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_disk_usage(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_disk_usage: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
period | PeriodSchema | | optional


# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["UNKNOWN", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_statistic_service_get_disk_usage.ApiResponseFor200) | OK

#### postgresql_statistic_service_get_disk_usage.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlStatisticGetDiskUsageResponse**](../../models/PostgresqlStatisticGetDiskUsageResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **postgresql_statistic_service_get_load_average**
<a name="postgresql_statistic_service_get_load_average"></a>
> PostgresqlStatisticGetLoadAverageResponse postgresql_statistic_service_get_load_average(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_statistic_service_api
from beget_openapi_cloud.model.postgresql_statistic_get_load_average_response import PostgresqlStatisticGetLoadAverageResponse
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
    api_instance = postgresql_statistic_service_api.PostgresqlStatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_load_average(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_load_average: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_load_average(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_load_average: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
period | PeriodSchema | | optional


# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["UNKNOWN", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_statistic_service_get_load_average.ApiResponseFor200) | OK

#### postgresql_statistic_service_get_load_average.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlStatisticGetLoadAverageResponse**](../../models/PostgresqlStatisticGetLoadAverageResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **postgresql_statistic_service_get_memory**
<a name="postgresql_statistic_service_get_memory"></a>
> PostgresqlStatisticGetMemoryResponse postgresql_statistic_service_get_memory(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_statistic_service_api
from beget_openapi_cloud.model.postgresql_statistic_get_memory_response import PostgresqlStatisticGetMemoryResponse
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
    api_instance = postgresql_statistic_service_api.PostgresqlStatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_memory(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_memory: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_memory(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_memory: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
period | PeriodSchema | | optional


# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["UNKNOWN", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_statistic_service_get_memory.ApiResponseFor200) | OK

#### postgresql_statistic_service_get_memory.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlStatisticGetMemoryResponse**](../../models/PostgresqlStatisticGetMemoryResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **postgresql_statistic_service_get_network**
<a name="postgresql_statistic_service_get_network"></a>
> PostgresqlStatisticGetNetworkResponse postgresql_statistic_service_get_network(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import postgresql_statistic_service_api
from beget_openapi_cloud.model.postgresql_statistic_get_network_response import PostgresqlStatisticGetNetworkResponse
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
    api_instance = postgresql_statistic_service_api.PostgresqlStatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_network(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_network: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.postgresql_statistic_service_get_network(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling PostgresqlStatisticServiceApi->postgresql_statistic_service_get_network: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
period | PeriodSchema | | optional


# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["UNKNOWN", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#postgresql_statistic_service_get_network.ApiResponseFor200) | OK

#### postgresql_statistic_service_get_network.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostgresqlStatisticGetNetworkResponse**](../../models/PostgresqlStatisticGetNetworkResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


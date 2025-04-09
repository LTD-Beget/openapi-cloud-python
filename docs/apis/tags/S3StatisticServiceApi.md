<a name="__pageTop"></a>
# beget_openapi_cloud.apis.tags.s3_statistic_service_api.S3StatisticServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s3_statistic_service_get_network**](#s3_statistic_service_get_network) | **get** /v1/cloud/s3/{service_id}/statistic/network | 
[**s3_statistic_service_get_quota**](#s3_statistic_service_get_quota) | **get** /v1/cloud/s3/{service_id}/statistic/quota | 
[**s3_statistic_service_get_request**](#s3_statistic_service_get_request) | **get** /v1/cloud/s3/{service_id}/statistic/count-request | 
[**s3_statistic_service_get_traffic**](#s3_statistic_service_get_traffic) | **get** /v1/cloud/s3/{service_id}/statistic/traffic-usage | 

# **s3_statistic_service_get_network**
<a name="s3_statistic_service_get_network"></a>
> S3StatisticGetNetworkResponse s3_statistic_service_get_network(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_statistic_service_api
from beget_openapi_cloud.model.s3_statistic_get_network_response import S3StatisticGetNetworkResponse
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
    api_instance = s3_statistic_service_api.S3StatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.s3_statistic_service_get_network(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3StatisticServiceApi->s3_statistic_service_get_network: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.s3_statistic_service_get_network(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3StatisticServiceApi->s3_statistic_service_get_network: %s\n" % e)
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
200 | [ApiResponseFor200](#s3_statistic_service_get_network.ApiResponseFor200) | OK

#### s3_statistic_service_get_network.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3StatisticGetNetworkResponse**](../../models/S3StatisticGetNetworkResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_statistic_service_get_quota**
<a name="s3_statistic_service_get_quota"></a>
> S3StatisticGetQuotaResponse s3_statistic_service_get_quota(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_statistic_service_api
from beget_openapi_cloud.model.s3_statistic_get_quota_response import S3StatisticGetQuotaResponse
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
    api_instance = s3_statistic_service_api.S3StatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.s3_statistic_service_get_quota(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3StatisticServiceApi->s3_statistic_service_get_quota: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.s3_statistic_service_get_quota(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3StatisticServiceApi->s3_statistic_service_get_quota: %s\n" % e)
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
200 | [ApiResponseFor200](#s3_statistic_service_get_quota.ApiResponseFor200) | OK

#### s3_statistic_service_get_quota.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3StatisticGetQuotaResponse**](../../models/S3StatisticGetQuotaResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_statistic_service_get_request**
<a name="s3_statistic_service_get_request"></a>
> S3StatisticGetRequestResponse s3_statistic_service_get_request(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_statistic_service_api
from beget_openapi_cloud.model.s3_statistic_get_request_response import S3StatisticGetRequestResponse
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
    api_instance = s3_statistic_service_api.S3StatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.s3_statistic_service_get_request(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3StatisticServiceApi->s3_statistic_service_get_request: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.s3_statistic_service_get_request(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3StatisticServiceApi->s3_statistic_service_get_request: %s\n" % e)
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
200 | [ApiResponseFor200](#s3_statistic_service_get_request.ApiResponseFor200) | OK

#### s3_statistic_service_get_request.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3StatisticGetRequestResponse**](../../models/S3StatisticGetRequestResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_statistic_service_get_traffic**
<a name="s3_statistic_service_get_traffic"></a>
> S3StatisticGetTrafficResponse s3_statistic_service_get_traffic(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_statistic_service_api
from beget_openapi_cloud.model.s3_statistic_get_traffic_response import S3StatisticGetTrafficResponse
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
    api_instance = s3_statistic_service_api.S3StatisticServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.s3_statistic_service_get_traffic(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3StatisticServiceApi->s3_statistic_service_get_traffic: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    query_params = {
        'period': "UNKNOWN",
    }
    try:
        api_response = api_instance.s3_statistic_service_get_traffic(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3StatisticServiceApi->s3_statistic_service_get_traffic: %s\n" % e)
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
200 | [ApiResponseFor200](#s3_statistic_service_get_traffic.ApiResponseFor200) | OK

#### s3_statistic_service_get_traffic.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3StatisticGetTrafficResponse**](../../models/S3StatisticGetTrafficResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


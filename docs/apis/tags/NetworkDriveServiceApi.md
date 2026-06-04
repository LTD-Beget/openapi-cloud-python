<a id="__pageTop"></a>
# beget_openapi_cloud.apis.tags.network_drive_service_api.NetworkDriveServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_drive_service_get_limits**](#network_drive_service_get_limits) | **get** /v1/cloud/network-drive/limits | 
[**network_drive_service_get_mounts**](#network_drive_service_get_mounts) | **get** /v1/cloud/network-drive/mounts | 
[**network_drive_service_get_price**](#network_drive_service_get_price) | **get** /v1/cloud/network-drive/price | 
[**network_drive_service_mount**](#network_drive_service_mount) | **post** /v1/cloud/network-drive/{service_id}/mount | 
[**network_drive_service_resize**](#network_drive_service_resize) | **post** /v1/cloud/network-drive/{service_id}/resize | 
[**network_drive_service_set_mounts**](#network_drive_service_set_mounts) | **post** /v1/cloud/network-drive/mounts | 
[**network_drive_service_unmount**](#network_drive_service_unmount) | **post** /v1/cloud/network-drive/{service_id}/unmount | 

# **network_drive_service_get_limits**
<a id="network_drive_service_get_limits"></a>
> NetworkDriveGetLimitsResponse network_drive_service_get_limits()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import network_drive_service_api
from beget_openapi_cloud.model.network_drive_get_limits_response import NetworkDriveGetLimitsResponse
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
    api_instance = network_drive_service_api.NetworkDriveServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.network_drive_service_get_limits()
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling NetworkDriveServiceApi->network_drive_service_get_limits: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#network_drive_service_get_limits.ApiResponseFor200) | OK

#### network_drive_service_get_limits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetworkDriveGetLimitsResponse**](../../models/NetworkDriveGetLimitsResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_drive_service_get_mounts**
<a id="network_drive_service_get_mounts"></a>
> NetworkDriveGetMountsResponse network_drive_service_get_mounts()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import network_drive_service_api
from beget_openapi_cloud.model.network_drive_get_mounts_response import NetworkDriveGetMountsResponse
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
    api_instance = network_drive_service_api.NetworkDriveServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'resource_id': "resource_id_example",
        'resource_type': "VPS",
    }
    try:
        api_response = api_instance.network_drive_service_get_mounts(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling NetworkDriveServiceApi->network_drive_service_get_mounts: %s\n" % e)
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
resource_id | ResourceIdSchema | | optional
resource_type | ResourceTypeSchema | | optional


# ResourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["VPS", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#network_drive_service_get_mounts.ApiResponseFor200) | OK

#### network_drive_service_get_mounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetworkDriveGetMountsResponse**](../../models/NetworkDriveGetMountsResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_drive_service_get_price**
<a id="network_drive_service_get_price"></a>
> NetworkDriveGetPriceResponse network_drive_service_get_price()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import network_drive_service_api
from beget_openapi_cloud.model.network_drive_get_price_response import NetworkDriveGetPriceResponse
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
    api_instance = network_drive_service_api.NetworkDriveServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.network_drive_service_get_price()
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling NetworkDriveServiceApi->network_drive_service_get_price: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#network_drive_service_get_price.ApiResponseFor200) | OK

#### network_drive_service_get_price.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetworkDriveGetPriceResponse**](../../models/NetworkDriveGetPriceResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_drive_service_mount**
<a id="network_drive_service_mount"></a>
> NetworkDriveMountResponse network_drive_service_mount(service_idnetwork_drive_mount_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import network_drive_service_api
from beget_openapi_cloud.model.network_drive_mount_response import NetworkDriveMountResponse
from beget_openapi_cloud.model.network_drive_mount_request import NetworkDriveMountRequest
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
    api_instance = network_drive_service_api.NetworkDriveServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = NetworkDriveMountRequest(
        service_id="service_id_example",
        resource_id="resource_id_example",
        resource_type="VPS",
    )
    try:
        api_response = api_instance.network_drive_service_mount(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling NetworkDriveServiceApi->network_drive_service_mount: %s\n" % e)
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
[**NetworkDriveMountRequest**](../../models/NetworkDriveMountRequest.md) |  | 


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
200 | [ApiResponseFor200](#network_drive_service_mount.ApiResponseFor200) | OK

#### network_drive_service_mount.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetworkDriveMountResponse**](../../models/NetworkDriveMountResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_drive_service_resize**
<a id="network_drive_service_resize"></a>
> NetworkDriveResizeResponse network_drive_service_resize(service_idnetwork_drive_resize_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import network_drive_service_api
from beget_openapi_cloud.model.network_drive_resize_response import NetworkDriveResizeResponse
from beget_openapi_cloud.model.network_drive_resize_request import NetworkDriveResizeRequest
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
    api_instance = network_drive_service_api.NetworkDriveServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = NetworkDriveResizeRequest(
        service_id="service_id_example",
        size=1,
    )
    try:
        api_response = api_instance.network_drive_service_resize(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling NetworkDriveServiceApi->network_drive_service_resize: %s\n" % e)
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
[**NetworkDriveResizeRequest**](../../models/NetworkDriveResizeRequest.md) |  | 


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
200 | [ApiResponseFor200](#network_drive_service_resize.ApiResponseFor200) | OK

#### network_drive_service_resize.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetworkDriveResizeResponse**](../../models/NetworkDriveResizeResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_drive_service_set_mounts**
<a id="network_drive_service_set_mounts"></a>
> NetworkDriveSetMountsResponse network_drive_service_set_mounts(network_drive_set_mounts_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import network_drive_service_api
from beget_openapi_cloud.model.network_drive_set_mounts_request import NetworkDriveSetMountsRequest
from beget_openapi_cloud.model.network_drive_set_mounts_response import NetworkDriveSetMountsResponse
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
    api_instance = network_drive_service_api.NetworkDriveServiceApi(api_client)

    # example passing only required values which don't have defaults set
    body = NetworkDriveSetMountsRequest(
        service_id=[
            "service_id_example"
        ],
        resource_id="resource_id_example",
        resource_type="VPS",
    )
    try:
        api_response = api_instance.network_drive_service_set_mounts(
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling NetworkDriveServiceApi->network_drive_service_set_mounts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetworkDriveSetMountsRequest**](../../models/NetworkDriveSetMountsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#network_drive_service_set_mounts.ApiResponseFor200) | OK

#### network_drive_service_set_mounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetworkDriveSetMountsResponse**](../../models/NetworkDriveSetMountsResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_drive_service_unmount**
<a id="network_drive_service_unmount"></a>
> NetworkDriveUnmountResponse network_drive_service_unmount(service_idnetwork_drive_unmount_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import network_drive_service_api
from beget_openapi_cloud.model.network_drive_unmount_request import NetworkDriveUnmountRequest
from beget_openapi_cloud.model.network_drive_unmount_response import NetworkDriveUnmountResponse
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
    api_instance = network_drive_service_api.NetworkDriveServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = NetworkDriveUnmountRequest(
        service_id="service_id_example",
    )
    try:
        api_response = api_instance.network_drive_service_unmount(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling NetworkDriveServiceApi->network_drive_service_unmount: %s\n" % e)
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
[**NetworkDriveUnmountRequest**](../../models/NetworkDriveUnmountRequest.md) |  | 


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
200 | [ApiResponseFor200](#network_drive_service_unmount.ApiResponseFor200) | OK

#### network_drive_service_unmount.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetworkDriveUnmountResponse**](../../models/NetworkDriveUnmountResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


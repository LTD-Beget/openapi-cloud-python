<a name="__pageTop"></a>
# beget_openapi_cloud.apis.tags.s3_service_api.S3ServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s3_service_change_access_key**](#s3_service_change_access_key) | **patch** /v1/cloud/s3/{service_id}/access-key | 
[**s3_service_change_cors**](#s3_service_change_cors) | **patch** /v1/cloud/s3/{service_id}/cors | 
[**s3_service_change_domain**](#s3_service_change_domain) | **patch** /v1/cloud/s3/{service_id}/domain | 
[**s3_service_change_public**](#s3_service_change_public) | **patch** /v1/cloud/s3/{service_id}/public | 
[**s3_service_enable_ftp**](#s3_service_enable_ftp) | **patch** /v1/cloud/s3/{service_id}/enable-ftp | 
[**s3_service_get_prefix**](#s3_service_get_prefix) | **get** /v1/cloud/s3/prefix | 
[**s3_service_get_price**](#s3_service_get_price) | **get** /v1/cloud/s3/price | 
[**s3_service_get_quota**](#s3_service_get_quota) | **get** /v1/cloud/s3/quota | 

# **s3_service_change_access_key**
<a name="s3_service_change_access_key"></a>
> S3ChangeAccessKeyResponse s3_service_change_access_key(service_ids3_change_access_key_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_service_api
from beget_openapi_cloud.model.s3_change_access_key_response import S3ChangeAccessKeyResponse
from beget_openapi_cloud.model.s3_change_access_key_request import S3ChangeAccessKeyRequest
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
    api_instance = s3_service_api.S3ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = S3ChangeAccessKeyRequest(
        service_id="service_id_example",
    )
    try:
        api_response = api_instance.s3_service_change_access_key(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3ServiceApi->s3_service_change_access_key: %s\n" % e)
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
[**S3ChangeAccessKeyRequest**](../../models/S3ChangeAccessKeyRequest.md) |  | 


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
200 | [ApiResponseFor200](#s3_service_change_access_key.ApiResponseFor200) | OK

#### s3_service_change_access_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3ChangeAccessKeyResponse**](../../models/S3ChangeAccessKeyResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_service_change_cors**
<a name="s3_service_change_cors"></a>
> S3ChangeCorsResponse s3_service_change_cors(service_ids3_change_cors_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_service_api
from beget_openapi_cloud.model.s3_change_cors_response import S3ChangeCorsResponse
from beget_openapi_cloud.model.s3_change_cors_request import S3ChangeCorsRequest
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
    api_instance = s3_service_api.S3ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = S3ChangeCorsRequest(
        service_id="service_id_example",
        cors=[
            S3Cors(
                id=1,
                http_method=[
                    "http_method_example"
                ],
,
,
                cache_ttl="cache_ttl_example",
                fqdn="fqdn_example",
            )
        ],
    )
    try:
        api_response = api_instance.s3_service_change_cors(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3ServiceApi->s3_service_change_cors: %s\n" % e)
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
[**S3ChangeCorsRequest**](../../models/S3ChangeCorsRequest.md) |  | 


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
200 | [ApiResponseFor200](#s3_service_change_cors.ApiResponseFor200) | OK

#### s3_service_change_cors.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3ChangeCorsResponse**](../../models/S3ChangeCorsResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_service_change_domain**
<a name="s3_service_change_domain"></a>
> S3ChangeDomainResponse s3_service_change_domain(service_ids3_change_domain_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_service_api
from beget_openapi_cloud.model.s3_change_domain_response import S3ChangeDomainResponse
from beget_openapi_cloud.model.s3_change_domain_request import S3ChangeDomainRequest
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
    api_instance = s3_service_api.S3ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = S3ChangeDomainRequest(
        service_id="service_id_example",
        fqdn="fqdn_example",
    )
    try:
        api_response = api_instance.s3_service_change_domain(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3ServiceApi->s3_service_change_domain: %s\n" % e)
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
[**S3ChangeDomainRequest**](../../models/S3ChangeDomainRequest.md) |  | 


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
200 | [ApiResponseFor200](#s3_service_change_domain.ApiResponseFor200) | OK

#### s3_service_change_domain.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3ChangeDomainResponse**](../../models/S3ChangeDomainResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_service_change_public**
<a name="s3_service_change_public"></a>
> S3ChangePublicResponse s3_service_change_public(service_ids3_change_public_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_service_api
from beget_openapi_cloud.model.s3_change_public_request import S3ChangePublicRequest
from beget_openapi_cloud.model.s3_change_public_response import S3ChangePublicResponse
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
    api_instance = s3_service_api.S3ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = S3ChangePublicRequest(
        service_id="service_id_example",
        public=True,
    )
    try:
        api_response = api_instance.s3_service_change_public(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3ServiceApi->s3_service_change_public: %s\n" % e)
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
[**S3ChangePublicRequest**](../../models/S3ChangePublicRequest.md) |  | 


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
200 | [ApiResponseFor200](#s3_service_change_public.ApiResponseFor200) | OK

#### s3_service_change_public.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3ChangePublicResponse**](../../models/S3ChangePublicResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_service_enable_ftp**
<a name="s3_service_enable_ftp"></a>
> S3EnableFtpResponse s3_service_enable_ftp(service_ids3_enable_ftp_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_service_api
from beget_openapi_cloud.model.s3_enable_ftp_response import S3EnableFtpResponse
from beget_openapi_cloud.model.s3_enable_ftp_request import S3EnableFtpRequest
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
    api_instance = s3_service_api.S3ServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = S3EnableFtpRequest(
        service_id="service_id_example",
        enable=True,
    )
    try:
        api_response = api_instance.s3_service_enable_ftp(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3ServiceApi->s3_service_enable_ftp: %s\n" % e)
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
[**S3EnableFtpRequest**](../../models/S3EnableFtpRequest.md) |  | 


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
200 | [ApiResponseFor200](#s3_service_enable_ftp.ApiResponseFor200) | OK

#### s3_service_enable_ftp.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3EnableFtpResponse**](../../models/S3EnableFtpResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_service_get_prefix**
<a name="s3_service_get_prefix"></a>
> S3GetPrefixResponse s3_service_get_prefix()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_service_api
from beget_openapi_cloud.model.s3_get_prefix_response import S3GetPrefixResponse
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
    api_instance = s3_service_api.S3ServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.s3_service_get_prefix()
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3ServiceApi->s3_service_get_prefix: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#s3_service_get_prefix.ApiResponseFor200) | OK

#### s3_service_get_prefix.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3GetPrefixResponse**](../../models/S3GetPrefixResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_service_get_price**
<a name="s3_service_get_price"></a>
> S3GetPriceResponse s3_service_get_price()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_service_api
from beget_openapi_cloud.model.s3_get_price_response import S3GetPriceResponse
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
    api_instance = s3_service_api.S3ServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.s3_service_get_price()
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3ServiceApi->s3_service_get_price: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#s3_service_get_price.ApiResponseFor200) | OK

#### s3_service_get_price.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3GetPriceResponse**](../../models/S3GetPriceResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **s3_service_get_quota**
<a name="s3_service_get_quota"></a>
> S3GetQuotaResponse s3_service_get_quota()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import s3_service_api
from beget_openapi_cloud.model.s3_get_quota_response import S3GetQuotaResponse
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
    api_instance = s3_service_api.S3ServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.s3_service_get_quota()
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling S3ServiceApi->s3_service_get_quota: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#s3_service_get_quota.ApiResponseFor200) | OK

#### s3_service_get_quota.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**S3GetQuotaResponse**](../../models/S3GetQuotaResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


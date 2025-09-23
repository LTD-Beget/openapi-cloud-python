<a name="__pageTop"></a>
# beget_openapi_cloud.apis.tags.cdn_service_api.CdnServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cdn_service_change_resource_domains**](#cdn_service_change_resource_domains) | **post** /v1/cloud/cdn/{service_id}/resource-domains | 
[**cdn_service_change_setting**](#cdn_service_change_setting) | **post** /v1/cloud/cdn/{service_id}/setting | 
[**cdn_service_get_price**](#cdn_service_get_price) | **get** /v1/cloud/cdn/price | 
[**cdn_service_get_source_domains**](#cdn_service_get_source_domains) | **get** /v1/cloud/cdn/source-domains | 
[**cdn_service_preload_cache_by_paths**](#cdn_service_preload_cache_by_paths) | **post** /v1/cloud/cdn/{service_id}/preload-cache-by-paths | 
[**cdn_service_purge_all_cache**](#cdn_service_purge_all_cache) | **get** /v1/cloud/cdn/{service_id}/purge-all-cache | 
[**cdn_service_purge_cache_by_paths**](#cdn_service_purge_cache_by_paths) | **post** /v1/cloud/cdn/{service_id}/purge-cache-by-paths | 

# **cdn_service_change_resource_domains**
<a name="cdn_service_change_resource_domains"></a>
> CdnChangeResourceDomainsResponse cdn_service_change_resource_domains(service_idcdn_change_resource_domains_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cdn_service_api
from beget_openapi_cloud.model.cdn_change_resource_domains_request import CdnChangeResourceDomainsRequest
from beget_openapi_cloud.model.cdn_change_resource_domains_response import CdnChangeResourceDomainsResponse
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
    api_instance = cdn_service_api.CdnServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = CdnChangeResourceDomainsRequest(
        service_id="service_id_example",
        domain=[
            "domain_example"
        ],
    )
    try:
        api_response = api_instance.cdn_service_change_resource_domains(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CdnServiceApi->cdn_service_change_resource_domains: %s\n" % e)
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
[**CdnChangeResourceDomainsRequest**](../../models/CdnChangeResourceDomainsRequest.md) |  | 


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
200 | [ApiResponseFor200](#cdn_service_change_resource_domains.ApiResponseFor200) | OK

#### cdn_service_change_resource_domains.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CdnChangeResourceDomainsResponse**](../../models/CdnChangeResourceDomainsResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cdn_service_change_setting**
<a name="cdn_service_change_setting"></a>
> CdnChangeSettingResponse cdn_service_change_setting(service_idcdn_change_setting_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cdn_service_api
from beget_openapi_cloud.model.cdn_change_setting_response import CdnChangeSettingResponse
from beget_openapi_cloud.model.cdn_change_setting_request import CdnChangeSettingRequest
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
    api_instance = cdn_service_api.CdnServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = CdnChangeSettingRequest(
        service_id="service_id_example",
        settings=CdnSettings(
            caching_time=1,
            follow_origin_redirect=CdnSettingsFollowOriginRedirect(
                enable=True,
                code=[
                    "HTTP_301"
                ],
            ),
            caching_time_browser=CdnSettingsCachingTimeBrowser(
                enable=True,
                time=1,
            ),
            ignore_cookie=True,
            ignore_query_string=True,
            stale=CdnSettingsStale(
                enable=True,
                type=[
                    "HTTP_403"
                ],
            ),
            geo_acl=CdnSettingsGeoAcl(
                enable=True,
                policy_type="ALLOW",
                excepted_values=dict(
                    "key": CdnSettingsGeoAclStringArray(
                        values=[
                            "values_example"
                        ],
                    ),
                ),
            ),
            referer_acl=CdnSettingsRefererAcl(
                enable=True,
                policy_type="ALLOW",
,
            ),
            ip_address_acl=CdnSettingsIpAddressAcl(
                enable=True,
                policy_type="ALLOW",
,
            ),
            redirect_http_to_https=True,
            user_agent_acl=CdnSettingsUserAgentAcl(
                enable=True,
                policy_type="ALLOW",
,
            ),
            tokenized_url_secure_key=CdnSettingsTokenizedUrlSecureKey(
                enable=True,
                key="key_example",
                include_ip=True,
            ),
            allowed_http_methods=CdnSettingsAllowedHttpMethods(
                enable=True,
                http_method=[
                    "GET"
                ],
            ),
            http3_enabled=True,
            gzip_compression=CdnSettingsGzipCompression(
                enable=True,
,
            ),
            content_slice=True,
            static_request_headers=CdnSettingsStaticRequestHeaders(
                enabled=True,
                value=dict(
                    "key": "key_example",
                ),
            ),
            cors=CdnSettingsCors(
                enabled=True,
,
                always=True,
            ),
            static_response_headers=CdnSettingsStaticResponseHeader(
                enable=True,
                header=[
                    CdnSettingsStaticResponseHeaderHeader(
                        name="name_example",
,
                        always=True,
                    )
                ],
            ),
            response_headers_hiding_policy=CdnSettingsResponseHeadersHidingPolicy(
                enabled=True,
,
                mode="HIDE",
            ),
        ),
    )
    try:
        api_response = api_instance.cdn_service_change_setting(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CdnServiceApi->cdn_service_change_setting: %s\n" % e)
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
[**CdnChangeSettingRequest**](../../models/CdnChangeSettingRequest.md) |  | 


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
200 | [ApiResponseFor200](#cdn_service_change_setting.ApiResponseFor200) | OK

#### cdn_service_change_setting.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CdnChangeSettingResponse**](../../models/CdnChangeSettingResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cdn_service_get_price**
<a name="cdn_service_get_price"></a>
> CdnGetPriceResponse cdn_service_get_price()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cdn_service_api
from beget_openapi_cloud.model.cdn_get_price_response import CdnGetPriceResponse
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
    api_instance = cdn_service_api.CdnServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.cdn_service_get_price()
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CdnServiceApi->cdn_service_get_price: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cdn_service_get_price.ApiResponseFor200) | OK

#### cdn_service_get_price.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CdnGetPriceResponse**](../../models/CdnGetPriceResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cdn_service_get_source_domains**
<a name="cdn_service_get_source_domains"></a>
> CdnGetSourceDomainsResponse cdn_service_get_source_domains()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cdn_service_api
from beget_openapi_cloud.model.cdn_get_source_domains_response import CdnGetSourceDomainsResponse
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
    api_instance = cdn_service_api.CdnServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.cdn_service_get_source_domains()
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CdnServiceApi->cdn_service_get_source_domains: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cdn_service_get_source_domains.ApiResponseFor200) | OK

#### cdn_service_get_source_domains.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CdnGetSourceDomainsResponse**](../../models/CdnGetSourceDomainsResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cdn_service_preload_cache_by_paths**
<a name="cdn_service_preload_cache_by_paths"></a>
> CdnPreloadCacheByPathsResponse cdn_service_preload_cache_by_paths(service_idcdn_preload_cache_by_paths_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cdn_service_api
from beget_openapi_cloud.model.cdn_preload_cache_by_paths_request import CdnPreloadCacheByPathsRequest
from beget_openapi_cloud.model.cdn_preload_cache_by_paths_response import CdnPreloadCacheByPathsResponse
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
    api_instance = cdn_service_api.CdnServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = CdnPreloadCacheByPathsRequest(
        service_id="service_id_example",
        path=[
            "path_example"
        ],
    )
    try:
        api_response = api_instance.cdn_service_preload_cache_by_paths(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CdnServiceApi->cdn_service_preload_cache_by_paths: %s\n" % e)
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
[**CdnPreloadCacheByPathsRequest**](../../models/CdnPreloadCacheByPathsRequest.md) |  | 


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
200 | [ApiResponseFor200](#cdn_service_preload_cache_by_paths.ApiResponseFor200) | OK

#### cdn_service_preload_cache_by_paths.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CdnPreloadCacheByPathsResponse**](../../models/CdnPreloadCacheByPathsResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cdn_service_purge_all_cache**
<a name="cdn_service_purge_all_cache"></a>
> CdnPurgeAllCacheResponse cdn_service_purge_all_cache(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cdn_service_api
from beget_openapi_cloud.model.cdn_purge_all_cache_response import CdnPurgeAllCacheResponse
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
    api_instance = cdn_service_api.CdnServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    try:
        api_response = api_instance.cdn_service_purge_all_cache(
            path_params=path_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CdnServiceApi->cdn_service_purge_all_cache: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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
200 | [ApiResponseFor200](#cdn_service_purge_all_cache.ApiResponseFor200) | OK

#### cdn_service_purge_all_cache.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CdnPurgeAllCacheResponse**](../../models/CdnPurgeAllCacheResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cdn_service_purge_cache_by_paths**
<a name="cdn_service_purge_cache_by_paths"></a>
> CdnPurgeCacheByPathsResponse cdn_service_purge_cache_by_paths(service_idcdn_purge_cache_by_paths_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cdn_service_api
from beget_openapi_cloud.model.cdn_purge_cache_by_paths_response import CdnPurgeCacheByPathsResponse
from beget_openapi_cloud.model.cdn_purge_cache_by_paths_request import CdnPurgeCacheByPathsRequest
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
    api_instance = cdn_service_api.CdnServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = CdnPurgeCacheByPathsRequest(
        service_id="service_id_example",
        path=[
            "path_example"
        ],
    )
    try:
        api_response = api_instance.cdn_service_purge_cache_by_paths(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CdnServiceApi->cdn_service_purge_cache_by_paths: %s\n" % e)
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
[**CdnPurgeCacheByPathsRequest**](../../models/CdnPurgeCacheByPathsRequest.md) |  | 


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
200 | [ApiResponseFor200](#cdn_service_purge_cache_by_paths.ApiResponseFor200) | OK

#### cdn_service_purge_cache_by_paths.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CdnPurgeCacheByPathsResponse**](../../models/CdnPurgeCacheByPathsResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


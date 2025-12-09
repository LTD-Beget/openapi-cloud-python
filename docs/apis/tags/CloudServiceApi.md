<a name="__pageTop"></a>
# beget_openapi_cloud.apis.tags.cloud_service_api.CloudServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_service_bind_project**](#cloud_service_bind_project) | **put** /v1/cloud/{service_id}/project | 
[**cloud_service_change_configuration**](#cloud_service_change_configuration) | **patch** /v1/cloud/{service_id}/configuration | 
[**cloud_service_change_pinned**](#cloud_service_change_pinned) | **put** /v1/cloud/{service_id}/pin | 
[**cloud_service_create**](#cloud_service_create) | **post** /v1/cloud | 
[**cloud_service_get**](#cloud_service_get) | **get** /v1/cloud/{service_id} | 
[**cloud_service_get_configuration_list**](#cloud_service_get_configuration_list) | **get** /v1/cloud/configuration | 
[**cloud_service_get_list**](#cloud_service_get_list) | **get** /v1/cloud | 
[**cloud_service_remove**](#cloud_service_remove) | **delete** /v1/cloud/{service_id} | 
[**cloud_service_update**](#cloud_service_update) | **patch** /v1/cloud/{service_id} | 

# **cloud_service_bind_project**
<a name="cloud_service_bind_project"></a>
> CloudBindProjectResponse cloud_service_bind_project(service_idcloud_bind_project_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cloud_service_api
from beget_openapi_cloud.model.cloud_bind_project_response import CloudBindProjectResponse
from beget_openapi_cloud.model.cloud_bind_project_request import CloudBindProjectRequest
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
    api_instance = cloud_service_api.CloudServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = CloudBindProjectRequest(
        service_id="service_id_example",
        project_id="project_id_example",
    )
    try:
        api_response = api_instance.cloud_service_bind_project(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CloudServiceApi->cloud_service_bind_project: %s\n" % e)
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
[**CloudBindProjectRequest**](../../models/CloudBindProjectRequest.md) |  | 


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
200 | [ApiResponseFor200](#cloud_service_bind_project.ApiResponseFor200) | OK

#### cloud_service_bind_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudBindProjectResponse**](../../models/CloudBindProjectResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cloud_service_change_configuration**
<a name="cloud_service_change_configuration"></a>
> CloudChangeConfigurationResponse cloud_service_change_configuration(service_idcloud_change_configuration_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cloud_service_api
from beget_openapi_cloud.model.cloud_change_configuration_request import CloudChangeConfigurationRequest
from beget_openapi_cloud.model.cloud_change_configuration_response import CloudChangeConfigurationResponse
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
    api_instance = cloud_service_api.CloudServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = CloudChangeConfigurationRequest(
        service_id="service_id_example",
        configuration_id="configuration_id_example",
    )
    try:
        api_response = api_instance.cloud_service_change_configuration(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CloudServiceApi->cloud_service_change_configuration: %s\n" % e)
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
[**CloudChangeConfigurationRequest**](../../models/CloudChangeConfigurationRequest.md) |  | 


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
200 | [ApiResponseFor200](#cloud_service_change_configuration.ApiResponseFor200) | OK

#### cloud_service_change_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudChangeConfigurationResponse**](../../models/CloudChangeConfigurationResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cloud_service_change_pinned**
<a name="cloud_service_change_pinned"></a>
> CloudChangePinnedResponse cloud_service_change_pinned(service_idcloud_change_pinned_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cloud_service_api
from beget_openapi_cloud.model.cloud_change_pinned_request import CloudChangePinnedRequest
from beget_openapi_cloud.model.cloud_change_pinned_response import CloudChangePinnedResponse
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
    api_instance = cloud_service_api.CloudServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = CloudChangePinnedRequest(
        service_id="service_id_example",
        ui_pinned=True,
    )
    try:
        api_response = api_instance.cloud_service_change_pinned(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CloudServiceApi->cloud_service_change_pinned: %s\n" % e)
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
[**CloudChangePinnedRequest**](../../models/CloudChangePinnedRequest.md) |  | 


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
200 | [ApiResponseFor200](#cloud_service_change_pinned.ApiResponseFor200) | OK

#### cloud_service_change_pinned.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudChangePinnedResponse**](../../models/CloudChangePinnedResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cloud_service_create**
<a name="cloud_service_create"></a>
> CloudCreateResponse cloud_service_create(cloud_create_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cloud_service_api
from beget_openapi_cloud.model.cloud_create_response import CloudCreateResponse
from beget_openapi_cloud.model.cloud_create_request import CloudCreateRequest
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
    api_instance = cloud_service_api.CloudServiceApi(api_client)

    # example passing only required values which don't have defaults set
    body = CloudCreateRequest(
        configuration_id="configuration_id_example",
        display_name="display_name_example",
        description="description_example",
        mysql_params=MysqlCreateParams(
            db_name="db_name_example",
            access_password="access_password_example",
            param=dict(
                "key": "key_example",
            ),
            save_pma_password=True,
        ),
        postgresql_params=PostgresqlPgCreateParams(
            db_name="db_name_example",
            role_name="role_name_example",
            password="password_example",
            param=dict(),
        ),
        s3_params=S3S3CreateParams(
            public=True,
            bucket_name="bucket_name_example",
        ),
        cdn_params=CdnCdnCreateParams(
            resource_domain=[
                "resource_domain_example"
            ],
            source_domain=CdnSourceDomain(
                cdn_service_id="cdn_service_id_example",
                source_service_id="source_service_id_example",
                source_service_type="DOMAIN",
                domain="domain_example",
                source_service_display_name="source_service_display_name_example",
                source_service_slug="source_service_slug_example",
            ),
            settings=dict(),
        ),
        extra="extra_example",
        region="region_example",
        project_id="project_id_example",
        ui_pinned=True,
    )
    try:
        api_response = api_instance.cloud_service_create(
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CloudServiceApi->cloud_service_create: %s\n" % e)
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
[**CloudCreateRequest**](../../models/CloudCreateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cloud_service_create.ApiResponseFor200) | OK

#### cloud_service_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudCreateResponse**](../../models/CloudCreateResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cloud_service_get**
<a name="cloud_service_get"></a>
> CloudGetResponse cloud_service_get(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cloud_service_api
from beget_openapi_cloud.model.cloud_get_response import CloudGetResponse
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
    api_instance = cloud_service_api.CloudServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    try:
        api_response = api_instance.cloud_service_get(
            path_params=path_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CloudServiceApi->cloud_service_get: %s\n" % e)
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
200 | [ApiResponseFor200](#cloud_service_get.ApiResponseFor200) | OK

#### cloud_service_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudGetResponse**](../../models/CloudGetResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cloud_service_get_configuration_list**
<a name="cloud_service_get_configuration_list"></a>
> CloudGetConfigurationListResponse cloud_service_get_configuration_list()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cloud_service_api
from beget_openapi_cloud.model.cloud_get_configuration_list_response import CloudGetConfigurationListResponse
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
    api_instance = cloud_service_api.CloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.cloud_service_get_configuration_list()
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CloudServiceApi->cloud_service_get_configuration_list: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cloud_service_get_configuration_list.ApiResponseFor200) | OK

#### cloud_service_get_configuration_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudGetConfigurationListResponse**](../../models/CloudGetConfigurationListResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cloud_service_get_list**
<a name="cloud_service_get_list"></a>
> CloudGetListResponse cloud_service_get_list()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cloud_service_api
from beget_openapi_cloud.model.cloud_get_list_response import CloudGetListResponse
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
    api_instance = cloud_service_api.CloudServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 1,
        'limit': 1,
        'sort': "sort_example",
        'filter': "filter_example",
        'view': "SERVICE_VIEW_FULL",
    }
    try:
        api_response = api_instance.cloud_service_get_list(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CloudServiceApi->cloud_service_get_list: %s\n" % e)
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
offset | OffsetSchema | | optional
limit | LimitSchema | | optional
sort | SortSchema | | optional
filter | FilterSchema | | optional
view | ViewSchema | | optional


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ViewSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["SERVICE_VIEW_FULL", "SERVICE_VIEW_BASIC", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cloud_service_get_list.ApiResponseFor200) | OK

#### cloud_service_get_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudGetListResponse**](../../models/CloudGetListResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cloud_service_remove**
<a name="cloud_service_remove"></a>
> CloudRemoveResponse cloud_service_remove(service_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cloud_service_api
from beget_openapi_cloud.model.cloud_remove_response import CloudRemoveResponse
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
    api_instance = cloud_service_api.CloudServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    try:
        api_response = api_instance.cloud_service_remove(
            path_params=path_params,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CloudServiceApi->cloud_service_remove: %s\n" % e)
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
200 | [ApiResponseFor200](#cloud_service_remove.ApiResponseFor200) | OK

#### cloud_service_remove.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudRemoveResponse**](../../models/CloudRemoveResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cloud_service_update**
<a name="cloud_service_update"></a>
> CloudUpdateResponse cloud_service_update(service_idcloud_update_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_cloud
from beget_openapi_cloud.apis.tags import cloud_service_api
from beget_openapi_cloud.model.cloud_update_response import CloudUpdateResponse
from beget_openapi_cloud.model.cloud_update_request import CloudUpdateRequest
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
    api_instance = cloud_service_api.CloudServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    body = CloudUpdateRequest(
        service_id="service_id_example",
        display_name="display_name_example",
        description="description_example",
    )
    try:
        api_response = api_instance.cloud_service_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_cloud.ApiException as e:
        print("Exception when calling CloudServiceApi->cloud_service_update: %s\n" % e)
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
[**CloudUpdateRequest**](../../models/CloudUpdateRequest.md) |  | 


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
200 | [ApiResponseFor200](#cloud_service_update.ApiResponseFor200) | OK

#### cloud_service_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudUpdateResponse**](../../models/CloudUpdateResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


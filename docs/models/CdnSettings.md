# beget_openapi_cloud.model.cdn_settings.CdnSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**caching_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**follow_origin_redirect** | [**CdnSettingsFollowOriginRedirect**](CdnSettingsFollowOriginRedirect.md) | [**CdnSettingsFollowOriginRedirect**](CdnSettingsFollowOriginRedirect.md) |  | [optional] 
**caching_time_browser** | [**CdnSettingsCachingTimeBrowser**](CdnSettingsCachingTimeBrowser.md) | [**CdnSettingsCachingTimeBrowser**](CdnSettingsCachingTimeBrowser.md) |  | [optional] 
**ignore_cookie** | bool,  | BoolClass,  |  | [optional] 
**ignore_query_string** | bool,  | BoolClass,  |  | [optional] 
**stale** | [**CdnSettingsStale**](CdnSettingsStale.md) | [**CdnSettingsStale**](CdnSettingsStale.md) |  | [optional] 
**geo_acl** | [**CdnSettingsGeoAcl**](CdnSettingsGeoAcl.md) | [**CdnSettingsGeoAcl**](CdnSettingsGeoAcl.md) |  | [optional] 
**referer_acl** | [**CdnSettingsRefererAcl**](CdnSettingsRefererAcl.md) | [**CdnSettingsRefererAcl**](CdnSettingsRefererAcl.md) |  | [optional] 
**ip_address_acl** | [**CdnSettingsIpAddressAcl**](CdnSettingsIpAddressAcl.md) | [**CdnSettingsIpAddressAcl**](CdnSettingsIpAddressAcl.md) |  | [optional] 
**redirect_http_to_https** | bool,  | BoolClass,  |  | [optional] 
**user_agent_acl** | [**CdnSettingsUserAgentAcl**](CdnSettingsUserAgentAcl.md) | [**CdnSettingsUserAgentAcl**](CdnSettingsUserAgentAcl.md) |  | [optional] 
**tokenized_url_secure_key** | [**CdnSettingsTokenizedUrlSecureKey**](CdnSettingsTokenizedUrlSecureKey.md) | [**CdnSettingsTokenizedUrlSecureKey**](CdnSettingsTokenizedUrlSecureKey.md) |  | [optional] 
**allowed_http_methods** | [**CdnSettingsAllowedHttpMethods**](CdnSettingsAllowedHttpMethods.md) | [**CdnSettingsAllowedHttpMethods**](CdnSettingsAllowedHttpMethods.md) |  | [optional] 
**http3_enabled** | bool,  | BoolClass,  |  | [optional] 
**gzip_compression** | [**CdnSettingsGzipCompression**](CdnSettingsGzipCompression.md) | [**CdnSettingsGzipCompression**](CdnSettingsGzipCompression.md) |  | [optional] 
**content_slice** | bool,  | BoolClass,  |  | [optional] 
**static_request_headers** | [**CdnSettingsStaticRequestHeaders**](CdnSettingsStaticRequestHeaders.md) | [**CdnSettingsStaticRequestHeaders**](CdnSettingsStaticRequestHeaders.md) |  | [optional] 
**cors** | [**CdnSettingsCors**](CdnSettingsCors.md) | [**CdnSettingsCors**](CdnSettingsCors.md) |  | [optional] 
**static_response_headers** | [**CdnSettingsStaticResponseHeader**](CdnSettingsStaticResponseHeader.md) | [**CdnSettingsStaticResponseHeader**](CdnSettingsStaticResponseHeader.md) |  | [optional] 
**response_headers_hiding_policy** | [**CdnSettingsResponseHeadersHidingPolicy**](CdnSettingsResponseHeadersHidingPolicy.md) | [**CdnSettingsResponseHeadersHidingPolicy**](CdnSettingsResponseHeadersHidingPolicy.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


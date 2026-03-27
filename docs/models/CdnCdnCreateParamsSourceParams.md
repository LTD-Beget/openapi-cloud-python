# beget_openapi_cloud.model.cdn_cdn_create_params_source_params.CdnCdnCreateParamsSourceParams

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cdn_service_id** | str,  | str,  |  | [optional] 
**source_service_id** | str,  | str,  |  | [optional] 
**source_service_type** | str,  | str,  |  | [optional] must be one of ["DOMAIN", "S3", "VPS", ] 
**domain** | str,  | str,  |  | [optional] 
**source_protocol** | str,  | str,  |  | [optional] must be one of ["HTTPS", "HTTP", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


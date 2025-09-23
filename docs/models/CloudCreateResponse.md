# beget_openapi_cloud.model.cloud_create_response.CloudCreateResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**service** | [**CloudService**](CloudService.md) | [**CloudService**](CloudService.md) |  | [optional] 
**mysql_error** | [**MysqlCreateError**](MysqlCreateError.md) | [**MysqlCreateError**](MysqlCreateError.md) |  | [optional] 
**postgresql_error** | [**PostgresqlPgCreateError**](PostgresqlPgCreateError.md) | [**PostgresqlPgCreateError**](PostgresqlPgCreateError.md) |  | [optional] 
**s3_error** | [**S3S3CreateError**](S3S3CreateError.md) | [**S3S3CreateError**](S3S3CreateError.md) |  | [optional] 
**cdn_error** | [**CdnCdnCreateError**](CdnCdnCreateError.md) | [**CdnCdnCreateError**](CdnCdnCreateError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


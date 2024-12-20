# beget_openapi_cloud.model.cloud_create_request.CloudCreateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**configuration_id** | str,  | str,  |  | [optional] 
**display_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**mysql_params** | [**MysqlCreateParams**](MysqlCreateParams.md) | [**MysqlCreateParams**](MysqlCreateParams.md) |  | [optional] 
**postgresql_params** | [**PostgresqlPgCreateParams**](PostgresqlPgCreateParams.md) | [**PostgresqlPgCreateParams**](PostgresqlPgCreateParams.md) |  | [optional] 
**s3_params** | [**S3S3CreateParams**](S3S3CreateParams.md) | [**S3S3CreateParams**](S3S3CreateParams.md) |  | [optional] 
**extra** | str,  | str,  |  | [optional] 
**region** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


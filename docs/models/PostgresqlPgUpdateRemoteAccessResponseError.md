# beget_openapi_cloud.model.postgresql_pg_update_remote_access_response_error.PostgresqlPgUpdateRemoteAccessResponseError

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**code** | str,  | str,  |  | [optional] must be one of ["_", "INVALID_STATE", "SERVICE_DISABLED", "INVALID_SUBNET_ADDRESS", "IP_IS_IN_EXISTED_SUBNET", "SUBNET_IS_IN_EXISTED_SUBNET", "SUBNET_IS_PRIVATE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


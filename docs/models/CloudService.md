# beget_openapi_cloud.model.cloud_service.CloudService

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**configuration_id** | str,  | str,  |  | [optional] 
**display_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["CREATING", "RUNNING", "RESTARTING", "STOPPED", "RECONFIGURING", ] 
**created_at** | str,  | str,  |  | [optional] 
**price_day** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**price_month** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**mysql5** | [**MysqlMysql5**](MysqlMysql5.md) | [**MysqlMysql5**](MysqlMysql5.md) |  | [optional] 
**mysql8** | [**MysqlMysql8**](MysqlMysql8.md) | [**MysqlMysql8**](MysqlMysql8.md) |  | [optional] 
**postgresql15** | [**PostgresqlPostgresql15**](PostgresqlPostgresql15.md) | [**PostgresqlPostgresql15**](PostgresqlPostgresql15.md) |  | [optional] 
**postgresql14** | [**PostgresqlPostgresql14**](PostgresqlPostgresql14.md) | [**PostgresqlPostgresql14**](PostgresqlPostgresql14.md) |  | [optional] 
**manage_enabled** | bool,  | BoolClass,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**[monitorable_resources](#monitorable_resources)** | list, tuple,  | tuple,  |  | [optional] 
**unblocking** | bool,  | BoolClass,  |  | [optional] 
**migrating** | bool,  | BoolClass,  |  | [optional] 
**region** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# monitorable_resources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


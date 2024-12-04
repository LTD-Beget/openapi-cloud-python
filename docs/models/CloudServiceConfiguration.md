# beget_openapi_cloud.model.cloud_service_configuration.CloudServiceConfiguration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**price_day** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**price_month** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**region** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["MYSQL5", "MYSQL8", "MYSQL84", "POSTGRESQL14", "POSTGRESQL15", "S_3", "POSTGRESQL164", ] 
**mysql5** | [**MysqlMysql5Configuration**](MysqlMysql5Configuration.md) | [**MysqlMysql5Configuration**](MysqlMysql5Configuration.md) |  | [optional] 
**mysql8** | [**MysqlMysql8Configuration**](MysqlMysql8Configuration.md) | [**MysqlMysql8Configuration**](MysqlMysql8Configuration.md) |  | [optional] 
**mysql84** | [**MysqlMysql84Configuration**](MysqlMysql84Configuration.md) | [**MysqlMysql84Configuration**](MysqlMysql84Configuration.md) |  | [optional] 
**postgresql15** | [**PostgresqlPostgresql15Configuration**](PostgresqlPostgresql15Configuration.md) | [**PostgresqlPostgresql15Configuration**](PostgresqlPostgresql15Configuration.md) |  | [optional] 
**postgresql14** | [**PostgresqlPostgresql14Configuration**](PostgresqlPostgresql14Configuration.md) | [**PostgresqlPostgresql14Configuration**](PostgresqlPostgresql14Configuration.md) |  | [optional] 
**postgresql164** | [**PostgresqlPostgresql164Configuration**](PostgresqlPostgresql164Configuration.md) | [**PostgresqlPostgresql164Configuration**](PostgresqlPostgresql164Configuration.md) |  | [optional] 
**s3** | [**S3S3Configuration**](S3S3Configuration.md) | [**S3S3Configuration**](S3S3Configuration.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


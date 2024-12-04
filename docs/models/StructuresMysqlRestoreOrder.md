# beget_openapi_cloud.model.structures_mysql_restore_order.StructuresMysqlRestoreOrder

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**copy_info** | [**StructuresMysqlCopy**](StructuresMysqlCopy.md) | [**StructuresMysqlCopy**](StructuresMysqlCopy.md) |  | [optional] 
**backup_date_create** | str,  | str,  |  | [optional] 
**service_id** | str,  | str,  |  | [optional] 
**service_name** | str,  | str,  |  | [optional] 
**date_create** | str,  | str,  |  | [optional] 
**date_complete** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["_", "PROCESSING", "COMPLETED", "ERROR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


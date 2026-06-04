# beget_openapi_cloud.model.network_drive_get_limits_response_limits.NetworkDriveGetLimitsResponseLimits

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**region** | str,  | str,  |  | [optional] 
**max_network_drives** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**available_network_drives** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**max_mounts_per_resource** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[max_total_size](#max_total_size)** | list, tuple,  | tuple,  |  | [optional] 
**[available_total_size](#available_total_size)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# max_total_size

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NetworkDriveGetLimitsResponseLimitsTotalSize**](NetworkDriveGetLimitsResponseLimitsTotalSize.md) | [**NetworkDriveGetLimitsResponseLimitsTotalSize**](NetworkDriveGetLimitsResponseLimitsTotalSize.md) | [**NetworkDriveGetLimitsResponseLimitsTotalSize**](NetworkDriveGetLimitsResponseLimitsTotalSize.md) |  | 

# available_total_size

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NetworkDriveGetLimitsResponseLimitsTotalSize**](NetworkDriveGetLimitsResponseLimitsTotalSize.md) | [**NetworkDriveGetLimitsResponseLimitsTotalSize**](NetworkDriveGetLimitsResponseLimitsTotalSize.md) | [**NetworkDriveGetLimitsResponseLimitsTotalSize**](NetworkDriveGetLimitsResponseLimitsTotalSize.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


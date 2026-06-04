# beget_openapi_cloud.model.network_drive_network_drive.NetworkDriveNetworkDrive

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**storage_class** | str,  | str,  |  | [optional] must be one of ["_", "NVME", "HDD", ] 
**mounted_resource** | [**NetworkDriveNetworkDriveMountedResource**](NetworkDriveNetworkDriveMountedResource.md) | [**NetworkDriveNetworkDriveMountedResource**](NetworkDriveNetworkDriveMountedResource.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


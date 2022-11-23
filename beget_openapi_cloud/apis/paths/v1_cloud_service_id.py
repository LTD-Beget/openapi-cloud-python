from beget_openapi_cloud.paths.v1_cloud_service_id.get import ApiForget
from beget_openapi_cloud.paths.v1_cloud_service_id.delete import ApiFordelete
from beget_openapi_cloud.paths.v1_cloud_service_id.patch import ApiForpatch


class V1CloudServiceId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

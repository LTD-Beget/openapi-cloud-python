# coding: utf-8

"""
    API Управляемых сервисов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.4.0
    Generated by: https://openapi-generator.tech
"""

from beget_openapi_cloud.paths.v1_cloud_s3_service_id_access_key.patch import S3ServiceChangeAccessKey
from beget_openapi_cloud.paths.v1_cloud_s3_service_id_cors.patch import S3ServiceChangeCors
from beget_openapi_cloud.paths.v1_cloud_s3_service_id_domain.patch import S3ServiceChangeDomain
from beget_openapi_cloud.paths.v1_cloud_s3_service_id_public.patch import S3ServiceChangePublic
from beget_openapi_cloud.paths.v1_cloud_s3_prefix.get import S3ServiceGetPrefix
from beget_openapi_cloud.paths.v1_cloud_s3_price.get import S3ServiceGetPrice
from beget_openapi_cloud.paths.v1_cloud_s3_quota.get import S3ServiceGetQuota


class S3ServiceApi(
    S3ServiceChangeAccessKey,
    S3ServiceChangeCors,
    S3ServiceChangeDomain,
    S3ServiceChangePublic,
    S3ServiceGetPrefix,
    S3ServiceGetPrice,
    S3ServiceGetQuota,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
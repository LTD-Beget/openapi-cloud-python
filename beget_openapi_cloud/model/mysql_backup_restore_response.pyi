# coding: utf-8

"""
    API Управляемых сервисов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.4.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from beget_openapi_cloud import schemas  # noqa: F401


class MysqlBackupRestoreResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def items() -> typing.Type['StructuresMysqlRestoreOrder']:
                return StructuresMysqlRestoreOrder
        
            @staticmethod
            def error() -> typing.Type['MysqlBackupRestoreResponseError']:
                return MysqlBackupRestoreResponseError
            __annotations__ = {
                "items": items,
                "error": error,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> 'StructuresMysqlRestoreOrder': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> 'MysqlBackupRestoreResponseError': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["items", "error", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union['StructuresMysqlRestoreOrder', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union['MysqlBackupRestoreResponseError', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["items", "error", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        items: typing.Union['StructuresMysqlRestoreOrder', schemas.Unset] = schemas.unset,
        error: typing.Union['MysqlBackupRestoreResponseError', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MysqlBackupRestoreResponse':
        return super().__new__(
            cls,
            *args,
            items=items,
            error=error,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_cloud.model.mysql_backup_restore_response_error import MysqlBackupRestoreResponseError
from beget_openapi_cloud.model.structures_mysql_restore_order import StructuresMysqlRestoreOrder
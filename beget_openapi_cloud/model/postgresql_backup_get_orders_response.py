# coding: utf-8

"""
    API Управляемых сервисов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.4.2
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


class PostgresqlBackupGetOrdersResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class order(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StructuresPostgresqlRestoreOrder']:
                        return StructuresPostgresqlRestoreOrder
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StructuresPostgresqlRestoreOrder'], typing.List['StructuresPostgresqlRestoreOrder']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'order':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StructuresPostgresqlRestoreOrder':
                    return super().__getitem__(i)
            __annotations__ = {
                "order": order,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["order", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["order", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        order: typing.Union[MetaOapg.properties.order, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostgresqlBackupGetOrdersResponse':
        return super().__new__(
            cls,
            *args,
            order=order,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_cloud.model.structures_postgresql_restore_order import StructuresPostgresqlRestoreOrder

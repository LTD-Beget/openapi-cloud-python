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


class PostgresqlPgCreateDbRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            service_id = schemas.StrSchema
            db_name = schemas.StrSchema
            owner_name = schemas.StrSchema
            description = schemas.StrSchema
            __annotations__ = {
                "service_id": service_id,
                "db_name": db_name,
                "owner_name": owner_name,
                "description": description,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service_id"]) -> MetaOapg.properties.service_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["db_name"]) -> MetaOapg.properties.db_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_name"]) -> MetaOapg.properties.owner_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["service_id", "db_name", "owner_name", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service_id"]) -> typing.Union[MetaOapg.properties.service_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["db_name"]) -> typing.Union[MetaOapg.properties.db_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_name"]) -> typing.Union[MetaOapg.properties.owner_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["service_id", "db_name", "owner_name", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        service_id: typing.Union[MetaOapg.properties.service_id, str, schemas.Unset] = schemas.unset,
        db_name: typing.Union[MetaOapg.properties.db_name, str, schemas.Unset] = schemas.unset,
        owner_name: typing.Union[MetaOapg.properties.owner_name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostgresqlPgCreateDbRequest':
        return super().__new__(
            cls,
            *args,
            service_id=service_id,
            db_name=db_name,
            owner_name=owner_name,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )

# coding: utf-8

"""
    API Управляемых сервисов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.1.1
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


class MysqlCreateParams(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            db_name = schemas.StrSchema
            access_password = schemas.StrSchema
            
            
            class param(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'param':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            preset_name = schemas.StrSchema
            save_pma_password = schemas.BoolSchema
            __annotations__ = {
                "db_name": db_name,
                "access_password": access_password,
                "param": param,
                "preset_name": preset_name,
                "save_pma_password": save_pma_password,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["db_name"]) -> MetaOapg.properties.db_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_password"]) -> MetaOapg.properties.access_password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["param"]) -> MetaOapg.properties.param: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preset_name"]) -> MetaOapg.properties.preset_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["save_pma_password"]) -> MetaOapg.properties.save_pma_password: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["db_name", "access_password", "param", "preset_name", "save_pma_password", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["db_name"]) -> typing.Union[MetaOapg.properties.db_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_password"]) -> typing.Union[MetaOapg.properties.access_password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["param"]) -> typing.Union[MetaOapg.properties.param, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preset_name"]) -> typing.Union[MetaOapg.properties.preset_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["save_pma_password"]) -> typing.Union[MetaOapg.properties.save_pma_password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["db_name", "access_password", "param", "preset_name", "save_pma_password", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        db_name: typing.Union[MetaOapg.properties.db_name, str, schemas.Unset] = schemas.unset,
        access_password: typing.Union[MetaOapg.properties.access_password, str, schemas.Unset] = schemas.unset,
        param: typing.Union[MetaOapg.properties.param, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        preset_name: typing.Union[MetaOapg.properties.preset_name, str, schemas.Unset] = schemas.unset,
        save_pma_password: typing.Union[MetaOapg.properties.save_pma_password, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MysqlCreateParams':
        return super().__new__(
            cls,
            *args,
            db_name=db_name,
            access_password=access_password,
            param=param,
            preset_name=preset_name,
            save_pma_password=save_pma_password,
            _configuration=_configuration,
            **kwargs,
        )
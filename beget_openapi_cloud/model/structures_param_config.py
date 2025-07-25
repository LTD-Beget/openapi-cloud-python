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


class StructuresParamConfig(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            documentation_link = schemas.StrSchema
            integer_value = schemas.DictSchema
            float_value = schemas.DictSchema
            string_value = schemas.DictSchema
        
            @staticmethod
            def enum_value() -> typing.Type['StructuresParamConfigEnumValue']:
                return StructuresParamConfigEnumValue
        
            @staticmethod
            def set_value() -> typing.Type['StructuresParamConfigSetValue']:
                return StructuresParamConfigSetValue
            __annotations__ = {
                "name": name,
                "documentation_link": documentation_link,
                "integer_value": integer_value,
                "float_value": float_value,
                "string_value": string_value,
                "enum_value": enum_value,
                "set_value": set_value,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentation_link"]) -> MetaOapg.properties.documentation_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integer_value"]) -> MetaOapg.properties.integer_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float_value"]) -> MetaOapg.properties.float_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["string_value"]) -> MetaOapg.properties.string_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_value"]) -> 'StructuresParamConfigEnumValue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["set_value"]) -> 'StructuresParamConfigSetValue': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "documentation_link", "integer_value", "float_value", "string_value", "enum_value", "set_value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentation_link"]) -> typing.Union[MetaOapg.properties.documentation_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["integer_value"]) -> typing.Union[MetaOapg.properties.integer_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["float_value"]) -> typing.Union[MetaOapg.properties.float_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["string_value"]) -> typing.Union[MetaOapg.properties.string_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enum_value"]) -> typing.Union['StructuresParamConfigEnumValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["set_value"]) -> typing.Union['StructuresParamConfigSetValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "documentation_link", "integer_value", "float_value", "string_value", "enum_value", "set_value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        documentation_link: typing.Union[MetaOapg.properties.documentation_link, str, schemas.Unset] = schemas.unset,
        integer_value: typing.Union[MetaOapg.properties.integer_value, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        float_value: typing.Union[MetaOapg.properties.float_value, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        string_value: typing.Union[MetaOapg.properties.string_value, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        enum_value: typing.Union['StructuresParamConfigEnumValue', schemas.Unset] = schemas.unset,
        set_value: typing.Union['StructuresParamConfigSetValue', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StructuresParamConfig':
        return super().__new__(
            cls,
            *args,
            name=name,
            documentation_link=documentation_link,
            integer_value=integer_value,
            float_value=float_value,
            string_value=string_value,
            enum_value=enum_value,
            set_value=set_value,
            _configuration=_configuration,
            **kwargs,
        )

from beget_openapi_cloud.model.structures_param_config_enum_value import StructuresParamConfigEnumValue
from beget_openapi_cloud.model.structures_param_config_set_value import StructuresParamConfigSetValue

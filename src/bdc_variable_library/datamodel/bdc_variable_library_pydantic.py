from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'bdc_variable_library',
     'default_range': 'string',
     'description': 'LinkML models for variables in the BDC Knowledge Library',
     'id': 'https://w3id.org/linkml/bdc-variable-library',
     'imports': ['linkml:types'],
     'license': 'BSD-3-Clause',
     'name': 'bdc-variable-library',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'bdc_variable_library': {'prefix_prefix': 'bdc_variable_library',
                                           'prefix_reference': 'https://w3id.org/linkml/bdc-variable-library/'},
                  'bdchm': {'prefix_prefix': 'bdchm',
                            'prefix_reference': 'https://w3id.org/bdchm/'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'http://www.example.org/rdf#'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://linkml.github.io/bdc-variable-library'],
     'source_file': 'src/bdc_variable_library/schema/bdc_variable_library.yaml',
     'title': 'bdc-variable-library'} )

class DataTypeEnum(str, Enum):
    """
    A category of data
    """
    NUMERIC = "NUMERIC"
    """
    decimal or integer data type for continuous variables
    """
    STRING = "STRING"
    """
    free text data type
    """
    CODE = "CODE"
    """
    data are a list of acceptable values or a controlled vocabulary
    """


class BdchmTypeEnum(str, Enum):
    """
    A list of BDCHM entities used to describe variables
    """
    OBSERVATION = "OBSERVATION"
    CONDITION = "CONDITION"
    PROCEDURE = "PROCEDURE"
    EXPOSURE = "EXPOSURE"



class Entity(ConfiguredBaseModel):
    """
    Any resource that has its own identifier
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/linkml/bdc-variable-library'})

    id: str = Field(default=..., description="""A unique identifier for a variable within BDC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })


class Variable(Entity):
    """
    A generic grouping for any variable
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/bdc-variable-library'})

    associated_study: Optional[str] = Field(default=None, description="""The study that produced the variable data""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable'], 'slot_uri': 'bdchm:ResearchStudy'} })
    variable_description: Optional[str] = Field(default=None, description="""Human readable description of the variable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    concept_type: Optional[str] = Field(default=None, description="""CURIE describing the main content of the variable. This can be from OBA, OMOP, or LOINC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    variable_label: Optional[str] = Field(default=None, description="""Human readable label describing the variable""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    id: str = Field(default=..., description="""A unique identifier for a variable within BDC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })


class SingleVariable(Variable):
    """
    Represents a single entry in a data dictionary
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/bdc-variable-library'})

    source_id: Optional[str] = Field(default=None, description="""Identifier used by the organization providing the variable to BDC to uniquely identify the variable in their system. In most cases this will be a phv value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    file_id: Optional[str] = Field(default=None, description="""Identifier used by the organization providing the variable to BDC to uniquely identify the file or data table in their system. In most cases this will be a pht value""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    file_name: Optional[str] = Field(default=None, description="""Name of file containing variable data""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    variable_name: Optional[str] = Field(default=None, description="""The name of the variable according to the original data provider Corresponds to the VARNAME field in dbGAP""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    source_variable_description: Optional[str] = Field(default=None, description="""Description of the variable provided by the original data provider Corresponds to the VARDESC field in dbGAP""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    data_type: Optional[DataTypeEnum] = Field(default=None, description="""The data type found in this variable. Corresponds to the TYPE field in dbGAP""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    unit: Optional[str] = Field(default=None, description="""Ideally a unit of measure from UCUM. Corresponds to the UNITS field in dbGAP""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    minimum_value: Optional[Decimal] = Field(default=None, description="""The lowest value present in the data for this variable. Corresponds to  the MIN field in dbGAP""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    maximum_value: Optional[Decimal] = Field(default=None, description="""The highest value present in the data for this variable. Corresponds to the MAX field in dbGAP""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    resolution: Optional[int] = Field(default=None, description="""The number of decimal places a measurement is represented in the data. Corresponds to the RESOLUTION field in dbGAP""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    coded_values: Optional[str] = Field(default=None, description="""Pipe-delimited string of allowable values. Should only be used if the data_type is enum. Corresponds to VALUES field in dbGAP""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    missing_value: Optional[list[str]] = Field(default=None, description="""Sentinel value to indicate a missing value or other data nuance""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    comment: Optional[str] = Field(default=None, description="""Any text comment provided by the original data provider. Corresponds to the  COMMENT field in dbGAP""", json_schema_extra = { "linkml_meta": {'domain_of': ['SingleVariable']} })
    associated_study: Optional[str] = Field(default=None, description="""The study that produced the variable data""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable'], 'slot_uri': 'bdchm:ResearchStudy'} })
    variable_description: Optional[str] = Field(default=None, description="""Human readable description of the variable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    concept_type: Optional[str] = Field(default=None, description="""CURIE describing the main content of the variable. This can be from OBA, OMOP, or LOINC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    variable_label: Optional[str] = Field(default=None, description="""Human readable label describing the variable""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    id: str = Field(default=..., description="""A unique identifier for a variable within BDC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })


class CompoundVariable(Variable):
    """
    Represents a variable and all metadata
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/bdc-variable-library'})

    cde_id: Optional[str] = Field(default=None, description="""CURIE from Condor""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompoundVariable']} })
    bdchm_type: Optional[BdchmTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompoundVariable']} })
    metadata: Optional[list[str]] = Field(default=None, description="""List of variable identifiers providing metadata for a compound variable""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompoundVariable']} })
    alert_value: Optional[list[str]] = Field(default=None, description="""List of values that provide extra optional information about a variable. Often this is used to indicate a violation of QA/QC""", json_schema_extra = { "linkml_meta": {'domain_of': ['CompoundVariable']} })
    associated_study: Optional[str] = Field(default=None, description="""The study that produced the variable data""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable'], 'slot_uri': 'bdchm:ResearchStudy'} })
    variable_description: Optional[str] = Field(default=None, description="""Human readable description of the variable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    concept_type: Optional[str] = Field(default=None, description="""CURIE describing the main content of the variable. This can be from OBA, OMOP, or LOINC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    variable_label: Optional[str] = Field(default=None, description="""Human readable label describing the variable""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variable']} })
    id: str = Field(default=..., description="""A unique identifier for a variable within BDC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })


class MissingValue(Entity):
    """
    Character used to indicate a missing value in a data set
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/bdc-variable-library'})

    indicator_char: Optional[str] = Field(default=None, description="""Sentinel value used to add information to a datum or indicate a missing datum""", json_schema_extra = { "linkml_meta": {'domain_of': ['MissingValue', 'AlertValue']} })
    indicator_meaning: Optional[str] = Field(default=None, description="""Meaning of the indicator character verbatim from original data provider when possible""", json_schema_extra = { "linkml_meta": {'domain_of': ['MissingValue', 'AlertValue']} })
    id: str = Field(default=..., description="""A unique identifier for a variable within BDC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })


class AlertValue(Entity):
    """
    Character used to add information to a datum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/bdc-variable-library'})

    indicator_char: Optional[str] = Field(default=None, description="""Sentinel value used to add information to a datum or indicate a missing datum""", json_schema_extra = { "linkml_meta": {'domain_of': ['MissingValue', 'AlertValue']} })
    indicator_meaning: Optional[str] = Field(default=None, description="""Meaning of the indicator character verbatim from original data provider when possible""", json_schema_extra = { "linkml_meta": {'domain_of': ['MissingValue', 'AlertValue']} })
    id: str = Field(default=..., description="""A unique identifier for a variable within BDC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })


class ResearchStudy(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'bdchm:ResearchStudy',
         'from_schema': 'https://w3id.org/linkml/bdc-variable-library'})

    id: str = Field(default=..., description="""A unique identifier for a variable within BDC""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Entity.model_rebuild()
Variable.model_rebuild()
SingleVariable.model_rebuild()
CompoundVariable.model_rebuild()
MissingValue.model_rebuild()
AlertValue.model_rebuild()
ResearchStudy.model_rebuild()

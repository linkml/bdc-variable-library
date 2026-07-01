# Auto generated from bdc_variable_library.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-01T15:26:04
# Schema: bdc-variable-library
#
# id: https://w3id.org/linkml/bdc-variable-library
# description: LinkML models for variables in the BDC Knowledge Library
# license: BSD-3-Clause

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Decimal, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Decimal, URIorCURIE

metamodel_version = "1.11.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BDC_VARIABLE_LIBRARY = CurieNamespace('bdc_variable_library', 'https://w3id.org/linkml/bdc-variable-library/')
BDCHM = CurieNamespace('bdchm', 'https://w3id.org/bdchm/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
EXAMPLE = CurieNamespace('example', 'http://www.example.org/rdf#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = BDC_VARIABLE_LIBRARY


# Types

# Class references
class EntityId(URIorCURIE):
    pass


class VariableId(EntityId):
    pass


class SingleVariableId(VariableId):
    pass


class CompoundVariableId(VariableId):
    pass


class MissingValueId(EntityId):
    pass


class AlertValueId(EntityId):
    pass


class ResearchStudyId(EntityId):
    pass


@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    Any resource that has its own identifier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Entity

    id: Union[str, EntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Variable(Entity):
    """
    A generic grouping for any variable
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["Variable"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:Variable"
    class_name: ClassVar[str] = "Variable"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Variable

    id: Union[str, VariableId] = None
    associated_study: Optional[Union[str, ResearchStudyId]] = None
    variable_description: Optional[str] = None
    concept_type: Optional[Union[str, URIorCURIE]] = None
    variable_label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariableId):
            self.id = VariableId(self.id)

        if self.associated_study is not None and not isinstance(self.associated_study, ResearchStudyId):
            self.associated_study = ResearchStudyId(self.associated_study)

        if self.variable_description is not None and not isinstance(self.variable_description, str):
            self.variable_description = str(self.variable_description)

        if self.concept_type is not None and not isinstance(self.concept_type, URIorCURIE):
            self.concept_type = URIorCURIE(self.concept_type)

        if self.variable_label is not None and not isinstance(self.variable_label, str):
            self.variable_label = str(self.variable_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SingleVariable(Variable):
    """
    Represents a single entry in a data dictionary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["SingleVariable"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:SingleVariable"
    class_name: ClassVar[str] = "SingleVariable"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.SingleVariable

    id: Union[str, SingleVariableId] = None
    source_id: Optional[str] = None
    file_id: Optional[str] = None
    file_name: Optional[str] = None
    variable_name: Optional[str] = None
    source_variable_description: Optional[str] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None
    unit: Optional[str] = None
    minimum_value: Optional[Decimal] = None
    maximum_value: Optional[Decimal] = None
    resolution: Optional[int] = None
    coded_values: Optional[str] = None
    missing_value: Optional[Union[Union[str, MissingValueId], list[Union[str, MissingValueId]]]] = empty_list()
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SingleVariableId):
            self.id = SingleVariableId(self.id)

        if self.source_id is not None and not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        if self.file_id is not None and not isinstance(self.file_id, str):
            self.file_id = str(self.file_id)

        if self.file_name is not None and not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.variable_name is not None and not isinstance(self.variable_name, str):
            self.variable_name = str(self.variable_name)

        if self.source_variable_description is not None and not isinstance(self.source_variable_description, str):
            self.source_variable_description = str(self.source_variable_description)

        if self.data_type is not None and not isinstance(self.data_type, DataTypeEnum):
            self.data_type = DataTypeEnum(self.data_type)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.minimum_value is not None and not isinstance(self.minimum_value, Decimal):
            self.minimum_value = Decimal(self.minimum_value)

        if self.maximum_value is not None and not isinstance(self.maximum_value, Decimal):
            self.maximum_value = Decimal(self.maximum_value)

        if self.resolution is not None and not isinstance(self.resolution, int):
            self.resolution = int(self.resolution)

        if self.coded_values is not None and not isinstance(self.coded_values, str):
            self.coded_values = str(self.coded_values)

        if not isinstance(self.missing_value, list):
            self.missing_value = [self.missing_value] if self.missing_value is not None else []
        self.missing_value = [v if isinstance(v, MissingValueId) else MissingValueId(v) for v in self.missing_value]

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundVariable(Variable):
    """
    Represents a variable and all metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundVariable"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundVariable"
    class_name: ClassVar[str] = "CompoundVariable"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundVariable

    id: Union[str, CompoundVariableId] = None
    cde_id: Optional[Union[str, URIorCURIE]] = None
    bdchm_type: Optional[Union[str, "BdchmTypeEnum"]] = None
    metadata: Optional[Union[str, list[str]]] = empty_list()
    alert_value: Optional[Union[Union[str, AlertValueId], list[Union[str, AlertValueId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundVariableId):
            self.id = CompoundVariableId(self.id)

        if self.cde_id is not None and not isinstance(self.cde_id, URIorCURIE):
            self.cde_id = URIorCURIE(self.cde_id)

        if self.bdchm_type is not None and not isinstance(self.bdchm_type, BdchmTypeEnum):
            self.bdchm_type = BdchmTypeEnum(self.bdchm_type)

        if not isinstance(self.metadata, list):
            self.metadata = [self.metadata] if self.metadata is not None else []
        self.metadata = [v if isinstance(v, str) else str(v) for v in self.metadata]

        if not isinstance(self.alert_value, list):
            self.alert_value = [self.alert_value] if self.alert_value is not None else []
        self.alert_value = [v if isinstance(v, AlertValueId) else AlertValueId(v) for v in self.alert_value]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MissingValue(Entity):
    """
    Character used to indicate a missing value in a data set
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["MissingValue"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:MissingValue"
    class_name: ClassVar[str] = "MissingValue"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.MissingValue

    id: Union[str, MissingValueId] = None
    indicator_char: Optional[str] = None
    indicator_meaning: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MissingValueId):
            self.id = MissingValueId(self.id)

        if self.indicator_char is not None and not isinstance(self.indicator_char, str):
            self.indicator_char = str(self.indicator_char)

        if self.indicator_meaning is not None and not isinstance(self.indicator_meaning, str):
            self.indicator_meaning = str(self.indicator_meaning)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlertValue(Entity):
    """
    Character used to add information to a datum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["AlertValue"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:AlertValue"
    class_name: ClassVar[str] = "AlertValue"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AlertValue

    id: Union[str, AlertValueId] = None
    indicator_char: Optional[str] = None
    indicator_meaning: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlertValueId):
            self.id = AlertValueId(self.id)

        if self.indicator_char is not None and not isinstance(self.indicator_char, str):
            self.indicator_char = str(self.indicator_char)

        if self.indicator_meaning is not None and not isinstance(self.indicator_meaning, str):
            self.indicator_meaning = str(self.indicator_meaning)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResearchStudy(Entity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["ResearchStudy"]
    class_class_curie: ClassVar[str] = "bdchm:ResearchStudy"
    class_name: ClassVar[str] = "ResearchStudy"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ResearchStudy

    id: Union[str, ResearchStudyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResearchStudyId):
            self.id = ResearchStudyId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class DataTypeEnum(EnumDefinitionImpl):
    """
    A category of data
    """
    NUMERIC = PermissibleValue(
        text="NUMERIC",
        description="decimal or integer data type for continuous variables")
    STRING = PermissibleValue(
        text="STRING",
        description="free text data type")
    CODE = PermissibleValue(
        text="CODE",
        description="data are a list of acceptable values or a controlled vocabulary")

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="A category of data",
    )

class BdchmTypeEnum(EnumDefinitionImpl):
    """
    A list of BDCHM entities used to describe variables
    """
    OBSERVATION = PermissibleValue(
        text="OBSERVATION",
        meaning=BDCHM["Observation"])
    CONDITION = PermissibleValue(
        text="CONDITION",
        meaning=BDCHM["Condition"])
    PROCEDURE = PermissibleValue(
        text="PROCEDURE",
        meaning=BDCHM["Procedure"])
    EXPOSURE = PermissibleValue(
        text="EXPOSURE",
        meaning=BDCHM["Exposure"])

    _defn = EnumDefinition(
        name="BdchmTypeEnum",
        description="A list of BDCHM entities used to describe variables",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=BDC_VARIABLE_LIBRARY.id, domain=None, range=URIRef)

slots.associated_study = Slot(uri=BDCHM.ResearchStudy, name="associated_study", curie=BDCHM.curie('ResearchStudy'),
                   model_uri=BDC_VARIABLE_LIBRARY.associated_study, domain=None, range=Optional[Union[str, ResearchStudyId]])

slots.source_id = Slot(uri=BDC_VARIABLE_LIBRARY.source_id, name="source_id", curie=BDC_VARIABLE_LIBRARY.curie('source_id'),
                   model_uri=BDC_VARIABLE_LIBRARY.source_id, domain=None, range=Optional[str])

slots.file_id = Slot(uri=BDC_VARIABLE_LIBRARY.file_id, name="file_id", curie=BDC_VARIABLE_LIBRARY.curie('file_id'),
                   model_uri=BDC_VARIABLE_LIBRARY.file_id, domain=None, range=Optional[str])

slots.file_name = Slot(uri=BDC_VARIABLE_LIBRARY.file_name, name="file_name", curie=BDC_VARIABLE_LIBRARY.curie('file_name'),
                   model_uri=BDC_VARIABLE_LIBRARY.file_name, domain=None, range=Optional[str])

slots.variable_name = Slot(uri=BDC_VARIABLE_LIBRARY.variable_name, name="variable_name", curie=BDC_VARIABLE_LIBRARY.curie('variable_name'),
                   model_uri=BDC_VARIABLE_LIBRARY.variable_name, domain=None, range=Optional[str])

slots.variable_description = Slot(uri=BDC_VARIABLE_LIBRARY.variable_description, name="variable_description", curie=BDC_VARIABLE_LIBRARY.curie('variable_description'),
                   model_uri=BDC_VARIABLE_LIBRARY.variable_description, domain=None, range=Optional[str])

slots.source_variable_description = Slot(uri=BDC_VARIABLE_LIBRARY.source_variable_description, name="source_variable_description", curie=BDC_VARIABLE_LIBRARY.curie('source_variable_description'),
                   model_uri=BDC_VARIABLE_LIBRARY.source_variable_description, domain=None, range=Optional[str])

slots.data_type = Slot(uri=BDC_VARIABLE_LIBRARY.data_type, name="data_type", curie=BDC_VARIABLE_LIBRARY.curie('data_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.unit = Slot(uri=BDC_VARIABLE_LIBRARY.unit, name="unit", curie=BDC_VARIABLE_LIBRARY.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.unit, domain=None, range=Optional[str])

slots.minimum_value = Slot(uri=BDC_VARIABLE_LIBRARY.minimum_value, name="minimum_value", curie=BDC_VARIABLE_LIBRARY.curie('minimum_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.minimum_value, domain=None, range=Optional[Decimal])

slots.maximum_value = Slot(uri=BDC_VARIABLE_LIBRARY.maximum_value, name="maximum_value", curie=BDC_VARIABLE_LIBRARY.curie('maximum_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.maximum_value, domain=None, range=Optional[Decimal])

slots.resolution = Slot(uri=BDC_VARIABLE_LIBRARY.resolution, name="resolution", curie=BDC_VARIABLE_LIBRARY.curie('resolution'),
                   model_uri=BDC_VARIABLE_LIBRARY.resolution, domain=None, range=Optional[int])

slots.coded_values = Slot(uri=BDC_VARIABLE_LIBRARY.coded_values, name="coded_values", curie=BDC_VARIABLE_LIBRARY.curie('coded_values'),
                   model_uri=BDC_VARIABLE_LIBRARY.coded_values, domain=None, range=Optional[str])

slots.missing_value = Slot(uri=BDC_VARIABLE_LIBRARY.missing_value, name="missing_value", curie=BDC_VARIABLE_LIBRARY.curie('missing_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.missing_value, domain=None, range=Optional[Union[Union[str, MissingValueId], list[Union[str, MissingValueId]]]])

slots.comment = Slot(uri=BDC_VARIABLE_LIBRARY.comment, name="comment", curie=BDC_VARIABLE_LIBRARY.curie('comment'),
                   model_uri=BDC_VARIABLE_LIBRARY.comment, domain=None, range=Optional[str])

slots.cde_id = Slot(uri=BDC_VARIABLE_LIBRARY.cde_id, name="cde_id", curie=BDC_VARIABLE_LIBRARY.curie('cde_id'),
                   model_uri=BDC_VARIABLE_LIBRARY.cde_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.variable_label = Slot(uri=BDC_VARIABLE_LIBRARY.variable_label, name="variable_label", curie=BDC_VARIABLE_LIBRARY.curie('variable_label'),
                   model_uri=BDC_VARIABLE_LIBRARY.variable_label, domain=None, range=Optional[str])

slots.concept_type = Slot(uri=BDC_VARIABLE_LIBRARY.concept_type, name="concept_type", curie=BDC_VARIABLE_LIBRARY.curie('concept_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.concept_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.bdchm_type = Slot(uri=BDC_VARIABLE_LIBRARY.bdchm_type, name="bdchm_type", curie=BDC_VARIABLE_LIBRARY.curie('bdchm_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.bdchm_type, domain=None, range=Optional[Union[str, "BdchmTypeEnum"]])

slots.metadata = Slot(uri=BDC_VARIABLE_LIBRARY.metadata, name="metadata", curie=BDC_VARIABLE_LIBRARY.curie('metadata'),
                   model_uri=BDC_VARIABLE_LIBRARY.metadata, domain=None, range=Optional[Union[str, list[str]]])

slots.alert_value = Slot(uri=BDC_VARIABLE_LIBRARY.alert_value, name="alert_value", curie=BDC_VARIABLE_LIBRARY.curie('alert_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.alert_value, domain=None, range=Optional[Union[Union[str, AlertValueId], list[Union[str, AlertValueId]]]])

slots.indicator_char = Slot(uri=BDC_VARIABLE_LIBRARY.indicator_char, name="indicator_char", curie=BDC_VARIABLE_LIBRARY.curie('indicator_char'),
                   model_uri=BDC_VARIABLE_LIBRARY.indicator_char, domain=None, range=Optional[str])

slots.indicator_meaning = Slot(uri=BDC_VARIABLE_LIBRARY.indicator_meaning, name="indicator_meaning", curie=BDC_VARIABLE_LIBRARY.curie('indicator_meaning'),
                   model_uri=BDC_VARIABLE_LIBRARY.indicator_meaning, domain=None, range=Optional[str])

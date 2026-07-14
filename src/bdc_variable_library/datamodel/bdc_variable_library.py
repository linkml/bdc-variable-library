# Auto generated from bdc_variable_library.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-14T11:45:29
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

from linkml_runtime.linkml_model.types import Datetime, Decimal, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Decimal, URIorCURIE, XSDDateTime

metamodel_version = "1.11.0"
version = None

# Namespaces
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
ISO11179 = CurieNamespace('ISO11179', 'http://purl.org/iso11179/')
LOINC = CurieNamespace('LOINC', 'https://loinc.org/')
MMO = CurieNamespace('MMO', 'http://purl.obolibrary.org/obo/MMO_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
OBA = CurieNamespace('OBA', 'http://purl.obolibrary.org/obo/OBA_')
OMOP = CurieNamespace('OMOP', 'https://athena.ohdsi.org/search-terms/terms/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
RXNORM = CurieNamespace('RxNorm', 'http://purl.bioontology.org/ontology/RXNORM/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UCUM = CurieNamespace('UCUM', 'https://units-of-measurement.org/')
BDC_VARIABLE_LIBRARY = CurieNamespace('bdc_variable_library', 'https://w3id.org/linkml/bdc-variable-library/')
BDCHM = CurieNamespace('bdchm', 'https://w3id.org/bdchm/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
CM = CurieNamespace('cm', 'http://example.org/UNKNOWN/cm/')
CMS = CurieNamespace('cms', 'https://w3id.org/linkml/clinical-microschemas/')
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


class IntegratedVariableId(VariableId):
    pass


class MissingValueId(EntityId):
    pass


class AlertValueId(EntityId):
    pass


class MetadataVariableId(EntityId):
    pass


class CompoundHeight002Id(CompoundVariableId):
    pass


class IntegratedHeight001Id(IntegratedVariableId):
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
    unit: Optional[Union[str, URIorCURIE]] = None

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

        if self.unit is not None and not isinstance(self.unit, URIorCURIE):
            self.unit = URIorCURIE(self.unit)

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
    minimum_value: Optional[Decimal] = None
    maximum_value: Optional[Decimal] = None
    resolution: Optional[int] = None
    coded_values: Optional[str] = None
    missing_value: Optional[Union[dict[Union[str, MissingValueId], Union[dict, "MissingValue"]], list[Union[dict, "MissingValue"]]]] = empty_dict()
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

        if self.minimum_value is not None and not isinstance(self.minimum_value, Decimal):
            self.minimum_value = Decimal(self.minimum_value)

        if self.maximum_value is not None and not isinstance(self.maximum_value, Decimal):
            self.maximum_value = Decimal(self.maximum_value)

        if self.resolution is not None and not isinstance(self.resolution, int):
            self.resolution = int(self.resolution)

        if self.coded_values is not None and not isinstance(self.coded_values, str):
            self.coded_values = str(self.coded_values)

        self._normalize_inlined_as_list(slot_name="missing_value", slot_type=MissingValue, key_name="id", keyed=True)

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
    metadata: Optional[Union[dict[Union[str, MetadataVariableId], Union[dict, "MetadataVariable"]], list[Union[dict, "MetadataVariable"]]]] = empty_dict()
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

        self._normalize_inlined_as_list(slot_name="metadata", slot_type=MetadataVariable, key_name="id", keyed=True)

        if not isinstance(self.alert_value, list):
            self.alert_value = [self.alert_value] if self.alert_value is not None else []
        self.alert_value = [v if isinstance(v, AlertValueId) else AlertValueId(v) for v in self.alert_value]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedVariable(Variable):
    """
    Represents a variable that contains data from multiple studies. Typically, some or all of the data must undergo a
    transformation in order to be successfully integrated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedVariable"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedVariable"
    class_name: ClassVar[str] = "IntegratedVariable"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedVariable

    id: Union[str, IntegratedVariableId] = None
    cde_id: Optional[Union[str, URIorCURIE]] = None
    bdchm_type: Optional[Union[str, "BdchmTypeEnum"]] = None
    integrates: Optional[Union[Union[str, CompoundVariableId], list[Union[str, CompoundVariableId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedVariableId):
            self.id = IntegratedVariableId(self.id)

        if self.cde_id is not None and not isinstance(self.cde_id, URIorCURIE):
            self.cde_id = URIorCURIE(self.cde_id)

        if self.bdchm_type is not None and not isinstance(self.bdchm_type, BdchmTypeEnum):
            self.bdchm_type = BdchmTypeEnum(self.bdchm_type)

        if not isinstance(self.integrates, list):
            self.integrates = [self.integrates] if self.integrates is not None else []
        self.integrates = [v if isinstance(v, CompoundVariableId) else CompoundVariableId(v) for v in self.integrates]

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
class MetadataVariable(Entity):
    """
    Specific data point used to add information to an observation. This will typically be a unique identifier for a
    SingleVariable and a slot from a microschema
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["MetadataVariable"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:MetadataVariable"
    class_name: ClassVar[str] = "MetadataVariable"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.MetadataVariable

    id: Union[str, MetadataVariableId] = None
    microschema_slot: Optional[Union[str, "ClinicalMicroschemaEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetadataVariableId):
            self.id = MetadataVariableId(self.id)

        if self.microschema_slot is not None and not isinstance(self.microschema_slot, ClinicalMicroschemaEnum):
            self.microschema_slot = ClinicalMicroschemaEnum(self.microschema_slot)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHeight002(CompoundVariable):
    """
    Height variable with metadata, measured in inches and collected using a wall-mounted stadiometer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHeight002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHeight002"
    class_name: ClassVar[str] = "CompoundHeight002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHeight002

    id: Union[str, CompoundHeight002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHeight002Id):
            self.id = CompoundHeight002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHeight001(IntegratedVariable):
    """
    Height variable containing data from multiple studies, normalized to cm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHeight001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHeight001"
    class_name: ClassVar[str] = "IntegratedHeight001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHeight001

    id: Union[str, IntegratedHeight001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHeight001Id):
            self.id = IntegratedHeight001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResearchStudy(Entity):
    """
    Name of research study that produced the variable
    """
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


@dataclass(repr=False)
class MicroschemaDefinition(YAMLRoot):
    """
    A metaclass for classes that conform to the Microschema profile. Classes that instantiate this are designed for
    inline composition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["linkml-microschema-profile/MicroschemaDefinition"]
    class_class_curie: ClassVar[str] = "linkml:linkml-microschema-profile/MicroschemaDefinition"
    class_name: ClassVar[str] = "MicroschemaDefinition"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.MicroschemaDefinition

    subject: str = None
    observation_type: str = None
    location: str = None
    temporality: str = None
    methodology: str = None
    observation_result: Union[dict, "ValueMicroschemaDefinition"] = None
    profile_version: Optional[str] = None
    domain_of_use: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, str):
            self.observation_type = str(self.observation_type)

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        if self._is_empty(self.temporality):
            self.MissingRequiredField("temporality")
        if not isinstance(self.temporality, str):
            self.temporality = str(self.temporality)

        if self._is_empty(self.methodology):
            self.MissingRequiredField("methodology")
        if not isinstance(self.methodology, str):
            self.methodology = str(self.methodology)

        if self._is_empty(self.observation_result):
            self.MissingRequiredField("observation_result")
        if not isinstance(self.observation_result, ValueMicroschemaDefinition):
            self.observation_result = ValueMicroschemaDefinition()

        if self.profile_version is not None and not isinstance(self.profile_version, str):
            self.profile_version = str(self.profile_version)

        if not isinstance(self.domain_of_use, list):
            self.domain_of_use = [self.domain_of_use] if self.domain_of_use is not None else []
        self.domain_of_use = [v if isinstance(v, str) else str(v) for v in self.domain_of_use]

        super().__post_init__(**kwargs)


class ValueMicroschemaDefinition(YAMLRoot):
    """
    A microschema representing a typed value with optional unit/system. Examples: Quantity, Timepoint, CodedValue,
    Range. This is the range for observation result
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["linkml-microschema-profile/ValueMicroschemaDefinition"]
    class_class_curie: ClassVar[str] = "linkml:linkml-microschema-profile/ValueMicroschemaDefinition"
    class_name: ClassVar[str] = "ValueMicroschemaDefinition"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ValueMicroschemaDefinition


@dataclass(repr=False)
class Quantity(YAMLRoot):
    """
    A numerical value with unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["linkml-microschema-profile/Quantity"]
    class_class_curie: ClassVar[str] = "linkml:linkml-microschema-profile/Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Quantity

    quantity_value: Decimal = None
    quantity_unit: Union[str, URIorCURIE] = None
    comparator: Optional[Union[str, "ComparatorEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        if self._is_empty(self.quantity_unit):
            self.MissingRequiredField("quantity_unit")
        if not isinstance(self.quantity_unit, URIorCURIE):
            self.quantity_unit = URIorCURIE(self.quantity_unit)

        if self.comparator is not None and not isinstance(self.comparator, ComparatorEnum):
            self.comparator = ComparatorEnum(self.comparator)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Timepoint(YAMLRoot):
    """
    A point in time, potentially relative
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["linkml-microschema-profile/Timepoint"]
    class_class_curie: ClassVar[str] = "linkml:linkml-microschema-profile/Timepoint"
    class_name: ClassVar[str] = "Timepoint"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Timepoint

    datetime: Optional[Union[str, XSDDateTime]] = None
    relative_to_event: Optional[Union[str, URIorCURIE]] = None
    offset: Optional[Union[dict, Quantity]] = None
    subject_age: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.datetime is not None and not isinstance(self.datetime, XSDDateTime):
            self.datetime = XSDDateTime(self.datetime)

        if self.relative_to_event is not None and not isinstance(self.relative_to_event, URIorCURIE):
            self.relative_to_event = URIorCURIE(self.relative_to_event)

        if self.offset is not None and not isinstance(self.offset, Quantity):
            self.offset = Quantity(**as_dict(self.offset))

        if self.subject_age is not None and not isinstance(self.subject_age, Quantity):
            self.subject_age = Quantity(**as_dict(self.subject_age))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimeInterval(YAMLRoot):
    """
    A period between two timepoints
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["linkml-microschema-profile/TimeInterval"]
    class_class_curie: ClassVar[str] = "linkml:linkml-microschema-profile/TimeInterval"
    class_name: ClassVar[str] = "TimeInterval"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.TimeInterval

    interval_start: Optional[Union[dict, Timepoint]] = None
    interval_end: Optional[Union[dict, Timepoint]] = None
    duration: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.interval_start is not None and not isinstance(self.interval_start, Timepoint):
            self.interval_start = Timepoint(**as_dict(self.interval_start))

        if self.interval_end is not None and not isinstance(self.interval_end, Timepoint):
            self.interval_end = Timepoint(**as_dict(self.interval_end))

        if self.duration is not None and not isinstance(self.duration, Quantity):
            self.duration = Quantity(**as_dict(self.duration))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodedValue(YAMLRoot):
    """
    A value from a controlled vocabulary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["linkml-microschema-profile/CodedValue"]
    class_class_curie: ClassVar[str] = "linkml:linkml-microschema-profile/CodedValue"
    class_name: ClassVar[str] = "CodedValue"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CodedValue

    code: Union[str, URIorCURIE] = None
    code_label: Optional[str] = None
    code_system: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, URIorCURIE):
            self.code = URIorCURIE(self.code)

        if self.code_label is not None and not isinstance(self.code_label, str):
            self.code_label = str(self.code_label)

        if self.code_system is not None and not isinstance(self.code_system, URIorCURIE):
            self.code_system = URIorCURIE(self.code_system)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalMeasurementRecord(YAMLRoot):
    """
    A data structure with key and value attributes that represents a single observation. This can include results of
    clinical labs, scores and indices, socioeconomic, or behavioral observations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Observation"]
    class_class_curie: ClassVar[str] = "bdchm:Observation"
    class_name: ClassVar[str] = "ClinicalMeasurementRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ClinicalMeasurementRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, Quantity] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[Union[str, URIorCURIE]] = None
    method: Optional[Union[str, "MethodEnum"]] = None
    instrument: Optional[Union[str, "InstrumentEnum"]] = None
    reagent_kit: Optional[Union[str, "ReagentKitEnum"]] = None
    calculated_from: Optional[str] = None
    body_location: Optional[Union[str, URIorCURIE]] = None
    body_position: Optional[Union[str, "BodyPositionEnum"]] = None
    context: Optional[Union[str, "ContextEnum"]] = None
    collected_by: Optional[Union[str, "CollectedByEnum"]] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None
    study_site: Optional[str] = None
    absolute_time: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_identifier):
            self.MissingRequiredField("subject_identifier")
        if not isinstance(self.subject_identifier, URIorCURIE):
            self.subject_identifier = URIorCURIE(self.subject_identifier)

        if self._is_empty(self.measurement_type):
            self.MissingRequiredField("measurement_type")
        if not isinstance(self.measurement_type, URIorCURIE):
            self.measurement_type = URIorCURIE(self.measurement_type)

        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, Quantity):
            self.measurement_value = Quantity(**as_dict(self.measurement_value))

        if self._is_empty(self.age_at_measurement):
            self.MissingRequiredField("age_at_measurement")
        if not isinstance(self.age_at_measurement, Quantity):
            self.age_at_measurement = Quantity(**as_dict(self.age_at_measurement))

        if self.unit is not None and not isinstance(self.unit, URIorCURIE):
            self.unit = URIorCURIE(self.unit)

        if self.method is not None and not isinstance(self.method, MethodEnum):
            self.method = MethodEnum(self.method)

        if self.instrument is not None and not isinstance(self.instrument, InstrumentEnum):
            self.instrument = InstrumentEnum(self.instrument)

        if self.reagent_kit is not None and not isinstance(self.reagent_kit, ReagentKitEnum):
            self.reagent_kit = ReagentKitEnum(self.reagent_kit)

        if self.calculated_from is not None and not isinstance(self.calculated_from, str):
            self.calculated_from = str(self.calculated_from)

        if self.body_location is not None and not isinstance(self.body_location, URIorCURIE):
            self.body_location = URIorCURIE(self.body_location)

        if self.body_position is not None and not isinstance(self.body_position, BodyPositionEnum):
            self.body_position = BodyPositionEnum(self.body_position)

        if self.context is not None and not isinstance(self.context, ContextEnum):
            self.context = ContextEnum(self.context)

        if self.collected_by is not None and not isinstance(self.collected_by, CollectedByEnum):
            self.collected_by = CollectedByEnum(self.collected_by)

        if self.data_type is not None and not isinstance(self.data_type, DataTypeEnum):
            self.data_type = DataTypeEnum(self.data_type)

        if self.study_site is not None and not isinstance(self.study_site, str):
            self.study_site = str(self.study_site)

        if self.absolute_time is not None and not isinstance(self.absolute_time, XSDDateTime):
            self.absolute_time = XSDDateTime(self.absolute_time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConditionStatusRecord(YAMLRoot):
    """
    Record suggesting the presence of a disease or medical condition stated as a diagnosis, sign, or symptom
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Condition"]
    class_class_curie: ClassVar[str] = "bdchm:Condition"
    class_name: ClassVar[str] = "ConditionStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ConditionStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    condition_type: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    associated_evidence: Optional[Union[str, "AssociatedEvidenceEnum"]] = None
    instrument: Optional[Union[str, "InstrumentEnum"]] = None
    age_at_condition_start: Optional[Union[dict, Quantity]] = None
    age_at_condition_end: Optional[Union[dict, Quantity]] = None
    condition_provenance: Optional[Union[str, "ProvenanceEnum"]] = None
    condition_severity: Optional[Union[str, "ConditionSeverityEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_identifier):
            self.MissingRequiredField("subject_identifier")
        if not isinstance(self.subject_identifier, URIorCURIE):
            self.subject_identifier = URIorCURIE(self.subject_identifier)

        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        if self._is_empty(self.age_at_condition_record):
            self.MissingRequiredField("age_at_condition_record")
        if not isinstance(self.age_at_condition_record, Quantity):
            self.age_at_condition_record = Quantity(**as_dict(self.age_at_condition_record))

        if self._is_empty(self.condition_status):
            self.MissingRequiredField("condition_status")
        if not isinstance(self.condition_status, HistoricalStatusEnum):
            self.condition_status = HistoricalStatusEnum(self.condition_status)

        if self._is_empty(self.relationship_to_participant):
            self.MissingRequiredField("relationship_to_participant")
        if not isinstance(self.relationship_to_participant, FamilyRelationshipEnum):
            self.relationship_to_participant = FamilyRelationshipEnum(self.relationship_to_participant)

        if self.associated_evidence is not None and not isinstance(self.associated_evidence, AssociatedEvidenceEnum):
            self.associated_evidence = AssociatedEvidenceEnum(self.associated_evidence)

        if self.instrument is not None and not isinstance(self.instrument, InstrumentEnum):
            self.instrument = InstrumentEnum(self.instrument)

        if self.age_at_condition_start is not None and not isinstance(self.age_at_condition_start, Quantity):
            self.age_at_condition_start = Quantity(**as_dict(self.age_at_condition_start))

        if self.age_at_condition_end is not None and not isinstance(self.age_at_condition_end, Quantity):
            self.age_at_condition_end = Quantity(**as_dict(self.age_at_condition_end))

        if self.condition_provenance is not None and not isinstance(self.condition_provenance, ProvenanceEnum):
            self.condition_provenance = ProvenanceEnum(self.condition_provenance)

        if self.condition_severity is not None and not isinstance(self.condition_severity, ConditionSeverityEnum):
            self.condition_severity = ConditionSeverityEnum(self.condition_severity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugStatusRecord(YAMLRoot):
    """
    Record suggesting exposure to a medication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["DrugExposure"]
    class_class_curie: ClassVar[str] = "bdchm:DrugExposure"
    class_name: ClassVar[str] = "DrugStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.DrugStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    drug_type: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    age_at_drug_start: Optional[Union[dict, Quantity]] = None
    age_at_drug_end: Optional[Union[dict, Quantity]] = None
    route_of_administration: Optional[Union[str, "RouteAdminEnum"]] = None
    dose: Optional[Union[dict, Quantity]] = None
    frequency: Optional[Union[dict, Quantity]] = None
    indication: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_identifier):
            self.MissingRequiredField("subject_identifier")
        if not isinstance(self.subject_identifier, URIorCURIE):
            self.subject_identifier = URIorCURIE(self.subject_identifier)

        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        if self._is_empty(self.age_at_drug_record):
            self.MissingRequiredField("age_at_drug_record")
        if not isinstance(self.age_at_drug_record, Quantity):
            self.age_at_drug_record = Quantity(**as_dict(self.age_at_drug_record))

        if self.age_at_drug_start is not None and not isinstance(self.age_at_drug_start, Quantity):
            self.age_at_drug_start = Quantity(**as_dict(self.age_at_drug_start))

        if self.age_at_drug_end is not None and not isinstance(self.age_at_drug_end, Quantity):
            self.age_at_drug_end = Quantity(**as_dict(self.age_at_drug_end))

        if self.route_of_administration is not None and not isinstance(self.route_of_administration, RouteAdminEnum):
            self.route_of_administration = RouteAdminEnum(self.route_of_administration)

        if self.dose is not None and not isinstance(self.dose, Quantity):
            self.dose = Quantity(**as_dict(self.dose))

        if self.frequency is not None and not isinstance(self.frequency, Quantity):
            self.frequency = Quantity(**as_dict(self.frequency))

        if self.indication is not None and not isinstance(self.indication, URIorCURIE):
            self.indication = URIorCURIE(self.indication)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProcedureStatusRecord(YAMLRoot):
    """
    Record of activity or process ordered by or carried out by a healthcare provider for a diagnostic or therapeutic
    reason
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Procedure"]
    class_class_curie: ClassVar[str] = "bdchm:Procedure"
    class_name: ClassVar[str] = "ProcedureStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ProcedureStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    procedure_type: Union[str, URIorCURIE] = None
    age_at_procedure_record: Union[dict, Quantity] = None
    collected_by: Optional[Union[str, "CollectedByEnum"]] = None
    age_at_procedure_start: Optional[Union[dict, Quantity]] = None
    age_at_procedure_end: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_identifier):
            self.MissingRequiredField("subject_identifier")
        if not isinstance(self.subject_identifier, URIorCURIE):
            self.subject_identifier = URIorCURIE(self.subject_identifier)

        if self._is_empty(self.procedure_type):
            self.MissingRequiredField("procedure_type")
        if not isinstance(self.procedure_type, URIorCURIE):
            self.procedure_type = URIorCURIE(self.procedure_type)

        if self._is_empty(self.age_at_procedure_record):
            self.MissingRequiredField("age_at_procedure_record")
        if not isinstance(self.age_at_procedure_record, Quantity):
            self.age_at_procedure_record = Quantity(**as_dict(self.age_at_procedure_record))

        if self.collected_by is not None and not isinstance(self.collected_by, CollectedByEnum):
            self.collected_by = CollectedByEnum(self.collected_by)

        if self.age_at_procedure_start is not None and not isinstance(self.age_at_procedure_start, Quantity):
            self.age_at_procedure_start = Quantity(**as_dict(self.age_at_procedure_start))

        if self.age_at_procedure_end is not None and not isinstance(self.age_at_procedure_end, Quantity):
            self.age_at_procedure_end = Quantity(**as_dict(self.age_at_procedure_end))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord(ClinicalMeasurementRecord):
    """
    Measurement of linear distance of a human body from the bottom of a flat foot to the top-most point of the head
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord"
    class_name: ClassVar[str] = "HumanBodyHeightRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyHeightQuantity):
            self.measurement_value = HumanBodyHeightQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord001(HumanBodyHeightRecord):
    """
    Measurement of linear distance of a standing human body from the bottom of a flat foot to the top-most point of
    the head measured in centimeters with a wall-mounted stadiometer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord001"
    class_name: ClassVar[str] = "HumanBodyHeightRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity001"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyHeightQuantity001):
            self.measurement_value = HumanBodyHeightQuantity001(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord002(HumanBodyHeightRecord):
    """
    Measurement of linear distance of a standing human body from the bottom of a flat foot to the top-most point of
    the head measured in inches with a wall-mounted stadiometer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord002"
    class_name: ClassVar[str] = "HumanBodyHeightRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity002"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyHeightQuantity002):
            self.measurement_value = HumanBodyHeightQuantity002(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord003(HumanBodyHeightRecord):
    """
    Measurement of linear distance of a standing human body from the bottom of a flat foot to the top-most point of
    the head measured in inches with a portable stadiometer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord003"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord003"
    class_name: ClassVar[str] = "HumanBodyHeightRecord003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord003

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity002"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyHeightQuantity002):
            self.measurement_value = HumanBodyHeightQuantity002(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord004(HumanBodyHeightRecord):
    """
    Measurement of linear distance of a standing human body from the bottom of a flat foot to the top-most point of
    the head measured in centimeters with an anthropometer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord004"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord004"
    class_name: ClassVar[str] = "HumanBodyHeightRecord004"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord004

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity003"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyHeightQuantity003):
            self.measurement_value = HumanBodyHeightQuantity003(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord005(HumanBodyHeightRecord):
    """
    Measurement of linear distance of a standing human body from the bottom of a flat foot to the top-most point of
    the head measured in feet with a wall-mounted stadiometer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord005"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord005"
    class_name: ClassVar[str] = "HumanBodyHeightRecord005"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord005

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity004"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyHeightQuantity004):
            self.measurement_value = HumanBodyHeightQuantity004(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord006(HumanBodyHeightRecord):
    """
    Measurement of linear distance of a human body from the bottom of a flat foot to the top-most point of the head in
    cm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord006"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord006"
    class_name: ClassVar[str] = "HumanBodyHeightRecord006"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord006

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity003"] = None
    unit: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyHeightQuantity003):
            self.measurement_value = HumanBodyHeightQuantity003(**as_dict(self.measurement_value))

        if self.unit is not None and not isinstance(self.unit, URIorCURIE):
            self.unit = URIorCURIE(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyWeightRecord(ClinicalMeasurementRecord):
    """
    Measurement of the force exerted by a human body on a scale due to gravity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyWeightRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyWeightRecord"
    class_name: ClassVar[str] = "HumanBodyWeightRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyWeightRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyWeightQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyWeightQuantity):
            self.measurement_value = HumanBodyWeightQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyWeightRecord001(HumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body on a mechanical beam balance due to gravity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyWeightRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyWeightRecord001"
    class_name: ClassVar[str] = "HumanBodyWeightRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyWeightRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyWeightQuantity001"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyWeightQuantity001):
            self.measurement_value = HumanBodyWeightQuantity001(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyWeightRecord002(HumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body on a mechanical beam balance due to gravity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyWeightRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyWeightRecord002"
    class_name: ClassVar[str] = "HumanBodyWeightRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyWeightRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyWeightQuantity002"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyWeightQuantity002):
            self.measurement_value = HumanBodyWeightQuantity002(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyWeightRecord003(HumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body on a body composition analyzer due to gravity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyWeightRecord003"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyWeightRecord003"
    class_name: ClassVar[str] = "HumanBodyWeightRecord003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyWeightRecord003

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyWeightQuantity003"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyWeightQuantity003):
            self.measurement_value = HumanBodyWeightQuantity003(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BodyMassIndexRecord(ClinicalMeasurementRecord):
    """
    A calculated numerical quantity representing an individual's weight-to-height ratio. BMI is calculated as weight
    (kg) divided by height (m) squared. The height is measured in cm and the weight is collected in kg.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["BodyMassIndexRecord"]
    class_class_curie: ClassVar[str] = "cms:BodyMassIndexRecord"
    class_name: ClassVar[str] = "BodyMassIndexRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.BodyMassIndexRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "BodyMassIndexQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, BodyMassIndexQuantity):
            self.measurement_value = BodyMassIndexQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BodyMassIndexRecord001(BodyMassIndexRecord):
    """
    A calculated numerical quantity representing an individual's weight-to-height ratio. BMI is calculated as weight
    (kg) divided by height (m) squared. The height is measured in cm and the weight is collected in kg.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["BodyMassIndexRecord001"]
    class_class_curie: ClassVar[str] = "cms:BodyMassIndexRecord001"
    class_name: ClassVar[str] = "BodyMassIndexRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.BodyMassIndexRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "BodyMassIndexQuantity"] = None
    calculated_from: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, BodyMassIndexQuantity):
            self.measurement_value = BodyMassIndexQuantity(**as_dict(self.measurement_value))

        if self.calculated_from is not None and not isinstance(self.calculated_from, str):
            self.calculated_from = str(self.calculated_from)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BodyMassIndexRecord002(BodyMassIndexRecord):
    """
    A calculated numerical quantity representing an individual's weight-to-height ratio. BMI is calculated as weight
    (kg) divided by height (m) squared. The height is measured in inches and the weight is collected in lbs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["BodyMassIndexRecord002"]
    class_class_curie: ClassVar[str] = "cms:BodyMassIndexRecord002"
    class_name: ClassVar[str] = "BodyMassIndexRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.BodyMassIndexRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "BodyMassIndexQuantity"] = None
    calculated_from: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, BodyMassIndexQuantity):
            self.measurement_value = BodyMassIndexQuantity(**as_dict(self.measurement_value))

        if self.calculated_from is not None and not isinstance(self.calculated_from, str):
            self.calculated_from = str(self.calculated_from)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFvcRecord(ClinicalMeasurementRecord):
    """
    Total amount of air a person can forcibly exhale after taking the deepest breath possible. This microschema uses
    the Relativity mixin to bundle measured, predicted, and percent predicted values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFvcRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanFvcRecord"
    class_name: ClassVar[str] = "HumanFvcRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFvcRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFvcQuantity"] = None
    predicted_value: Decimal = None
    percent_predicted_value: Decimal = None
    lower_limit_normal: Optional[Decimal] = None
    upper_limit_normal: Optional[Decimal] = None
    activity_type: Optional[Union[str, "ActivityTypeEnum"]] = None
    relative_timing: Optional[Union[str, "RelativeTimingEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanFvcQuantity):
            self.measurement_value = HumanFvcQuantity(**as_dict(self.measurement_value))

        if self._is_empty(self.predicted_value):
            self.MissingRequiredField("predicted_value")
        if not isinstance(self.predicted_value, Decimal):
            self.predicted_value = Decimal(self.predicted_value)

        if self._is_empty(self.percent_predicted_value):
            self.MissingRequiredField("percent_predicted_value")
        if not isinstance(self.percent_predicted_value, Decimal):
            self.percent_predicted_value = Decimal(self.percent_predicted_value)

        if self.lower_limit_normal is not None and not isinstance(self.lower_limit_normal, Decimal):
            self.lower_limit_normal = Decimal(self.lower_limit_normal)

        if self.upper_limit_normal is not None and not isinstance(self.upper_limit_normal, Decimal):
            self.upper_limit_normal = Decimal(self.upper_limit_normal)

        if self.activity_type is not None and not isinstance(self.activity_type, ActivityTypeEnum):
            self.activity_type = ActivityTypeEnum(self.activity_type)

        if self.relative_timing is not None and not isinstance(self.relative_timing, RelativeTimingEnum):
            self.relative_timing = RelativeTimingEnum(self.relative_timing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMeasuredFvcRecord(ClinicalMeasurementRecord):
    """
    Total amount of air a person can forcibly exhale after taking the deepest breath possible
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMeasuredFvcRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMeasuredFvcRecord"
    class_name: ClassVar[str] = "HumanMeasuredFvcRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMeasuredFvcRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMeasuredFvcQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMeasuredFvcQuantity):
            self.measurement_value = HumanMeasuredFvcQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMeasuredFvcRecord001(HumanMeasuredFvcRecord):
    """
    Total amount of air a person can forcibly exhale after taking the deepest breath possible
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMeasuredFvcRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanMeasuredFvcRecord001"
    class_name: ClassVar[str] = "HumanMeasuredFvcRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMeasuredFvcRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMeasuredFvcQuantity001"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMeasuredFvcQuantity001):
            self.measurement_value = HumanMeasuredFvcQuantity001(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPredictedFvcRecord(ClinicalMeasurementRecord):
    """
    Predicted total amount of air a person can forcibly exhale after taking the deepest breath possible. Predictions
    are based on a reference equation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPredictedFvcRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanPredictedFvcRecord"
    class_name: ClassVar[str] = "HumanPredictedFvcRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPredictedFvcRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPredictedFvcQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPredictedFvcQuantity):
            self.measurement_value = HumanPredictedFvcQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPercentPredictedFvcRecord(ClinicalMeasurementRecord):
    """
    Percent of the predicted FVC that is achieved by the patient
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPercentPredictedFvcRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanPercentPredictedFvcRecord"
    class_name: ClassVar[str] = "HumanPercentPredictedFvcRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPercentPredictedFvcRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPercentPredictedFvcQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPercentPredictedFvcQuantity):
            self.measurement_value = HumanPercentPredictedFvcQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFev1Record(ClinicalMeasurementRecord):
    """
    Maximum amount of air a person can forcibly exhale in the first second of a breathing test
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFev1Record"]
    class_class_curie: ClassVar[str] = "cms:HumanFev1Record"
    class_name: ClassVar[str] = "HumanFev1Record"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFev1Record

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFev1Quantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanFev1Quantity):
            self.measurement_value = HumanFev1Quantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBasophilCountRecord(ClinicalMeasurementRecord):
    """
    Concentration of basophil cells in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBasophilCountRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBasophilCountRecord"
    class_name: ClassVar[str] = "HumanBasophilCountRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBasophilCountQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBasophilCountQuantity):
            self.measurement_value = HumanBasophilCountQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBasophilCountRecord001(HumanBasophilCountRecord):
    """
    Concentration of basophil cells in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBasophilCountRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanBasophilCountRecord001"
    class_name: ClassVar[str] = "HumanBasophilCountRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBasophilCountQuantity001"] = None
    unit: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBasophilCountQuantity001):
            self.measurement_value = HumanBasophilCountQuantity001(**as_dict(self.measurement_value))

        if self.unit is not None and not isinstance(self.unit, URIorCURIE):
            self.unit = URIorCURIE(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBasophilCountRecord002(HumanBasophilCountRecord):
    """
    Concentration of basophil cells in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBasophilCountRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanBasophilCountRecord002"
    class_name: ClassVar[str] = "HumanBasophilCountRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBasophilCountQuantity001"] = None
    unit: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBasophilCountQuantity001):
            self.measurement_value = HumanBasophilCountQuantity001(**as_dict(self.measurement_value))

        if self.unit is not None and not isinstance(self.unit, URIorCURIE):
            self.unit = URIorCURIE(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relativity(YAMLRoot):
    """
    Mixin providing slots for bundling measured, predicted, and percent predicted values with their normal limits.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["Relativity"]
    class_class_curie: ClassVar[str] = "cms:Relativity"
    class_name: ClassVar[str] = "Relativity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Relativity

    predicted_value: Optional[Decimal] = None
    lower_limit_normal: Optional[Decimal] = None
    upper_limit_normal: Optional[Decimal] = None
    percent_predicted_value: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.predicted_value is not None and not isinstance(self.predicted_value, Decimal):
            self.predicted_value = Decimal(self.predicted_value)

        if self.lower_limit_normal is not None and not isinstance(self.lower_limit_normal, Decimal):
            self.lower_limit_normal = Decimal(self.lower_limit_normal)

        if self.upper_limit_normal is not None and not isinstance(self.upper_limit_normal, Decimal):
            self.upper_limit_normal = Decimal(self.upper_limit_normal)

        if self.percent_predicted_value is not None and not isinstance(self.percent_predicted_value, Decimal):
            self.percent_predicted_value = Decimal(self.percent_predicted_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Context(YAMLRoot):
    """
    Mixin providing contextual slots that describe the activity type and relative timing associated with a clinical
    measurement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["Context"]
    class_class_curie: ClassVar[str] = "cms:Context"
    class_name: ClassVar[str] = "Context"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Context

    activity_type: Optional[Union[str, "ActivityTypeEnum"]] = None
    relative_timing: Optional[Union[str, "RelativeTimingEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.activity_type is not None and not isinstance(self.activity_type, ActivityTypeEnum):
            self.activity_type = ActivityTypeEnum(self.activity_type)

        if self.relative_timing is not None and not isinstance(self.relative_timing, RelativeTimingEnum):
            self.relative_timing = RelativeTimingEnum(self.relative_timing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightQuantity(Quantity):
    """
    Human body height. Negative heights are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightQuantity"
    class_name: ClassVar[str] = "HumanBodyHeightQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightQuantity001(HumanBodyHeightQuantity):
    """
    Standing wall-mounted or portable stadiometer human body height in cm, bounded 30–230. Minimum represents observed
    limits on human height. Maximum represents limit of measurement device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightQuantity001"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightQuantity001"
    class_name: ClassVar[str] = "HumanBodyHeightQuantity001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity001

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightQuantity002(HumanBodyHeightQuantity):
    """
    Standing wall-mounted or portable stadiometer human body height in inches, bounded 20–90. Minimum represents
    observed limits on human height. Maximum represents limit of measurement device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightQuantity002"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightQuantity002"
    class_name: ClassVar[str] = "HumanBodyHeightQuantity002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity002

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightQuantity003(HumanBodyHeightQuantity):
    """
    Standing anthropometer human body height in cm, bounded 30-250. Minimum represents observed limits on human
    height. Maximum represents limit of measurement device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightQuantity003"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightQuantity003"
    class_name: ClassVar[str] = "HumanBodyHeightQuantity003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity003

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightQuantity004(HumanBodyHeightQuantity):
    """
    Standing wall-mounted or portable stadiometer human body height in ft, bounded 0.98-8.2. Minimum represents
    observed limits on human height. Maximum represents limit of measurement device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightQuantity004"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightQuantity004"
    class_name: ClassVar[str] = "HumanBodyHeightQuantity004"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity004

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyWeightQuantity(Quantity):
    """
    Human body weight. Negative weights are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyWeightQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyWeightQuantity"
    class_name: ClassVar[str] = "HumanBodyWeightQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyWeightQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyWeightQuantity001(HumanBodyWeightQuantity):
    """
    Mechanical-beam-balance human body weight in kg, bounded 0–230. Maximum weight set based on limits of measurement
    device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyWeightQuantity001"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyWeightQuantity001"
    class_name: ClassVar[str] = "HumanBodyWeightQuantity001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyWeightQuantity001

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyWeightQuantity002(HumanBodyWeightQuantity):
    """
    Mechanical-beam-balance human body weight in lbs, bounded 0–500. Maximum weight set based on limits of measurement
    device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyWeightQuantity002"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyWeightQuantity002"
    class_name: ClassVar[str] = "HumanBodyWeightQuantity002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyWeightQuantity002

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyWeightQuantity003(HumanBodyWeightQuantity):
    """
    Body composition analyzer human body weight in kg, bounded 0–270. Maximum weight set based on limits of
    measurement device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyWeightQuantity003"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyWeightQuantity003"
    class_name: ClassVar[str] = "HumanBodyWeightQuantity003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyWeightQuantity003

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BodyMassIndexQuantity(Quantity):
    """
    Body mass index value in kg/m², bounded 5–200. Limits based on observed limits  of human body size.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["BodyMassIndexQuantity"]
    class_class_curie: ClassVar[str] = "cms:BodyMassIndexQuantity"
    class_name: ClassVar[str] = "BodyMassIndexQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.BodyMassIndexQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFvcQuantity(Quantity):
    """
    FVC measurement, bounded 0–12000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFvcQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanFvcQuantity"
    class_name: ClassVar[str] = "HumanFvcQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFvcQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMeasuredFvcQuantity(Quantity):
    """
    Measured FVC, bounded 0–12000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMeasuredFvcQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMeasuredFvcQuantity"
    class_name: ClassVar[str] = "HumanMeasuredFvcQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMeasuredFvcQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMeasuredFvcQuantity001(HumanMeasuredFvcQuantity):
    """
    Measured FVC in L, bounded 0–12.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMeasuredFvcQuantity001"]
    class_class_curie: ClassVar[str] = "cms:HumanMeasuredFvcQuantity001"
    class_name: ClassVar[str] = "HumanMeasuredFvcQuantity001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMeasuredFvcQuantity001

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPredictedFvcQuantity(Quantity):
    """
    Predicted FVC in L, bounded 0–12.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPredictedFvcQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPredictedFvcQuantity"
    class_name: ClassVar[str] = "HumanPredictedFvcQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPredictedFvcQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPercentPredictedFvcQuantity(Quantity):
    """
    Percent-predicted FVC, bounded 0–150.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPercentPredictedFvcQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPercentPredictedFvcQuantity"
    class_name: ClassVar[str] = "HumanPercentPredictedFvcQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPercentPredictedFvcQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFev1Quantity(Quantity):
    """
    FEV1 measurement, bounded 0–12000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFev1Quantity"]
    class_class_curie: ClassVar[str] = "cms:HumanFev1Quantity"
    class_name: ClassVar[str] = "HumanFev1Quantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFev1Quantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBasophilCountQuantity(Quantity):
    """
    Basophil concentration measurement. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBasophilCountQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanBasophilCountQuantity"
    class_name: ClassVar[str] = "HumanBasophilCountQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBasophilCountQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBasophilCountQuantity001(HumanBasophilCountQuantity):
    """
    Basophil concentration measurement, bounded 0-0.3 based on observed  biological limits.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBasophilCountQuantity001"]
    class_class_curie: ClassVar[str] = "cms:HumanBasophilCountQuantity001"
    class_name: ClassVar[str] = "HumanBasophilCountQuantity001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBasophilCountQuantity001

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBasophilCountQuantity002(HumanBasophilCountQuantity):
    """
    Basophil concentration measurement, bounded 0-300 based on observed  biological limits.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBasophilCountQuantity002"]
    class_class_curie: ClassVar[str] = "cms:HumanBasophilCountQuantity002"
    class_name: ClassVar[str] = "HumanBasophilCountQuantity002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBasophilCountQuantity002

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


# Enumerations
class BdchmTypeEnum(EnumDefinitionImpl):
    """
    A list of BDCHM entities used to describe variables
    """
    observation = PermissibleValue(
        text="observation",
        meaning=BDCHM["Observation"])
    condition = PermissibleValue(
        text="condition",
        meaning=BDCHM["Condition"])
    procedure = PermissibleValue(
        text="procedure",
        meaning=BDCHM["Procedure"])
    exposure = PermissibleValue(
        text="exposure",
        meaning=BDCHM["Exposure"])

    _defn = EnumDefinition(
        name="BdchmTypeEnum",
        description="A list of BDCHM entities used to describe variables",
    )

class ClinicalMicroschemaEnum(EnumDefinitionImpl):
    """
    A list of slots describing clinical measurements in microschema
    """
    subject_identifier = PermissibleValue(text="subject_identifier")
    measurement_type = PermissibleValue(text="measurement_type")
    measurement_value = PermissibleValue(text="measurement_value")
    unit = PermissibleValue(text="unit")
    method = PermissibleValue(text="method")
    instrument = PermissibleValue(text="instrument")
    reagent_kit = PermissibleValue(text="reagent_kit")
    calculated_from = PermissibleValue(text="calculated_from")
    body_location = PermissibleValue(text="body_location")
    body_position = PermissibleValue(text="body_position")
    context = PermissibleValue(text="context")
    collected_by = PermissibleValue(text="collected_by")
    data_type = PermissibleValue(text="data_type")
    age_at_measurement = PermissibleValue(text="age_at_measurement")
    study_site = PermissibleValue(text="study_site")
    absolute_time = PermissibleValue(text="absolute_time")

    _defn = EnumDefinition(
        name="ClinicalMicroschemaEnum",
        description="A list of slots describing clinical measurements in microschema",
    )

class ComparatorEnum(EnumDefinitionImpl):
    """
    Comparator for quantity values
    """
    lt = PermissibleValue(
        text="lt",
        description="Less than")
    le = PermissibleValue(
        text="le",
        description="Less than or equal to")
    ge = PermissibleValue(
        text="ge",
        description="Greater than or equal to")
    gt = PermissibleValue(
        text="gt",
        description="Greater than")

    _defn = EnumDefinition(
        name="ComparatorEnum",
        description="Comparator for quantity values",
    )

class HistoricalStatusEnum(EnumDefinitionImpl):
    """
    Indicates whether something is present, absent, historical, or its status is unknown.
    """
    present = PermissibleValue(
        text="present",
        description="Was present in the patient at observation time.")
    absent = PermissibleValue(
        text="absent",
        description="Was absent in the patient at observation time.")
    unknown = PermissibleValue(
        text="unknown",
        description="Was of unknown status in the patient at observation time.")
    historical = PermissibleValue(
        text="historical",
        description="Was present in the patient historically.")

    _defn = EnumDefinition(
        name="HistoricalStatusEnum",
        description="Indicates whether something is present, absent, historical, or its status is unknown.",
    )

class ProvenanceEnum(EnumDefinitionImpl):
    """
    A set of values indicating the source or origin of a clinical record.
    """
    ehr_billing_diagnosis = PermissibleValue(
        text="ehr_billing_diagnosis",
        description="Diagnosis from EHR billing.")
    ehr_chief_complaint = PermissibleValue(
        text="ehr_chief_complaint",
        description="Chief complaint from EHR.")
    ehr_encounter_diagnosis = PermissibleValue(
        text="ehr_encounter_diagnosis",
        description="Encounter diagnosis from EHR.")
    ehr_episode_entry = PermissibleValue(
        text="ehr_episode_entry",
        description="Episode entry from EHR.")
    ehr_problem_list_entry = PermissibleValue(
        text="ehr_problem_list_entry",
        description="Problem list entry from EHR.")
    first_position_condition = PermissibleValue(
        text="first_position_condition",
        description="First position condition.")
    primary_condition = PermissibleValue(
        text="primary_condition",
        description="Primary condition.")
    secondary_condition = PermissibleValue(
        text="secondary_condition",
        description="Secondary condition.")
    nlp_derived = PermissibleValue(
        text="nlp_derived",
        description="Derived from natural language processing.")
    observation_recorded_from_ehr = PermissibleValue(
        text="observation_recorded_from_ehr",
        description="Observation recorded from EHR.")
    patient_self_reported_condition = PermissibleValue(
        text="patient_self_reported_condition",
        description="Patient self-reported condition.")
    referral_record = PermissibleValue(
        text="referral_record",
        description="From referral record.")
    tumor_registry = PermissibleValue(
        text="tumor_registry",
        description="From tumor registry.")
    working_diagnosis = PermissibleValue(
        text="working_diagnosis",
        description="Working diagnosis.")
    clinical_diagnosis = PermissibleValue(
        text="clinical_diagnosis",
        description="Clinical diagnosis.")

    _defn = EnumDefinition(
        name="ProvenanceEnum",
        description="A set of values indicating the source or origin of a clinical record.",
    )

class ConditionSeverityEnum(EnumDefinitionImpl):
    """
    A subjective assessment of the severity of a condition.
    """
    mild = PermissibleValue(
        text="mild",
        description="Lower intensity condition.",
        meaning=OMOP["4116992"])
    moderate = PermissibleValue(
        text="moderate",
        description="Medium intensity condition.",
        meaning=OMOP["3272197"])
    severe = PermissibleValue(
        text="severe",
        description="Higher intensity condition.",
        meaning=OMOP["4087703"])

    _defn = EnumDefinition(
        name="ConditionSeverityEnum",
        description="A subjective assessment of the severity of a condition.",
    )

class FamilyRelationshipEnum(EnumDefinitionImpl):
    """
    Values describing kinship connections between individuals.
    """
    oneself = PermissibleValue(
        text="oneself",
        description="Self-reference.")
    natural_parent = PermissibleValue(
        text="natural_parent",
        description="Mother or father unspecified.",
        meaning=OMOP["4029630"])
    natural_father = PermissibleValue(
        text="natural_father",
        description="Biological father.",
        meaning=OMOP["4321888"])
    natural_mother = PermissibleValue(
        text="natural_mother",
        description="Biological mother.",
        meaning=OMOP["4277283"])
    natural_sibling = PermissibleValue(
        text="natural_sibling",
        description="Sister or brother unspecified.",
        meaning=OMOP["4218412"])
    natural_brother = PermissibleValue(
        text="natural_brother",
        description="Biological brother.",
        meaning=OMOP["4263682"])
    natural_sister = PermissibleValue(
        text="natural_sister",
        description="Biological sister.",
        meaning=OMOP["4251326"])
    natural_child = PermissibleValue(
        text="natural_child",
        description="Biological offspring.",
        meaning=OMOP["4326600"])
    blood_relative = PermissibleValue(
        text="blood_relative",
        description="Generic consanguineous relation.",
        meaning=OMOP["4053608"])

    _defn = EnumDefinition(
        name="FamilyRelationshipEnum",
        description="Values describing kinship connections between individuals.",
    )

class RouteAdminEnum(EnumDefinitionImpl):
    """
    Routes of drug administration
    """
    oral = PermissibleValue(
        text="oral",
        description="Oral administration",
        meaning=OMOP["4132161"])
    intravenous = PermissibleValue(
        text="intravenous",
        description="Intravenous administration",
        meaning=OMOP["4171047"])
    intramuscular = PermissibleValue(
        text="intramuscular",
        description="Intramuscular administration",
        meaning=OMOP["4302612"])
    subcutaneous = PermissibleValue(
        text="subcutaneous",
        description="Subcutaneous administration",
        meaning=OMOP["4142048"])
    intradermal = PermissibleValue(
        text="intradermal",
        description="Intradermal administration",
        meaning=OMOP["4156706"])
    transdermal = PermissibleValue(
        text="transdermal",
        description="Transdermal administration",
        meaning=OMOP["4262099"])
    rectal = PermissibleValue(
        text="rectal",
        description="Rectal administration",
        meaning=OMOP["4290759"])
    vaginal = PermissibleValue(
        text="vaginal",
        description="Vaginal administration",
        meaning=OMOP["4057765"])
    nasal = PermissibleValue(
        text="nasal",
        description="Nasal administration",
        meaning=OMOP["4262914"])
    topical = PermissibleValue(
        text="topical",
        description="Topical administration",
        meaning=OMOP["4263689"])
    sublingual = PermissibleValue(
        text="sublingual",
        description="Sublingual administration",
        meaning=OMOP["4292110"])
    buccal = PermissibleValue(
        text="buccal",
        description="Buccal administration",
        meaning=OMOP["4181897"])
    intra_articular = PermissibleValue(
        text="intra_articular",
        description="Intra-articular administration",
        meaning=OMOP["4006860"])
    intraperitoneal = PermissibleValue(
        text="intraperitoneal",
        description="Intraperitoneal administration",
        meaning=OMOP["4243022"])
    intrathecal = PermissibleValue(
        text="intrathecal",
        description="Intrathecal administration",
        meaning=OMOP["4217202"])
    epidural = PermissibleValue(
        text="epidural",
        description="Epidural administration",
        meaning=OMOP["4225555"])
    intra_arterial = PermissibleValue(
        text="intra_arterial",
        description="Intra-arterial administration",
        meaning=OMOP["4240824"])
    ophthalmic = PermissibleValue(
        text="ophthalmic",
        description="Ophthalmic administration",
        meaning=OMOP["4184451"])
    otic = PermissibleValue(
        text="otic",
        description="Otic (ear) administration",
        meaning=OMOP["4023156"])
    enteral = PermissibleValue(
        text="enteral",
        description="Enteral administration",
        meaning=OMOP["4167540"])
    percutaneous = PermissibleValue(
        text="percutaneous",
        description="Percutaneous administration",
        meaning=OMOP["4177987"])

    _defn = EnumDefinition(
        name="RouteAdminEnum",
        description="Routes of drug administration",
    )

class DataTypeEnum(EnumDefinitionImpl):
    """
    The data type of an observation value
    """
    decimal = PermissibleValue(
        text="decimal",
        description="Decimal number")
    integer = PermissibleValue(
        text="integer",
        description="Integer number")
    enum = PermissibleValue(
        text="enum",
        description="Enumerated value")
    boolean = PermissibleValue(
        text="boolean",
        description="Boolean value")
    string = PermissibleValue(
        text="string",
        description="String value")
    numeric = PermissibleValue(
        text="numeric",
        description="decimal or integer - from dbGAP data types")
    code = PermissibleValue(
        text="code",
        description="""data are a list of acceptable values or a controlled vocabulary, from dbGAP data types, same as enum""")
    uriorcurie = PermissibleValue(
        text="uriorcurie",
        description="A URI or CURIE value")

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="The data type of an observation value",
    )

class MethodEnum(EnumDefinitionImpl):
    """
    The method used for a measurement or observation
    """
    anthropometry = PermissibleValue(
        text="anthropometry",
        description="physical measurement of the human body, including height, weight, and other body dimensions")
    survey = PermissibleValue(
        text="survey",
        description="""list of questions given to a participant for data collection purposes - the survey is filled out by the participant independently""")
    interview = PermissibleValue(
        text="interview",
        description="series of questions posed to a participant by an interviewer for data collection purposes")
    calculated = PermissibleValue(
        text="calculated",
        description="clinical record that results from a calculation rather than being directly measured")
    spirometry = PermissibleValue(
        text="spirometry",
        description="breathing test used to assess lung function")
    body_plesmography = PermissibleValue(
        text="body_plesmography",
        description="""precise pulmonary function test where the patient sits in a sealed chamber and breathes into a specialized mouthpiece. This method uses Boyle's Law  and is considered a \"gold standard\"""")
    gli = PermissibleValue(
        text="gli",
        description="""a standard reference range and calculator for spirometry and lung function tests published by the Global Lung Function Initiative in 2012""")
    gli_global = PermissibleValue(
        text="gli_global",
        description="""a standard reference range and calculator for spirometry and lung function tests published by the Global Lung Function Initiative in 2022. This is an update of the 2012 standard that is more ethnically diverse""")
    nhanesiii = PermissibleValue(
        text="nhanesiii",
        description="standard reference equations for spirometry published in 2005")

    _defn = EnumDefinition(
        name="MethodEnum",
        description="The method used for a measurement or observation",
    )

class InstrumentEnum(EnumDefinitionImpl):
    """
    The instrument used for a measurement
    """
    wall_mounted_stadiometer = PermissibleValue(
        text="wall_mounted_stadiometer",
        description="""fixed, high-precision medical device used to measure human height, consisting of a vertical measuring rod or tape fastened to a wall with a sliding headpiece""",
        meaning=MMO["0000105"])
    flexible_measuring_tape = PermissibleValue(
        text="flexible_measuring_tape",
        description="flexible tape used to measure height or body circumference")
    portable_stadiometer = PermissibleValue(
        text="portable_stadiometer",
        description="portable device used to measure height, typically used in field settings")
    anthropometer_rod = PermissibleValue(
        text="anthropometer_rod",
        description="rigid rod-based instrument used to measure body dimensions including height")
    sonar_stadiometer = PermissibleValue(
        text="sonar_stadiometer",
        description="ultrasound-based device used to measure height without contact")
    mechanical_beam_balance_scale = PermissibleValue(
        text="mechanical_beam_balance_scale",
        description="medical device used to measure human weight",
        meaning=MMO["0000087"])
    digital_scale = PermissibleValue(
        text="digital_scale",
        description="electronic device used to measure human weight using strain gauge sensors",
        meaning=MMO["0000087"])
    spring_scale = PermissibleValue(
        text="spring_scale",
        description="mechanical device that measures weight by the displacement of a spring")
    spirometer = PermissibleValue(
        text="spirometer",
        description="""medical device that measures lung function by recording the amount and speed of air a person can inhale and exhale""")
    vitalograph = PermissibleValue(
        text="vitalograph",
        description="""a portable medical device that measures lung function by recording the amount and speed of air a person can inhale and exhale""")
    body_plesmograph = PermissibleValue(
        text="body_plesmograph",
        description="sealed, clear chamber with a mouthpiece for a person to breath through")
    peak_flow_meter = PermissibleValue(
        text="peak_flow_meter",
        description="portable, handheld device used to measure how fast and hard a person can exhale")

    _defn = EnumDefinition(
        name="InstrumentEnum",
        description="The instrument used for a measurement",
    )

class ReagentKitEnum(EnumDefinitionImpl):
    """
    The reagent kit used for a measurement
    """
    placeholder = PermissibleValue(
        text="placeholder",
        description="Placeholder value")

    _defn = EnumDefinition(
        name="ReagentKitEnum",
        description="The reagent kit used for a measurement",
    )

class BodyPositionEnum(EnumDefinitionImpl):
    """
    The body position during a measurement
    """
    supine = PermissibleValue(
        text="supine",
        description="Lying face up")
    standing = PermissibleValue(
        text="standing",
        description="Standing upright")
    sitting = PermissibleValue(
        text="sitting",
        description="Seated position")

    _defn = EnumDefinition(
        name="BodyPositionEnum",
        description="The body position during a measurement",
    )

class ContextEnum(EnumDefinitionImpl):
    """
    The context in which a measurement was taken
    """
    fasted_8_hrs = PermissibleValue(
        text="fasted_8_hrs",
        description="Fasted for 8 hours")
    fasted_12_hrs = PermissibleValue(
        text="fasted_12_hrs",
        description="Fasted for 12 hours")
    before_bronchodilator = PermissibleValue(
        text="before_bronchodilator",
        description="Before bronchodilator administration")
    after_bronchodilator = PermissibleValue(
        text="after_bronchodilator",
        description="After bronchodilator administration")
    taking_lipid_lowering_medications = PermissibleValue(
        text="taking_lipid_lowering_medications",
        description="While taking lipid-lowering medications")
    before_physical_activity = PermissibleValue(
        text="before_physical_activity",
        description="Before physical activity")
    during_physical_activity = PermissibleValue(
        text="during_physical_activity",
        description="During physical activity")
    after_physical_activity = PermissibleValue(
        text="after_physical_activity",
        description="After physical activity")
    during_procedure = PermissibleValue(
        text="during_procedure",
        description="During a procedure")
    taking_diabetes_medication = PermissibleValue(
        text="taking_diabetes_medication",
        description="While taking diabetes medication")
    lowest = PermissibleValue(
        text="lowest",
        description="Lowest recorded value")

    _defn = EnumDefinition(
        name="ContextEnum",
        description="The context in which a measurement was taken",
    )

class CollectedByEnum(EnumDefinitionImpl):
    """
    Who collected the measurement
    """
    doctor = PermissibleValue(
        text="doctor",
        description="Collected by a doctor")
    nurse = PermissibleValue(
        text="nurse",
        description="Collected by a nurse")
    technician = PermissibleValue(
        text="technician",
        description="Collected by a technician")
    self_administered = PermissibleValue(
        text="self_administered",
        description="Self-administered by the patient")
    first_examiner = PermissibleValue(
        text="first_examiner",
        description="Collected by the first examiner")
    second_examiner = PermissibleValue(
        text="second_examiner",
        description="Collected by the second examiner")

    _defn = EnumDefinition(
        name="CollectedByEnum",
        description="Who collected the measurement",
    )

class AssociatedEvidenceEnum(EnumDefinitionImpl):
    """
    The method used for diagnosis
    """
    placeholder = PermissibleValue(
        text="placeholder",
        description="Placeholder value")

    _defn = EnumDefinition(
        name="AssociatedEvidenceEnum",
        description="The method used for diagnosis",
    )

class ActivityTypeEnum(EnumDefinitionImpl):
    """
    Type of activity being recorded
    """
    fasting = PermissibleValue(text="fasting")
    bronchodilator_medication_use = PermissibleValue(text="bronchodilator_medication_use")
    diabetes_medication_use = PermissibleValue(text="diabetes_medication_use")
    antihyperlipidemics_medication_use = PermissibleValue(text="antihyperlipidemics_medication_use")
    physical_activity = PermissibleValue(text="physical_activity")
    medical_procedure = PermissibleValue(text="medical_procedure")

    _defn = EnumDefinition(
        name="ActivityTypeEnum",
        description="Type of activity being recorded",
    )

class RelativeTimingEnum(EnumDefinitionImpl):
    """
    Set of values describing the relative timing of an activity
    """
    after = PermissibleValue(text="after")
    before = PermissibleValue(text="before")
    during = PermissibleValue(text="during")

    _defn = EnumDefinition(
        name="RelativeTimingEnum",
        description="Set of values describing the relative timing of an activity",
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

slots.minimum_value = Slot(uri=BDC_VARIABLE_LIBRARY.minimum_value, name="minimum_value", curie=BDC_VARIABLE_LIBRARY.curie('minimum_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.minimum_value, domain=None, range=Optional[Decimal])

slots.maximum_value = Slot(uri=BDC_VARIABLE_LIBRARY.maximum_value, name="maximum_value", curie=BDC_VARIABLE_LIBRARY.curie('maximum_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.maximum_value, domain=None, range=Optional[Decimal])

slots.resolution = Slot(uri=BDC_VARIABLE_LIBRARY.resolution, name="resolution", curie=BDC_VARIABLE_LIBRARY.curie('resolution'),
                   model_uri=BDC_VARIABLE_LIBRARY.resolution, domain=None, range=Optional[int])

slots.coded_values = Slot(uri=BDC_VARIABLE_LIBRARY.coded_values, name="coded_values", curie=BDC_VARIABLE_LIBRARY.curie('coded_values'),
                   model_uri=BDC_VARIABLE_LIBRARY.coded_values, domain=None, range=Optional[str])

slots.missing_value = Slot(uri=BDC_VARIABLE_LIBRARY.missing_value, name="missing_value", curie=BDC_VARIABLE_LIBRARY.curie('missing_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.missing_value, domain=None, range=Optional[Union[dict[Union[str, MissingValueId], Union[dict, MissingValue]], list[Union[dict, MissingValue]]]])

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
                   model_uri=BDC_VARIABLE_LIBRARY.metadata, domain=None, range=Optional[Union[dict[Union[str, MetadataVariableId], Union[dict, MetadataVariable]], list[Union[dict, MetadataVariable]]]])

slots.alert_value = Slot(uri=BDC_VARIABLE_LIBRARY.alert_value, name="alert_value", curie=BDC_VARIABLE_LIBRARY.curie('alert_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.alert_value, domain=None, range=Optional[Union[Union[str, AlertValueId], list[Union[str, AlertValueId]]]])

slots.indicator_char = Slot(uri=BDC_VARIABLE_LIBRARY.indicator_char, name="indicator_char", curie=BDC_VARIABLE_LIBRARY.curie('indicator_char'),
                   model_uri=BDC_VARIABLE_LIBRARY.indicator_char, domain=None, range=Optional[str])

slots.indicator_meaning = Slot(uri=BDC_VARIABLE_LIBRARY.indicator_meaning, name="indicator_meaning", curie=BDC_VARIABLE_LIBRARY.curie('indicator_meaning'),
                   model_uri=BDC_VARIABLE_LIBRARY.indicator_meaning, domain=None, range=Optional[str])

slots.microschema_slot = Slot(uri=BDC_VARIABLE_LIBRARY.microschema_slot, name="microschema_slot", curie=BDC_VARIABLE_LIBRARY.curie('microschema_slot'),
                   model_uri=BDC_VARIABLE_LIBRARY.microschema_slot, domain=None, range=Optional[Union[str, "ClinicalMicroschemaEnum"]])

slots.integrates = Slot(uri=BDC_VARIABLE_LIBRARY.integrates, name="integrates", curie=BDC_VARIABLE_LIBRARY.curie('integrates'),
                   model_uri=BDC_VARIABLE_LIBRARY.integrates, domain=None, range=Optional[Union[Union[str, CompoundVariableId], list[Union[str, CompoundVariableId]]]])

slots.profile_version = Slot(uri=LINKML['linkml-microschema-profile/profile_version'], name="profile_version", curie=LINKML.curie('linkml-microschema-profile/profile_version'),
                   model_uri=BDC_VARIABLE_LIBRARY.profile_version, domain=None, range=Optional[str])

slots.domain_of_use = Slot(uri=LINKML['linkml-microschema-profile/domain_of_use'], name="domain_of_use", curie=LINKML.curie('linkml-microschema-profile/domain_of_use'),
                   model_uri=BDC_VARIABLE_LIBRARY.domain_of_use, domain=None, range=Optional[Union[str, list[str]]])

slots.subject = Slot(uri=LINKML['linkml-microschema-profile/subject'], name="subject", curie=LINKML.curie('linkml-microschema-profile/subject'),
                   model_uri=BDC_VARIABLE_LIBRARY.subject, domain=None, range=str)

slots.observation_type = Slot(uri=LINKML['linkml-microschema-profile/observation_type'], name="observation_type", curie=LINKML.curie('linkml-microschema-profile/observation_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.observation_type, domain=None, range=str)

slots.location = Slot(uri=LINKML['linkml-microschema-profile/location'], name="location", curie=LINKML.curie('linkml-microschema-profile/location'),
                   model_uri=BDC_VARIABLE_LIBRARY.location, domain=None, range=str)

slots.temporality = Slot(uri=LINKML['linkml-microschema-profile/temporality'], name="temporality", curie=LINKML.curie('linkml-microschema-profile/temporality'),
                   model_uri=BDC_VARIABLE_LIBRARY.temporality, domain=None, range=str)

slots.methodology = Slot(uri=LINKML['linkml-microschema-profile/methodology'], name="methodology", curie=LINKML.curie('linkml-microschema-profile/methodology'),
                   model_uri=BDC_VARIABLE_LIBRARY.methodology, domain=None, range=str)

slots.observation_result = Slot(uri=LINKML['linkml-microschema-profile/observation_result'], name="observation_result", curie=LINKML.curie('linkml-microschema-profile/observation_result'),
                   model_uri=BDC_VARIABLE_LIBRARY.observation_result, domain=None, range=Union[dict, ValueMicroschemaDefinition])

slots.quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.quantity_value, domain=None, range=Decimal)

slots.quantity_unit = Slot(uri=SCHEMA.unitCode, name="quantity_unit", curie=SCHEMA.curie('unitCode'),
                   model_uri=BDC_VARIABLE_LIBRARY.quantity_unit, domain=None, range=Union[str, URIorCURIE])

slots.comparator = Slot(uri=LINKML['linkml-microschema-profile/comparator'], name="comparator", curie=LINKML.curie('linkml-microschema-profile/comparator'),
                   model_uri=BDC_VARIABLE_LIBRARY.comparator, domain=None, range=Optional[Union[str, "ComparatorEnum"]])

slots.datetime = Slot(uri=LINKML['linkml-microschema-profile/datetime'], name="datetime", curie=LINKML.curie('linkml-microschema-profile/datetime'),
                   model_uri=BDC_VARIABLE_LIBRARY.datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.relative_to_event = Slot(uri=LINKML['linkml-microschema-profile/relative_to_event'], name="relative_to_event", curie=LINKML.curie('linkml-microschema-profile/relative_to_event'),
                   model_uri=BDC_VARIABLE_LIBRARY.relative_to_event, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.offset = Slot(uri=LINKML['linkml-microschema-profile/offset'], name="offset", curie=LINKML.curie('linkml-microschema-profile/offset'),
                   model_uri=BDC_VARIABLE_LIBRARY.offset, domain=None, range=Optional[Union[dict, Quantity]])

slots.subject_age = Slot(uri=LINKML['linkml-microschema-profile/subject_age'], name="subject_age", curie=LINKML.curie('linkml-microschema-profile/subject_age'),
                   model_uri=BDC_VARIABLE_LIBRARY.subject_age, domain=None, range=Optional[Union[dict, Quantity]])

slots.interval_start = Slot(uri=LINKML['linkml-microschema-profile/interval_start'], name="interval_start", curie=LINKML.curie('linkml-microschema-profile/interval_start'),
                   model_uri=BDC_VARIABLE_LIBRARY.interval_start, domain=None, range=Optional[Union[dict, Timepoint]])

slots.interval_end = Slot(uri=LINKML['linkml-microschema-profile/interval_end'], name="interval_end", curie=LINKML.curie('linkml-microschema-profile/interval_end'),
                   model_uri=BDC_VARIABLE_LIBRARY.interval_end, domain=None, range=Optional[Union[dict, Timepoint]])

slots.duration = Slot(uri=LINKML['linkml-microschema-profile/duration'], name="duration", curie=LINKML.curie('linkml-microschema-profile/duration'),
                   model_uri=BDC_VARIABLE_LIBRARY.duration, domain=None, range=Optional[Union[dict, Quantity]])

slots.code = Slot(uri=LINKML['linkml-microschema-profile/code'], name="code", curie=LINKML.curie('linkml-microschema-profile/code'),
                   model_uri=BDC_VARIABLE_LIBRARY.code, domain=None, range=Union[str, URIorCURIE])

slots.code_label = Slot(uri=LINKML['linkml-microschema-profile/code_label'], name="code_label", curie=LINKML.curie('linkml-microschema-profile/code_label'),
                   model_uri=BDC_VARIABLE_LIBRARY.code_label, domain=None, range=Optional[str])

slots.code_system = Slot(uri=LINKML['linkml-microschema-profile/code_system'], name="code_system", curie=LINKML.curie('linkml-microschema-profile/code_system'),
                   model_uri=BDC_VARIABLE_LIBRARY.code_system, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.dose = Slot(uri=CMS.dose, name="dose", curie=CMS.curie('dose'),
                   model_uri=BDC_VARIABLE_LIBRARY.dose, domain=None, range=Optional[Union[dict, Quantity]])

slots.frequency = Slot(uri=CMS.frequency, name="frequency", curie=CMS.curie('frequency'),
                   model_uri=BDC_VARIABLE_LIBRARY.frequency, domain=None, range=Optional[Union[dict, Quantity]])

slots.indication = Slot(uri=CMS.indication, name="indication", curie=CMS.curie('indication'),
                   model_uri=BDC_VARIABLE_LIBRARY.indication, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.subject_identifier = Slot(uri=CMS.subject_identifier, name="subject_identifier", curie=CMS.curie('subject_identifier'),
                   model_uri=BDC_VARIABLE_LIBRARY.subject_identifier, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.measurement_type = Slot(uri=BDCHM.observation_type, name="measurement_type", curie=BDCHM.curie('observation_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.measurement_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.unit = Slot(uri=BDCHM.unit, name="unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.unit, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.method = Slot(uri=BDCHM.method_type, name="method", curie=BDCHM.curie('method_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.method, domain=None, range=Optional[Union[str, "MethodEnum"]])

slots.instrument = Slot(uri=CMS.instrument, name="instrument", curie=CMS.curie('instrument'),
                   model_uri=BDC_VARIABLE_LIBRARY.instrument, domain=None, range=Optional[Union[str, "InstrumentEnum"]])

slots.reagent_kit = Slot(uri=CMS.reagent_kit, name="reagent_kit", curie=CMS.curie('reagent_kit'),
                   model_uri=BDC_VARIABLE_LIBRARY.reagent_kit, domain=None, range=Optional[Union[str, "ReagentKitEnum"]])

slots.calculated_from = Slot(uri=CMS.calculated_from, name="calculated_from", curie=CMS.curie('calculated_from'),
                   model_uri=BDC_VARIABLE_LIBRARY.calculated_from, domain=None, range=Optional[str])

slots.body_location = Slot(uri=BDCHM.BodySite, name="body_location", curie=BDCHM.curie('BodySite'),
                   model_uri=BDC_VARIABLE_LIBRARY.body_location, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.body_position = Slot(uri=CMS.body_position, name="body_position", curie=CMS.curie('body_position'),
                   model_uri=BDC_VARIABLE_LIBRARY.body_position, domain=None, range=Optional[Union[str, "BodyPositionEnum"]])

slots.context = Slot(uri=CMS.context, name="context", curie=CMS.curie('context'),
                   model_uri=BDC_VARIABLE_LIBRARY.context, domain=None, range=Optional[Union[str, "ContextEnum"]])

slots.collected_by = Slot(uri=CMS.collected_by, name="collected_by", curie=CMS.curie('collected_by'),
                   model_uri=BDC_VARIABLE_LIBRARY.collected_by, domain=None, range=Optional[Union[str, "CollectedByEnum"]])

slots.condition_type = Slot(uri=BDCHM.condition_concept, name="condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.condition_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.associated_evidence = Slot(uri=CMS.associated_evidence, name="associated_evidence", curie=CMS.curie('associated_evidence'),
                   model_uri=BDC_VARIABLE_LIBRARY.associated_evidence, domain=None, range=Optional[Union[str, "AssociatedEvidenceEnum"]])

slots.drug_type = Slot(uri=BDCHM.drug_concept, name="drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.drug_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.procedure_type = Slot(uri=BDCHM.procedure_concept, name="procedure_type", curie=BDCHM.curie('procedure_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.procedure_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.data_type = Slot(uri=CMS.data_type, name="data_type", curie=CMS.curie('data_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.age_at_measurement = Slot(uri=CMS.age_at_measurement, name="age_at_measurement", curie=CMS.curie('age_at_measurement'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_measurement, domain=None, range=Optional[Union[dict, Quantity]])

slots.age_at_condition_start = Slot(uri=CMS.age_at_condition_start, name="age_at_condition_start", curie=CMS.curie('age_at_condition_start'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_condition_start, domain=None, range=Optional[Union[dict, Quantity]])

slots.age_at_condition_end = Slot(uri=CMS.age_at_condition_end, name="age_at_condition_end", curie=CMS.curie('age_at_condition_end'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_condition_end, domain=None, range=Optional[Union[dict, Quantity]])

slots.condition_status = Slot(uri=CMS.condition_status, name="condition_status", curie=CMS.curie('condition_status'),
                   model_uri=BDC_VARIABLE_LIBRARY.condition_status, domain=None, range=Optional[Union[str, "HistoricalStatusEnum"]])

slots.condition_provenance = Slot(uri=CMS.condition_provenance, name="condition_provenance", curie=CMS.curie('condition_provenance'),
                   model_uri=BDC_VARIABLE_LIBRARY.condition_provenance, domain=None, range=Optional[Union[str, "ProvenanceEnum"]])

slots.condition_severity = Slot(uri=CMS.condition_severity, name="condition_severity", curie=CMS.curie('condition_severity'),
                   model_uri=BDC_VARIABLE_LIBRARY.condition_severity, domain=None, range=Optional[Union[str, "ConditionSeverityEnum"]])

slots.relationship_to_participant = Slot(uri=CMS.relationship_to_participant, name="relationship_to_participant", curie=CMS.curie('relationship_to_participant'),
                   model_uri=BDC_VARIABLE_LIBRARY.relationship_to_participant, domain=None, range=Optional[Union[str, "FamilyRelationshipEnum"]])

slots.age_at_drug_start = Slot(uri=CMS.age_at_drug_start, name="age_at_drug_start", curie=CMS.curie('age_at_drug_start'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_drug_start, domain=None, range=Optional[Union[dict, Quantity]])

slots.age_at_drug_end = Slot(uri=CMS.age_at_drug_end, name="age_at_drug_end", curie=CMS.curie('age_at_drug_end'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_drug_end, domain=None, range=Optional[Union[dict, Quantity]])

slots.age_at_procedure_start = Slot(uri=CMS.age_at_procedure_start, name="age_at_procedure_start", curie=CMS.curie('age_at_procedure_start'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_procedure_start, domain=None, range=Optional[Union[dict, Quantity]])

slots.age_at_procedure_end = Slot(uri=CMS.age_at_procedure_end, name="age_at_procedure_end", curie=CMS.curie('age_at_procedure_end'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_procedure_end, domain=None, range=Optional[Union[dict, Quantity]])

slots.route_of_administration = Slot(uri=CMS.route_of_administration, name="route_of_administration", curie=CMS.curie('route_of_administration'),
                   model_uri=BDC_VARIABLE_LIBRARY.route_of_administration, domain=None, range=Optional[Union[str, "RouteAdminEnum"]])

slots.measurement_value = Slot(uri=CMS.measurement_value, name="measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.measurement_value, domain=None, range=Optional[Union[dict, Quantity]])

slots.predicted_value = Slot(uri=CMS.predicted_value, name="predicted_value", curie=CMS.curie('predicted_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.predicted_value, domain=None, range=Optional[Decimal])

slots.lower_limit_normal = Slot(uri=CMS.lower_limit_normal, name="lower_limit_normal", curie=CMS.curie('lower_limit_normal'),
                   model_uri=BDC_VARIABLE_LIBRARY.lower_limit_normal, domain=None, range=Optional[Decimal])

slots.upper_limit_normal = Slot(uri=CMS.upper_limit_normal, name="upper_limit_normal", curie=CMS.curie('upper_limit_normal'),
                   model_uri=BDC_VARIABLE_LIBRARY.upper_limit_normal, domain=None, range=Optional[Decimal])

slots.percent_predicted_value = Slot(uri=CMS.percent_predicted_value, name="percent_predicted_value", curie=CMS.curie('percent_predicted_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.percent_predicted_value, domain=None, range=Optional[Decimal])

slots.activity_type = Slot(uri=CMS.activity_type, name="activity_type", curie=CMS.curie('activity_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.activity_type, domain=None, range=Optional[Union[str, "ActivityTypeEnum"]])

slots.relative_timing = Slot(uri=CMS.relative_timing, name="relative_timing", curie=CMS.curie('relative_timing'),
                   model_uri=BDC_VARIABLE_LIBRARY.relative_timing, domain=None, range=Optional[Union[str, "RelativeTimingEnum"]])

slots.study_site = Slot(uri=CMS.study_site, name="study_site", curie=CMS.curie('study_site'),
                   model_uri=BDC_VARIABLE_LIBRARY.study_site, domain=None, range=Optional[str])

slots.absolute_time = Slot(uri=CMS.absolute_time, name="absolute_time", curie=CMS.curie('absolute_time'),
                   model_uri=BDC_VARIABLE_LIBRARY.absolute_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.age_at_condition_record = Slot(uri=CMS.age_at_condition_record, name="age_at_condition_record", curie=CMS.curie('age_at_condition_record'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_condition_record, domain=None, range=Optional[Union[dict, Quantity]])

slots.age_at_drug_record = Slot(uri=CMS.age_at_drug_record, name="age_at_drug_record", curie=CMS.curie('age_at_drug_record'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_drug_record, domain=None, range=Optional[Union[dict, Quantity]])

slots.age_at_procedure_record = Slot(uri=CMS.age_at_procedure_record, name="age_at_procedure_record", curie=CMS.curie('age_at_procedure_record'),
                   model_uri=BDC_VARIABLE_LIBRARY.age_at_procedure_record, domain=None, range=Optional[Union[dict, Quantity]])

slots.ClinicalMeasurementRecord_subject_identifier = Slot(uri=CMS.subject_identifier, name="ClinicalMeasurementRecord_subject_identifier", curie=CMS.curie('subject_identifier'),
                   model_uri=BDC_VARIABLE_LIBRARY.ClinicalMeasurementRecord_subject_identifier, domain=ClinicalMeasurementRecord, range=Union[str, URIorCURIE])

slots.ClinicalMeasurementRecord_measurement_type = Slot(uri=BDCHM.observation_type, name="ClinicalMeasurementRecord_measurement_type", curie=BDCHM.curie('observation_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.ClinicalMeasurementRecord_measurement_type, domain=ClinicalMeasurementRecord, range=Union[str, URIorCURIE])

slots.ClinicalMeasurementRecord_measurement_value = Slot(uri=CMS.measurement_value, name="ClinicalMeasurementRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.ClinicalMeasurementRecord_measurement_value, domain=ClinicalMeasurementRecord, range=Union[dict, Quantity])

slots.ClinicalMeasurementRecord_age_at_measurement = Slot(uri=CMS.age_at_measurement, name="ClinicalMeasurementRecord_age_at_measurement", curie=CMS.curie('age_at_measurement'),
                   model_uri=BDC_VARIABLE_LIBRARY.ClinicalMeasurementRecord_age_at_measurement, domain=ClinicalMeasurementRecord, range=Union[dict, Quantity])

slots.ConditionStatusRecord_subject_identifier = Slot(uri=CMS.subject_identifier, name="ConditionStatusRecord_subject_identifier", curie=CMS.curie('subject_identifier'),
                   model_uri=BDC_VARIABLE_LIBRARY.ConditionStatusRecord_subject_identifier, domain=ConditionStatusRecord, range=Union[str, URIorCURIE])

slots.ConditionStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="ConditionStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.ConditionStatusRecord_condition_type, domain=ConditionStatusRecord, range=Union[str, URIorCURIE])

slots.ConditionStatusRecord_condition_status = Slot(uri=CMS.condition_status, name="ConditionStatusRecord_condition_status", curie=CMS.curie('condition_status'),
                   model_uri=BDC_VARIABLE_LIBRARY.ConditionStatusRecord_condition_status, domain=ConditionStatusRecord, range=Union[str, "HistoricalStatusEnum"])

slots.ConditionStatusRecord_relationship_to_participant = Slot(uri=CMS.relationship_to_participant, name="ConditionStatusRecord_relationship_to_participant", curie=CMS.curie('relationship_to_participant'),
                   model_uri=BDC_VARIABLE_LIBRARY.ConditionStatusRecord_relationship_to_participant, domain=ConditionStatusRecord, range=Union[str, "FamilyRelationshipEnum"])

slots.ConditionStatusRecord_age_at_condition_record = Slot(uri=CMS.age_at_condition_record, name="ConditionStatusRecord_age_at_condition_record", curie=CMS.curie('age_at_condition_record'),
                   model_uri=BDC_VARIABLE_LIBRARY.ConditionStatusRecord_age_at_condition_record, domain=ConditionStatusRecord, range=Union[dict, Quantity])

slots.DrugStatusRecord_subject_identifier = Slot(uri=CMS.subject_identifier, name="DrugStatusRecord_subject_identifier", curie=CMS.curie('subject_identifier'),
                   model_uri=BDC_VARIABLE_LIBRARY.DrugStatusRecord_subject_identifier, domain=DrugStatusRecord, range=Union[str, URIorCURIE])

slots.DrugStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="DrugStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.DrugStatusRecord_drug_type, domain=DrugStatusRecord, range=Union[str, URIorCURIE])

slots.DrugStatusRecord_age_at_drug_record = Slot(uri=CMS.age_at_drug_record, name="DrugStatusRecord_age_at_drug_record", curie=CMS.curie('age_at_drug_record'),
                   model_uri=BDC_VARIABLE_LIBRARY.DrugStatusRecord_age_at_drug_record, domain=DrugStatusRecord, range=Union[dict, Quantity])

slots.ProcedureStatusRecord_subject_identifier = Slot(uri=CMS.subject_identifier, name="ProcedureStatusRecord_subject_identifier", curie=CMS.curie('subject_identifier'),
                   model_uri=BDC_VARIABLE_LIBRARY.ProcedureStatusRecord_subject_identifier, domain=ProcedureStatusRecord, range=Union[str, URIorCURIE])

slots.ProcedureStatusRecord_procedure_type = Slot(uri=BDCHM.procedure_concept, name="ProcedureStatusRecord_procedure_type", curie=BDCHM.curie('procedure_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.ProcedureStatusRecord_procedure_type, domain=ProcedureStatusRecord, range=Union[str, URIorCURIE])

slots.ProcedureStatusRecord_age_at_procedure_record = Slot(uri=CMS.age_at_procedure_record, name="ProcedureStatusRecord_age_at_procedure_record", curie=CMS.curie('age_at_procedure_record'),
                   model_uri=BDC_VARIABLE_LIBRARY.ProcedureStatusRecord_age_at_procedure_record, domain=ProcedureStatusRecord, range=Union[dict, Quantity])

slots.HumanBodyHeightRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyHeightRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord_measurement_value, domain=HumanBodyHeightRecord, range=Union[dict, "HumanBodyHeightQuantity"])

slots.HumanBodyHeightRecord001_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyHeightRecord001_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord001_measurement_value, domain=HumanBodyHeightRecord001, range=Union[dict, "HumanBodyHeightQuantity001"])

slots.HumanBodyHeightRecord002_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyHeightRecord002_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord002_measurement_value, domain=HumanBodyHeightRecord002, range=Union[dict, "HumanBodyHeightQuantity002"])

slots.HumanBodyHeightRecord003_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyHeightRecord003_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord003_measurement_value, domain=HumanBodyHeightRecord003, range=Union[dict, "HumanBodyHeightQuantity002"])

slots.HumanBodyHeightRecord004_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyHeightRecord004_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord004_measurement_value, domain=HumanBodyHeightRecord004, range=Union[dict, "HumanBodyHeightQuantity003"])

slots.HumanBodyHeightRecord005_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyHeightRecord005_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord005_measurement_value, domain=HumanBodyHeightRecord005, range=Union[dict, "HumanBodyHeightQuantity004"])

slots.HumanBodyHeightRecord006_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyHeightRecord006_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord006_measurement_value, domain=HumanBodyHeightRecord006, range=Union[dict, "HumanBodyHeightQuantity003"])

slots.HumanBodyHeightRecord006_unit = Slot(uri=BDCHM.unit, name="HumanBodyHeightRecord006_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord006_unit, domain=HumanBodyHeightRecord006, range=Optional[Union[str, URIorCURIE]])

slots.HumanBodyWeightRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyWeightRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightRecord_measurement_value, domain=HumanBodyWeightRecord, range=Union[dict, "HumanBodyWeightQuantity"])

slots.HumanBodyWeightRecord001_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyWeightRecord001_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightRecord001_measurement_value, domain=HumanBodyWeightRecord001, range=Union[dict, "HumanBodyWeightQuantity001"])

slots.HumanBodyWeightRecord002_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyWeightRecord002_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightRecord002_measurement_value, domain=HumanBodyWeightRecord002, range=Union[dict, "HumanBodyWeightQuantity002"])

slots.HumanBodyWeightRecord003_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyWeightRecord003_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightRecord003_measurement_value, domain=HumanBodyWeightRecord003, range=Union[dict, "HumanBodyWeightQuantity003"])

slots.BodyMassIndexRecord_measurement_value = Slot(uri=CMS.measurement_value, name="BodyMassIndexRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.BodyMassIndexRecord_measurement_value, domain=BodyMassIndexRecord, range=Union[dict, "BodyMassIndexQuantity"])

slots.BodyMassIndexRecord001_measurement_value = Slot(uri=CMS.measurement_value, name="BodyMassIndexRecord001_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.BodyMassIndexRecord001_measurement_value, domain=BodyMassIndexRecord001, range=Union[dict, "BodyMassIndexQuantity"])

slots.BodyMassIndexRecord001_calculated_from = Slot(uri=CMS.calculated_from, name="BodyMassIndexRecord001_calculated_from", curie=CMS.curie('calculated_from'),
                   model_uri=BDC_VARIABLE_LIBRARY.BodyMassIndexRecord001_calculated_from, domain=BodyMassIndexRecord001, range=Optional[str])

slots.BodyMassIndexRecord002_measurement_value = Slot(uri=CMS.measurement_value, name="BodyMassIndexRecord002_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.BodyMassIndexRecord002_measurement_value, domain=BodyMassIndexRecord002, range=Union[dict, "BodyMassIndexQuantity"])

slots.BodyMassIndexRecord002_calculated_from = Slot(uri=CMS.calculated_from, name="BodyMassIndexRecord002_calculated_from", curie=CMS.curie('calculated_from'),
                   model_uri=BDC_VARIABLE_LIBRARY.BodyMassIndexRecord002_calculated_from, domain=BodyMassIndexRecord002, range=Optional[str])

slots.HumanFvcRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFvcRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFvcRecord_measurement_value, domain=HumanFvcRecord, range=Union[dict, "HumanFvcQuantity"])

slots.HumanFvcRecord_predicted_value = Slot(uri=CMS.predicted_value, name="HumanFvcRecord_predicted_value", curie=CMS.curie('predicted_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFvcRecord_predicted_value, domain=HumanFvcRecord, range=Decimal)

slots.HumanFvcRecord_percent_predicted_value = Slot(uri=CMS.percent_predicted_value, name="HumanFvcRecord_percent_predicted_value", curie=CMS.curie('percent_predicted_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFvcRecord_percent_predicted_value, domain=HumanFvcRecord, range=Decimal)

slots.HumanMeasuredFvcRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMeasuredFvcRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMeasuredFvcRecord_measurement_value, domain=HumanMeasuredFvcRecord, range=Union[dict, "HumanMeasuredFvcQuantity"])

slots.HumanMeasuredFvcRecord001_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMeasuredFvcRecord001_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMeasuredFvcRecord001_measurement_value, domain=HumanMeasuredFvcRecord001, range=Union[dict, "HumanMeasuredFvcQuantity001"])

slots.HumanPredictedFvcRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPredictedFvcRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPredictedFvcRecord_measurement_value, domain=HumanPredictedFvcRecord, range=Union[dict, "HumanPredictedFvcQuantity"])

slots.HumanPercentPredictedFvcRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPercentPredictedFvcRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPercentPredictedFvcRecord_measurement_value, domain=HumanPercentPredictedFvcRecord, range=Union[dict, "HumanPercentPredictedFvcQuantity"])

slots.HumanFev1Record_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFev1Record_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFev1Record_measurement_value, domain=HumanFev1Record, range=Union[dict, "HumanFev1Quantity"])

slots.HumanBasophilCountRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBasophilCountRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord_measurement_value, domain=HumanBasophilCountRecord, range=Union[dict, "HumanBasophilCountQuantity"])

slots.HumanBasophilCountRecord001_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBasophilCountRecord001_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord001_measurement_value, domain=HumanBasophilCountRecord001, range=Union[dict, "HumanBasophilCountQuantity001"])

slots.HumanBasophilCountRecord001_unit = Slot(uri=BDCHM.unit, name="HumanBasophilCountRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord001_unit, domain=HumanBasophilCountRecord001, range=Optional[Union[str, URIorCURIE]])

slots.HumanBasophilCountRecord002_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBasophilCountRecord002_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord002_measurement_value, domain=HumanBasophilCountRecord002, range=Union[dict, "HumanBasophilCountQuantity001"])

slots.HumanBasophilCountRecord002_unit = Slot(uri=BDCHM.unit, name="HumanBasophilCountRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord002_unit, domain=HumanBasophilCountRecord002, range=Optional[Union[str, URIorCURIE]])

slots.HumanBodyHeightQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyHeightQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity_quantity_value, domain=HumanBodyHeightQuantity, range=Decimal)

slots.HumanBodyHeightQuantity001_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyHeightQuantity001_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity001_quantity_value, domain=HumanBodyHeightQuantity001, range=Decimal)

slots.HumanBodyHeightQuantity002_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyHeightQuantity002_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity002_quantity_value, domain=HumanBodyHeightQuantity002, range=Decimal)

slots.HumanBodyHeightQuantity003_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyHeightQuantity003_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity003_quantity_value, domain=HumanBodyHeightQuantity003, range=Decimal)

slots.HumanBodyHeightQuantity004_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyHeightQuantity004_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity004_quantity_value, domain=HumanBodyHeightQuantity004, range=Decimal)

slots.HumanBodyWeightQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyWeightQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightQuantity_quantity_value, domain=HumanBodyWeightQuantity, range=Decimal)

slots.HumanBodyWeightQuantity001_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyWeightQuantity001_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightQuantity001_quantity_value, domain=HumanBodyWeightQuantity001, range=Decimal)

slots.HumanBodyWeightQuantity002_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyWeightQuantity002_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightQuantity002_quantity_value, domain=HumanBodyWeightQuantity002, range=Decimal)

slots.HumanBodyWeightQuantity003_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyWeightQuantity003_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightQuantity003_quantity_value, domain=HumanBodyWeightQuantity003, range=Decimal)

slots.BodyMassIndexQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="BodyMassIndexQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.BodyMassIndexQuantity_quantity_value, domain=BodyMassIndexQuantity, range=Decimal)

slots.HumanFvcQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFvcQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFvcQuantity_quantity_value, domain=HumanFvcQuantity, range=Decimal)

slots.HumanMeasuredFvcQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMeasuredFvcQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMeasuredFvcQuantity_quantity_value, domain=HumanMeasuredFvcQuantity, range=Decimal)

slots.HumanMeasuredFvcQuantity001_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMeasuredFvcQuantity001_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMeasuredFvcQuantity001_quantity_value, domain=HumanMeasuredFvcQuantity001, range=Decimal)

slots.HumanPredictedFvcQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPredictedFvcQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPredictedFvcQuantity_quantity_value, domain=HumanPredictedFvcQuantity, range=Decimal)

slots.HumanPercentPredictedFvcQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPercentPredictedFvcQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPercentPredictedFvcQuantity_quantity_value, domain=HumanPercentPredictedFvcQuantity, range=Decimal)

slots.HumanFev1Quantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFev1Quantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFev1Quantity_quantity_value, domain=HumanFev1Quantity, range=Decimal)

slots.HumanBasophilCountQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBasophilCountQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountQuantity_quantity_value, domain=HumanBasophilCountQuantity, range=Decimal)

slots.HumanBasophilCountQuantity001_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBasophilCountQuantity001_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountQuantity001_quantity_value, domain=HumanBasophilCountQuantity001, range=Decimal)

slots.HumanBasophilCountQuantity002_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBasophilCountQuantity002_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountQuantity002_quantity_value, domain=HumanBasophilCountQuantity002, range=Decimal)

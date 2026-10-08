# Auto generated from bdc_variable_library.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-10-07T14:45:51
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


class SingleContinuousVariableId(VariableId):
    pass


class SingleCategoricalVariableId(VariableId):
    pass


class CompoundVariableId(VariableId):
    pass


class IntegratedVariableId(VariableId):
    pass


class MetadataVariableId(EntityId):
    pass


class CompoundHeight002Id(CompoundVariableId):
    pass


class CompoundHeight001Id(CompoundVariableId):
    pass


class IntegratedHeight001Id(IntegratedVariableId):
    pass


class CompoundWeight001Id(CompoundVariableId):
    pass


class CompoundWeight002Id(CompoundVariableId):
    pass


class CompoundWeight003Id(CompoundVariableId):
    pass


class CompoundWeight004Id(CompoundVariableId):
    pass


class IntegratedWeight001Id(IntegratedVariableId):
    pass


class CompoundBMI001Id(CompoundVariableId):
    pass


class IntegratedBMI001Id(IntegratedVariableId):
    pass


class CompoundBasophilCount001Id(CompoundVariableId):
    pass


class CompoundBasophilCount002Id(CompoundVariableId):
    pass


class IntegratedBasophilCount001Id(IntegratedVariableId):
    pass


class Compound8epiPGF2a001Id(CompoundVariableId):
    pass


class Integrated8epiPGF2a001Id(IntegratedVariableId):
    pass


class CompoundLPPLA2Activity001Id(CompoundVariableId):
    pass


class IntegratedLPPLA2Activity001Id(IntegratedVariableId):
    pass


class CompoundCreatinineUrine001Id(CompoundVariableId):
    pass


class CompoundCreatinineUrine002Id(CompoundVariableId):
    pass


class IntegratedCreatinineUrine001Id(IntegratedVariableId):
    pass


class CompoundAlbuminUrine001Id(CompoundVariableId):
    pass


class CompoundAlbuminUrine002Id(CompoundVariableId):
    pass


class CompoundAlbuminUrine003Id(CompoundVariableId):
    pass


class CompoundAlbuminUrine004Id(CompoundVariableId):
    pass


class CompoundAlbuminUrine005Id(CompoundVariableId):
    pass


class IntegratedAlbuminUrine001Id(IntegratedVariableId):
    pass


class CompoundAlbuminCreatinineRatioUrine001Id(CompoundVariableId):
    pass


class IntegratedAlbuminCreatinineRatioUrine001Id(IntegratedVariableId):
    pass


class CompoundAsthma001Id(CompoundVariableId):
    pass


class IntegratedAsthma001Id(IntegratedVariableId):
    pass


class CompoundHeartFailure001Id(CompoundVariableId):
    pass


class IntegratedHeartFailure001Id(IntegratedVariableId):
    pass


class CompoundObesity001Id(CompoundVariableId):
    pass


class IntegratedObesity001Id(IntegratedVariableId):
    pass


class CompoundAspirin001Id(CompoundVariableId):
    pass


class IntegratedAspirin001Id(IntegratedVariableId):
    pass


class CompoundPacemaker001Id(CompoundVariableId):
    pass


class IntegratedPacemaker001Id(IntegratedVariableId):
    pass


class CompoundAtrialFibrillation001Id(CompoundVariableId):
    pass


class IntegratedAtrialFibrillation001Id(IntegratedVariableId):
    pass


class CompoundAngina001Id(CompoundVariableId):
    pass


class IntegratedAngina001Id(IntegratedVariableId):
    pass


class CompoundCardiovascularDisease001Id(CompoundVariableId):
    pass


class IntegratedCardiovascularDisease001Id(IntegratedVariableId):
    pass


class CompoundCarotidPlaque001Id(CompoundVariableId):
    pass


class IntegratedCarotidPlaque001Id(IntegratedVariableId):
    pass


class CompoundCOPD001Id(CompoundVariableId):
    pass


class IntegratedCOPD001Id(IntegratedVariableId):
    pass


class CompoundDiabetes001Id(CompoundVariableId):
    pass


class IntegratedDiabetes001Id(IntegratedVariableId):
    pass


class CompoundStroke001Id(CompoundVariableId):
    pass


class IntegratedStroke001Id(IntegratedVariableId):
    pass


class CompoundHeartDisease001Id(CompoundVariableId):
    pass


class IntegratedHeartDisease001Id(IntegratedVariableId):
    pass


class CompoundMyocardialInfarction001Id(CompoundVariableId):
    pass


class IntegratedMyocardialInfarction001Id(IntegratedVariableId):
    pass


class CompoundHypertension001Id(CompoundVariableId):
    pass


class IntegratedHypertension001Id(IntegratedVariableId):
    pass


class CompoundLeftVentricularHypertrophy001Id(CompoundVariableId):
    pass


class IntegratedLeftVentricularHypertrophy001Id(IntegratedVariableId):
    pass


class CompoundPeripheralArterialDisease001Id(CompoundVariableId):
    pass


class IntegratedPeripheralArterialDisease001Id(IntegratedVariableId):
    pass


class CompoundSleepApnea001Id(CompoundVariableId):
    pass


class IntegratedSleepApnea001Id(IntegratedVariableId):
    pass


class CompoundValvularHeartDisease001Id(CompoundVariableId):
    pass


class IntegratedValvularHeartDisease001Id(IntegratedVariableId):
    pass


class CompoundVenousThromboembolism001Id(CompoundVariableId):
    pass


class IntegratedVenousThromboembolism001Id(IntegratedVariableId):
    pass


class CompoundBetaBlocker001Id(CompoundVariableId):
    pass


class IntegratedBetaBlocker001Id(IntegratedVariableId):
    pass


class CompoundDiabetesMedication001Id(CompoundVariableId):
    pass


class IntegratedDiabetesMedication001Id(IntegratedVariableId):
    pass


class CompoundHypertensionMedication001Id(CompoundVariableId):
    pass


class IntegratedHypertensionMedication001Id(IntegratedVariableId):
    pass


class CompoundAceInhibitor001Id(CompoundVariableId):
    pass


class IntegratedAceInhibitor001Id(IntegratedVariableId):
    pass


class CompoundAldosteroneReceptorBlocker001Id(CompoundVariableId):
    pass


class IntegratedAldosteroneReceptorBlocker001Id(IntegratedVariableId):
    pass


class CompoundAlphaBlocker001Id(CompoundVariableId):
    pass


class IntegratedAlphaBlocker001Id(IntegratedVariableId):
    pass


class CompoundAngiotensinReceptorBlocker001Id(CompoundVariableId):
    pass


class IntegratedAngiotensinReceptorBlocker001Id(IntegratedVariableId):
    pass


class CompoundCalciumChannelBlocker001Id(CompoundVariableId):
    pass


class IntegratedCalciumChannelBlocker001Id(IntegratedVariableId):
    pass


class CompoundCentrallyActingAgents001Id(CompoundVariableId):
    pass


class IntegratedCentrallyActingAgents001Id(IntegratedVariableId):
    pass


class CompoundDiuretics001Id(CompoundVariableId):
    pass


class IntegratedDiuretics001Id(IntegratedVariableId):
    pass


class CompoundInsulin001Id(CompoundVariableId):
    pass


class IntegratedInsulin001Id(IntegratedVariableId):
    pass


class CompoundNiacinMedication001Id(CompoundVariableId):
    pass


class IntegratedNiacinMedication001Id(IntegratedVariableId):
    pass


class CompoundLipidLoweringMedication001Id(CompoundVariableId):
    pass


class IntegratedLipidLoweringMedication001Id(IntegratedVariableId):
    pass


class CompoundFibrates001Id(CompoundVariableId):
    pass


class IntegratedFibrates001Id(IntegratedVariableId):
    pass


class CompoundBileAcidSequestrant001Id(CompoundVariableId):
    pass


class IntegratedBileAcidSequestrant001Id(IntegratedVariableId):
    pass


class CompoundOralHypoglycemicAgent001Id(CompoundVariableId):
    pass


class IntegratedOralHypoglycemicAgent001Id(IntegratedVariableId):
    pass


class CompoundStatin001Id(CompoundVariableId):
    pass


class IntegratedStatin001Id(IntegratedVariableId):
    pass


class CompoundSystemicSteroid001Id(CompoundVariableId):
    pass


class IntegratedSystemicSteroid001Id(IntegratedVariableId):
    pass


class CompoundVasodilator001Id(CompoundVariableId):
    pass


class IntegratedVasodilator001Id(IntegratedVariableId):
    pass


class CompoundCoronaryAngioplasty001Id(CompoundVariableId):
    pass


class IntegratedCoronaryAngioplasty001Id(IntegratedVariableId):
    pass


class CompoundCoronaryBypass001Id(CompoundVariableId):
    pass


class IntegratedCoronaryBypass001Id(IntegratedVariableId):
    pass


class CompoundApneaHypopneaIndex001Id(CompoundVariableId):
    pass


class IntegratedApneaHypopneaIndex001Id(IntegratedVariableId):
    pass


class CompoundAlbuminBlood001Id(CompoundVariableId):
    pass


class IntegratedAlbuminBlood001Id(IntegratedVariableId):
    pass


class CompoundAlcoholConsumption001Id(CompoundVariableId):
    pass


class IntegratedAlcoholConsumption001Id(IntegratedVariableId):
    pass


class CompoundAltSgpt001Id(CompoundVariableId):
    pass


class IntegratedAltSgpt001Id(IntegratedVariableId):
    pass


class CompoundAstSgot001Id(CompoundVariableId):
    pass


class IntegratedAstSgot001Id(IntegratedVariableId):
    pass


class CompoundBilirubinConjugated001Id(CompoundVariableId):
    pass


class IntegratedBilirubinConjugated001Id(IntegratedVariableId):
    pass


class CompoundBilirubinTotal001Id(CompoundVariableId):
    pass


class IntegratedBilirubinTotal001Id(IntegratedVariableId):
    pass


class CompoundBNP001Id(CompoundVariableId):
    pass


class IntegratedBNP001Id(IntegratedVariableId):
    pass


class CompoundBloodPressure001Id(CompoundVariableId):
    pass


class IntegratedBloodPressure001Id(IntegratedVariableId):
    pass


class CompoundBloodUreaNitrogen001Id(CompoundVariableId):
    pass


class IntegratedBloodUreaNitrogen001Id(IntegratedVariableId):
    pass


class CompoundBodyTemperature001Id(CompoundVariableId):
    pass


class IntegratedBodyTemperature001Id(IntegratedVariableId):
    pass


class CompoundBUNCreatinineRatio001Id(CompoundVariableId):
    pass


class IntegratedBUNCreatinineRatio001Id(IntegratedVariableId):
    pass


class CompoundCarotidIntimamediaThickness001Id(CompoundVariableId):
    pass


class IntegratedCarotidIntimamediaThickness001Id(IntegratedVariableId):
    pass


class CompoundCarotidStenosisLeft001Id(CompoundVariableId):
    pass


class IntegratedCarotidStenosisLeft001Id(IntegratedVariableId):
    pass


class CompoundCarotidStenosisRight001Id(CompoundVariableId):
    pass


class IntegratedCarotidStenosisRight001Id(IntegratedVariableId):
    pass


class CompoundCESDScore001Id(CompoundVariableId):
    pass


class IntegratedCESDScore001Id(IntegratedVariableId):
    pass


class CompoundChlorideBlood001Id(CompoundVariableId):
    pass


class CompoundChlorideBlood002Id(CompoundVariableId):
    pass


class IntegratedChlorideBlood001Id(IntegratedVariableId):
    pass


class CompoundCoronaryArteryCalciumScore001Id(CompoundVariableId):
    pass


class IntegratedCoronaryArteryCalciumScore001Id(IntegratedVariableId):
    pass


class CompoundCoronaryArteryCalciumVolume001Id(CompoundVariableId):
    pass


class IntegratedCoronaryArteryCalciumVolume001Id(IntegratedVariableId):
    pass


class CompoundCReactiveProtein001Id(CompoundVariableId):
    pass


class CompoundCReactiveProtein002Id(CompoundVariableId):
    pass


class CompoundCReactiveProtein003Id(CompoundVariableId):
    pass


class IntegratedCReactiveProtein001Id(IntegratedVariableId):
    pass


class CompoundCreatinineBlood001Id(CompoundVariableId):
    pass


class IntegratedCreatinineBlood001Id(IntegratedVariableId):
    pass


class CompoundCystatinCBlood001Id(CompoundVariableId):
    pass


class IntegratedCystatinCBlood001Id(IntegratedVariableId):
    pass


class CompoundDDimer001Id(CompoundVariableId):
    pass


class CompoundDDimer002Id(CompoundVariableId):
    pass


class IntegratedDDimer001Id(IntegratedVariableId):
    pass


class CompoundDiastolicBloodPressure001Id(CompoundVariableId):
    pass


class IntegratedDiastolicBloodPressure001Id(IntegratedVariableId):
    pass


class CompoundEosinophilCount001Id(CompoundVariableId):
    pass


class IntegratedEosinophilCount001Id(IntegratedVariableId):
    pass


class CompoundESelectinBlood001Id(CompoundVariableId):
    pass


class IntegratedESelectinBlood001Id(IntegratedVariableId):
    pass


class CompoundEstimatedGFR001Id(CompoundVariableId):
    pass


class IntegratedEstimatedGFR001Id(IntegratedVariableId):
    pass


class CompoundFactorVII001Id(CompoundVariableId):
    pass


class IntegratedFactorVII001Id(IntegratedVariableId):
    pass


class CompoundFactorVIII001Id(CompoundVariableId):
    pass


class IntegratedFactorVIII001Id(IntegratedVariableId):
    pass


class CompoundFastingGlucose001Id(CompoundVariableId):
    pass


class CompoundFastingGlucose002Id(CompoundVariableId):
    pass


class IntegratedFastingGlucose001Id(IntegratedVariableId):
    pass


class CompoundFerritin001Id(CompoundVariableId):
    pass


class IntegratedFerritin001Id(IntegratedVariableId):
    pass


class CompoundFibrinogen001Id(CompoundVariableId):
    pass


class IntegratedFibrinogen001Id(IntegratedVariableId):
    pass


class CompoundFruitConsumption001Id(CompoundVariableId):
    pass


class IntegratedFruitConsumption001Id(IntegratedVariableId):
    pass


class CompoundGFR001Id(CompoundVariableId):
    pass


class IntegratedGFR001Id(IntegratedVariableId):
    pass


class CompoundGlucoseBlood001Id(CompoundVariableId):
    pass


class IntegratedGlucoseBlood001Id(IntegratedVariableId):
    pass


class CompoundHDL001Id(CompoundVariableId):
    pass


class CompoundHDL002Id(CompoundVariableId):
    pass


class IntegratedHDL001Id(IntegratedVariableId):
    pass


class CompoundHeartRate001Id(CompoundVariableId):
    pass


class IntegratedHeartRate001Id(IntegratedVariableId):
    pass


class CompoundHematocrit001Id(CompoundVariableId):
    pass


class IntegratedHematocrit001Id(IntegratedVariableId):
    pass


class CompoundHemoglobin001Id(CompoundVariableId):
    pass


class IntegratedHemoglobin001Id(IntegratedVariableId):
    pass


class CompoundHipCircumference001Id(CompoundVariableId):
    pass


class CompoundHipCircumference002Id(CompoundVariableId):
    pass


class IntegratedHipCircumference001Id(IntegratedVariableId):
    pass


class CompoundInsulinBlood001Id(CompoundVariableId):
    pass


class CompoundInsulinBlood002Id(CompoundVariableId):
    pass


class IntegratedInsulinBlood001Id(IntegratedVariableId):
    pass


class CompoundLactateBlood001Id(CompoundVariableId):
    pass


class IntegratedLactateBlood001Id(IntegratedVariableId):
    pass


class CompoundLactateDehydrogenase001Id(CompoundVariableId):
    pass


class IntegratedLactateDehydrogenase001Id(IntegratedVariableId):
    pass


class CompoundLDL001Id(CompoundVariableId):
    pass


class IntegratedLDL001Id(IntegratedVariableId):
    pass


class CompoundLymphocyteCount001Id(CompoundVariableId):
    pass


class IntegratedLymphocyteCount001Id(IntegratedVariableId):
    pass


class CompoundLymphocytePercent001Id(CompoundVariableId):
    pass


class IntegratedLymphocytePercent001Id(IntegratedVariableId):
    pass


class CompoundMCH001Id(CompoundVariableId):
    pass


class IntegratedMCH001Id(IntegratedVariableId):
    pass


class CompoundMCHC001Id(CompoundVariableId):
    pass


class IntegratedMCHC001Id(IntegratedVariableId):
    pass


class CompoundMCV001Id(CompoundVariableId):
    pass


class IntegratedMCV001Id(IntegratedVariableId):
    pass


class CompoundMeanArterialPressure001Id(CompoundVariableId):
    pass


class IntegratedMeanArterialPressure001Id(IntegratedVariableId):
    pass


class CompoundMonocyteCount001Id(CompoundVariableId):
    pass


class IntegratedMonocyteCount001Id(IntegratedVariableId):
    pass


class CompoundMPV001Id(CompoundVariableId):
    pass


class IntegratedMPV001Id(IntegratedVariableId):
    pass


class CompoundMyeloperoxidaseBlood001Id(CompoundVariableId):
    pass


class IntegratedMyeloperoxidaseBlood001Id(IntegratedVariableId):
    pass


class CompoundNeutrophilCount001Id(CompoundVariableId):
    pass


class IntegratedNeutrophilCount001Id(IntegratedVariableId):
    pass


class CompoundNeutrophilPercent001Id(CompoundVariableId):
    pass


class IntegratedNeutrophilPercent001Id(IntegratedVariableId):
    pass


class CompoundNTproBNP001Id(CompoundVariableId):
    pass


class IntegratedNTproBNP001Id(IntegratedVariableId):
    pass


class CompoundOsteoprotegerinBlood001Id(CompoundVariableId):
    pass


class IntegratedOsteoprotegerinBlood001Id(IntegratedVariableId):
    pass


class CompoundPlateletCount001Id(CompoundVariableId):
    pass


class IntegratedPlateletCount001Id(IntegratedVariableId):
    pass


class CompoundPotassiumBlood001Id(CompoundVariableId):
    pass


class IntegratedPotassiumBlood001Id(IntegratedVariableId):
    pass


class CompoundPRInterval001Id(CompoundVariableId):
    pass


class IntegratedPRInterval001Id(IntegratedVariableId):
    pass


class CompoundPSelectinBlood001Id(CompoundVariableId):
    pass


class IntegratedPSelectinBlood001Id(IntegratedVariableId):
    pass


class CompoundQRSInterval001Id(CompoundVariableId):
    pass


class IntegratedQRSInterval001Id(IntegratedVariableId):
    pass


class CompoundQTInterval001Id(CompoundVariableId):
    pass


class IntegratedQTInterval001Id(IntegratedVariableId):
    pass


class CompoundRBCCount001Id(CompoundVariableId):
    pass


class IntegratedRBCCount001Id(IntegratedVariableId):
    pass


class CompoundRDW001Id(CompoundVariableId):
    pass


class IntegratedRDW001Id(IntegratedVariableId):
    pass


class CompoundSleepDuration001Id(CompoundVariableId):
    pass


class IntegratedSleepDuration001Id(IntegratedVariableId):
    pass


class CompoundSodiumBlood001Id(CompoundVariableId):
    pass


class IntegratedSodiumBlood001Id(IntegratedVariableId):
    pass


class CompoundSodiumIntake001Id(CompoundVariableId):
    pass


class IntegratedSodiumIntake001Id(IntegratedVariableId):
    pass


class CompoundSystolicBloodPressure001Id(CompoundVariableId):
    pass


class IntegratedSystolicBloodPressure001Id(IntegratedVariableId):
    pass


class CompoundTNFAlphaBlood001Id(CompoundVariableId):
    pass


class IntegratedTNFAlphaBlood001Id(IntegratedVariableId):
    pass


class CompoundTotalCholesterol001Id(CompoundVariableId):
    pass


class CompoundTotalCholesterol002Id(CompoundVariableId):
    pass


class IntegratedTotalCholesterol001Id(IntegratedVariableId):
    pass


class CompoundTriglyceridesBlood001Id(CompoundVariableId):
    pass


class CompoundTriglyceridesBlood002Id(CompoundVariableId):
    pass


class IntegratedTriglyceridesBlood001Id(IntegratedVariableId):
    pass


class CompoundTroponin001Id(CompoundVariableId):
    pass


class IntegratedTroponin001Id(IntegratedVariableId):
    pass


class CompoundVegetableConsumption001Id(CompoundVariableId):
    pass


class IntegratedVegetableConsumption001Id(IntegratedVariableId):
    pass


class CompoundVonWillebrandFactor001Id(CompoundVariableId):
    pass


class IntegratedVonWillebrandFactor001Id(IntegratedVariableId):
    pass


class CompoundWaistCircumference001Id(CompoundVariableId):
    pass


class CompoundWaistCircumference002Id(CompoundVariableId):
    pass


class CompoundWaistCircumference003Id(CompoundVariableId):
    pass


class IntegratedWaistCircumference001Id(IntegratedVariableId):
    pass


class CompoundWaistHipRatio001Id(CompoundVariableId):
    pass


class IntegratedWaistHipRatio001Id(IntegratedVariableId):
    pass


class CompoundWhiteBloodCellCount001Id(CompoundVariableId):
    pass


class IntegratedWhiteBloodCellCount001Id(IntegratedVariableId):
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
class SingleContinuousVariable(Variable):
    """
    Represents a single entry in a data dictionary of a variable with a continuous value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["SingleContinuousVariable"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:SingleContinuousVariable"
    class_name: ClassVar[str] = "SingleContinuousVariable"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.SingleContinuousVariable

    id: Union[str, SingleContinuousVariableId] = None
    source_id: Optional[str] = None
    file_id: Optional[str] = None
    file_name: Optional[str] = None
    variable_name: Optional[str] = None
    source_variable_description: Optional[str] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None
    minimum_value: Optional[Decimal] = None
    maximum_value: Optional[Decimal] = None
    resolution: Optional[int] = None
    missing_value: Optional[Union[Union[dict, "MissingValue"], list[Union[dict, "MissingValue"]]]] = empty_list()
    unit: Optional[str] = None
    alert_values: Optional[Union[Union[dict, "AlertValue"], list[Union[dict, "AlertValue"]]]] = empty_list()
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SingleContinuousVariableId):
            self.id = SingleContinuousVariableId(self.id)

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

        if not isinstance(self.missing_value, list):
            self.missing_value = [self.missing_value] if self.missing_value is not None else []
        self.missing_value = [v if isinstance(v, MissingValue) else MissingValue(**as_dict(v)) for v in self.missing_value]

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if not isinstance(self.alert_values, list):
            self.alert_values = [self.alert_values] if self.alert_values is not None else []
        self.alert_values = [v if isinstance(v, AlertValue) else AlertValue(**as_dict(v)) for v in self.alert_values]

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SingleCategoricalVariable(Variable):
    """
    Represents a single entry in a data dictionary of a variable with a categorical value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["SingleCategoricalVariable"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:SingleCategoricalVariable"
    class_name: ClassVar[str] = "SingleCategoricalVariable"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.SingleCategoricalVariable

    id: Union[str, SingleCategoricalVariableId] = None
    source_id: Optional[str] = None
    file_id: Optional[str] = None
    file_name: Optional[str] = None
    variable_name: Optional[str] = None
    source_variable_description: Optional[str] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None
    missing_value: Optional[Union[Union[dict, "MissingValue"], list[Union[dict, "MissingValue"]]]] = empty_list()
    coded_values: Optional[Union[Union[dict, "EnumValue"], list[Union[dict, "EnumValue"]]]] = empty_list()
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SingleCategoricalVariableId):
            self.id = SingleCategoricalVariableId(self.id)

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

        if not isinstance(self.missing_value, list):
            self.missing_value = [self.missing_value] if self.missing_value is not None else []
        self.missing_value = [v if isinstance(v, MissingValue) else MissingValue(**as_dict(v)) for v in self.missing_value]

        if not isinstance(self.coded_values, list):
            self.coded_values = [self.coded_values] if self.coded_values is not None else []
        self.coded_values = [v if isinstance(v, EnumValue) else EnumValue(**as_dict(v)) for v in self.coded_values]

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
    unit: Optional[str] = None
    row_metadata: Optional[Union[dict[Union[str, MetadataVariableId], Union[dict, "MetadataVariable"]], list[Union[dict, "MetadataVariable"]]]] = empty_dict()
    documentation_metadata: Optional[Union[Union[dict, "DocumentationVariable"], list[Union[dict, "DocumentationVariable"]]]] = empty_list()
    alert_value: Optional[Union[Union[dict, "AlertValue"], list[Union[dict, "AlertValue"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundVariableId):
            self.id = CompoundVariableId(self.id)

        if self.cde_id is not None and not isinstance(self.cde_id, URIorCURIE):
            self.cde_id = URIorCURIE(self.cde_id)

        if self.bdchm_type is not None and not isinstance(self.bdchm_type, BdchmTypeEnum):
            self.bdchm_type = BdchmTypeEnum(self.bdchm_type)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        self._normalize_inlined_as_list(slot_name="row_metadata", slot_type=MetadataVariable, key_name="id", keyed=True)

        if not isinstance(self.documentation_metadata, list):
            self.documentation_metadata = [self.documentation_metadata] if self.documentation_metadata is not None else []
        self.documentation_metadata = [v if isinstance(v, DocumentationVariable) else DocumentationVariable(**as_dict(v)) for v in self.documentation_metadata]

        if not isinstance(self.alert_value, list):
            self.alert_value = [self.alert_value] if self.alert_value is not None else []
        self.alert_value = [v if isinstance(v, AlertValue) else AlertValue(**as_dict(v)) for v in self.alert_value]

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
    unit: Optional[str] = None
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

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if not isinstance(self.integrates, list):
            self.integrates = [self.integrates] if self.integrates is not None else []
        self.integrates = [v if isinstance(v, CompoundVariableId) else CompoundVariableId(v) for v in self.integrates]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MissingValue(YAMLRoot):
    """
    Character used to indicate a missing value in a data set
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["MissingValue"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:MissingValue"
    class_name: ClassVar[str] = "MissingValue"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.MissingValue

    indicator_char: Optional[str] = None
    indicator_meaning: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.indicator_char is not None and not isinstance(self.indicator_char, str):
            self.indicator_char = str(self.indicator_char)

        if self.indicator_meaning is not None and not isinstance(self.indicator_meaning, str):
            self.indicator_meaning = str(self.indicator_meaning)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlertValue(YAMLRoot):
    """
    Character used to add information to a datum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["AlertValue"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:AlertValue"
    class_name: ClassVar[str] = "AlertValue"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AlertValue

    indicator_char: Optional[str] = None
    indicator_meaning: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.indicator_char is not None and not isinstance(self.indicator_char, str):
            self.indicator_char = str(self.indicator_char)

        if self.indicator_meaning is not None and not isinstance(self.indicator_meaning, str):
            self.indicator_meaning = str(self.indicator_meaning)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnumValue(YAMLRoot):
    """
    One possible answer in a list of enumerated values
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["EnumValue"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:EnumValue"
    class_name: ClassVar[str] = "EnumValue"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.EnumValue

    indicator_char: Optional[str] = None
    indicator_meaning: Optional[str] = None
    indicator_type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.indicator_char is not None and not isinstance(self.indicator_char, str):
            self.indicator_char = str(self.indicator_char)

        if self.indicator_meaning is not None and not isinstance(self.indicator_meaning, str):
            self.indicator_meaning = str(self.indicator_meaning)

        if self.indicator_type is not None and not isinstance(self.indicator_type, URIorCURIE):
            self.indicator_type = URIorCURIE(self.indicator_type)

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
    microschema_slot: Optional[Union[Union[str, "ClinicalMicroschemaEnum"], list[Union[str, "ClinicalMicroschemaEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetadataVariableId):
            self.id = MetadataVariableId(self.id)

        if not isinstance(self.microschema_slot, list):
            self.microschema_slot = [self.microschema_slot] if self.microschema_slot is not None else []
        self.microschema_slot = [v if isinstance(v, ClinicalMicroschemaEnum) else ClinicalMicroschemaEnum(v) for v in self.microschema_slot]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DocumentationVariable(YAMLRoot):
    """
    Information derived from study documentation or text in a data dictionary that provides essential metadata for a
    variable
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["DocumentationVariable"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:DocumentationVariable"
    class_name: ClassVar[str] = "DocumentationVariable"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.DocumentationVariable

    contr_vocab: Optional[str] = None
    microschema_slot: Optional[Union[Union[str, "ClinicalMicroschemaEnum"], list[Union[str, "ClinicalMicroschemaEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contr_vocab is not None and not isinstance(self.contr_vocab, str):
            self.contr_vocab = str(self.contr_vocab)

        if not isinstance(self.microschema_slot, list):
            self.microschema_slot = [self.microschema_slot] if self.microschema_slot is not None else []
        self.microschema_slot = [v if isinstance(v, ClinicalMicroschemaEnum) else ClinicalMicroschemaEnum(v) for v in self.microschema_slot]

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
class CompoundHeight001(CompoundVariable):
    """
    Height variable with metadata, measured in cm and collected using a wall-mounted stadiometer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHeight001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHeight001"
    class_name: ClassVar[str] = "CompoundHeight001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHeight001

    id: Union[str, CompoundHeight001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHeight001Id):
            self.id = CompoundHeight001Id(self.id)

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
class CompoundWeight001(CompoundVariable):
    """
    Weight variable with metadata, measured in kg using a mechanical beam balance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundWeight001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundWeight001"
    class_name: ClassVar[str] = "CompoundWeight001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundWeight001

    id: Union[str, CompoundWeight001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundWeight001Id):
            self.id = CompoundWeight001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundWeight002(CompoundVariable):
    """
    Weight variable with metadata, measured in pounds using a mechanical beam balance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundWeight002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundWeight002"
    class_name: ClassVar[str] = "CompoundWeight002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundWeight002

    id: Union[str, CompoundWeight002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundWeight002Id):
            self.id = CompoundWeight002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundWeight003(CompoundVariable):
    """
    Weight variable with metadata, measured in kg using a body composition analyzer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundWeight003"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundWeight003"
    class_name: ClassVar[str] = "CompoundWeight003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundWeight003

    id: Union[str, CompoundWeight003Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundWeight003Id):
            self.id = CompoundWeight003Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundWeight004(CompoundVariable):
    """
    Weight variable with metadata, measured in kg using a digital scale
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundWeight004"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundWeight004"
    class_name: ClassVar[str] = "CompoundWeight004"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundWeight004

    id: Union[str, CompoundWeight004Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundWeight004Id):
            self.id = CompoundWeight004Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedWeight001(IntegratedVariable):
    """
    Weight variable containing data from multiple studies, normalized to kg
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedWeight001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedWeight001"
    class_name: ClassVar[str] = "IntegratedWeight001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedWeight001

    id: Union[str, IntegratedWeight001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedWeight001Id):
            self.id = IntegratedWeight001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBMI001(CompoundVariable):
    """
    Body mass index variable with metadata, calculated as weight (kg) divided by height (m) squared
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBMI001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBMI001"
    class_name: ClassVar[str] = "CompoundBMI001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBMI001

    id: Union[str, CompoundBMI001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBMI001Id):
            self.id = CompoundBMI001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBMI001(IntegratedVariable):
    """
    Body mass index variable containing data from multiple studies, normalized to kg/m2
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBMI001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBMI001"
    class_name: ClassVar[str] = "IntegratedBMI001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBMI001

    id: Union[str, IntegratedBMI001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBMI001Id):
            self.id = IntegratedBMI001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBasophilCount001(CompoundVariable):
    """
    Basophil count variable with metadata, measured in 10*3/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBasophilCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBasophilCount001"
    class_name: ClassVar[str] = "CompoundBasophilCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBasophilCount001

    id: Union[str, CompoundBasophilCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBasophilCount001Id):
            self.id = CompoundBasophilCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBasophilCount002(CompoundVariable):
    """
    Basophil count variable with metadata, measured in cells/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBasophilCount002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBasophilCount002"
    class_name: ClassVar[str] = "CompoundBasophilCount002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBasophilCount002

    id: Union[str, CompoundBasophilCount002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBasophilCount002Id):
            self.id = CompoundBasophilCount002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBasophilCount001(IntegratedVariable):
    """
    Basophil count variable containing data from multiple studies, normalized to 10*3/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBasophilCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBasophilCount001"
    class_name: ClassVar[str] = "IntegratedBasophilCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBasophilCount001

    id: Union[str, IntegratedBasophilCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBasophilCount001Id):
            self.id = IntegratedBasophilCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Compound8epiPGF2a001(CompoundVariable):
    """
    8-epi-prostaglandin F2 alpha concentration in urine variable with metadata, measured in pg/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["Compound8epiPGF2a001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:Compound8epiPGF2a001"
    class_name: ClassVar[str] = "Compound8epiPGF2a001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Compound8epiPGF2a001

    id: Union[str, Compound8epiPGF2a001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Compound8epiPGF2a001Id):
            self.id = Compound8epiPGF2a001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Integrated8epiPGF2a001(IntegratedVariable):
    """
    8-epi-prostaglandin F2 alpha concentration in urine variable containing data from multiple studies, normalized to
    pg/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["Integrated8epiPGF2a001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:Integrated8epiPGF2a001"
    class_name: ClassVar[str] = "Integrated8epiPGF2a001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Integrated8epiPGF2a001

    id: Union[str, Integrated8epiPGF2a001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Integrated8epiPGF2a001Id):
            self.id = Integrated8epiPGF2a001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundLPPLA2Activity001(CompoundVariable):
    """
    LP-PLA2 activity in blood variable with metadata, measured in nmol/min/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundLPPLA2Activity001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundLPPLA2Activity001"
    class_name: ClassVar[str] = "CompoundLPPLA2Activity001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundLPPLA2Activity001

    id: Union[str, CompoundLPPLA2Activity001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundLPPLA2Activity001Id):
            self.id = CompoundLPPLA2Activity001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedLPPLA2Activity001(IntegratedVariable):
    """
    LP-PLA2 activity in blood variable containing data from multiple studies, normalized to nmol/min/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedLPPLA2Activity001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedLPPLA2Activity001"
    class_name: ClassVar[str] = "IntegratedLPPLA2Activity001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedLPPLA2Activity001

    id: Union[str, IntegratedLPPLA2Activity001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedLPPLA2Activity001Id):
            self.id = IntegratedLPPLA2Activity001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCreatinineUrine001(CompoundVariable):
    """
    Creatinine concentration in urine variable with metadata, measured in mg/dL using the Jaffe reaction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCreatinineUrine001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCreatinineUrine001"
    class_name: ClassVar[str] = "CompoundCreatinineUrine001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCreatinineUrine001

    id: Union[str, CompoundCreatinineUrine001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCreatinineUrine001Id):
            self.id = CompoundCreatinineUrine001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCreatinineUrine002(CompoundVariable):
    """
    Creatinine concentration in urine variable with metadata, measured in mmol/L using the Jaffe reaction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCreatinineUrine002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCreatinineUrine002"
    class_name: ClassVar[str] = "CompoundCreatinineUrine002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCreatinineUrine002

    id: Union[str, CompoundCreatinineUrine002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCreatinineUrine002Id):
            self.id = CompoundCreatinineUrine002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCreatinineUrine001(IntegratedVariable):
    """
    Creatinine concentration in urine variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCreatinineUrine001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCreatinineUrine001"
    class_name: ClassVar[str] = "IntegratedCreatinineUrine001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCreatinineUrine001

    id: Union[str, IntegratedCreatinineUrine001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCreatinineUrine001Id):
            self.id = IntegratedCreatinineUrine001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAlbuminUrine001(CompoundVariable):
    """
    Albumin concentration in urine variable with metadata, measured in mg/dL using immunoturbidometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAlbuminUrine001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAlbuminUrine001"
    class_name: ClassVar[str] = "CompoundAlbuminUrine001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAlbuminUrine001

    id: Union[str, CompoundAlbuminUrine001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAlbuminUrine001Id):
            self.id = CompoundAlbuminUrine001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAlbuminUrine002(CompoundVariable):
    """
    Albumin concentration in urine variable with metadata, measured in mg/L using an albumin dipstick
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAlbuminUrine002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAlbuminUrine002"
    class_name: ClassVar[str] = "CompoundAlbuminUrine002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAlbuminUrine002

    id: Union[str, CompoundAlbuminUrine002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAlbuminUrine002Id):
            self.id = CompoundAlbuminUrine002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAlbuminUrine003(CompoundVariable):
    """
    Albumin concentration in urine variable with metadata, measured in mg/L using HPLC
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAlbuminUrine003"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAlbuminUrine003"
    class_name: ClassVar[str] = "CompoundAlbuminUrine003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAlbuminUrine003

    id: Union[str, CompoundAlbuminUrine003Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAlbuminUrine003Id):
            self.id = CompoundAlbuminUrine003Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAlbuminUrine004(CompoundVariable):
    """
    Albumin concentration in urine variable with metadata, measured in mg/L using immunonephelometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAlbuminUrine004"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAlbuminUrine004"
    class_name: ClassVar[str] = "CompoundAlbuminUrine004"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAlbuminUrine004

    id: Union[str, CompoundAlbuminUrine004Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAlbuminUrine004Id):
            self.id = CompoundAlbuminUrine004Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAlbuminUrine005(CompoundVariable):
    """
    Albumin concentration in urine variable with metadata, measured in mg/L using immunoturbidometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAlbuminUrine005"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAlbuminUrine005"
    class_name: ClassVar[str] = "CompoundAlbuminUrine005"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAlbuminUrine005

    id: Union[str, CompoundAlbuminUrine005Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAlbuminUrine005Id):
            self.id = CompoundAlbuminUrine005Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAlbuminUrine001(IntegratedVariable):
    """
    Albumin concentration in urine variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAlbuminUrine001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAlbuminUrine001"
    class_name: ClassVar[str] = "IntegratedAlbuminUrine001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAlbuminUrine001

    id: Union[str, IntegratedAlbuminUrine001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAlbuminUrine001Id):
            self.id = IntegratedAlbuminUrine001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAlbuminCreatinineRatioUrine001(CompoundVariable):
    """
    Albumin to creatinine ratio in urine variable with metadata, measured in mg/g{creat}
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAlbuminCreatinineRatioUrine001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAlbuminCreatinineRatioUrine001"
    class_name: ClassVar[str] = "CompoundAlbuminCreatinineRatioUrine001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAlbuminCreatinineRatioUrine001

    id: Union[str, CompoundAlbuminCreatinineRatioUrine001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAlbuminCreatinineRatioUrine001Id):
            self.id = CompoundAlbuminCreatinineRatioUrine001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAlbuminCreatinineRatioUrine001(IntegratedVariable):
    """
    Albumin to creatinine ratio in urine variable containing data from multiple studies, normalized to mg/g{creat}
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAlbuminCreatinineRatioUrine001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAlbuminCreatinineRatioUrine001"
    class_name: ClassVar[str] = "IntegratedAlbuminCreatinineRatioUrine001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAlbuminCreatinineRatioUrine001

    id: Union[str, IntegratedAlbuminCreatinineRatioUrine001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAlbuminCreatinineRatioUrine001Id):
            self.id = IntegratedAlbuminCreatinineRatioUrine001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAsthma001(CompoundVariable):
    """
    A record of participant asthma status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAsthma001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAsthma001"
    class_name: ClassVar[str] = "CompoundAsthma001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAsthma001

    id: Union[str, CompoundAsthma001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAsthma001Id):
            self.id = CompoundAsthma001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAsthma001(IntegratedVariable):
    """
    Participant asthma status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAsthma001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAsthma001"
    class_name: ClassVar[str] = "IntegratedAsthma001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAsthma001

    id: Union[str, IntegratedAsthma001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAsthma001Id):
            self.id = IntegratedAsthma001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHeartFailure001(CompoundVariable):
    """
    A record of a participant heart failure status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHeartFailure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHeartFailure001"
    class_name: ClassVar[str] = "CompoundHeartFailure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHeartFailure001

    id: Union[str, CompoundHeartFailure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHeartFailure001Id):
            self.id = CompoundHeartFailure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHeartFailure001(IntegratedVariable):
    """
    Participant heart failure status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHeartFailure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHeartFailure001"
    class_name: ClassVar[str] = "IntegratedHeartFailure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHeartFailure001

    id: Union[str, IntegratedHeartFailure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHeartFailure001Id):
            self.id = IntegratedHeartFailure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundObesity001(CompoundVariable):
    """
    A record of a participant obesity status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundObesity001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundObesity001"
    class_name: ClassVar[str] = "CompoundObesity001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundObesity001

    id: Union[str, CompoundObesity001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundObesity001Id):
            self.id = CompoundObesity001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedObesity001(IntegratedVariable):
    """
    Participant obesity status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedObesity001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedObesity001"
    class_name: ClassVar[str] = "IntegratedObesity001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedObesity001

    id: Union[str, IntegratedObesity001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedObesity001Id):
            self.id = IntegratedObesity001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAspirin001(CompoundVariable):
    """
    A record of participant aspirin usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAspirin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAspirin001"
    class_name: ClassVar[str] = "CompoundAspirin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAspirin001

    id: Union[str, CompoundAspirin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAspirin001Id):
            self.id = CompoundAspirin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAspirin001(IntegratedVariable):
    """
    Participant aspirin status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAspirin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAspirin001"
    class_name: ClassVar[str] = "IntegratedAspirin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAspirin001

    id: Union[str, IntegratedAspirin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAspirin001Id):
            self.id = IntegratedAspirin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundPacemaker001(CompoundVariable):
    """
    A record of participant pacemaker status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundPacemaker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundPacemaker001"
    class_name: ClassVar[str] = "CompoundPacemaker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundPacemaker001

    id: Union[str, CompoundPacemaker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundPacemaker001Id):
            self.id = CompoundPacemaker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedPacemaker001(IntegratedVariable):
    """
    Participant pacemaker status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedPacemaker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedPacemaker001"
    class_name: ClassVar[str] = "IntegratedPacemaker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedPacemaker001

    id: Union[str, IntegratedPacemaker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedPacemaker001Id):
            self.id = IntegratedPacemaker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAtrialFibrillation001(CompoundVariable):
    """
    A record of participant atrial fibrillation status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAtrialFibrillation001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAtrialFibrillation001"
    class_name: ClassVar[str] = "CompoundAtrialFibrillation001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAtrialFibrillation001

    id: Union[str, CompoundAtrialFibrillation001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAtrialFibrillation001Id):
            self.id = CompoundAtrialFibrillation001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAtrialFibrillation001(IntegratedVariable):
    """
    Participant atrial fibrillation status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAtrialFibrillation001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAtrialFibrillation001"
    class_name: ClassVar[str] = "IntegratedAtrialFibrillation001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAtrialFibrillation001

    id: Union[str, IntegratedAtrialFibrillation001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAtrialFibrillation001Id):
            self.id = IntegratedAtrialFibrillation001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAngina001(CompoundVariable):
    """
    A record of participant angina status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAngina001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAngina001"
    class_name: ClassVar[str] = "CompoundAngina001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAngina001

    id: Union[str, CompoundAngina001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAngina001Id):
            self.id = CompoundAngina001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAngina001(IntegratedVariable):
    """
    Participant angina status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAngina001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAngina001"
    class_name: ClassVar[str] = "IntegratedAngina001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAngina001

    id: Union[str, IntegratedAngina001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAngina001Id):
            self.id = IntegratedAngina001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCardiovascularDisease001(CompoundVariable):
    """
    A record of participant cardiovascular disease status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCardiovascularDisease001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCardiovascularDisease001"
    class_name: ClassVar[str] = "CompoundCardiovascularDisease001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCardiovascularDisease001

    id: Union[str, CompoundCardiovascularDisease001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCardiovascularDisease001Id):
            self.id = CompoundCardiovascularDisease001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCardiovascularDisease001(IntegratedVariable):
    """
    Participant cardiovascular disease status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCardiovascularDisease001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCardiovascularDisease001"
    class_name: ClassVar[str] = "IntegratedCardiovascularDisease001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCardiovascularDisease001

    id: Union[str, IntegratedCardiovascularDisease001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCardiovascularDisease001Id):
            self.id = IntegratedCardiovascularDisease001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCarotidPlaque001(CompoundVariable):
    """
    A record of participant carotid plaque status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCarotidPlaque001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCarotidPlaque001"
    class_name: ClassVar[str] = "CompoundCarotidPlaque001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCarotidPlaque001

    id: Union[str, CompoundCarotidPlaque001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCarotidPlaque001Id):
            self.id = CompoundCarotidPlaque001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCarotidPlaque001(IntegratedVariable):
    """
    Participant carotid plaque status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCarotidPlaque001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCarotidPlaque001"
    class_name: ClassVar[str] = "IntegratedCarotidPlaque001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCarotidPlaque001

    id: Union[str, IntegratedCarotidPlaque001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCarotidPlaque001Id):
            self.id = IntegratedCarotidPlaque001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCOPD001(CompoundVariable):
    """
    A record of participant COPD status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCOPD001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCOPD001"
    class_name: ClassVar[str] = "CompoundCOPD001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCOPD001

    id: Union[str, CompoundCOPD001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCOPD001Id):
            self.id = CompoundCOPD001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCOPD001(IntegratedVariable):
    """
    Participant COPD status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCOPD001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCOPD001"
    class_name: ClassVar[str] = "IntegratedCOPD001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCOPD001

    id: Union[str, IntegratedCOPD001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCOPD001Id):
            self.id = IntegratedCOPD001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundDiabetes001(CompoundVariable):
    """
    A record of participant diabetes status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundDiabetes001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundDiabetes001"
    class_name: ClassVar[str] = "CompoundDiabetes001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundDiabetes001

    id: Union[str, CompoundDiabetes001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundDiabetes001Id):
            self.id = CompoundDiabetes001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedDiabetes001(IntegratedVariable):
    """
    Participant diabetes status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedDiabetes001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedDiabetes001"
    class_name: ClassVar[str] = "IntegratedDiabetes001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedDiabetes001

    id: Union[str, IntegratedDiabetes001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedDiabetes001Id):
            self.id = IntegratedDiabetes001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundStroke001(CompoundVariable):
    """
    A record of participant stroke status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundStroke001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundStroke001"
    class_name: ClassVar[str] = "CompoundStroke001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundStroke001

    id: Union[str, CompoundStroke001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundStroke001Id):
            self.id = CompoundStroke001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedStroke001(IntegratedVariable):
    """
    Participant stroke status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedStroke001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedStroke001"
    class_name: ClassVar[str] = "IntegratedStroke001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedStroke001

    id: Union[str, IntegratedStroke001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedStroke001Id):
            self.id = IntegratedStroke001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHeartDisease001(CompoundVariable):
    """
    A record of participant heart disease status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHeartDisease001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHeartDisease001"
    class_name: ClassVar[str] = "CompoundHeartDisease001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHeartDisease001

    id: Union[str, CompoundHeartDisease001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHeartDisease001Id):
            self.id = CompoundHeartDisease001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHeartDisease001(IntegratedVariable):
    """
    Participant heart disease status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHeartDisease001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHeartDisease001"
    class_name: ClassVar[str] = "IntegratedHeartDisease001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHeartDisease001

    id: Union[str, IntegratedHeartDisease001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHeartDisease001Id):
            self.id = IntegratedHeartDisease001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundMyocardialInfarction001(CompoundVariable):
    """
    A record of participant myocardial infarction status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundMyocardialInfarction001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundMyocardialInfarction001"
    class_name: ClassVar[str] = "CompoundMyocardialInfarction001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundMyocardialInfarction001

    id: Union[str, CompoundMyocardialInfarction001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundMyocardialInfarction001Id):
            self.id = CompoundMyocardialInfarction001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedMyocardialInfarction001(IntegratedVariable):
    """
    Participant myocardial infarction status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedMyocardialInfarction001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedMyocardialInfarction001"
    class_name: ClassVar[str] = "IntegratedMyocardialInfarction001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedMyocardialInfarction001

    id: Union[str, IntegratedMyocardialInfarction001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedMyocardialInfarction001Id):
            self.id = IntegratedMyocardialInfarction001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHypertension001(CompoundVariable):
    """
    A record of participant hypertension status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHypertension001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHypertension001"
    class_name: ClassVar[str] = "CompoundHypertension001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHypertension001

    id: Union[str, CompoundHypertension001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHypertension001Id):
            self.id = CompoundHypertension001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHypertension001(IntegratedVariable):
    """
    Participant hypertension status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHypertension001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHypertension001"
    class_name: ClassVar[str] = "IntegratedHypertension001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHypertension001

    id: Union[str, IntegratedHypertension001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHypertension001Id):
            self.id = IntegratedHypertension001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundLeftVentricularHypertrophy001(CompoundVariable):
    """
    A record of participant left ventricular hypertrophy status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundLeftVentricularHypertrophy001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundLeftVentricularHypertrophy001"
    class_name: ClassVar[str] = "CompoundLeftVentricularHypertrophy001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundLeftVentricularHypertrophy001

    id: Union[str, CompoundLeftVentricularHypertrophy001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundLeftVentricularHypertrophy001Id):
            self.id = CompoundLeftVentricularHypertrophy001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedLeftVentricularHypertrophy001(IntegratedVariable):
    """
    Participant left ventricular hypertrophy status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedLeftVentricularHypertrophy001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedLeftVentricularHypertrophy001"
    class_name: ClassVar[str] = "IntegratedLeftVentricularHypertrophy001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedLeftVentricularHypertrophy001

    id: Union[str, IntegratedLeftVentricularHypertrophy001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedLeftVentricularHypertrophy001Id):
            self.id = IntegratedLeftVentricularHypertrophy001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundPeripheralArterialDisease001(CompoundVariable):
    """
    A record of participant peripheral arterial disease status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundPeripheralArterialDisease001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundPeripheralArterialDisease001"
    class_name: ClassVar[str] = "CompoundPeripheralArterialDisease001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundPeripheralArterialDisease001

    id: Union[str, CompoundPeripheralArterialDisease001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundPeripheralArterialDisease001Id):
            self.id = CompoundPeripheralArterialDisease001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedPeripheralArterialDisease001(IntegratedVariable):
    """
    Participant peripheral arterial disease status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedPeripheralArterialDisease001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedPeripheralArterialDisease001"
    class_name: ClassVar[str] = "IntegratedPeripheralArterialDisease001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedPeripheralArterialDisease001

    id: Union[str, IntegratedPeripheralArterialDisease001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedPeripheralArterialDisease001Id):
            self.id = IntegratedPeripheralArterialDisease001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundSleepApnea001(CompoundVariable):
    """
    A record of participant sleep apnea status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundSleepApnea001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundSleepApnea001"
    class_name: ClassVar[str] = "CompoundSleepApnea001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundSleepApnea001

    id: Union[str, CompoundSleepApnea001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundSleepApnea001Id):
            self.id = CompoundSleepApnea001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedSleepApnea001(IntegratedVariable):
    """
    Participant sleep apnea status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedSleepApnea001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedSleepApnea001"
    class_name: ClassVar[str] = "IntegratedSleepApnea001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedSleepApnea001

    id: Union[str, IntegratedSleepApnea001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedSleepApnea001Id):
            self.id = IntegratedSleepApnea001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundValvularHeartDisease001(CompoundVariable):
    """
    A record of participant valvular heart disease status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundValvularHeartDisease001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundValvularHeartDisease001"
    class_name: ClassVar[str] = "CompoundValvularHeartDisease001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundValvularHeartDisease001

    id: Union[str, CompoundValvularHeartDisease001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundValvularHeartDisease001Id):
            self.id = CompoundValvularHeartDisease001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedValvularHeartDisease001(IntegratedVariable):
    """
    Participant valvular heart disease status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedValvularHeartDisease001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedValvularHeartDisease001"
    class_name: ClassVar[str] = "IntegratedValvularHeartDisease001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedValvularHeartDisease001

    id: Union[str, IntegratedValvularHeartDisease001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedValvularHeartDisease001Id):
            self.id = IntegratedValvularHeartDisease001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundVenousThromboembolism001(CompoundVariable):
    """
    A record of participant venous thromboembolism status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundVenousThromboembolism001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundVenousThromboembolism001"
    class_name: ClassVar[str] = "CompoundVenousThromboembolism001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundVenousThromboembolism001

    id: Union[str, CompoundVenousThromboembolism001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundVenousThromboembolism001Id):
            self.id = CompoundVenousThromboembolism001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedVenousThromboembolism001(IntegratedVariable):
    """
    Participant venous thromboembolism status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedVenousThromboembolism001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedVenousThromboembolism001"
    class_name: ClassVar[str] = "IntegratedVenousThromboembolism001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedVenousThromboembolism001

    id: Union[str, IntegratedVenousThromboembolism001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedVenousThromboembolism001Id):
            self.id = IntegratedVenousThromboembolism001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBetaBlocker001(CompoundVariable):
    """
    A record of participant beta blocker usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBetaBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBetaBlocker001"
    class_name: ClassVar[str] = "CompoundBetaBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBetaBlocker001

    id: Union[str, CompoundBetaBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBetaBlocker001Id):
            self.id = CompoundBetaBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBetaBlocker001(IntegratedVariable):
    """
    Participant beta blocker status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBetaBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBetaBlocker001"
    class_name: ClassVar[str] = "IntegratedBetaBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBetaBlocker001

    id: Union[str, IntegratedBetaBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBetaBlocker001Id):
            self.id = IntegratedBetaBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundDiabetesMedication001(CompoundVariable):
    """
    A record of participant diabetes medication usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundDiabetesMedication001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundDiabetesMedication001"
    class_name: ClassVar[str] = "CompoundDiabetesMedication001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundDiabetesMedication001

    id: Union[str, CompoundDiabetesMedication001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundDiabetesMedication001Id):
            self.id = CompoundDiabetesMedication001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedDiabetesMedication001(IntegratedVariable):
    """
    Participant diabetes medication status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedDiabetesMedication001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedDiabetesMedication001"
    class_name: ClassVar[str] = "IntegratedDiabetesMedication001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedDiabetesMedication001

    id: Union[str, IntegratedDiabetesMedication001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedDiabetesMedication001Id):
            self.id = IntegratedDiabetesMedication001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHypertensionMedication001(CompoundVariable):
    """
    A record of participant hypertension medication usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHypertensionMedication001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHypertensionMedication001"
    class_name: ClassVar[str] = "CompoundHypertensionMedication001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHypertensionMedication001

    id: Union[str, CompoundHypertensionMedication001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHypertensionMedication001Id):
            self.id = CompoundHypertensionMedication001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHypertensionMedication001(IntegratedVariable):
    """
    Participant hypertension medication status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHypertensionMedication001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHypertensionMedication001"
    class_name: ClassVar[str] = "IntegratedHypertensionMedication001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHypertensionMedication001

    id: Union[str, IntegratedHypertensionMedication001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHypertensionMedication001Id):
            self.id = IntegratedHypertensionMedication001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAceInhibitor001(CompoundVariable):
    """
    A record of participant ACE inhibitor usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAceInhibitor001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAceInhibitor001"
    class_name: ClassVar[str] = "CompoundAceInhibitor001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAceInhibitor001

    id: Union[str, CompoundAceInhibitor001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAceInhibitor001Id):
            self.id = CompoundAceInhibitor001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAceInhibitor001(IntegratedVariable):
    """
    Participant ACE inhibitor status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAceInhibitor001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAceInhibitor001"
    class_name: ClassVar[str] = "IntegratedAceInhibitor001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAceInhibitor001

    id: Union[str, IntegratedAceInhibitor001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAceInhibitor001Id):
            self.id = IntegratedAceInhibitor001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAldosteroneReceptorBlocker001(CompoundVariable):
    """
    A record of participant aldosterone receptor blocker usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAldosteroneReceptorBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAldosteroneReceptorBlocker001"
    class_name: ClassVar[str] = "CompoundAldosteroneReceptorBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAldosteroneReceptorBlocker001

    id: Union[str, CompoundAldosteroneReceptorBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAldosteroneReceptorBlocker001Id):
            self.id = CompoundAldosteroneReceptorBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAldosteroneReceptorBlocker001(IntegratedVariable):
    """
    Participant aldosterone receptor blocker status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAldosteroneReceptorBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAldosteroneReceptorBlocker001"
    class_name: ClassVar[str] = "IntegratedAldosteroneReceptorBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAldosteroneReceptorBlocker001

    id: Union[str, IntegratedAldosteroneReceptorBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAldosteroneReceptorBlocker001Id):
            self.id = IntegratedAldosteroneReceptorBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAlphaBlocker001(CompoundVariable):
    """
    A record of participant alpha blocker usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAlphaBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAlphaBlocker001"
    class_name: ClassVar[str] = "CompoundAlphaBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAlphaBlocker001

    id: Union[str, CompoundAlphaBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAlphaBlocker001Id):
            self.id = CompoundAlphaBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAlphaBlocker001(IntegratedVariable):
    """
    Participant alpha blocker status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAlphaBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAlphaBlocker001"
    class_name: ClassVar[str] = "IntegratedAlphaBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAlphaBlocker001

    id: Union[str, IntegratedAlphaBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAlphaBlocker001Id):
            self.id = IntegratedAlphaBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAngiotensinReceptorBlocker001(CompoundVariable):
    """
    A record of participant angiotensin receptor blocker usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAngiotensinReceptorBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAngiotensinReceptorBlocker001"
    class_name: ClassVar[str] = "CompoundAngiotensinReceptorBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAngiotensinReceptorBlocker001

    id: Union[str, CompoundAngiotensinReceptorBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAngiotensinReceptorBlocker001Id):
            self.id = CompoundAngiotensinReceptorBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAngiotensinReceptorBlocker001(IntegratedVariable):
    """
    Participant angiotensin receptor blocker status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAngiotensinReceptorBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAngiotensinReceptorBlocker001"
    class_name: ClassVar[str] = "IntegratedAngiotensinReceptorBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAngiotensinReceptorBlocker001

    id: Union[str, IntegratedAngiotensinReceptorBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAngiotensinReceptorBlocker001Id):
            self.id = IntegratedAngiotensinReceptorBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCalciumChannelBlocker001(CompoundVariable):
    """
    A record of participant calcium channel blocker usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCalciumChannelBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCalciumChannelBlocker001"
    class_name: ClassVar[str] = "CompoundCalciumChannelBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCalciumChannelBlocker001

    id: Union[str, CompoundCalciumChannelBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCalciumChannelBlocker001Id):
            self.id = CompoundCalciumChannelBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCalciumChannelBlocker001(IntegratedVariable):
    """
    Participant calcium channel blocker status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCalciumChannelBlocker001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCalciumChannelBlocker001"
    class_name: ClassVar[str] = "IntegratedCalciumChannelBlocker001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCalciumChannelBlocker001

    id: Union[str, IntegratedCalciumChannelBlocker001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCalciumChannelBlocker001Id):
            self.id = IntegratedCalciumChannelBlocker001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCentrallyActingAgents001(CompoundVariable):
    """
    A record of participant centrally acting agent usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCentrallyActingAgents001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCentrallyActingAgents001"
    class_name: ClassVar[str] = "CompoundCentrallyActingAgents001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCentrallyActingAgents001

    id: Union[str, CompoundCentrallyActingAgents001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCentrallyActingAgents001Id):
            self.id = CompoundCentrallyActingAgents001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCentrallyActingAgents001(IntegratedVariable):
    """
    Participant centrally acting agent status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCentrallyActingAgents001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCentrallyActingAgents001"
    class_name: ClassVar[str] = "IntegratedCentrallyActingAgents001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCentrallyActingAgents001

    id: Union[str, IntegratedCentrallyActingAgents001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCentrallyActingAgents001Id):
            self.id = IntegratedCentrallyActingAgents001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundDiuretics001(CompoundVariable):
    """
    A record of participant diuretic usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundDiuretics001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundDiuretics001"
    class_name: ClassVar[str] = "CompoundDiuretics001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundDiuretics001

    id: Union[str, CompoundDiuretics001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundDiuretics001Id):
            self.id = CompoundDiuretics001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedDiuretics001(IntegratedVariable):
    """
    Participant diuretic status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedDiuretics001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedDiuretics001"
    class_name: ClassVar[str] = "IntegratedDiuretics001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedDiuretics001

    id: Union[str, IntegratedDiuretics001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedDiuretics001Id):
            self.id = IntegratedDiuretics001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundInsulin001(CompoundVariable):
    """
    A record of participant insulin usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundInsulin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundInsulin001"
    class_name: ClassVar[str] = "CompoundInsulin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundInsulin001

    id: Union[str, CompoundInsulin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundInsulin001Id):
            self.id = CompoundInsulin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedInsulin001(IntegratedVariable):
    """
    Participant insulin status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedInsulin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedInsulin001"
    class_name: ClassVar[str] = "IntegratedInsulin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedInsulin001

    id: Union[str, IntegratedInsulin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedInsulin001Id):
            self.id = IntegratedInsulin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundNiacinMedication001(CompoundVariable):
    """
    A record of participant niacin medication usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundNiacinMedication001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundNiacinMedication001"
    class_name: ClassVar[str] = "CompoundNiacinMedication001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundNiacinMedication001

    id: Union[str, CompoundNiacinMedication001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundNiacinMedication001Id):
            self.id = CompoundNiacinMedication001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedNiacinMedication001(IntegratedVariable):
    """
    Participant niacin medication status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedNiacinMedication001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedNiacinMedication001"
    class_name: ClassVar[str] = "IntegratedNiacinMedication001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedNiacinMedication001

    id: Union[str, IntegratedNiacinMedication001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedNiacinMedication001Id):
            self.id = IntegratedNiacinMedication001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundLipidLoweringMedication001(CompoundVariable):
    """
    A record of participant lipid-lowering medication usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundLipidLoweringMedication001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundLipidLoweringMedication001"
    class_name: ClassVar[str] = "CompoundLipidLoweringMedication001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundLipidLoweringMedication001

    id: Union[str, CompoundLipidLoweringMedication001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundLipidLoweringMedication001Id):
            self.id = CompoundLipidLoweringMedication001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedLipidLoweringMedication001(IntegratedVariable):
    """
    Participant lipid-lowering medication status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedLipidLoweringMedication001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedLipidLoweringMedication001"
    class_name: ClassVar[str] = "IntegratedLipidLoweringMedication001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedLipidLoweringMedication001

    id: Union[str, IntegratedLipidLoweringMedication001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedLipidLoweringMedication001Id):
            self.id = IntegratedLipidLoweringMedication001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundFibrates001(CompoundVariable):
    """
    A record of participant fibrate usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundFibrates001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundFibrates001"
    class_name: ClassVar[str] = "CompoundFibrates001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundFibrates001

    id: Union[str, CompoundFibrates001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundFibrates001Id):
            self.id = CompoundFibrates001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedFibrates001(IntegratedVariable):
    """
    Participant fibrate status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedFibrates001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedFibrates001"
    class_name: ClassVar[str] = "IntegratedFibrates001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedFibrates001

    id: Union[str, IntegratedFibrates001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedFibrates001Id):
            self.id = IntegratedFibrates001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBileAcidSequestrant001(CompoundVariable):
    """
    A record of participant bile acid sequestrant usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBileAcidSequestrant001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBileAcidSequestrant001"
    class_name: ClassVar[str] = "CompoundBileAcidSequestrant001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBileAcidSequestrant001

    id: Union[str, CompoundBileAcidSequestrant001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBileAcidSequestrant001Id):
            self.id = CompoundBileAcidSequestrant001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBileAcidSequestrant001(IntegratedVariable):
    """
    Participant bile acid sequestrant status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBileAcidSequestrant001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBileAcidSequestrant001"
    class_name: ClassVar[str] = "IntegratedBileAcidSequestrant001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBileAcidSequestrant001

    id: Union[str, IntegratedBileAcidSequestrant001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBileAcidSequestrant001Id):
            self.id = IntegratedBileAcidSequestrant001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundOralHypoglycemicAgent001(CompoundVariable):
    """
    A record of participant oral hypoglycemic agent usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundOralHypoglycemicAgent001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundOralHypoglycemicAgent001"
    class_name: ClassVar[str] = "CompoundOralHypoglycemicAgent001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundOralHypoglycemicAgent001

    id: Union[str, CompoundOralHypoglycemicAgent001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundOralHypoglycemicAgent001Id):
            self.id = CompoundOralHypoglycemicAgent001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedOralHypoglycemicAgent001(IntegratedVariable):
    """
    Participant oral hypoglycemic agent status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedOralHypoglycemicAgent001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedOralHypoglycemicAgent001"
    class_name: ClassVar[str] = "IntegratedOralHypoglycemicAgent001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedOralHypoglycemicAgent001

    id: Union[str, IntegratedOralHypoglycemicAgent001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedOralHypoglycemicAgent001Id):
            self.id = IntegratedOralHypoglycemicAgent001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundStatin001(CompoundVariable):
    """
    A record of participant statin usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundStatin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundStatin001"
    class_name: ClassVar[str] = "CompoundStatin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundStatin001

    id: Union[str, CompoundStatin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundStatin001Id):
            self.id = CompoundStatin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedStatin001(IntegratedVariable):
    """
    Participant statin status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedStatin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedStatin001"
    class_name: ClassVar[str] = "IntegratedStatin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedStatin001

    id: Union[str, IntegratedStatin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedStatin001Id):
            self.id = IntegratedStatin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundSystemicSteroid001(CompoundVariable):
    """
    A record of participant systemic steroid usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundSystemicSteroid001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundSystemicSteroid001"
    class_name: ClassVar[str] = "CompoundSystemicSteroid001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundSystemicSteroid001

    id: Union[str, CompoundSystemicSteroid001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundSystemicSteroid001Id):
            self.id = CompoundSystemicSteroid001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedSystemicSteroid001(IntegratedVariable):
    """
    Participant systemic steroid status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedSystemicSteroid001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedSystemicSteroid001"
    class_name: ClassVar[str] = "IntegratedSystemicSteroid001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedSystemicSteroid001

    id: Union[str, IntegratedSystemicSteroid001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedSystemicSteroid001Id):
            self.id = IntegratedSystemicSteroid001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundVasodilator001(CompoundVariable):
    """
    A record of participant vasodilator usage status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundVasodilator001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundVasodilator001"
    class_name: ClassVar[str] = "CompoundVasodilator001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundVasodilator001

    id: Union[str, CompoundVasodilator001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundVasodilator001Id):
            self.id = CompoundVasodilator001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedVasodilator001(IntegratedVariable):
    """
    Participant vasodilator status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedVasodilator001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedVasodilator001"
    class_name: ClassVar[str] = "IntegratedVasodilator001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedVasodilator001

    id: Union[str, IntegratedVasodilator001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedVasodilator001Id):
            self.id = IntegratedVasodilator001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCoronaryAngioplasty001(CompoundVariable):
    """
    A record of participant coronary angioplasty procedure status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCoronaryAngioplasty001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCoronaryAngioplasty001"
    class_name: ClassVar[str] = "CompoundCoronaryAngioplasty001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCoronaryAngioplasty001

    id: Union[str, CompoundCoronaryAngioplasty001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCoronaryAngioplasty001Id):
            self.id = CompoundCoronaryAngioplasty001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCoronaryAngioplasty001(IntegratedVariable):
    """
    Participant coronary angioplasty status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCoronaryAngioplasty001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCoronaryAngioplasty001"
    class_name: ClassVar[str] = "IntegratedCoronaryAngioplasty001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCoronaryAngioplasty001

    id: Union[str, IntegratedCoronaryAngioplasty001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCoronaryAngioplasty001Id):
            self.id = IntegratedCoronaryAngioplasty001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCoronaryBypass001(CompoundVariable):
    """
    A record of participant coronary artery bypass graft procedure status
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCoronaryBypass001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCoronaryBypass001"
    class_name: ClassVar[str] = "CompoundCoronaryBypass001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCoronaryBypass001

    id: Union[str, CompoundCoronaryBypass001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCoronaryBypass001Id):
            self.id = CompoundCoronaryBypass001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCoronaryBypass001(IntegratedVariable):
    """
    Participant coronary artery bypass graft status containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCoronaryBypass001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCoronaryBypass001"
    class_name: ClassVar[str] = "IntegratedCoronaryBypass001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCoronaryBypass001

    id: Union[str, IntegratedCoronaryBypass001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCoronaryBypass001Id):
            self.id = IntegratedCoronaryBypass001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundApneaHypopneaIndex001(CompoundVariable):
    """
    Apnea-hypopnea index variable with metadata, measured in events/h using polysomnography or home sleep apnea testing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundApneaHypopneaIndex001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundApneaHypopneaIndex001"
    class_name: ClassVar[str] = "CompoundApneaHypopneaIndex001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundApneaHypopneaIndex001

    id: Union[str, CompoundApneaHypopneaIndex001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundApneaHypopneaIndex001Id):
            self.id = CompoundApneaHypopneaIndex001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedApneaHypopneaIndex001(IntegratedVariable):
    """
    Apnea-hypopnea index variable containing data from multiple studies, normalized to events/h
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedApneaHypopneaIndex001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedApneaHypopneaIndex001"
    class_name: ClassVar[str] = "IntegratedApneaHypopneaIndex001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedApneaHypopneaIndex001

    id: Union[str, IntegratedApneaHypopneaIndex001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedApneaHypopneaIndex001Id):
            self.id = IntegratedApneaHypopneaIndex001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAlbuminBlood001(CompoundVariable):
    """
    Albumin concentration in blood variable with metadata, measured in g/dL using BCG/BCP colorimetric assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAlbuminBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAlbuminBlood001"
    class_name: ClassVar[str] = "CompoundAlbuminBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAlbuminBlood001

    id: Union[str, CompoundAlbuminBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAlbuminBlood001Id):
            self.id = CompoundAlbuminBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAlbuminBlood001(IntegratedVariable):
    """
    Albumin concentration in blood variable containing data from multiple studies, normalized to g/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAlbuminBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAlbuminBlood001"
    class_name: ClassVar[str] = "IntegratedAlbuminBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAlbuminBlood001

    id: Union[str, IntegratedAlbuminBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAlbuminBlood001Id):
            self.id = IntegratedAlbuminBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAlcoholConsumption001(CompoundVariable):
    """
    Alcohol consumption variable with metadata, measured in servings per week using questionnaire, survey, or interview
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAlcoholConsumption001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAlcoholConsumption001"
    class_name: ClassVar[str] = "CompoundAlcoholConsumption001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAlcoholConsumption001

    id: Union[str, CompoundAlcoholConsumption001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAlcoholConsumption001Id):
            self.id = CompoundAlcoholConsumption001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAlcoholConsumption001(IntegratedVariable):
    """
    Alcohol consumption variable containing data from multiple studies, normalized to servings per week
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAlcoholConsumption001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAlcoholConsumption001"
    class_name: ClassVar[str] = "IntegratedAlcoholConsumption001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAlcoholConsumption001

    id: Union[str, IntegratedAlcoholConsumption001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAlcoholConsumption001Id):
            self.id = IntegratedAlcoholConsumption001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAltSgpt001(CompoundVariable):
    """
    ALT (alanine transaminase/SGPT) concentration in blood variable with metadata, measured in IU/L using an enzymatic
    kinetic assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAltSgpt001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAltSgpt001"
    class_name: ClassVar[str] = "CompoundAltSgpt001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAltSgpt001

    id: Union[str, CompoundAltSgpt001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAltSgpt001Id):
            self.id = CompoundAltSgpt001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAltSgpt001(IntegratedVariable):
    """
    ALT (SGPT) concentration in blood variable containing data from multiple studies, normalized to IU/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAltSgpt001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAltSgpt001"
    class_name: ClassVar[str] = "IntegratedAltSgpt001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAltSgpt001

    id: Union[str, IntegratedAltSgpt001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAltSgpt001Id):
            self.id = IntegratedAltSgpt001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundAstSgot001(CompoundVariable):
    """
    AST (aspartate aminotransferase/SGOT) concentration in blood variable with metadata, measured in IU/L using an
    enzymatic kinetic assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundAstSgot001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundAstSgot001"
    class_name: ClassVar[str] = "CompoundAstSgot001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundAstSgot001

    id: Union[str, CompoundAstSgot001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundAstSgot001Id):
            self.id = CompoundAstSgot001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedAstSgot001(IntegratedVariable):
    """
    AST (SGOT) concentration in blood variable containing data from multiple studies, normalized to IU/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedAstSgot001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedAstSgot001"
    class_name: ClassVar[str] = "IntegratedAstSgot001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedAstSgot001

    id: Union[str, IntegratedAstSgot001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedAstSgot001Id):
            self.id = IntegratedAstSgot001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBilirubinConjugated001(CompoundVariable):
    """
    Conjugated (direct) bilirubin concentration in blood variable with metadata, measured in mg/dL using the diazo
    colorimetric method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBilirubinConjugated001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBilirubinConjugated001"
    class_name: ClassVar[str] = "CompoundBilirubinConjugated001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBilirubinConjugated001

    id: Union[str, CompoundBilirubinConjugated001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBilirubinConjugated001Id):
            self.id = CompoundBilirubinConjugated001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBilirubinConjugated001(IntegratedVariable):
    """
    Conjugated bilirubin concentration in blood variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBilirubinConjugated001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBilirubinConjugated001"
    class_name: ClassVar[str] = "IntegratedBilirubinConjugated001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBilirubinConjugated001

    id: Union[str, IntegratedBilirubinConjugated001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBilirubinConjugated001Id):
            self.id = IntegratedBilirubinConjugated001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBilirubinTotal001(CompoundVariable):
    """
    Total bilirubin concentration in blood variable with metadata, measured in mg/dL using the diazo colorimetric
    method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBilirubinTotal001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBilirubinTotal001"
    class_name: ClassVar[str] = "CompoundBilirubinTotal001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBilirubinTotal001

    id: Union[str, CompoundBilirubinTotal001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBilirubinTotal001Id):
            self.id = CompoundBilirubinTotal001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBilirubinTotal001(IntegratedVariable):
    """
    Total bilirubin concentration in blood variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBilirubinTotal001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBilirubinTotal001"
    class_name: ClassVar[str] = "IntegratedBilirubinTotal001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBilirubinTotal001

    id: Union[str, IntegratedBilirubinTotal001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBilirubinTotal001Id):
            self.id = IntegratedBilirubinTotal001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBNP001(CompoundVariable):
    """
    BNP (B-type natriuretic peptide) concentration in blood variable with metadata, measured in pg/mL using
    chemiluminescence immunoassay or ELISA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBNP001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBNP001"
    class_name: ClassVar[str] = "CompoundBNP001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBNP001

    id: Union[str, CompoundBNP001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBNP001Id):
            self.id = CompoundBNP001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBNP001(IntegratedVariable):
    """
    BNP concentration in blood variable containing data from multiple studies, normalized to pg/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBNP001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBNP001"
    class_name: ClassVar[str] = "IntegratedBNP001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBNP001

    id: Union[str, IntegratedBNP001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBNP001Id):
            self.id = IntegratedBNP001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBloodPressure001(CompoundVariable):
    """
    Blood pressure variable with metadata, represented as a systolic/diastolic string calculated from blood pressure
    measurements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBloodPressure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBloodPressure001"
    class_name: ClassVar[str] = "CompoundBloodPressure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBloodPressure001

    id: Union[str, CompoundBloodPressure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBloodPressure001Id):
            self.id = CompoundBloodPressure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBloodPressure001(IntegratedVariable):
    """
    Blood pressure variable containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBloodPressure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBloodPressure001"
    class_name: ClassVar[str] = "IntegratedBloodPressure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBloodPressure001

    id: Union[str, IntegratedBloodPressure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBloodPressure001Id):
            self.id = IntegratedBloodPressure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBloodUreaNitrogen001(CompoundVariable):
    """
    Blood urea nitrogen (BUN) concentration variable with metadata, measured in mg/dL using the urease-GLDH method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBloodUreaNitrogen001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBloodUreaNitrogen001"
    class_name: ClassVar[str] = "CompoundBloodUreaNitrogen001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBloodUreaNitrogen001

    id: Union[str, CompoundBloodUreaNitrogen001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBloodUreaNitrogen001Id):
            self.id = CompoundBloodUreaNitrogen001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBloodUreaNitrogen001(IntegratedVariable):
    """
    Blood urea nitrogen concentration variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBloodUreaNitrogen001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBloodUreaNitrogen001"
    class_name: ClassVar[str] = "IntegratedBloodUreaNitrogen001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBloodUreaNitrogen001

    id: Union[str, IntegratedBloodUreaNitrogen001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBloodUreaNitrogen001Id):
            self.id = IntegratedBloodUreaNitrogen001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBodyTemperature001(CompoundVariable):
    """
    Body temperature variable with metadata, measured in degrees Celsius using thermometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBodyTemperature001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBodyTemperature001"
    class_name: ClassVar[str] = "CompoundBodyTemperature001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBodyTemperature001

    id: Union[str, CompoundBodyTemperature001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBodyTemperature001Id):
            self.id = CompoundBodyTemperature001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBodyTemperature001(IntegratedVariable):
    """
    Body temperature variable containing data from multiple studies, normalized to degrees Celsius
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBodyTemperature001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBodyTemperature001"
    class_name: ClassVar[str] = "IntegratedBodyTemperature001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBodyTemperature001

    id: Union[str, IntegratedBodyTemperature001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBodyTemperature001Id):
            self.id = IntegratedBodyTemperature001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundBUNCreatinineRatio001(CompoundVariable):
    """
    BUN to creatinine ratio variable with metadata, calculated from blood urea nitrogen and creatinine measurements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundBUNCreatinineRatio001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundBUNCreatinineRatio001"
    class_name: ClassVar[str] = "CompoundBUNCreatinineRatio001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundBUNCreatinineRatio001

    id: Union[str, CompoundBUNCreatinineRatio001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundBUNCreatinineRatio001Id):
            self.id = CompoundBUNCreatinineRatio001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedBUNCreatinineRatio001(IntegratedVariable):
    """
    BUN to creatinine ratio variable containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedBUNCreatinineRatio001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedBUNCreatinineRatio001"
    class_name: ClassVar[str] = "IntegratedBUNCreatinineRatio001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedBUNCreatinineRatio001

    id: Union[str, IntegratedBUNCreatinineRatio001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedBUNCreatinineRatio001Id):
            self.id = IntegratedBUNCreatinineRatio001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCarotidIntimamediaThickness001(CompoundVariable):
    """
    Carotid intima-media thickness variable with metadata, measured in mm using carotid ultrasound
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCarotidIntimamediaThickness001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCarotidIntimamediaThickness001"
    class_name: ClassVar[str] = "CompoundCarotidIntimamediaThickness001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCarotidIntimamediaThickness001

    id: Union[str, CompoundCarotidIntimamediaThickness001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCarotidIntimamediaThickness001Id):
            self.id = CompoundCarotidIntimamediaThickness001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCarotidIntimamediaThickness001(IntegratedVariable):
    """
    Carotid intima-media thickness variable containing data from multiple studies, normalized to mm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCarotidIntimamediaThickness001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCarotidIntimamediaThickness001"
    class_name: ClassVar[str] = "IntegratedCarotidIntimamediaThickness001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCarotidIntimamediaThickness001

    id: Union[str, IntegratedCarotidIntimamediaThickness001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCarotidIntimamediaThickness001Id):
            self.id = IntegratedCarotidIntimamediaThickness001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCarotidStenosisLeft001(CompoundVariable):
    """
    Left carotid artery stenosis variable with metadata, measured as percent stenosis using duplex ultrasound or CT
    angiography
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCarotidStenosisLeft001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCarotidStenosisLeft001"
    class_name: ClassVar[str] = "CompoundCarotidStenosisLeft001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCarotidStenosisLeft001

    id: Union[str, CompoundCarotidStenosisLeft001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCarotidStenosisLeft001Id):
            self.id = CompoundCarotidStenosisLeft001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCarotidStenosisLeft001(IntegratedVariable):
    """
    Left carotid artery stenosis variable containing data from multiple studies, normalized to percent stenosis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCarotidStenosisLeft001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCarotidStenosisLeft001"
    class_name: ClassVar[str] = "IntegratedCarotidStenosisLeft001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCarotidStenosisLeft001

    id: Union[str, IntegratedCarotidStenosisLeft001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCarotidStenosisLeft001Id):
            self.id = IntegratedCarotidStenosisLeft001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCarotidStenosisRight001(CompoundVariable):
    """
    Right carotid artery stenosis variable with metadata, measured as percent stenosis using duplex ultrasound or CT
    angiography
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCarotidStenosisRight001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCarotidStenosisRight001"
    class_name: ClassVar[str] = "CompoundCarotidStenosisRight001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCarotidStenosisRight001

    id: Union[str, CompoundCarotidStenosisRight001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCarotidStenosisRight001Id):
            self.id = CompoundCarotidStenosisRight001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCarotidStenosisRight001(IntegratedVariable):
    """
    Right carotid artery stenosis variable containing data from multiple studies, normalized to percent stenosis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCarotidStenosisRight001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCarotidStenosisRight001"
    class_name: ClassVar[str] = "IntegratedCarotidStenosisRight001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCarotidStenosisRight001

    id: Union[str, IntegratedCarotidStenosisRight001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCarotidStenosisRight001Id):
            self.id = IntegratedCarotidStenosisRight001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCESDScore001(CompoundVariable):
    """
    CES-D (Center for Epidemiological Studies Depression Scale) score variable with metadata, collected via
    questionnaire
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCESDScore001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCESDScore001"
    class_name: ClassVar[str] = "CompoundCESDScore001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCESDScore001

    id: Union[str, CompoundCESDScore001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCESDScore001Id):
            self.id = CompoundCESDScore001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCESDScore001(IntegratedVariable):
    """
    CES-D depression scale score variable containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCESDScore001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCESDScore001"
    class_name: ClassVar[str] = "IntegratedCESDScore001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCESDScore001

    id: Union[str, IntegratedCESDScore001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCESDScore001Id):
            self.id = IntegratedCESDScore001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundChlorideBlood001(CompoundVariable):
    """
    Chloride concentration in blood variable with metadata, measured in mmol/L using an ion selective electrode
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundChlorideBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundChlorideBlood001"
    class_name: ClassVar[str] = "CompoundChlorideBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundChlorideBlood001

    id: Union[str, CompoundChlorideBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundChlorideBlood001Id):
            self.id = CompoundChlorideBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundChlorideBlood002(CompoundVariable):
    """
    Chloride concentration in blood variable with metadata, measured in mmol/dL using an ion selective electrode
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundChlorideBlood002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundChlorideBlood002"
    class_name: ClassVar[str] = "CompoundChlorideBlood002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundChlorideBlood002

    id: Union[str, CompoundChlorideBlood002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundChlorideBlood002Id):
            self.id = CompoundChlorideBlood002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedChlorideBlood001(IntegratedVariable):
    """
    Chloride concentration in blood variable containing data from multiple studies, normalized to mmol/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedChlorideBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedChlorideBlood001"
    class_name: ClassVar[str] = "IntegratedChlorideBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedChlorideBlood001

    id: Union[str, IntegratedChlorideBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedChlorideBlood001Id):
            self.id = IntegratedChlorideBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCoronaryArteryCalciumScore001(CompoundVariable):
    """
    Coronary artery calcium Agatston score variable with metadata, derived from non-contrast cardiac CT using Agatston
    scoring
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCoronaryArteryCalciumScore001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCoronaryArteryCalciumScore001"
    class_name: ClassVar[str] = "CompoundCoronaryArteryCalciumScore001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCoronaryArteryCalciumScore001

    id: Union[str, CompoundCoronaryArteryCalciumScore001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCoronaryArteryCalciumScore001Id):
            self.id = CompoundCoronaryArteryCalciumScore001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCoronaryArteryCalciumScore001(IntegratedVariable):
    """
    Coronary artery calcium Agatston score variable containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCoronaryArteryCalciumScore001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCoronaryArteryCalciumScore001"
    class_name: ClassVar[str] = "IntegratedCoronaryArteryCalciumScore001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCoronaryArteryCalciumScore001

    id: Union[str, IntegratedCoronaryArteryCalciumScore001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCoronaryArteryCalciumScore001Id):
            self.id = IntegratedCoronaryArteryCalciumScore001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCoronaryArteryCalciumVolume001(CompoundVariable):
    """
    Coronary artery calcium volume variable with metadata, measured in mm3 by CT using volume scoring
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCoronaryArteryCalciumVolume001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCoronaryArteryCalciumVolume001"
    class_name: ClassVar[str] = "CompoundCoronaryArteryCalciumVolume001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCoronaryArteryCalciumVolume001

    id: Union[str, CompoundCoronaryArteryCalciumVolume001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCoronaryArteryCalciumVolume001Id):
            self.id = CompoundCoronaryArteryCalciumVolume001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCoronaryArteryCalciumVolume001(IntegratedVariable):
    """
    Coronary artery calcium volume variable containing data from multiple studies, normalized to mm3
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCoronaryArteryCalciumVolume001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCoronaryArteryCalciumVolume001"
    class_name: ClassVar[str] = "IntegratedCoronaryArteryCalciumVolume001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCoronaryArteryCalciumVolume001

    id: Union[str, IntegratedCoronaryArteryCalciumVolume001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCoronaryArteryCalciumVolume001Id):
            self.id = IntegratedCoronaryArteryCalciumVolume001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCReactiveProtein001(CompoundVariable):
    """
    C-reactive protein (CRP) concentration in blood variable with metadata, measured in mg/L using immunoturbidometry
    or immunonephelometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCReactiveProtein001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCReactiveProtein001"
    class_name: ClassVar[str] = "CompoundCReactiveProtein001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCReactiveProtein001

    id: Union[str, CompoundCReactiveProtein001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCReactiveProtein001Id):
            self.id = CompoundCReactiveProtein001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCReactiveProtein002(CompoundVariable):
    """
    C-reactive protein (CRP) concentration in blood variable with metadata, measured in mg/dL using immunoturbidometry
    or immunonephelometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCReactiveProtein002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCReactiveProtein002"
    class_name: ClassVar[str] = "CompoundCReactiveProtein002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCReactiveProtein002

    id: Union[str, CompoundCReactiveProtein002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCReactiveProtein002Id):
            self.id = CompoundCReactiveProtein002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCReactiveProtein003(CompoundVariable):
    """
    C-reactive protein (CRP) concentration in blood variable with metadata, measured in ug/mL using immunoturbidometry
    or immunonephelometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCReactiveProtein003"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCReactiveProtein003"
    class_name: ClassVar[str] = "CompoundCReactiveProtein003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCReactiveProtein003

    id: Union[str, CompoundCReactiveProtein003Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCReactiveProtein003Id):
            self.id = CompoundCReactiveProtein003Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCReactiveProtein001(IntegratedVariable):
    """
    C-reactive protein concentration in blood variable containing data from multiple studies, normalized to mg/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCReactiveProtein001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCReactiveProtein001"
    class_name: ClassVar[str] = "IntegratedCReactiveProtein001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCReactiveProtein001

    id: Union[str, IntegratedCReactiveProtein001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCReactiveProtein001Id):
            self.id = IntegratedCReactiveProtein001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCreatinineBlood001(CompoundVariable):
    """
    Creatinine concentration in blood variable with metadata, measured in mg/dL using the Jaffe reaction or enzymatic
    creatinine assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCreatinineBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCreatinineBlood001"
    class_name: ClassVar[str] = "CompoundCreatinineBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCreatinineBlood001

    id: Union[str, CompoundCreatinineBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCreatinineBlood001Id):
            self.id = CompoundCreatinineBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCreatinineBlood001(IntegratedVariable):
    """
    Creatinine concentration in blood variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCreatinineBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCreatinineBlood001"
    class_name: ClassVar[str] = "IntegratedCreatinineBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCreatinineBlood001

    id: Union[str, IntegratedCreatinineBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCreatinineBlood001Id):
            self.id = IntegratedCreatinineBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundCystatinCBlood001(CompoundVariable):
    """
    Cystatin C concentration in blood variable with metadata, measured in mg/L using immunoturbidometry or
    immunonephelometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundCystatinCBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundCystatinCBlood001"
    class_name: ClassVar[str] = "CompoundCystatinCBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundCystatinCBlood001

    id: Union[str, CompoundCystatinCBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundCystatinCBlood001Id):
            self.id = CompoundCystatinCBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedCystatinCBlood001(IntegratedVariable):
    """
    Cystatin C concentration in blood variable containing data from multiple studies, normalized to mg/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedCystatinCBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedCystatinCBlood001"
    class_name: ClassVar[str] = "IntegratedCystatinCBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedCystatinCBlood001

    id: Union[str, IntegratedCystatinCBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedCystatinCBlood001Id):
            self.id = IntegratedCystatinCBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundDDimer001(CompoundVariable):
    """
    D-dimer concentration in blood variable with metadata, measured in ug/mL fibrinogen-equivalent units (FEU)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundDDimer001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundDDimer001"
    class_name: ClassVar[str] = "CompoundDDimer001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundDDimer001

    id: Union[str, CompoundDDimer001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundDDimer001Id):
            self.id = CompoundDDimer001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundDDimer002(CompoundVariable):
    """
    D-dimer concentration in blood variable with metadata, measured in ng/mL fibrinogen-equivalent units (FEU)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundDDimer002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundDDimer002"
    class_name: ClassVar[str] = "CompoundDDimer002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundDDimer002

    id: Union[str, CompoundDDimer002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundDDimer002Id):
            self.id = CompoundDDimer002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedDDimer001(IntegratedVariable):
    """
    D-dimer concentration in blood variable containing data from multiple studies, normalized to ug/mL (FEU)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedDDimer001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedDDimer001"
    class_name: ClassVar[str] = "IntegratedDDimer001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedDDimer001

    id: Union[str, IntegratedDDimer001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedDDimer001Id):
            self.id = IntegratedDDimer001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundDiastolicBloodPressure001(CompoundVariable):
    """
    Diastolic blood pressure variable with metadata, measured in mmHg using auscultatory or oscillometric method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundDiastolicBloodPressure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundDiastolicBloodPressure001"
    class_name: ClassVar[str] = "CompoundDiastolicBloodPressure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundDiastolicBloodPressure001

    id: Union[str, CompoundDiastolicBloodPressure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundDiastolicBloodPressure001Id):
            self.id = CompoundDiastolicBloodPressure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedDiastolicBloodPressure001(IntegratedVariable):
    """
    Diastolic blood pressure variable containing data from multiple studies, normalized to mmHg
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedDiastolicBloodPressure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedDiastolicBloodPressure001"
    class_name: ClassVar[str] = "IntegratedDiastolicBloodPressure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedDiastolicBloodPressure001

    id: Union[str, IntegratedDiastolicBloodPressure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedDiastolicBloodPressure001Id):
            self.id = IntegratedDiastolicBloodPressure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundEosinophilCount001(CompoundVariable):
    """
    Eosinophil count variable with metadata, measured in 10*3/uL using a complete blood count or manual differential
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundEosinophilCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundEosinophilCount001"
    class_name: ClassVar[str] = "CompoundEosinophilCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundEosinophilCount001

    id: Union[str, CompoundEosinophilCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundEosinophilCount001Id):
            self.id = CompoundEosinophilCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedEosinophilCount001(IntegratedVariable):
    """
    Eosinophil count variable containing data from multiple studies, normalized to 10*3/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedEosinophilCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedEosinophilCount001"
    class_name: ClassVar[str] = "IntegratedEosinophilCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedEosinophilCount001

    id: Union[str, IntegratedEosinophilCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedEosinophilCount001Id):
            self.id = IntegratedEosinophilCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundESelectinBlood001(CompoundVariable):
    """
    E-selectin concentration in blood variable with metadata, measured in ng/mL using ELISA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundESelectinBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundESelectinBlood001"
    class_name: ClassVar[str] = "CompoundESelectinBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundESelectinBlood001

    id: Union[str, CompoundESelectinBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundESelectinBlood001Id):
            self.id = CompoundESelectinBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedESelectinBlood001(IntegratedVariable):
    """
    E-selectin concentration in blood variable containing data from multiple studies, normalized to ng/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedESelectinBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedESelectinBlood001"
    class_name: ClassVar[str] = "IntegratedESelectinBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedESelectinBlood001

    id: Union[str, IntegratedESelectinBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedESelectinBlood001Id):
            self.id = IntegratedESelectinBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundEstimatedGFR001(CompoundVariable):
    """
    Estimated glomerular filtration rate (eGFR) variable with metadata, calculated from serum creatinine and other
    factors, measured in mL/min/1.73m2
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundEstimatedGFR001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundEstimatedGFR001"
    class_name: ClassVar[str] = "CompoundEstimatedGFR001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundEstimatedGFR001

    id: Union[str, CompoundEstimatedGFR001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundEstimatedGFR001Id):
            self.id = CompoundEstimatedGFR001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedEstimatedGFR001(IntegratedVariable):
    """
    Estimated glomerular filtration rate variable containing data from multiple studies, normalized to mL/min/1.73m2
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedEstimatedGFR001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedEstimatedGFR001"
    class_name: ClassVar[str] = "IntegratedEstimatedGFR001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedEstimatedGFR001

    id: Union[str, IntegratedEstimatedGFR001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedEstimatedGFR001Id):
            self.id = IntegratedEstimatedGFR001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundFactorVII001(CompoundVariable):
    """
    Factor VII (proconvertin) activity variable with metadata, measured as percent of normal using one-stage clotting
    assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundFactorVII001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundFactorVII001"
    class_name: ClassVar[str] = "CompoundFactorVII001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundFactorVII001

    id: Union[str, CompoundFactorVII001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundFactorVII001Id):
            self.id = CompoundFactorVII001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedFactorVII001(IntegratedVariable):
    """
    Factor VII activity variable containing data from multiple studies, normalized to percent of normal
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedFactorVII001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedFactorVII001"
    class_name: ClassVar[str] = "IntegratedFactorVII001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedFactorVII001

    id: Union[str, IntegratedFactorVII001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedFactorVII001Id):
            self.id = IntegratedFactorVII001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundFactorVIII001(CompoundVariable):
    """
    Factor VIII activity variable with metadata, measured in IU/mL using one-stage clotting or chromogenic assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundFactorVIII001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundFactorVIII001"
    class_name: ClassVar[str] = "CompoundFactorVIII001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundFactorVIII001

    id: Union[str, CompoundFactorVIII001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundFactorVIII001Id):
            self.id = CompoundFactorVIII001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedFactorVIII001(IntegratedVariable):
    """
    Factor VIII activity variable containing data from multiple studies, normalized to IU/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedFactorVIII001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedFactorVIII001"
    class_name: ClassVar[str] = "IntegratedFactorVIII001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedFactorVIII001

    id: Union[str, IntegratedFactorVIII001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedFactorVIII001Id):
            self.id = IntegratedFactorVIII001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundFastingGlucose001(CompoundVariable):
    """
    Fasting glucose concentration in blood variable with metadata, measured in mg/dL using hexokinase or glucose
    oxidase method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundFastingGlucose001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundFastingGlucose001"
    class_name: ClassVar[str] = "CompoundFastingGlucose001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundFastingGlucose001

    id: Union[str, CompoundFastingGlucose001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundFastingGlucose001Id):
            self.id = CompoundFastingGlucose001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundFastingGlucose002(CompoundVariable):
    """
    Fasting glucose concentration in blood variable with metadata, measured in mmol/L using hexokinase or glucose
    oxidase method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundFastingGlucose002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundFastingGlucose002"
    class_name: ClassVar[str] = "CompoundFastingGlucose002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundFastingGlucose002

    id: Union[str, CompoundFastingGlucose002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundFastingGlucose002Id):
            self.id = CompoundFastingGlucose002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedFastingGlucose001(IntegratedVariable):
    """
    Fasting glucose concentration in blood variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedFastingGlucose001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedFastingGlucose001"
    class_name: ClassVar[str] = "IntegratedFastingGlucose001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedFastingGlucose001

    id: Union[str, IntegratedFastingGlucose001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedFastingGlucose001Id):
            self.id = IntegratedFastingGlucose001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundFerritin001(CompoundVariable):
    """
    Ferritin concentration in blood variable with metadata, measured in ng/mL using chemiluminescence immunoassay or
    ELISA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundFerritin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundFerritin001"
    class_name: ClassVar[str] = "CompoundFerritin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundFerritin001

    id: Union[str, CompoundFerritin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundFerritin001Id):
            self.id = CompoundFerritin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedFerritin001(IntegratedVariable):
    """
    Ferritin concentration in blood variable containing data from multiple studies, normalized to ng/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedFerritin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedFerritin001"
    class_name: ClassVar[str] = "IntegratedFerritin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedFerritin001

    id: Union[str, IntegratedFerritin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedFerritin001Id):
            self.id = IntegratedFerritin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundFibrinogen001(CompoundVariable):
    """
    Fibrinogen concentration in plasma variable with metadata, measured in mg/dL using the Clauss assay or
    immunoturbidometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundFibrinogen001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundFibrinogen001"
    class_name: ClassVar[str] = "CompoundFibrinogen001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundFibrinogen001

    id: Union[str, CompoundFibrinogen001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundFibrinogen001Id):
            self.id = CompoundFibrinogen001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedFibrinogen001(IntegratedVariable):
    """
    Fibrinogen concentration in plasma variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedFibrinogen001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedFibrinogen001"
    class_name: ClassVar[str] = "IntegratedFibrinogen001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedFibrinogen001

    id: Union[str, IntegratedFibrinogen001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedFibrinogen001Id):
            self.id = IntegratedFibrinogen001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundFruitConsumption001(CompoundVariable):
    """
    Fruit consumption variable with metadata, measured in servings per week using questionnaire, survey, or interview
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundFruitConsumption001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundFruitConsumption001"
    class_name: ClassVar[str] = "CompoundFruitConsumption001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundFruitConsumption001

    id: Union[str, CompoundFruitConsumption001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundFruitConsumption001Id):
            self.id = CompoundFruitConsumption001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedFruitConsumption001(IntegratedVariable):
    """
    Fruit consumption variable containing data from multiple studies, normalized to servings per week
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedFruitConsumption001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedFruitConsumption001"
    class_name: ClassVar[str] = "IntegratedFruitConsumption001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedFruitConsumption001

    id: Union[str, IntegratedFruitConsumption001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedFruitConsumption001Id):
            self.id = IntegratedFruitConsumption001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundGFR001(CompoundVariable):
    """
    Glomerular filtration rate (GFR) variable with metadata, measured in mL/min/1.73m2 using a clearance test
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundGFR001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundGFR001"
    class_name: ClassVar[str] = "CompoundGFR001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundGFR001

    id: Union[str, CompoundGFR001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundGFR001Id):
            self.id = CompoundGFR001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedGFR001(IntegratedVariable):
    """
    Glomerular filtration rate variable containing data from multiple studies, normalized to mL/min/1.73m2
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedGFR001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedGFR001"
    class_name: ClassVar[str] = "IntegratedGFR001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedGFR001

    id: Union[str, IntegratedGFR001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedGFR001Id):
            self.id = IntegratedGFR001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundGlucoseBlood001(CompoundVariable):
    """
    Blood glucose concentration variable with metadata, measured in mg/dL using hexokinase or glucose oxidase method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundGlucoseBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundGlucoseBlood001"
    class_name: ClassVar[str] = "CompoundGlucoseBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundGlucoseBlood001

    id: Union[str, CompoundGlucoseBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundGlucoseBlood001Id):
            self.id = CompoundGlucoseBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedGlucoseBlood001(IntegratedVariable):
    """
    Blood glucose concentration variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedGlucoseBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedGlucoseBlood001"
    class_name: ClassVar[str] = "IntegratedGlucoseBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedGlucoseBlood001

    id: Union[str, IntegratedGlucoseBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedGlucoseBlood001Id):
            self.id = IntegratedGlucoseBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHDL001(CompoundVariable):
    """
    HDL cholesterol concentration in blood variable with metadata, measured in mg/dL using direct homogeneous
    enzymatic or precipitation method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHDL001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHDL001"
    class_name: ClassVar[str] = "CompoundHDL001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHDL001

    id: Union[str, CompoundHDL001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHDL001Id):
            self.id = CompoundHDL001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHDL002(CompoundVariable):
    """
    HDL cholesterol concentration in blood variable with metadata, measured in mmol/L using direct homogeneous
    enzymatic or precipitation method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHDL002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHDL002"
    class_name: ClassVar[str] = "CompoundHDL002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHDL002

    id: Union[str, CompoundHDL002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHDL002Id):
            self.id = CompoundHDL002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHDL001(IntegratedVariable):
    """
    HDL cholesterol concentration in blood variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHDL001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHDL001"
    class_name: ClassVar[str] = "IntegratedHDL001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHDL001

    id: Union[str, IntegratedHDL001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHDL001Id):
            self.id = IntegratedHDL001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHeartRate001(CompoundVariable):
    """
    Heart rate variable with metadata, measured in beats per minute using electrocardiography, pulse oximetry, or
    manual pulse palpation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHeartRate001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHeartRate001"
    class_name: ClassVar[str] = "CompoundHeartRate001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHeartRate001

    id: Union[str, CompoundHeartRate001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHeartRate001Id):
            self.id = CompoundHeartRate001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHeartRate001(IntegratedVariable):
    """
    Heart rate variable containing data from multiple studies, normalized to beats per minute
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHeartRate001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHeartRate001"
    class_name: ClassVar[str] = "IntegratedHeartRate001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHeartRate001

    id: Union[str, IntegratedHeartRate001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHeartRate001Id):
            self.id = IntegratedHeartRate001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHematocrit001(CompoundVariable):
    """
    Hematocrit variable with metadata, measured as percent using complete blood count or microhematocrit centrifugation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHematocrit001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHematocrit001"
    class_name: ClassVar[str] = "CompoundHematocrit001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHematocrit001

    id: Union[str, CompoundHematocrit001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHematocrit001Id):
            self.id = CompoundHematocrit001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHematocrit001(IntegratedVariable):
    """
    Hematocrit variable containing data from multiple studies, normalized to percent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHematocrit001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHematocrit001"
    class_name: ClassVar[str] = "IntegratedHematocrit001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHematocrit001

    id: Union[str, IntegratedHematocrit001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHematocrit001Id):
            self.id = IntegratedHematocrit001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHemoglobin001(CompoundVariable):
    """
    Hemoglobin concentration in blood variable with metadata, measured in g/dL using cyanmethemoglobin or complete
    blood count method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHemoglobin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHemoglobin001"
    class_name: ClassVar[str] = "CompoundHemoglobin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHemoglobin001

    id: Union[str, CompoundHemoglobin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHemoglobin001Id):
            self.id = CompoundHemoglobin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHemoglobin001(IntegratedVariable):
    """
    Hemoglobin concentration in blood variable containing data from multiple studies, normalized to g/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHemoglobin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHemoglobin001"
    class_name: ClassVar[str] = "IntegratedHemoglobin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHemoglobin001

    id: Union[str, IntegratedHemoglobin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHemoglobin001Id):
            self.id = IntegratedHemoglobin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHipCircumference001(CompoundVariable):
    """
    Hip circumference variable with metadata, measured in cm using a flexible measuring tape
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHipCircumference001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHipCircumference001"
    class_name: ClassVar[str] = "CompoundHipCircumference001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHipCircumference001

    id: Union[str, CompoundHipCircumference001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHipCircumference001Id):
            self.id = CompoundHipCircumference001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundHipCircumference002(CompoundVariable):
    """
    Hip circumference variable with metadata, measured in inches using a flexible measuring tape
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundHipCircumference002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundHipCircumference002"
    class_name: ClassVar[str] = "CompoundHipCircumference002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundHipCircumference002

    id: Union[str, CompoundHipCircumference002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundHipCircumference002Id):
            self.id = CompoundHipCircumference002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedHipCircumference001(IntegratedVariable):
    """
    Hip circumference variable containing data from multiple studies, normalized to cm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedHipCircumference001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedHipCircumference001"
    class_name: ClassVar[str] = "IntegratedHipCircumference001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedHipCircumference001

    id: Union[str, IntegratedHipCircumference001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedHipCircumference001Id):
            self.id = IntegratedHipCircumference001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundInsulinBlood001(CompoundVariable):
    """
    Insulin concentration in blood variable with metadata, measured in pmol/L using chemiluminescence immunoassay or
    ELISA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundInsulinBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundInsulinBlood001"
    class_name: ClassVar[str] = "CompoundInsulinBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundInsulinBlood001

    id: Union[str, CompoundInsulinBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundInsulinBlood001Id):
            self.id = CompoundInsulinBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundInsulinBlood002(CompoundVariable):
    """
    Insulin concentration in blood variable with metadata, measured in uIU/mL using chemiluminescence immunoassay or
    ELISA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundInsulinBlood002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundInsulinBlood002"
    class_name: ClassVar[str] = "CompoundInsulinBlood002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundInsulinBlood002

    id: Union[str, CompoundInsulinBlood002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundInsulinBlood002Id):
            self.id = CompoundInsulinBlood002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedInsulinBlood001(IntegratedVariable):
    """
    Insulin concentration in blood variable containing data from multiple studies, normalized to pmol/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedInsulinBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedInsulinBlood001"
    class_name: ClassVar[str] = "IntegratedInsulinBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedInsulinBlood001

    id: Union[str, IntegratedInsulinBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedInsulinBlood001Id):
            self.id = IntegratedInsulinBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundLactateBlood001(CompoundVariable):
    """
    Lactate concentration in blood variable with metadata, measured in mmol/L using an enzymatic kinetic assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundLactateBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundLactateBlood001"
    class_name: ClassVar[str] = "CompoundLactateBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundLactateBlood001

    id: Union[str, CompoundLactateBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundLactateBlood001Id):
            self.id = CompoundLactateBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedLactateBlood001(IntegratedVariable):
    """
    Lactate concentration in blood variable containing data from multiple studies, normalized to mmol/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedLactateBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedLactateBlood001"
    class_name: ClassVar[str] = "IntegratedLactateBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedLactateBlood001

    id: Union[str, IntegratedLactateBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedLactateBlood001Id):
            self.id = IntegratedLactateBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundLactateDehydrogenase001(CompoundVariable):
    """
    Lactate dehydrogenase (LDH) activity in blood variable with metadata, measured in IU/L using an enzymatic kinetic
    assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundLactateDehydrogenase001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundLactateDehydrogenase001"
    class_name: ClassVar[str] = "CompoundLactateDehydrogenase001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundLactateDehydrogenase001

    id: Union[str, CompoundLactateDehydrogenase001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundLactateDehydrogenase001Id):
            self.id = CompoundLactateDehydrogenase001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedLactateDehydrogenase001(IntegratedVariable):
    """
    Lactate dehydrogenase activity in blood variable containing data from multiple studies, normalized to IU/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedLactateDehydrogenase001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedLactateDehydrogenase001"
    class_name: ClassVar[str] = "IntegratedLactateDehydrogenase001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedLactateDehydrogenase001

    id: Union[str, IntegratedLactateDehydrogenase001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedLactateDehydrogenase001Id):
            self.id = IntegratedLactateDehydrogenase001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundLDL001(CompoundVariable):
    """
    LDL cholesterol concentration in blood variable with metadata, measured in mg/dL derived from the Friedewald
    calculation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundLDL001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundLDL001"
    class_name: ClassVar[str] = "CompoundLDL001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundLDL001

    id: Union[str, CompoundLDL001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundLDL001Id):
            self.id = CompoundLDL001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedLDL001(IntegratedVariable):
    """
    LDL cholesterol concentration in blood variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedLDL001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedLDL001"
    class_name: ClassVar[str] = "IntegratedLDL001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedLDL001

    id: Union[str, IntegratedLDL001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedLDL001Id):
            self.id = IntegratedLDL001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundLymphocyteCount001(CompoundVariable):
    """
    Lymphocyte count variable with metadata, measured in 10*3/uL using a complete blood count or manual differential
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundLymphocyteCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundLymphocyteCount001"
    class_name: ClassVar[str] = "CompoundLymphocyteCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundLymphocyteCount001

    id: Union[str, CompoundLymphocyteCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundLymphocyteCount001Id):
            self.id = CompoundLymphocyteCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedLymphocyteCount001(IntegratedVariable):
    """
    Lymphocyte count variable containing data from multiple studies, normalized to 10*3/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedLymphocyteCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedLymphocyteCount001"
    class_name: ClassVar[str] = "IntegratedLymphocyteCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedLymphocyteCount001

    id: Union[str, IntegratedLymphocyteCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedLymphocyteCount001Id):
            self.id = IntegratedLymphocyteCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundLymphocytePercent001(CompoundVariable):
    """
    Lymphocyte percent of total leukocytes variable with metadata, calculated from lymphocyte and white blood cell
    counts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundLymphocytePercent001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundLymphocytePercent001"
    class_name: ClassVar[str] = "CompoundLymphocytePercent001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundLymphocytePercent001

    id: Union[str, CompoundLymphocytePercent001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundLymphocytePercent001Id):
            self.id = CompoundLymphocytePercent001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedLymphocytePercent001(IntegratedVariable):
    """
    Lymphocyte percent variable containing data from multiple studies, normalized to percent of total white blood cells
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedLymphocytePercent001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedLymphocytePercent001"
    class_name: ClassVar[str] = "IntegratedLymphocytePercent001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedLymphocytePercent001

    id: Union[str, IntegratedLymphocytePercent001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedLymphocytePercent001Id):
            self.id = IntegratedLymphocytePercent001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundMCH001(CompoundVariable):
    """
    Mean corpuscular hemoglobin (MCH) variable with metadata, calculated average amount of hemoglobin per red blood
    cell, measured in pg/cell
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundMCH001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundMCH001"
    class_name: ClassVar[str] = "CompoundMCH001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundMCH001

    id: Union[str, CompoundMCH001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundMCH001Id):
            self.id = CompoundMCH001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedMCH001(IntegratedVariable):
    """
    Mean corpuscular hemoglobin variable containing data from multiple studies, normalized to pg/cell
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedMCH001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedMCH001"
    class_name: ClassVar[str] = "IntegratedMCH001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedMCH001

    id: Union[str, IntegratedMCH001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedMCH001Id):
            self.id = IntegratedMCH001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundMCHC001(CompoundVariable):
    """
    Mean corpuscular hemoglobin concentration (MCHC) variable with metadata, calculated average concentration of
    hemoglobin within red blood cells, measured in g/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundMCHC001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundMCHC001"
    class_name: ClassVar[str] = "CompoundMCHC001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundMCHC001

    id: Union[str, CompoundMCHC001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundMCHC001Id):
            self.id = CompoundMCHC001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedMCHC001(IntegratedVariable):
    """
    Mean corpuscular hemoglobin concentration variable containing data from multiple studies, normalized to g/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedMCHC001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedMCHC001"
    class_name: ClassVar[str] = "IntegratedMCHC001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedMCHC001

    id: Union[str, IntegratedMCHC001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedMCHC001Id):
            self.id = IntegratedMCHC001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundMCV001(CompoundVariable):
    """
    Mean corpuscular volume (MCV) variable with metadata, calculated average size of red blood cells, measured in fL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundMCV001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundMCV001"
    class_name: ClassVar[str] = "CompoundMCV001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundMCV001

    id: Union[str, CompoundMCV001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundMCV001Id):
            self.id = CompoundMCV001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedMCV001(IntegratedVariable):
    """
    Mean corpuscular volume variable containing data from multiple studies, normalized to fL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedMCV001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedMCV001"
    class_name: ClassVar[str] = "IntegratedMCV001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedMCV001

    id: Union[str, IntegratedMCV001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedMCV001Id):
            self.id = IntegratedMCV001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundMeanArterialPressure001(CompoundVariable):
    """
    Mean arterial pressure variable with metadata, calculated from systolic and diastolic blood pressure, measured in
    mmHg
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundMeanArterialPressure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundMeanArterialPressure001"
    class_name: ClassVar[str] = "CompoundMeanArterialPressure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundMeanArterialPressure001

    id: Union[str, CompoundMeanArterialPressure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundMeanArterialPressure001Id):
            self.id = CompoundMeanArterialPressure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedMeanArterialPressure001(IntegratedVariable):
    """
    Mean arterial pressure variable containing data from multiple studies, normalized to mmHg
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedMeanArterialPressure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedMeanArterialPressure001"
    class_name: ClassVar[str] = "IntegratedMeanArterialPressure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedMeanArterialPressure001

    id: Union[str, IntegratedMeanArterialPressure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedMeanArterialPressure001Id):
            self.id = IntegratedMeanArterialPressure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundMonocyteCount001(CompoundVariable):
    """
    Monocyte count variable with metadata, measured in 10*3/uL using a complete blood count or manual differential
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundMonocyteCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundMonocyteCount001"
    class_name: ClassVar[str] = "CompoundMonocyteCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundMonocyteCount001

    id: Union[str, CompoundMonocyteCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundMonocyteCount001Id):
            self.id = CompoundMonocyteCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedMonocyteCount001(IntegratedVariable):
    """
    Monocyte count variable containing data from multiple studies, normalized to 10*3/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedMonocyteCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedMonocyteCount001"
    class_name: ClassVar[str] = "IntegratedMonocyteCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedMonocyteCount001

    id: Union[str, IntegratedMonocyteCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedMonocyteCount001Id):
            self.id = IntegratedMonocyteCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundMPV001(CompoundVariable):
    """
    Mean platelet volume (MPV) variable with metadata, measured in fL using a complete blood count
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundMPV001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundMPV001"
    class_name: ClassVar[str] = "CompoundMPV001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundMPV001

    id: Union[str, CompoundMPV001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundMPV001Id):
            self.id = CompoundMPV001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedMPV001(IntegratedVariable):
    """
    Mean platelet volume variable containing data from multiple studies, normalized to fL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedMPV001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedMPV001"
    class_name: ClassVar[str] = "IntegratedMPV001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedMPV001

    id: Union[str, IntegratedMPV001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedMPV001Id):
            self.id = IntegratedMPV001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundMyeloperoxidaseBlood001(CompoundVariable):
    """
    Myeloperoxidase (MPO) concentration in blood variable with metadata, measured in ng/mL using ELISA or
    chemiluminescence immunoassay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundMyeloperoxidaseBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundMyeloperoxidaseBlood001"
    class_name: ClassVar[str] = "CompoundMyeloperoxidaseBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundMyeloperoxidaseBlood001

    id: Union[str, CompoundMyeloperoxidaseBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundMyeloperoxidaseBlood001Id):
            self.id = CompoundMyeloperoxidaseBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedMyeloperoxidaseBlood001(IntegratedVariable):
    """
    Myeloperoxidase concentration in blood variable containing data from multiple studies, normalized to ng/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedMyeloperoxidaseBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedMyeloperoxidaseBlood001"
    class_name: ClassVar[str] = "IntegratedMyeloperoxidaseBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedMyeloperoxidaseBlood001

    id: Union[str, IntegratedMyeloperoxidaseBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedMyeloperoxidaseBlood001Id):
            self.id = IntegratedMyeloperoxidaseBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundNeutrophilCount001(CompoundVariable):
    """
    Neutrophil count variable with metadata, measured in 10*3/uL using a complete blood count or manual differential
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundNeutrophilCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundNeutrophilCount001"
    class_name: ClassVar[str] = "CompoundNeutrophilCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundNeutrophilCount001

    id: Union[str, CompoundNeutrophilCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundNeutrophilCount001Id):
            self.id = CompoundNeutrophilCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedNeutrophilCount001(IntegratedVariable):
    """
    Neutrophil count variable containing data from multiple studies, normalized to 10*3/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedNeutrophilCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedNeutrophilCount001"
    class_name: ClassVar[str] = "IntegratedNeutrophilCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedNeutrophilCount001

    id: Union[str, IntegratedNeutrophilCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedNeutrophilCount001Id):
            self.id = IntegratedNeutrophilCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundNeutrophilPercent001(CompoundVariable):
    """
    Neutrophil percent of total leukocytes variable with metadata, calculated from neutrophil and white blood cell
    counts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundNeutrophilPercent001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundNeutrophilPercent001"
    class_name: ClassVar[str] = "CompoundNeutrophilPercent001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundNeutrophilPercent001

    id: Union[str, CompoundNeutrophilPercent001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundNeutrophilPercent001Id):
            self.id = CompoundNeutrophilPercent001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedNeutrophilPercent001(IntegratedVariable):
    """
    Neutrophil percent variable containing data from multiple studies, normalized to percent of total white blood cells
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedNeutrophilPercent001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedNeutrophilPercent001"
    class_name: ClassVar[str] = "IntegratedNeutrophilPercent001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedNeutrophilPercent001

    id: Union[str, IntegratedNeutrophilPercent001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedNeutrophilPercent001Id):
            self.id = IntegratedNeutrophilPercent001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundNTproBNP001(CompoundVariable):
    """
    NT-proBNP (N-terminal prohormone of brain natriuretic peptide) concentration in blood variable with metadata,
    measured in pg/mL using chemiluminescence immunoassay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundNTproBNP001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundNTproBNP001"
    class_name: ClassVar[str] = "CompoundNTproBNP001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundNTproBNP001

    id: Union[str, CompoundNTproBNP001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundNTproBNP001Id):
            self.id = CompoundNTproBNP001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedNTproBNP001(IntegratedVariable):
    """
    NT-proBNP concentration in blood variable containing data from multiple studies, normalized to pg/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedNTproBNP001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedNTproBNP001"
    class_name: ClassVar[str] = "IntegratedNTproBNP001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedNTproBNP001

    id: Union[str, IntegratedNTproBNP001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedNTproBNP001Id):
            self.id = IntegratedNTproBNP001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundOsteoprotegerinBlood001(CompoundVariable):
    """
    Osteoprotegerin (OPG) concentration in blood variable with metadata, measured in ng/mL using ELISA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundOsteoprotegerinBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundOsteoprotegerinBlood001"
    class_name: ClassVar[str] = "CompoundOsteoprotegerinBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundOsteoprotegerinBlood001

    id: Union[str, CompoundOsteoprotegerinBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundOsteoprotegerinBlood001Id):
            self.id = CompoundOsteoprotegerinBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedOsteoprotegerinBlood001(IntegratedVariable):
    """
    Osteoprotegerin concentration in blood variable containing data from multiple studies, normalized to ng/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedOsteoprotegerinBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedOsteoprotegerinBlood001"
    class_name: ClassVar[str] = "IntegratedOsteoprotegerinBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedOsteoprotegerinBlood001

    id: Union[str, IntegratedOsteoprotegerinBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedOsteoprotegerinBlood001Id):
            self.id = IntegratedOsteoprotegerinBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundPlateletCount001(CompoundVariable):
    """
    Platelet count variable with metadata, measured in 10*3/uL using a complete blood count
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundPlateletCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundPlateletCount001"
    class_name: ClassVar[str] = "CompoundPlateletCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundPlateletCount001

    id: Union[str, CompoundPlateletCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundPlateletCount001Id):
            self.id = CompoundPlateletCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedPlateletCount001(IntegratedVariable):
    """
    Platelet count variable containing data from multiple studies, normalized to 10*3/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedPlateletCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedPlateletCount001"
    class_name: ClassVar[str] = "IntegratedPlateletCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedPlateletCount001

    id: Union[str, IntegratedPlateletCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedPlateletCount001Id):
            self.id = IntegratedPlateletCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundPotassiumBlood001(CompoundVariable):
    """
    Potassium concentration in blood variable with metadata, measured in mmol/L using an ion selective electrode
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundPotassiumBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundPotassiumBlood001"
    class_name: ClassVar[str] = "CompoundPotassiumBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundPotassiumBlood001

    id: Union[str, CompoundPotassiumBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundPotassiumBlood001Id):
            self.id = CompoundPotassiumBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedPotassiumBlood001(IntegratedVariable):
    """
    Potassium concentration in blood variable containing data from multiple studies, normalized to mmol/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedPotassiumBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedPotassiumBlood001"
    class_name: ClassVar[str] = "IntegratedPotassiumBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedPotassiumBlood001

    id: Union[str, IntegratedPotassiumBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedPotassiumBlood001Id):
            self.id = IntegratedPotassiumBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundPRInterval001(CompoundVariable):
    """
    PR interval variable with metadata, measured in ms using electrocardiography
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundPRInterval001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundPRInterval001"
    class_name: ClassVar[str] = "CompoundPRInterval001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundPRInterval001

    id: Union[str, CompoundPRInterval001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundPRInterval001Id):
            self.id = CompoundPRInterval001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedPRInterval001(IntegratedVariable):
    """
    PR interval variable containing data from multiple studies, normalized to ms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedPRInterval001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedPRInterval001"
    class_name: ClassVar[str] = "IntegratedPRInterval001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedPRInterval001

    id: Union[str, IntegratedPRInterval001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedPRInterval001Id):
            self.id = IntegratedPRInterval001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundPSelectinBlood001(CompoundVariable):
    """
    P-selectin concentration in blood variable with metadata, measured in ng/mL using ELISA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundPSelectinBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundPSelectinBlood001"
    class_name: ClassVar[str] = "CompoundPSelectinBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundPSelectinBlood001

    id: Union[str, CompoundPSelectinBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundPSelectinBlood001Id):
            self.id = CompoundPSelectinBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedPSelectinBlood001(IntegratedVariable):
    """
    P-selectin concentration in blood variable containing data from multiple studies, normalized to ng/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedPSelectinBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedPSelectinBlood001"
    class_name: ClassVar[str] = "IntegratedPSelectinBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedPSelectinBlood001

    id: Union[str, IntegratedPSelectinBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedPSelectinBlood001Id):
            self.id = IntegratedPSelectinBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundQRSInterval001(CompoundVariable):
    """
    QRS interval variable with metadata, measured in ms using electrocardiography
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundQRSInterval001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundQRSInterval001"
    class_name: ClassVar[str] = "CompoundQRSInterval001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundQRSInterval001

    id: Union[str, CompoundQRSInterval001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundQRSInterval001Id):
            self.id = CompoundQRSInterval001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedQRSInterval001(IntegratedVariable):
    """
    QRS interval variable containing data from multiple studies, normalized to ms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedQRSInterval001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedQRSInterval001"
    class_name: ClassVar[str] = "IntegratedQRSInterval001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedQRSInterval001

    id: Union[str, IntegratedQRSInterval001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedQRSInterval001Id):
            self.id = IntegratedQRSInterval001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundQTInterval001(CompoundVariable):
    """
    QT interval variable with metadata, measured in ms using electrocardiography
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundQTInterval001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundQTInterval001"
    class_name: ClassVar[str] = "CompoundQTInterval001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundQTInterval001

    id: Union[str, CompoundQTInterval001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundQTInterval001Id):
            self.id = CompoundQTInterval001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedQTInterval001(IntegratedVariable):
    """
    QT interval variable containing data from multiple studies, normalized to ms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedQTInterval001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedQTInterval001"
    class_name: ClassVar[str] = "IntegratedQTInterval001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedQTInterval001

    id: Union[str, IntegratedQTInterval001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedQTInterval001Id):
            self.id = IntegratedQTInterval001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundRBCCount001(CompoundVariable):
    """
    Red blood cell (RBC) count variable with metadata, measured in 10*6/uL using a complete blood count
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundRBCCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundRBCCount001"
    class_name: ClassVar[str] = "CompoundRBCCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundRBCCount001

    id: Union[str, CompoundRBCCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundRBCCount001Id):
            self.id = CompoundRBCCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedRBCCount001(IntegratedVariable):
    """
    Red blood cell count variable containing data from multiple studies, normalized to 10*6/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedRBCCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedRBCCount001"
    class_name: ClassVar[str] = "IntegratedRBCCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedRBCCount001

    id: Union[str, IntegratedRBCCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedRBCCount001Id):
            self.id = IntegratedRBCCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundRDW001(CompoundVariable):
    """
    Red cell distribution width (RDW) variable with metadata, measured as percent using a complete blood count
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundRDW001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundRDW001"
    class_name: ClassVar[str] = "CompoundRDW001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundRDW001

    id: Union[str, CompoundRDW001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundRDW001Id):
            self.id = CompoundRDW001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedRDW001(IntegratedVariable):
    """
    Red cell distribution width variable containing data from multiple studies, normalized to percent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedRDW001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedRDW001"
    class_name: ClassVar[str] = "IntegratedRDW001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedRDW001

    id: Union[str, IntegratedRDW001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedRDW001Id):
            self.id = IntegratedRDW001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundSleepDuration001(CompoundVariable):
    """
    Sleep duration variable with metadata, measured in hours per night using questionnaire, survey, actigraphy, or
    polysomnography
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundSleepDuration001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundSleepDuration001"
    class_name: ClassVar[str] = "CompoundSleepDuration001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundSleepDuration001

    id: Union[str, CompoundSleepDuration001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundSleepDuration001Id):
            self.id = CompoundSleepDuration001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedSleepDuration001(IntegratedVariable):
    """
    Sleep duration variable containing data from multiple studies, normalized to hours per night
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedSleepDuration001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedSleepDuration001"
    class_name: ClassVar[str] = "IntegratedSleepDuration001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedSleepDuration001

    id: Union[str, IntegratedSleepDuration001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedSleepDuration001Id):
            self.id = IntegratedSleepDuration001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundSodiumBlood001(CompoundVariable):
    """
    Sodium concentration in blood variable with metadata, measured in mmol/L using an ion selective electrode
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundSodiumBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundSodiumBlood001"
    class_name: ClassVar[str] = "CompoundSodiumBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundSodiumBlood001

    id: Union[str, CompoundSodiumBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundSodiumBlood001Id):
            self.id = CompoundSodiumBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedSodiumBlood001(IntegratedVariable):
    """
    Sodium concentration in blood variable containing data from multiple studies, normalized to mmol/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedSodiumBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedSodiumBlood001"
    class_name: ClassVar[str] = "IntegratedSodiumBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedSodiumBlood001

    id: Union[str, IntegratedSodiumBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedSodiumBlood001Id):
            self.id = IntegratedSodiumBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundSodiumIntake001(CompoundVariable):
    """
    Sodium intake variable with metadata, measured in mg per day using questionnaire, survey, or interview
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundSodiumIntake001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundSodiumIntake001"
    class_name: ClassVar[str] = "CompoundSodiumIntake001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundSodiumIntake001

    id: Union[str, CompoundSodiumIntake001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundSodiumIntake001Id):
            self.id = CompoundSodiumIntake001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedSodiumIntake001(IntegratedVariable):
    """
    Sodium intake variable containing data from multiple studies, normalized to mg per day
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedSodiumIntake001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedSodiumIntake001"
    class_name: ClassVar[str] = "IntegratedSodiumIntake001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedSodiumIntake001

    id: Union[str, IntegratedSodiumIntake001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedSodiumIntake001Id):
            self.id = IntegratedSodiumIntake001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundSystolicBloodPressure001(CompoundVariable):
    """
    Systolic blood pressure variable with metadata, measured in mmHg using auscultatory or oscillometric method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundSystolicBloodPressure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundSystolicBloodPressure001"
    class_name: ClassVar[str] = "CompoundSystolicBloodPressure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundSystolicBloodPressure001

    id: Union[str, CompoundSystolicBloodPressure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundSystolicBloodPressure001Id):
            self.id = CompoundSystolicBloodPressure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedSystolicBloodPressure001(IntegratedVariable):
    """
    Systolic blood pressure variable containing data from multiple studies, normalized to mmHg
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedSystolicBloodPressure001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedSystolicBloodPressure001"
    class_name: ClassVar[str] = "IntegratedSystolicBloodPressure001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedSystolicBloodPressure001

    id: Union[str, IntegratedSystolicBloodPressure001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedSystolicBloodPressure001Id):
            self.id = IntegratedSystolicBloodPressure001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundTNFAlphaBlood001(CompoundVariable):
    """
    TNF-alpha (tumor necrosis factor alpha) concentration in blood variable with metadata, measured in pg/mL using
    ELISA or multiplex bead immunoassay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundTNFAlphaBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundTNFAlphaBlood001"
    class_name: ClassVar[str] = "CompoundTNFAlphaBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundTNFAlphaBlood001

    id: Union[str, CompoundTNFAlphaBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundTNFAlphaBlood001Id):
            self.id = CompoundTNFAlphaBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedTNFAlphaBlood001(IntegratedVariable):
    """
    TNF-alpha concentration in blood variable containing data from multiple studies, normalized to pg/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedTNFAlphaBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedTNFAlphaBlood001"
    class_name: ClassVar[str] = "IntegratedTNFAlphaBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedTNFAlphaBlood001

    id: Union[str, IntegratedTNFAlphaBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedTNFAlphaBlood001Id):
            self.id = IntegratedTNFAlphaBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundTotalCholesterol001(CompoundVariable):
    """
    Total cholesterol concentration in blood variable with metadata, measured in mg/dL using an enzymatic kinetic assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundTotalCholesterol001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundTotalCholesterol001"
    class_name: ClassVar[str] = "CompoundTotalCholesterol001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundTotalCholesterol001

    id: Union[str, CompoundTotalCholesterol001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundTotalCholesterol001Id):
            self.id = CompoundTotalCholesterol001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundTotalCholesterol002(CompoundVariable):
    """
    Total cholesterol concentration in blood variable with metadata, measured in mmol/L using an enzymatic kinetic
    assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundTotalCholesterol002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundTotalCholesterol002"
    class_name: ClassVar[str] = "CompoundTotalCholesterol002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundTotalCholesterol002

    id: Union[str, CompoundTotalCholesterol002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundTotalCholesterol002Id):
            self.id = CompoundTotalCholesterol002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedTotalCholesterol001(IntegratedVariable):
    """
    Total cholesterol concentration in blood variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedTotalCholesterol001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedTotalCholesterol001"
    class_name: ClassVar[str] = "IntegratedTotalCholesterol001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedTotalCholesterol001

    id: Union[str, IntegratedTotalCholesterol001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedTotalCholesterol001Id):
            self.id = IntegratedTotalCholesterol001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundTriglyceridesBlood001(CompoundVariable):
    """
    Triglycerides concentration in blood variable with metadata, measured in mg/dL using an enzymatic kinetic assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundTriglyceridesBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundTriglyceridesBlood001"
    class_name: ClassVar[str] = "CompoundTriglyceridesBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundTriglyceridesBlood001

    id: Union[str, CompoundTriglyceridesBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundTriglyceridesBlood001Id):
            self.id = CompoundTriglyceridesBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundTriglyceridesBlood002(CompoundVariable):
    """
    Triglycerides concentration in blood variable with metadata, measured in mmol/L using an enzymatic kinetic assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundTriglyceridesBlood002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundTriglyceridesBlood002"
    class_name: ClassVar[str] = "CompoundTriglyceridesBlood002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundTriglyceridesBlood002

    id: Union[str, CompoundTriglyceridesBlood002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundTriglyceridesBlood002Id):
            self.id = CompoundTriglyceridesBlood002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedTriglyceridesBlood001(IntegratedVariable):
    """
    Triglycerides concentration in blood variable containing data from multiple studies, normalized to mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedTriglyceridesBlood001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedTriglyceridesBlood001"
    class_name: ClassVar[str] = "IntegratedTriglyceridesBlood001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedTriglyceridesBlood001

    id: Union[str, IntegratedTriglyceridesBlood001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedTriglyceridesBlood001Id):
            self.id = IntegratedTriglyceridesBlood001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundTroponin001(CompoundVariable):
    """
    Troponin concentration in blood variable with metadata, measured in ng/mL using chemiluminescence immunoassay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundTroponin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundTroponin001"
    class_name: ClassVar[str] = "CompoundTroponin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundTroponin001

    id: Union[str, CompoundTroponin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundTroponin001Id):
            self.id = CompoundTroponin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedTroponin001(IntegratedVariable):
    """
    Troponin concentration in blood variable containing data from multiple studies, normalized to ng/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedTroponin001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedTroponin001"
    class_name: ClassVar[str] = "IntegratedTroponin001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedTroponin001

    id: Union[str, IntegratedTroponin001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedTroponin001Id):
            self.id = IntegratedTroponin001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundVegetableConsumption001(CompoundVariable):
    """
    Vegetable consumption variable with metadata, measured in servings per week using questionnaire, survey, or
    interview
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundVegetableConsumption001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundVegetableConsumption001"
    class_name: ClassVar[str] = "CompoundVegetableConsumption001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundVegetableConsumption001

    id: Union[str, CompoundVegetableConsumption001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundVegetableConsumption001Id):
            self.id = CompoundVegetableConsumption001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedVegetableConsumption001(IntegratedVariable):
    """
    Vegetable consumption variable containing data from multiple studies, normalized to servings per week
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedVegetableConsumption001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedVegetableConsumption001"
    class_name: ClassVar[str] = "IntegratedVegetableConsumption001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedVegetableConsumption001

    id: Union[str, IntegratedVegetableConsumption001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedVegetableConsumption001Id):
            self.id = IntegratedVegetableConsumption001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundVonWillebrandFactor001(CompoundVariable):
    """
    Von Willebrand factor (VWF) variable with metadata, measured as percent of normal using immunoturbidometry or
    ristocetin cofactor assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundVonWillebrandFactor001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundVonWillebrandFactor001"
    class_name: ClassVar[str] = "CompoundVonWillebrandFactor001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundVonWillebrandFactor001

    id: Union[str, CompoundVonWillebrandFactor001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundVonWillebrandFactor001Id):
            self.id = CompoundVonWillebrandFactor001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedVonWillebrandFactor001(IntegratedVariable):
    """
    Von Willebrand factor variable containing data from multiple studies, normalized to percent of normal
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedVonWillebrandFactor001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedVonWillebrandFactor001"
    class_name: ClassVar[str] = "IntegratedVonWillebrandFactor001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedVonWillebrandFactor001

    id: Union[str, IntegratedVonWillebrandFactor001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedVonWillebrandFactor001Id):
            self.id = IntegratedVonWillebrandFactor001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundWaistCircumference001(CompoundVariable):
    """
    Waist circumference variable with metadata, measured in cm using a flexible measuring tape
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundWaistCircumference001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundWaistCircumference001"
    class_name: ClassVar[str] = "CompoundWaistCircumference001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundWaistCircumference001

    id: Union[str, CompoundWaistCircumference001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundWaistCircumference001Id):
            self.id = CompoundWaistCircumference001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundWaistCircumference002(CompoundVariable):
    """
    Waist circumference variable with metadata, measured in mm using a flexible measuring tape
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundWaistCircumference002"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundWaistCircumference002"
    class_name: ClassVar[str] = "CompoundWaistCircumference002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundWaistCircumference002

    id: Union[str, CompoundWaistCircumference002Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundWaistCircumference002Id):
            self.id = CompoundWaistCircumference002Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundWaistCircumference003(CompoundVariable):
    """
    Waist circumference variable with metadata, measured in inches using a flexible measuring tape
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundWaistCircumference003"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundWaistCircumference003"
    class_name: ClassVar[str] = "CompoundWaistCircumference003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundWaistCircumference003

    id: Union[str, CompoundWaistCircumference003Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundWaistCircumference003Id):
            self.id = CompoundWaistCircumference003Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedWaistCircumference001(IntegratedVariable):
    """
    Waist circumference variable containing data from multiple studies, normalized to cm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedWaistCircumference001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedWaistCircumference001"
    class_name: ClassVar[str] = "IntegratedWaistCircumference001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedWaistCircumference001

    id: Union[str, IntegratedWaistCircumference001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedWaistCircumference001Id):
            self.id = IntegratedWaistCircumference001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundWaistHipRatio001(CompoundVariable):
    """
    Waist-to-hip ratio variable with metadata, calculated from waist and hip circumference measurements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundWaistHipRatio001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundWaistHipRatio001"
    class_name: ClassVar[str] = "CompoundWaistHipRatio001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundWaistHipRatio001

    id: Union[str, CompoundWaistHipRatio001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundWaistHipRatio001Id):
            self.id = CompoundWaistHipRatio001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedWaistHipRatio001(IntegratedVariable):
    """
    Waist-to-hip ratio variable containing data from multiple studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedWaistHipRatio001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedWaistHipRatio001"
    class_name: ClassVar[str] = "IntegratedWaistHipRatio001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedWaistHipRatio001

    id: Union[str, IntegratedWaistHipRatio001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedWaistHipRatio001Id):
            self.id = IntegratedWaistHipRatio001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompoundWhiteBloodCellCount001(CompoundVariable):
    """
    White blood cell (WBC) count variable with metadata, measured in 10*3/uL using a complete blood count or manual
    differential
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["CompoundWhiteBloodCellCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:CompoundWhiteBloodCellCount001"
    class_name: ClassVar[str] = "CompoundWhiteBloodCellCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CompoundWhiteBloodCellCount001

    id: Union[str, CompoundWhiteBloodCellCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompoundWhiteBloodCellCount001Id):
            self.id = CompoundWhiteBloodCellCount001Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntegratedWhiteBloodCellCount001(IntegratedVariable):
    """
    White blood cell count variable containing data from multiple studies, normalized to 10*3/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY["IntegratedWhiteBloodCellCount001"]
    class_class_curie: ClassVar[str] = "bdc_variable_library:IntegratedWhiteBloodCellCount001"
    class_name: ClassVar[str] = "IntegratedWhiteBloodCellCount001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.IntegratedWhiteBloodCellCount001

    id: Union[str, IntegratedWhiteBloodCellCount001Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntegratedWhiteBloodCellCount001Id):
            self.id = IntegratedWhiteBloodCellCount001Id(self.id)

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
    unit: Optional[str] = None
    method: Optional[Union[str, "MethodEnum"]] = None
    instrument: Optional[str] = None
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

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.method is not None and not isinstance(self.method, MethodEnum):
            self.method = MethodEnum(self.method)

        if self.instrument is not None and not isinstance(self.instrument, str):
            self.instrument = str(self.instrument)

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
    instrument: Optional[str] = None
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

        if self.instrument is not None and not isinstance(self.instrument, str):
            self.instrument = str(self.instrument)

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
    exposure_status: Optional[Union[str, "HistoricalStatusEnum"]] = None
    exposure_provenance: Optional[Union[str, "ProvenanceEnum"]] = None

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

        if self.exposure_status is not None and not isinstance(self.exposure_status, HistoricalStatusEnum):
            self.exposure_status = HistoricalStatusEnum(self.exposure_status)

        if self.exposure_provenance is not None and not isinstance(self.exposure_provenance, ProvenanceEnum):
            self.exposure_provenance = ProvenanceEnum(self.exposure_provenance)

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
    procedure_status: Optional[Union[str, "HistoricalStatusEnum"]] = None
    procedure_provenance: Optional[Union[str, "ProvenanceEnum"]] = None
    body_location: Optional[Union[str, URIorCURIE]] = None

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

        if self.procedure_status is not None and not isinstance(self.procedure_status, HistoricalStatusEnum):
            self.procedure_status = HistoricalStatusEnum(self.procedure_status)

        if self.procedure_provenance is not None and not isinstance(self.procedure_provenance, ProvenanceEnum):
            self.procedure_provenance = ProvenanceEnum(self.procedure_provenance)

        if self.body_location is not None and not isinstance(self.body_location, URIorCURIE):
            self.body_location = URIorCURIE(self.body_location)

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
    Measurement of linear distance of a standing human body (adult) from the bottom of a flat foot to the top-most
    point of the head measured in centimeters
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord001"
    class_name: ClassVar[str] = "HumanBodyHeightRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity"] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.age_at_measurement):
            self.MissingRequiredField("age_at_measurement")
        if not isinstance(self.age_at_measurement, Quantity):
            self.age_at_measurement = Quantity(**as_dict(self.age_at_measurement))

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord002(HumanBodyHeightRecord):
    """
    Measurement of linear distance of a standing human body (adult) from the bottom of a flat foot to the top-most
    point of the head measured in inches
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord002"
    class_name: ClassVar[str] = "HumanBodyHeightRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity"] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.age_at_measurement):
            self.MissingRequiredField("age_at_measurement")
        if not isinstance(self.age_at_measurement, Quantity):
            self.age_at_measurement = Quantity(**as_dict(self.age_at_measurement))

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord003(HumanBodyHeightRecord):
    """
    Measurement of linear distance of a standing human body (adult) from the bottom of a flat foot to the top-most
    point of the head measured in feet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord003"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord003"
    class_name: ClassVar[str] = "HumanBodyHeightRecord003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord003

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity"] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.age_at_measurement):
            self.MissingRequiredField("age_at_measurement")
        if not isinstance(self.age_at_measurement, Quantity):
            self.age_at_measurement = Quantity(**as_dict(self.age_at_measurement))

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyHeightRecord004(HumanBodyHeightRecord):
    """
    Measurement of linear distance of a standing human body (adult) from the bottom of a flat foot to the top-most
    point of the head measured in meters
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyHeightRecord004"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyHeightRecord004"
    class_name: ClassVar[str] = "HumanBodyHeightRecord004"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord004

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, "HumanBodyHeightQuantity"] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.age_at_measurement):
            self.MissingRequiredField("age_at_measurement")
        if not isinstance(self.age_at_measurement, Quantity):
            self.age_at_measurement = Quantity(**as_dict(self.age_at_measurement))

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

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
class AdultHumanBodyWeightRecord(HumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body (adult) on the earth due to gravity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AdultHumanBodyWeightRecord"]
    class_class_curie: ClassVar[str] = "cms:AdultHumanBodyWeightRecord"
    class_name: ClassVar[str] = "AdultHumanBodyWeightRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AdultHumanBodyWeightRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "AdultHumanBodyWeightQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, AdultHumanBodyWeightQuantity):
            self.measurement_value = AdultHumanBodyWeightQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdultHumanBodyWeightRecord001(AdultHumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body (adult) on the earth due to gravity in kg
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AdultHumanBodyWeightRecord001"]
    class_class_curie: ClassVar[str] = "cms:AdultHumanBodyWeightRecord001"
    class_name: ClassVar[str] = "AdultHumanBodyWeightRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AdultHumanBodyWeightRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "AdultHumanBodyWeightQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdultHumanBodyWeightRecord002(AdultHumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body (adult) on the earth due to gravity in lbs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AdultHumanBodyWeightRecord002"]
    class_class_curie: ClassVar[str] = "cms:AdultHumanBodyWeightRecord002"
    class_name: ClassVar[str] = "AdultHumanBodyWeightRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AdultHumanBodyWeightRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "AdultHumanBodyWeightQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChildHumanBodyWeightRecord(HumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body (child) on the earth due to gravity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ChildHumanBodyWeightRecord"]
    class_class_curie: ClassVar[str] = "cms:ChildHumanBodyWeightRecord"
    class_name: ClassVar[str] = "ChildHumanBodyWeightRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, "ChildHumanBodyWeightQuantity"] = None
    age_at_measurement: Union[dict, Quantity] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, ChildHumanBodyWeightQuantity):
            self.measurement_value = ChildHumanBodyWeightQuantity(**as_dict(self.measurement_value))

        if self._is_empty(self.age_at_measurement):
            self.MissingRequiredField("age_at_measurement")
        if not isinstance(self.age_at_measurement, Quantity):
            self.age_at_measurement = Quantity(**as_dict(self.age_at_measurement))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChildHumanBodyWeightRecord001(ChildHumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body (child) on the earth due to gravity in g
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ChildHumanBodyWeightRecord001"]
    class_class_curie: ClassVar[str] = "cms:ChildHumanBodyWeightRecord001"
    class_name: ClassVar[str] = "ChildHumanBodyWeightRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, "ChildHumanBodyWeightQuantity"] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChildHumanBodyWeightRecord002(ChildHumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body (child) on the earth due to gravity in kg
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ChildHumanBodyWeightRecord002"]
    class_class_curie: ClassVar[str] = "cms:ChildHumanBodyWeightRecord002"
    class_name: ClassVar[str] = "ChildHumanBodyWeightRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, "ChildHumanBodyWeightQuantity"] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChildHumanBodyWeightRecord003(ChildHumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body (child) on the earth due to gravity in lbs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ChildHumanBodyWeightRecord003"]
    class_class_curie: ClassVar[str] = "cms:ChildHumanBodyWeightRecord003"
    class_name: ClassVar[str] = "ChildHumanBodyWeightRecord003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord003

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, "ChildHumanBodyWeightQuantity"] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChildHumanBodyWeightRecord004(ChildHumanBodyWeightRecord):
    """
    Measurement of the force exerted by a human body (child) on the earth due to gravity in oz
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ChildHumanBodyWeightRecord004"]
    class_class_curie: ClassVar[str] = "cms:ChildHumanBodyWeightRecord004"
    class_name: ClassVar[str] = "ChildHumanBodyWeightRecord004"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord004

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, "ChildHumanBodyWeightQuantity"] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BodyMassIndexRecord(ClinicalMeasurementRecord):
    """
    A calculated numerical quantity representing an individual's weight-to-height ratio. BMI is calculated as weight
    (kg) divided by height (m) squared.
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
class AdultBodyMassIndexRecord(BodyMassIndexRecord):
    """
    A calculated numerical quantity representing an adult's weight-to-height ratio. BMI is calculated as weight (kg)
    divided by height (m) squared.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AdultBodyMassIndexRecord"]
    class_class_curie: ClassVar[str] = "cms:AdultBodyMassIndexRecord"
    class_name: ClassVar[str] = "AdultBodyMassIndexRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AdultBodyMassIndexRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "BodyMassIndexQuantity"] = None

@dataclass(repr=False)
class ChildBodyMassIndexRecord(BodyMassIndexRecord):
    """
    A calculated numerical quantity representing an child's weight-to-height ratio. BMI is calculated as weight (kg)
    divided by height (m) squared.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ChildBodyMassIndexRecord"]
    class_class_curie: ClassVar[str] = "cms:ChildBodyMassIndexRecord"
    class_name: ClassVar[str] = "ChildBodyMassIndexRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ChildBodyMassIndexRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "BodyMassIndexQuantity"] = None

@dataclass(repr=False)
class HumanFvcRecord(ClinicalMeasurementRecord):
    """
    Total amount of air a person can forcibly exhale after taking the deepest breath possible.
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

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanFvcQuantity):
            self.measurement_value = HumanFvcQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFvcRecord001(HumanFvcRecord):
    """
    Total amount of air a person can forcibly exhale after taking the deepest breath possible in L.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFvcRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanFvcRecord001"
    class_name: ClassVar[str] = "HumanFvcRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFvcRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFvcQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFvcRecord002(HumanFvcRecord):
    """
    Total amount of air a person can forcibly exhale after taking the deepest breath possible in mL.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFvcRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanFvcRecord002"
    class_name: ClassVar[str] = "HumanFvcRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFvcRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFvcQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

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
class HumanFev1Record001(HumanFev1Record):
    """
    Maximum amount of air a person can forcibly exhale in the first second of a breathing test in L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFev1Record001"]
    class_class_curie: ClassVar[str] = "cms:HumanFev1Record001"
    class_name: ClassVar[str] = "HumanFev1Record001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFev1Record001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFev1Quantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFev1Record002(HumanFev1Record):
    """
    Maximum amount of air a person can forcibly exhale in the first second of a breathing test in mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFev1Record002"]
    class_class_curie: ClassVar[str] = "cms:HumanFev1Record002"
    class_name: ClassVar[str] = "HumanFev1Record002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFev1Record002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFev1Quantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPredictedFev1Record(ClinicalMeasurementRecord):
    """
    Predicted maximum amount of air a person can forcibly exhale in the first second of a breathing test. Predictions
    are based on a reference equation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPredictedFev1Record"]
    class_class_curie: ClassVar[str] = "cms:HumanPredictedFev1Record"
    class_name: ClassVar[str] = "HumanPredictedFev1Record"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPredictedFev1Record

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPredictedFev1Quantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPredictedFev1Quantity):
            self.measurement_value = HumanPredictedFev1Quantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPercentPredictedFev1Record(ClinicalMeasurementRecord):
    """
    Percent of the predicted FEV1 that is achieved by the patient
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPercentPredictedFev1Record"]
    class_class_curie: ClassVar[str] = "cms:HumanPercentPredictedFev1Record"
    class_name: ClassVar[str] = "HumanPercentPredictedFev1Record"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPercentPredictedFev1Record

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPercentPredictedFev1Quantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPercentPredictedFev1Quantity):
            self.measurement_value = HumanPercentPredictedFev1Quantity(**as_dict(self.measurement_value))

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
    Concentration of basophil cells in whole blood in 10*3/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBasophilCountRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanBasophilCountRecord001"
    class_name: ClassVar[str] = "HumanBasophilCountRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBasophilCountQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBasophilCountRecord002(HumanBasophilCountRecord):
    """
    Concentration of basophil cells in whole blood as a discrete cell count in {#}/uL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBasophilCountRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanBasophilCountRecord002"
    class_name: ClassVar[str] = "HumanBasophilCountRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBasophilCountQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Human8epiPGF2aUrineRecord(ClinicalMeasurementRecord):
    """
    Concentration of 8-epi-prostaglandin F2 alpha in urine
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["Human8epiPGF2aUrineRecord"]
    class_class_curie: ClassVar[str] = "cms:Human8epiPGF2aUrineRecord"
    class_name: ClassVar[str] = "Human8epiPGF2aUrineRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Human8epiPGF2aUrineRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "Human8epiPGF2aUrineQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, Human8epiPGF2aUrineQuantity):
            self.measurement_value = Human8epiPGF2aUrineQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Human8epiPGF2aUrineRecord001(Human8epiPGF2aUrineRecord):
    """
    Concentration of 8-epi-prostaglandin F2 alpha in urine in pg/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["Human8epiPGF2aUrineRecord001"]
    class_class_curie: ClassVar[str] = "cms:Human8epiPGF2aUrineRecord001"
    class_name: ClassVar[str] = "Human8epiPGF2aUrineRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Human8epiPGF2aUrineRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "Human8epiPGF2aUrineQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLPPLA2ActivityBloodRecord(ClinicalMeasurementRecord):
    """
    Activity of LP-PLA2 in blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLPPLA2ActivityBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanLPPLA2ActivityBloodRecord"
    class_name: ClassVar[str] = "HumanLPPLA2ActivityBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLPPLA2ActivityBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanLPPLA2ActivityBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanLPPLA2ActivityBloodQuantity):
            self.measurement_value = HumanLPPLA2ActivityBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCreatinineUrineRecord(ClinicalMeasurementRecord):
    """
    Concentration of creatinine measured in urine
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCreatinineUrineRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanCreatinineUrineRecord"
    class_name: ClassVar[str] = "HumanCreatinineUrineRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCreatinineUrineRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCreatinineUrineQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanCreatinineUrineQuantity):
            self.measurement_value = HumanCreatinineUrineQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCreatinineUrineRecord001(HumanCreatinineUrineRecord):
    """
    Concentration of creatinine measured in urine using the Jaffe reaction in mg/dL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCreatinineUrineRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanCreatinineUrineRecord001"
    class_name: ClassVar[str] = "HumanCreatinineUrineRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCreatinineUrineRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCreatinineUrineQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCreatinineUrineRecord002(HumanCreatinineUrineRecord):
    """
    Concentration of creatinine measured in urine using the Jaffe reaction in mmol/L
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCreatinineUrineRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanCreatinineUrineRecord002"
    class_name: ClassVar[str] = "HumanCreatinineUrineRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCreatinineUrineRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCreatinineUrineQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineRecord(ClinicalMeasurementRecord):
    """
    Concentration of albumin measured in urine
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineRecord"
    class_name: ClassVar[str] = "HumanAlbuminUrineRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAlbuminUrineQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAlbuminUrineQuantity):
            self.measurement_value = HumanAlbuminUrineQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineRecord001(HumanAlbuminUrineRecord):
    """
    Concentration of albumin measured in urine in mg/dL using immunoturbidometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineRecord001"
    class_name: ClassVar[str] = "HumanAlbuminUrineRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAlbuminUrineQuantity001"] = None
    unit: Optional[str] = None
    method: Optional[Union[str, "MethodEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAlbuminUrineQuantity001):
            self.measurement_value = HumanAlbuminUrineQuantity001(**as_dict(self.measurement_value))

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.method is not None and not isinstance(self.method, MethodEnum):
            self.method = MethodEnum(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineRecord002(HumanAlbuminUrineRecord):
    """
    Concentration of albumin measured in urine in mg/L equivalent to ug/mL using an albumin dipstick
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineRecord002"
    class_name: ClassVar[str] = "HumanAlbuminUrineRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAlbuminUrineQuantity002"] = None
    unit: Optional[str] = None
    method: Optional[Union[str, "MethodEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAlbuminUrineQuantity002):
            self.measurement_value = HumanAlbuminUrineQuantity002(**as_dict(self.measurement_value))

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.method is not None and not isinstance(self.method, MethodEnum):
            self.method = MethodEnum(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineRecord003(HumanAlbuminUrineRecord):
    """
    Concentration of albumin measured in urine in mg/L equivalent to ug/mL using HPLC
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineRecord003"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineRecord003"
    class_name: ClassVar[str] = "HumanAlbuminUrineRecord003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord003

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAlbuminUrineQuantity003"] = None
    unit: Optional[str] = None
    method: Optional[Union[str, "MethodEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAlbuminUrineQuantity003):
            self.measurement_value = HumanAlbuminUrineQuantity003(**as_dict(self.measurement_value))

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.method is not None and not isinstance(self.method, MethodEnum):
            self.method = MethodEnum(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineRecord004(HumanAlbuminUrineRecord):
    """
    Concentration of albumin measured in urine in mg/L equivalent to ug/mL using immunonephelometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineRecord004"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineRecord004"
    class_name: ClassVar[str] = "HumanAlbuminUrineRecord004"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord004

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAlbuminUrineQuantity004"] = None
    unit: Optional[str] = None
    method: Optional[Union[str, "MethodEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAlbuminUrineQuantity004):
            self.measurement_value = HumanAlbuminUrineQuantity004(**as_dict(self.measurement_value))

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.method is not None and not isinstance(self.method, MethodEnum):
            self.method = MethodEnum(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineRecord005(HumanAlbuminUrineRecord):
    """
    Concentration of albumin measured in urine in mg/L equivalent to ug/mL using immunoturbidometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineRecord005"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineRecord005"
    class_name: ClassVar[str] = "HumanAlbuminUrineRecord005"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord005

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAlbuminUrineQuantity005"] = None
    unit: Optional[str] = None
    method: Optional[Union[str, "MethodEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAlbuminUrineQuantity005):
            self.measurement_value = HumanAlbuminUrineQuantity005(**as_dict(self.measurement_value))

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.method is not None and not isinstance(self.method, MethodEnum):
            self.method = MethodEnum(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminCreatinineRatioUrineRecord(ClinicalMeasurementRecord):
    """
    Ratio of albumin to creatinine measured in urine
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminCreatinineRatioUrineRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminCreatinineRatioUrineRecord"
    class_name: ClassVar[str] = "HumanAlbuminCreatinineRatioUrineRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminCreatinineRatioUrineRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAlbuminCreatinineRatioUrineQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAlbuminCreatinineRatioUrineQuantity):
            self.measurement_value = HumanAlbuminCreatinineRatioUrineQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ApneaHypopneaIndexRecord(ClinicalMeasurementRecord):
    """
    Measurement used to diagnose and assess the severity of sleep apnea. It is calculated by counting the number of
    apneas and hypopneas that occur per hour of sleep.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ApneaHypopneaIndexRecord"]
    class_class_curie: ClassVar[str] = "cms:ApneaHypopneaIndexRecord"
    class_name: ClassVar[str] = "ApneaHypopneaIndexRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ApneaHypopneaIndexRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "ApneaHypopneaIndexQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, ApneaHypopneaIndexQuantity):
            self.measurement_value = ApneaHypopneaIndexQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminBloodRecord(ClinicalMeasurementRecord):
    """
    Measurement of albumin concentration in blood serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminBloodRecord"
    class_name: ClassVar[str] = "HumanAlbuminBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAlbuminBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAlbuminBloodQuantity):
            self.measurement_value = HumanAlbuminBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlcoholConsumptionRecord(ClinicalMeasurementRecord):
    """
    Servings of alcohol consumed per week
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AlcoholConsumptionRecord"]
    class_class_curie: ClassVar[str] = "cms:AlcoholConsumptionRecord"
    class_name: ClassVar[str] = "AlcoholConsumptionRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AlcoholConsumptionRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "AlcoholConsumptionQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, AlcoholConsumptionQuantity):
            self.measurement_value = AlcoholConsumptionQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAltSgptRecord(ClinicalMeasurementRecord):
    """
    Concentration of ALT (alanine transaminase / SGPT) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAltSgptRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanAltSgptRecord"
    class_name: ClassVar[str] = "HumanAltSgptRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAltSgptRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAltSgptQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAltSgptQuantity):
            self.measurement_value = HumanAltSgptQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAstSgotRecord(ClinicalMeasurementRecord):
    """
    Concentration of AST (aspartate aminotransferase / SGOT) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAstSgotRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanAstSgotRecord"
    class_name: ClassVar[str] = "HumanAstSgotRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAstSgotRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanAstSgotQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanAstSgotQuantity):
            self.measurement_value = HumanAstSgotQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBilirubinConjugatedRecord(ClinicalMeasurementRecord):
    """
    Concentration of conjugated (direct) bilirubin in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBilirubinConjugatedRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBilirubinConjugatedRecord"
    class_name: ClassVar[str] = "HumanBilirubinConjugatedRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBilirubinConjugatedRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBilirubinConjugatedQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBilirubinConjugatedQuantity):
            self.measurement_value = HumanBilirubinConjugatedQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBilirubinTotalRecord(ClinicalMeasurementRecord):
    """
    Concentration of total bilirubin in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBilirubinTotalRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBilirubinTotalRecord"
    class_name: ClassVar[str] = "HumanBilirubinTotalRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBilirubinTotalRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBilirubinTotalQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBilirubinTotalQuantity):
            self.measurement_value = HumanBilirubinTotalQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBNPRecord(ClinicalMeasurementRecord):
    """
    Concentration of BNP (B-type natriuretic peptide) in blood, typically measured in plasma or whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBNPRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBNPRecord"
    class_name: ClassVar[str] = "HumanBNPRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBNPRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBNPQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBNPQuantity):
            self.measurement_value = HumanBNPQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBloodUreaNitrogenRecord(ClinicalMeasurementRecord):
    """
    Concentration of blood urea nitrogen (BUN) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBloodUreaNitrogenRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBloodUreaNitrogenRecord"
    class_name: ClassVar[str] = "HumanBloodUreaNitrogenRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBloodUreaNitrogenRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBloodUreaNitrogenQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBloodUreaNitrogenQuantity):
            self.measurement_value = HumanBloodUreaNitrogenQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBUNCreatinineRatioRecord(ClinicalMeasurementRecord):
    """
    Ratio of blood urea nitrogen (BUN) to creatinine in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBUNCreatinineRatioRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBUNCreatinineRatioRecord"
    class_name: ClassVar[str] = "HumanBUNCreatinineRatioRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBUNCreatinineRatioRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBUNCreatinineRatioQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBUNCreatinineRatioQuantity):
            self.measurement_value = HumanBUNCreatinineRatioQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCReactiveProteinRecord(ClinicalMeasurementRecord):
    """
    Concentration of C-reactive protein (CRP) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCReactiveProteinRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanCReactiveProteinRecord"
    class_name: ClassVar[str] = "HumanCReactiveProteinRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCReactiveProteinRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCReactiveProteinQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanCReactiveProteinQuantity):
            self.measurement_value = HumanCReactiveProteinQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCReactiveProteinRecord001(HumanCReactiveProteinRecord):
    """
    Concentration of C-reactive protein (CRP) in blood in mg/L, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCReactiveProteinRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanCReactiveProteinRecord001"
    class_name: ClassVar[str] = "HumanCReactiveProteinRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCReactiveProteinRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCReactiveProteinQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCReactiveProteinRecord002(HumanCReactiveProteinRecord):
    """
    Concentration of C-reactive protein (CRP) in blood in mg/dL, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCReactiveProteinRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanCReactiveProteinRecord002"
    class_name: ClassVar[str] = "HumanCReactiveProteinRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCReactiveProteinRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCReactiveProteinQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCReactiveProteinRecord003(HumanCReactiveProteinRecord):
    """
    Concentration of C-reactive protein (CRP) in blood in ug/mL, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCReactiveProteinRecord003"]
    class_class_curie: ClassVar[str] = "cms:HumanCReactiveProteinRecord003"
    class_name: ClassVar[str] = "HumanCReactiveProteinRecord003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCReactiveProteinRecord003

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCReactiveProteinQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoronaryArteryCalciumScoreRecord(ClinicalMeasurementRecord):
    """
    Coronary artery calcium (CAC) Agatston score derived from a non-contrast cardiac CT scan
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CoronaryArteryCalciumScoreRecord"]
    class_class_curie: ClassVar[str] = "cms:CoronaryArteryCalciumScoreRecord"
    class_name: ClassVar[str] = "CoronaryArteryCalciumScoreRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CoronaryArteryCalciumScoreRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "CoronaryArteryCalciumScoreQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, CoronaryArteryCalciumScoreQuantity):
            self.measurement_value = CoronaryArteryCalciumScoreQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoronaryArteryCalciumVolumeRecord(ClinicalMeasurementRecord):
    """
    Volume of coronary artery calcium in the arteries of the heart as measured by CT scan, reported in mm³
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CoronaryArteryCalciumVolumeRecord"]
    class_class_curie: ClassVar[str] = "cms:CoronaryArteryCalciumVolumeRecord"
    class_name: ClassVar[str] = "CoronaryArteryCalciumVolumeRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CoronaryArteryCalciumVolumeRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "CoronaryArteryCalciumVolumeQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, CoronaryArteryCalciumVolumeQuantity):
            self.measurement_value = CoronaryArteryCalciumVolumeQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CarotidIntimamediaThicknessRecord(ClinicalMeasurementRecord):
    """
    Carotid intima-media thickness (IMT) measured as the thickness of the inner two layers of the carotid artery wall
    using B-mode ultrasound
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CarotidIntimamediaThicknessRecord"]
    class_class_curie: ClassVar[str] = "cms:CarotidIntimamediaThicknessRecord"
    class_name: ClassVar[str] = "CarotidIntimamediaThicknessRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CarotidIntimamediaThicknessRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "CarotidIntimamediaThicknessQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, CarotidIntimamediaThicknessQuantity):
            self.measurement_value = CarotidIntimamediaThicknessQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CarotidStenosisLeftRecord(ClinicalMeasurementRecord):
    """
    Degree of stenosis in the left carotid artery as a percentage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CarotidStenosisLeftRecord"]
    class_class_curie: ClassVar[str] = "cms:CarotidStenosisLeftRecord"
    class_name: ClassVar[str] = "CarotidStenosisLeftRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CarotidStenosisLeftRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "CarotidStenosisQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, CarotidStenosisQuantity):
            self.measurement_value = CarotidStenosisQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CarotidStenosisRightRecord(ClinicalMeasurementRecord):
    """
    Degree of stenosis in the right carotid artery as a percentage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CarotidStenosisRightRecord"]
    class_class_curie: ClassVar[str] = "cms:CarotidStenosisRightRecord"
    class_name: ClassVar[str] = "CarotidStenosisRightRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CarotidStenosisRightRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "CarotidStenosisQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, CarotidStenosisQuantity):
            self.measurement_value = CarotidStenosisQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCD40BloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of CD40 (cluster of differentiation antigen 40) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCD40BloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanCD40BloodRecord"
    class_name: ClassVar[str] = "HumanCD40BloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCD40BloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCD40BloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanCD40BloodQuantity):
            self.measurement_value = HumanCD40BloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CESDScoreRecord(ClinicalMeasurementRecord):
    """
    Score from the CES-D (Center for Epidemiological Studies Depression Scale) self-report questionnaire
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CESDScoreRecord"]
    class_class_curie: ClassVar[str] = "cms:CESDScoreRecord"
    class_name: ClassVar[str] = "CESDScoreRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CESDScoreRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "CESDScoreQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, CESDScoreQuantity):
            self.measurement_value = CESDScoreQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanChlorideBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of chloride in blood (serum chloride), typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanChlorideBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanChlorideBloodRecord"
    class_name: ClassVar[str] = "HumanChlorideBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanChlorideBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanChlorideBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanChlorideBloodQuantity):
            self.measurement_value = HumanChlorideBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanChlorideBloodRecord001(HumanChlorideBloodRecord):
    """
    Concentration of chloride in blood in mmol/L (serum chloride), typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanChlorideBloodRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanChlorideBloodRecord001"
    class_name: ClassVar[str] = "HumanChlorideBloodRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanChlorideBloodRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanChlorideBloodQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanChlorideBloodRecord002(HumanChlorideBloodRecord):
    """
    Concentration of chloride in blood in mmol/dL (serum chloride), typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanChlorideBloodRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanChlorideBloodRecord002"
    class_name: ClassVar[str] = "HumanChlorideBloodRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanChlorideBloodRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanChlorideBloodQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCreatinineBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of creatinine in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCreatinineBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanCreatinineBloodRecord"
    class_name: ClassVar[str] = "HumanCreatinineBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCreatinineBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCreatinineBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanCreatinineBloodQuantity):
            self.measurement_value = HumanCreatinineBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCystatinCBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of cystatin C in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCystatinCBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanCystatinCBloodRecord"
    class_name: ClassVar[str] = "HumanCystatinCBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCystatinCBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanCystatinCBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanCystatinCBloodQuantity):
            self.measurement_value = HumanCystatinCBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanDDimerRecord(ClinicalMeasurementRecord):
    """
    Concentration of D-dimer in blood, measured in whole blood or plasma in fibrinogen-equivalent units (FEU)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanDDimerRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanDDimerRecord"
    class_name: ClassVar[str] = "HumanDDimerRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanDDimerRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanDDimerQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanDDimerQuantity):
            self.measurement_value = HumanDDimerQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanDDimerRecord001(HumanDDimerRecord):
    """
    Concentration of D-dimer in blood, measured in whole blood or plasma in fibrinogen-equivalent units (FEU) in ug/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanDDimerRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanDDimerRecord001"
    class_name: ClassVar[str] = "HumanDDimerRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanDDimerRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanDDimerQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanDDimerRecord002(HumanDDimerRecord):
    """
    Concentration of D-dimer in blood, measured in whole blood or plasma in fibrinogen-equivalent units (FEU) in ng/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanDDimerRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanDDimerRecord002"
    class_name: ClassVar[str] = "HumanDDimerRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanDDimerRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanDDimerQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanDiastolicBloodPressureRecord(ClinicalMeasurementRecord):
    """
    Measurement of pressure in the arteries when the heart is at rest between beats (the bottom number in a blood
    pressure reading)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanDiastolicBloodPressureRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanDiastolicBloodPressureRecord"
    class_name: ClassVar[str] = "HumanDiastolicBloodPressureRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanDiastolicBloodPressureRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanDiastolicBloodPressureQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanDiastolicBloodPressureQuantity):
            self.measurement_value = HumanDiastolicBloodPressureQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBloodPressureRecord(ClinicalMeasurementRecord):
    """
    Measurement of pressure in the arteries when the heart pumps blood (top number) and when the heart is at rest
    between beats (bottom number). Typically represented as a fraction rather than a decimal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBloodPressureRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBloodPressureRecord"
    class_name: ClassVar[str] = "HumanBloodPressureRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBloodPressureRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, Quantity] = None
    age_at_measurement: Union[dict, Quantity] = None

@dataclass(repr=False)
class HumanESelectinBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of E-selectin in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanESelectinBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanESelectinBloodRecord"
    class_name: ClassVar[str] = "HumanESelectinBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanESelectinBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanESelectinBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanESelectinBloodQuantity):
            self.measurement_value = HumanESelectinBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanEstimatedGFRRecord(ClinicalMeasurementRecord):
    """
    Estimated glomerular filtration rate (eGFR) calculated from serum creatinine and/or cystatin C, age, and sex using
    an estimating equation such as CKD-EPI or MDRD
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanEstimatedGFRRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanEstimatedGFRRecord"
    class_name: ClassVar[str] = "HumanEstimatedGFRRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanEstimatedGFRRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanEstimatedGFRQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanEstimatedGFRQuantity):
            self.measurement_value = HumanEstimatedGFRQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanEosinophilCountRecord(ClinicalMeasurementRecord):
    """
    Concentration of eosinophil cells in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanEosinophilCountRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanEosinophilCountRecord"
    class_name: ClassVar[str] = "HumanEosinophilCountRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanEosinophilCountRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanEosinophilCountQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanEosinophilCountQuantity):
            self.measurement_value = HumanEosinophilCountQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFactorVIIRecord(ClinicalMeasurementRecord):
    """
    Factor VII (proconvertin) activity in plasma, expressed as percent of normal
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFactorVIIRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanFactorVIIRecord"
    class_name: ClassVar[str] = "HumanFactorVIIRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFactorVIIRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFactorVIIQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanFactorVIIQuantity):
            self.measurement_value = HumanFactorVIIQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFactorVIIIRecord(ClinicalMeasurementRecord):
    """
    Factor VIII activity in plasma, expressed in IU/mL
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFactorVIIIRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanFactorVIIIRecord"
    class_name: ClassVar[str] = "HumanFactorVIIIRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFactorVIIIRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFactorVIIIQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanFactorVIIIQuantity):
            self.measurement_value = HumanFactorVIIIQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFastingGlucoseRecord(ClinicalMeasurementRecord):
    """
    Concentration of glucose in blood after fasting for a set period, typically 8–12 hours
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFastingGlucoseRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanFastingGlucoseRecord"
    class_name: ClassVar[str] = "HumanFastingGlucoseRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFastingGlucoseRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFastingGlucoseQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanFastingGlucoseQuantity):
            self.measurement_value = HumanFastingGlucoseQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFastingGlucoseRecord001(HumanFastingGlucoseRecord):
    """
    Concentration of glucose (mg/dL) in blood after fasting for a set period, typically 8–12 hours
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFastingGlucoseRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanFastingGlucoseRecord001"
    class_name: ClassVar[str] = "HumanFastingGlucoseRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFastingGlucoseRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFastingGlucoseQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFastingGlucoseRecord002(HumanFastingGlucoseRecord):
    """
    Concentration of glucose (mmol/L) in blood after fasting for a set period, typically 8–12 hours
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFastingGlucoseRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanFastingGlucoseRecord002"
    class_name: ClassVar[str] = "HumanFastingGlucoseRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFastingGlucoseRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFastingGlucoseQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFerritinRecord(ClinicalMeasurementRecord):
    """
    Concentration of ferritin in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFerritinRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanFerritinRecord"
    class_name: ClassVar[str] = "HumanFerritinRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFerritinRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFerritinQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanFerritinQuantity):
            self.measurement_value = HumanFerritinQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFEV1FVCRatioRecord(ClinicalMeasurementRecord):
    """
    Ratio of the forced expiratory volume in one second (FEV1) to the forced vital capacity (FVC), expressed as a
    percentage or ratio and measured before bronchodilator administration
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFEV1FVCRatioRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanFEV1FVCRatioRecord"
    class_name: ClassVar[str] = "HumanFEV1FVCRatioRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFEV1FVCRatioRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFEV1FVCRatioQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanFEV1FVCRatioQuantity):
            self.measurement_value = HumanFEV1FVCRatioQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFEV1FVCRatioRecord001(HumanFEV1FVCRatioRecord):
    """
    Ratio of the forced expiratory volume in one second (FEV1) to the forced vital capacity (FVC), expressed as a
    percentage or ratio and measured before bronchodilator administration - given as a ratio
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFEV1FVCRatioRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanFEV1FVCRatioRecord001"
    class_name: ClassVar[str] = "HumanFEV1FVCRatioRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFEV1FVCRatioRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFEV1FVCRatioQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFEV1FVCRatioRecord002(HumanFEV1FVCRatioRecord):
    """
    Ratio of the forced expiratory volume in one second (FEV1) to the forced vital capacity (FVC), expressed as a
    percentage or ratio and measured before bronchodilator administration - given as a percentage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFEV1FVCRatioRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanFEV1FVCRatioRecord002"
    class_name: ClassVar[str] = "HumanFEV1FVCRatioRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFEV1FVCRatioRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFEV1FVCRatioQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPredictedFEV1FVCRatioRecord(ClinicalMeasurementRecord):
    """
    Predicted ratio of the forced expiratory volume in one second (FEV1) to the forced vital capacity (FVC).
    Predictions are based on a reference equation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPredictedFEV1FVCRatioRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanPredictedFEV1FVCRatioRecord"
    class_name: ClassVar[str] = "HumanPredictedFEV1FVCRatioRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPredictedFEV1FVCRatioRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPredictedFEV1FVCRatioQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPredictedFEV1FVCRatioQuantity):
            self.measurement_value = HumanPredictedFEV1FVCRatioQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPercentPredictedFEV1FVCRatioRecord(ClinicalMeasurementRecord):
    """
    Predictof the predicted ratio of the forced expiratory volume in one second (FEV1) to the forced vital capacity
    (FVC) that is achieved by the patient.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPercentPredictedFEV1FVCRatioRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanPercentPredictedFEV1FVCRatioRecord"
    class_name: ClassVar[str] = "HumanPercentPredictedFEV1FVCRatioRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPercentPredictedFEV1FVCRatioRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPercentPredictedFEV1FVCRatioQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPercentPredictedFEV1FVCRatioQuantity):
            self.measurement_value = HumanPercentPredictedFEV1FVCRatioQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFibrinogenRecord(ClinicalMeasurementRecord):
    """
    Concentration of fibrinogen in plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFibrinogenRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanFibrinogenRecord"
    class_name: ClassVar[str] = "HumanFibrinogenRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFibrinogenRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanFibrinogenQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanFibrinogenQuantity):
            self.measurement_value = HumanFibrinogenQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FruitConsumptionRecord(ClinicalMeasurementRecord):
    """
    Servings of fruits consumed per week (includes fruit and fruit juice)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["FruitConsumptionRecord"]
    class_class_curie: ClassVar[str] = "cms:FruitConsumptionRecord"
    class_name: ClassVar[str] = "FruitConsumptionRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.FruitConsumptionRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "FruitConsumptionQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, FruitConsumptionQuantity):
            self.measurement_value = FruitConsumptionQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanGFRRecord(ClinicalMeasurementRecord):
    """
    Glomerular filtration rate (GFR) measuring how much blood passes through the glomeruli per minute
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanGFRRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanGFRRecord"
    class_name: ClassVar[str] = "HumanGFRRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanGFRRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanGFRQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanGFRQuantity):
            self.measurement_value = HumanGFRQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanGlucoseBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of glucose in blood, measured in whole blood, serum, or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanGlucoseBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanGlucoseBloodRecord"
    class_name: ClassVar[str] = "HumanGlucoseBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanGlucoseBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanGlucoseBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanGlucoseBloodQuantity):
            self.measurement_value = HumanGlucoseBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHDLRecord(ClinicalMeasurementRecord):
    """
    Concentration of high-density lipoprotein (HDL) cholesterol in blood, typically measured in serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHDLRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanHDLRecord"
    class_name: ClassVar[str] = "HumanHDLRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHDLRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHDLQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanHDLQuantity):
            self.measurement_value = HumanHDLQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHDLRecord001(HumanHDLRecord):
    """
    Concentration of high-density lipoprotein (HDL) cholesterol in blood in mg/dL, typically measured in serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHDLRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanHDLRecord001"
    class_name: ClassVar[str] = "HumanHDLRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHDLRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHDLQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHDLRecord002(HumanHDLRecord):
    """
    Concentration of high-density lipoprotein (HDL) cholesterol in blood in mmol/L, typically measured in serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHDLRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanHDLRecord002"
    class_name: ClassVar[str] = "HumanHDLRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHDLRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHDLQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHeartRateRecord(ClinicalMeasurementRecord):
    """
    Number of times the heart beats per minute (pulse rate)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHeartRateRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanHeartRateRecord"
    class_name: ClassVar[str] = "HumanHeartRateRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHeartRateRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHeartRateQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanHeartRateQuantity):
            self.measurement_value = HumanHeartRateQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHematocritRecord(ClinicalMeasurementRecord):
    """
    Percentage of whole blood volume that consists of red blood cells (packed cell volume)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHematocritRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanHematocritRecord"
    class_name: ClassVar[str] = "HumanHematocritRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHematocritRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHematocritQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanHematocritQuantity):
            self.measurement_value = HumanHematocritQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHemoglobinRecord(ClinicalMeasurementRecord):
    """
    Concentration of hemoglobin in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHemoglobinRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanHemoglobinRecord"
    class_name: ClassVar[str] = "HumanHemoglobinRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHemoglobinRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHemoglobinQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanHemoglobinQuantity):
            self.measurement_value = HumanHemoglobinQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHemoglobinA1cRecord(ClinicalMeasurementRecord):
    """
    Percentage of hemoglobin in red blood cells that has glucose attached to it (HbA1c), reflecting average blood
    glucose over the preceding 2–3 months
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHemoglobinA1cRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanHemoglobinA1cRecord"
    class_name: ClassVar[str] = "HumanHemoglobinA1cRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHemoglobinA1cRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHemoglobinA1cQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanHemoglobinA1cQuantity):
            self.measurement_value = HumanHemoglobinA1cQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHipCircumferenceRecord(ClinicalMeasurementRecord):
    """
    Distance measurement taken around the fullest part of the hips in cm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHipCircumferenceRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanHipCircumferenceRecord"
    class_name: ClassVar[str] = "HumanHipCircumferenceRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHipCircumferenceRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHipCircumferenceQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanHipCircumferenceQuantity):
            self.measurement_value = HumanHipCircumferenceQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHipCircumferenceRecord001(HumanHipCircumferenceRecord):
    """
    Distance measurement taken around the fullest part of the hips in centimeters (cm)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHipCircumferenceRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanHipCircumferenceRecord001"
    class_name: ClassVar[str] = "HumanHipCircumferenceRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHipCircumferenceRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHipCircumferenceQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHipCircumferenceRecord002(HumanHipCircumferenceRecord):
    """
    Distance measurement taken around the fullest part of the hips in inches
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHipCircumferenceRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanHipCircumferenceRecord002"
    class_name: ClassVar[str] = "HumanHipCircumferenceRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHipCircumferenceRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanHipCircumferenceQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanICAM1BloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of intercellular adhesion molecule 1 (ICAM-1) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanICAM1BloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanICAM1BloodRecord"
    class_name: ClassVar[str] = "HumanICAM1BloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanICAM1BloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanICAM1BloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanICAM1BloodQuantity):
            self.measurement_value = HumanICAM1BloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInsulinBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of insulin in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInsulinBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanInsulinBloodRecord"
    class_name: ClassVar[str] = "HumanInsulinBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInsulinBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanInsulinBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanInsulinBloodQuantity):
            self.measurement_value = HumanInsulinBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInsulinBloodRecord001(HumanInsulinBloodRecord):
    """
    Concentration of insulin in blood (pmol/L), typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInsulinBloodRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanInsulinBloodRecord001"
    class_name: ClassVar[str] = "HumanInsulinBloodRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInsulinBloodRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanInsulinBloodQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInsulinBloodRecord002(HumanInsulinBloodRecord):
    """
    Concentration of insulin in blood (u[iU]/mL), typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInsulinBloodRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanInsulinBloodRecord002"
    class_name: ClassVar[str] = "HumanInsulinBloodRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInsulinBloodRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanInsulinBloodQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInterleukin18BloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of interleukin-18 (IL-18) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInterleukin18BloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanInterleukin18BloodRecord"
    class_name: ClassVar[str] = "HumanInterleukin18BloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInterleukin18BloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanInterleukin18BloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanInterleukin18BloodQuantity):
            self.measurement_value = HumanInterleukin18BloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInterleukin1BetaBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of interleukin-1 beta (IL-1β) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInterleukin1BetaBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanInterleukin1BetaBloodRecord"
    class_name: ClassVar[str] = "HumanInterleukin1BetaBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInterleukin1BetaBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanInterleukin1BetaBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanInterleukin1BetaBloodQuantity):
            self.measurement_value = HumanInterleukin1BetaBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInterleukin10BloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of interleukin-10 (IL-10) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInterleukin10BloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanInterleukin10BloodRecord"
    class_name: ClassVar[str] = "HumanInterleukin10BloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInterleukin10BloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanInterleukin10BloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanInterleukin10BloodQuantity):
            self.measurement_value = HumanInterleukin10BloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInterleukin6BloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of interleukin-6 (IL-6) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInterleukin6BloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanInterleukin6BloodRecord"
    class_name: ClassVar[str] = "HumanInterleukin6BloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInterleukin6BloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanInterleukin6BloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanInterleukin6BloodQuantity):
            self.measurement_value = HumanInterleukin6BloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLactateDehydrogenaseRecord(ClinicalMeasurementRecord):
    """
    Activity of lactate dehydrogenase (LDH) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLactateDehydrogenaseRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanLactateDehydrogenaseRecord"
    class_name: ClassVar[str] = "HumanLactateDehydrogenaseRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLactateDehydrogenaseRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanLactateDehydrogenaseQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanLactateDehydrogenaseQuantity):
            self.measurement_value = HumanLactateDehydrogenaseQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLactateBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of lactate in blood, typically measured in whole blood or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLactateBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanLactateBloodRecord"
    class_name: ClassVar[str] = "HumanLactateBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLactateBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanLactateBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanLactateBloodQuantity):
            self.measurement_value = HumanLactateBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLDLRecord(ClinicalMeasurementRecord):
    """
    Concentration of low-density lipoprotein (LDL) cholesterol in blood, typically measured in serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLDLRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanLDLRecord"
    class_name: ClassVar[str] = "HumanLDLRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLDLRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanLDLQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanLDLQuantity):
            self.measurement_value = HumanLDLQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLDLRecord001(HumanLDLRecord):
    """
    Concentration of low-density lipoprotein (LDL) cholesterol in blood, typically measured in serum derived from the
    Friedewald calculation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLDLRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanLDLRecord001"
    class_name: ClassVar[str] = "HumanLDLRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLDLRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanLDLQuantity"] = None

@dataclass(repr=False)
class HumanLymphocyteCountRecord(ClinicalMeasurementRecord):
    """
    Concentration of lymphocytes in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLymphocyteCountRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanLymphocyteCountRecord"
    class_name: ClassVar[str] = "HumanLymphocyteCountRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLymphocyteCountRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanLymphocyteCountQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanLymphocyteCountQuantity):
            self.measurement_value = HumanLymphocyteCountQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLymphocytePercentRecord(ClinicalMeasurementRecord):
    """
    Percent of total leukocytes that are lymphocytes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLymphocytePercentRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanLymphocytePercentRecord"
    class_name: ClassVar[str] = "HumanLymphocytePercentRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLymphocytePercentRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanLymphocytePercentQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanLymphocytePercentQuantity):
            self.measurement_value = HumanLymphocytePercentQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLymphocytePercentRecord001(HumanLymphocytePercentRecord):
    """
    Calculated percent of total leukocytes that are lymphocytes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLymphocytePercentRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanLymphocytePercentRecord001"
    class_name: ClassVar[str] = "HumanLymphocytePercentRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLymphocytePercentRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanLymphocytePercentQuantity"] = None

@dataclass(repr=False)
class HumanLPPLA2MassBloodRecord(ClinicalMeasurementRecord):
    """
    Mass concentration of Lp-PLA2 (lipoprotein-associated phospholipase A2) enzyme in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLPPLA2MassBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanLPPLA2MassBloodRecord"
    class_name: ClassVar[str] = "HumanLPPLA2MassBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLPPLA2MassBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanLPPLA2MassBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanLPPLA2MassBloodQuantity):
            self.measurement_value = HumanLPPLA2MassBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMCP1BloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of monocyte chemoattractant protein-1 (MCP-1 / CCL2) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCP1BloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMCP1BloodRecord"
    class_name: ClassVar[str] = "HumanMCP1BloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCP1BloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMCP1BloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMCP1BloodQuantity):
            self.measurement_value = HumanMCP1BloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMeanArterialPressureRecord(ClinicalMeasurementRecord):
    """
    Average pressure in the arteries throughout one complete cardiac cycle. Can be calculated or measured directly.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMeanArterialPressureRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMeanArterialPressureRecord"
    class_name: ClassVar[str] = "HumanMeanArterialPressureRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMeanArterialPressureRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMeanArterialPressureQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMeanArterialPressureQuantity):
            self.measurement_value = HumanMeanArterialPressureQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMeanArterialPressureRecord001(HumanMeanArterialPressureRecord):
    """
    Average pressure in the arteries throughout one complete cardiac cycle - calculated - (MAP = DBP + 1/3 × [SBP −
    DBP])
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMeanArterialPressureRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanMeanArterialPressureRecord001"
    class_name: ClassVar[str] = "HumanMeanArterialPressureRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMeanArterialPressureRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMeanArterialPressureQuantity"] = None

@dataclass(repr=False)
class HumanMCHRecord(ClinicalMeasurementRecord):
    """
    Average amount of hemoglobin in each red blood cell (MCH - Mean Corpuscular Hemoglobin). This can be calculated
    and returned by a hematology analyzer or calculated separately.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCHRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMCHRecord"
    class_name: ClassVar[str] = "HumanMCHRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCHRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMCHQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMCHQuantity):
            self.measurement_value = HumanMCHQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMCHRecord001(HumanMCHRecord):
    """
    Calculated average amount of hemoglobin in each red blood cell (MCH - Mean Corpuscular Hemoglobin)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCHRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanMCHRecord001"
    class_name: ClassVar[str] = "HumanMCHRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCHRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMCHQuantity"] = None

@dataclass(repr=False)
class HumanMCHCRecord(ClinicalMeasurementRecord):
    """
    Average concentration of hemoglobin within a single red blood cell (MCHC - mean corpuscular hemoglobin
    concentration). This value can be calculated and returned by an analyzer or calculated separately.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCHCRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMCHCRecord"
    class_name: ClassVar[str] = "HumanMCHCRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCHCRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMCHCQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMCHCQuantity):
            self.measurement_value = HumanMCHCQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMCHCRecord001(HumanMCHCRecord):
    """
    Calculated average concentration of hemoglobin within a single red blood cell (MCHC - mean corpuscular hemoglobin
    concentration)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCHCRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanMCHCRecord001"
    class_name: ClassVar[str] = "HumanMCHCRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCHCRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMCHCQuantity"] = None

@dataclass(repr=False)
class HumanMCVRecord(ClinicalMeasurementRecord):
    """
    Average size/volume of a red blood cell (MCV - mean corpuscular volume). This value is measured directly by
    analyzers, but older data may have been manually calculated.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCVRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMCVRecord"
    class_name: ClassVar[str] = "HumanMCVRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCVRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMCVQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMCVQuantity):
            self.measurement_value = HumanMCVQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMCVRecord001(HumanMCVRecord):
    """
    Calculated average size/volume of a red blood cell (MCV - mean corpuscular volume).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCVRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanMCVRecord001"
    class_name: ClassVar[str] = "HumanMCVRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCVRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMCVQuantity"] = None

@dataclass(repr=False)
class HumanMPVRecord(ClinicalMeasurementRecord):
    """
    Average size/volume of a platelet (MPV - mean platelet volume)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMPVRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMPVRecord"
    class_name: ClassVar[str] = "HumanMPVRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMPVRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMPVQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMPVQuantity):
            self.measurement_value = HumanMPVQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMMP9BloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of matrix metalloproteinase-9 (MMP-9) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMMP9BloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMMP9BloodRecord"
    class_name: ClassVar[str] = "HumanMMP9BloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMMP9BloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMMP9BloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMMP9BloodQuantity):
            self.measurement_value = HumanMMP9BloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMonocyteCountRecord(ClinicalMeasurementRecord):
    """
    Concentration of monocyte cells in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMonocyteCountRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMonocyteCountRecord"
    class_name: ClassVar[str] = "HumanMonocyteCountRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMonocyteCountRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMonocyteCountQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMonocyteCountQuantity):
            self.measurement_value = HumanMonocyteCountQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMyeloperoxidaseBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of myeloperoxidase (MPO) in blood, typically measured in plasma or serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMyeloperoxidaseBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanMyeloperoxidaseBloodRecord"
    class_name: ClassVar[str] = "HumanMyeloperoxidaseBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMyeloperoxidaseBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanMyeloperoxidaseBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanMyeloperoxidaseBloodQuantity):
            self.measurement_value = HumanMyeloperoxidaseBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanNeutrophilCountRecord(ClinicalMeasurementRecord):
    """
    Concentration of neutrophil cells in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanNeutrophilCountRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanNeutrophilCountRecord"
    class_name: ClassVar[str] = "HumanNeutrophilCountRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanNeutrophilCountRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanNeutrophilCountQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanNeutrophilCountQuantity):
            self.measurement_value = HumanNeutrophilCountQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanNeutrophilPercentRecord(ClinicalMeasurementRecord):
    """
    Percent of total leukocytes that are neutrophils
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanNeutrophilPercentRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanNeutrophilPercentRecord"
    class_name: ClassVar[str] = "HumanNeutrophilPercentRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanNeutrophilPercentRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanNeutrophilPercentQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanNeutrophilPercentQuantity):
            self.measurement_value = HumanNeutrophilPercentQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanNeutrophilPercentRecord001(HumanNeutrophilPercentRecord):
    """
    Calculated percent of total leukocytes that are neutrophils
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanNeutrophilPercentRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanNeutrophilPercentRecord001"
    class_name: ClassVar[str] = "HumanNeutrophilPercentRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanNeutrophilPercentRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanNeutrophilPercentQuantity"] = None

@dataclass(repr=False)
class HumanNTproBNPRecord(ClinicalMeasurementRecord):
    """
    Concentration of NT-proBNP (N-terminal prohormone of brain natriuretic peptide) in blood, typically measured in
    serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanNTproBNPRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanNTproBNPRecord"
    class_name: ClassVar[str] = "HumanNTproBNPRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanNTproBNPRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanNTproBNPQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanNTproBNPQuantity):
            self.measurement_value = HumanNTproBNPQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanOsteoprotegerinBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of osteoprotegerin (OPG) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanOsteoprotegerinBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanOsteoprotegerinBloodRecord"
    class_name: ClassVar[str] = "HumanOsteoprotegerinBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanOsteoprotegerinBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanOsteoprotegerinBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanOsteoprotegerinBloodQuantity):
            self.measurement_value = HumanOsteoprotegerinBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPSelectinBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of P-selectin in blood, typically measured in plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPSelectinBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanPSelectinBloodRecord"
    class_name: ClassVar[str] = "HumanPSelectinBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPSelectinBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPSelectinBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPSelectinBloodQuantity):
            self.measurement_value = HumanPSelectinBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPlateletCountRecord(ClinicalMeasurementRecord):
    """
    Concentration of platelets in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPlateletCountRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanPlateletCountRecord"
    class_name: ClassVar[str] = "HumanPlateletCountRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPlateletCountRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPlateletCountQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPlateletCountQuantity):
            self.measurement_value = HumanPlateletCountQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPotassiumBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of potassium in blood, typically measured in whole blood or serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPotassiumBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanPotassiumBloodRecord"
    class_name: ClassVar[str] = "HumanPotassiumBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPotassiumBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPotassiumBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPotassiumBloodQuantity):
            self.measurement_value = HumanPotassiumBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPRIntervalRecord(ClinicalMeasurementRecord):
    """
    Time for electrical impulses to travel from the atria to the ventricles of the heart as measured by ECG/EKG, in
    milliseconds
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPRIntervalRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanPRIntervalRecord"
    class_name: ClassVar[str] = "HumanPRIntervalRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPRIntervalRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanPRIntervalQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanPRIntervalQuantity):
            self.measurement_value = HumanPRIntervalQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanQRSIntervalRecord(ClinicalMeasurementRecord):
    """
    Time that elapses from the beginning of the Q wave to the end of the S wave on an ECG/EKG, in milliseconds
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanQRSIntervalRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanQRSIntervalRecord"
    class_name: ClassVar[str] = "HumanQRSIntervalRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanQRSIntervalRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanQRSIntervalQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanQRSIntervalQuantity):
            self.measurement_value = HumanQRSIntervalQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanQTIntervalRecord(ClinicalMeasurementRecord):
    """
    Time for the ventricles of the heart to depolarize and repolarize as measured by ECG/EKG, in milliseconds
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanQTIntervalRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanQTIntervalRecord"
    class_name: ClassVar[str] = "HumanQTIntervalRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanQTIntervalRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanQTIntervalQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanQTIntervalQuantity):
            self.measurement_value = HumanQTIntervalQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanRBCCountRecord(ClinicalMeasurementRecord):
    """
    Concentration of red blood cells in whole blood - RBC
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanRBCCountRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanRBCCountRecord"
    class_name: ClassVar[str] = "HumanRBCCountRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanRBCCountRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanRBCCountQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanRBCCountQuantity):
            self.measurement_value = HumanRBCCountQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanRDWRecord(ClinicalMeasurementRecord):
    """
    Measure of the variation in size and volume of red blood cells (RDW - red cell distribution width), expressed as a
    coefficient of variation percentage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanRDWRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanRDWRecord"
    class_name: ClassVar[str] = "HumanRDWRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanRDWRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanRDWQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanRDWQuantity):
            self.measurement_value = HumanRDWQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanSleepDurationRecord(ClinicalMeasurementRecord):
    """
    Cumulative amount of time spent sleeping per night, in hours
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanSleepDurationRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanSleepDurationRecord"
    class_name: ClassVar[str] = "HumanSleepDurationRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanSleepDurationRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanSleepDurationQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanSleepDurationQuantity):
            self.measurement_value = HumanSleepDurationQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanSodiumBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of sodium in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanSodiumBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanSodiumBloodRecord"
    class_name: ClassVar[str] = "HumanSodiumBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanSodiumBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanSodiumBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanSodiumBloodQuantity):
            self.measurement_value = HumanSodiumBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SodiumIntakeRecord(ClinicalMeasurementRecord):
    """
    Mass of sodium consumed by an individual per day
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["SodiumIntakeRecord"]
    class_class_curie: ClassVar[str] = "cms:SodiumIntakeRecord"
    class_name: ClassVar[str] = "SodiumIntakeRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.SodiumIntakeRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "SodiumIntakeQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, SodiumIntakeQuantity):
            self.measurement_value = SodiumIntakeQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanSpO2Record(ClinicalMeasurementRecord):
    """
    Percentage of oxygen-carrying hemoglobin in the blood compared to the total amount of hemoglobin (oxygen
    saturation / SpO2)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanSpO2Record"]
    class_class_curie: ClassVar[str] = "cms:HumanSpO2Record"
    class_name: ClassVar[str] = "HumanSpO2Record"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanSpO2Record

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanSpO2Quantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanSpO2Quantity):
            self.measurement_value = HumanSpO2Quantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanSystolicBloodPressureRecord(ClinicalMeasurementRecord):
    """
    Measurement of pressure in the arteries when the heart pumps blood (the top number in a blood pressure reading)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanSystolicBloodPressureRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanSystolicBloodPressureRecord"
    class_name: ClassVar[str] = "HumanSystolicBloodPressureRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanSystolicBloodPressureRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanSystolicBloodPressureQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanSystolicBloodPressureQuantity):
            self.measurement_value = HumanSystolicBloodPressureQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyTemperatureRecord(ClinicalMeasurementRecord):
    """
    An individual's internal body temperature in degrees Celsius
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyTemperatureRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyTemperatureRecord"
    class_name: ClassVar[str] = "HumanBodyTemperatureRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyTemperatureRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanBodyTemperatureQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanBodyTemperatureQuantity):
            self.measurement_value = HumanBodyTemperatureQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTNFAlphaBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of TNF-alpha (tumor necrosis factor alpha) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTNFAlphaBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanTNFAlphaBloodRecord"
    class_name: ClassVar[str] = "HumanTNFAlphaBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTNFAlphaBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanTNFAlphaBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanTNFAlphaBloodQuantity):
            self.measurement_value = HumanTNFAlphaBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTNFAlphaR1BloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of TNF receptor 1 (TNFR1 / TNFRSF1A) in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTNFAlphaR1BloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanTNFAlphaR1BloodRecord"
    class_name: ClassVar[str] = "HumanTNFAlphaR1BloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTNFAlphaR1BloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanTNFAlphaR1BloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanTNFAlphaR1BloodQuantity):
            self.measurement_value = HumanTNFAlphaR1BloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTotalCholesterolRecord(ClinicalMeasurementRecord):
    """
    Concentration of all cholesterol in blood (total cholesterol), including both HDL and LDL, typically measured in
    serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTotalCholesterolRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanTotalCholesterolRecord"
    class_name: ClassVar[str] = "HumanTotalCholesterolRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTotalCholesterolRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanTotalCholesterolQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanTotalCholesterolQuantity):
            self.measurement_value = HumanTotalCholesterolQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTotalCholesterolRecord001(ClinicalMeasurementRecord):
    """
    Concentration of all cholesterol in blood (total cholesterol in mg/dL), including both HDL and LDL, typically
    measured in serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTotalCholesterolRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanTotalCholesterolRecord001"
    class_name: ClassVar[str] = "HumanTotalCholesterolRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTotalCholesterolRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    measurement_value: Union[dict, Quantity] = None
    age_at_measurement: Union[dict, Quantity] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTotalCholesterolRecord002(HumanTotalCholesterolRecord):
    """
    Concentration of all cholesterol in blood (total cholesterol in mmol/L), including both HDL and LDL, typically
    measured in serum
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTotalCholesterolRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanTotalCholesterolRecord002"
    class_name: ClassVar[str] = "HumanTotalCholesterolRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTotalCholesterolRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanTotalCholesterolQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTriglyceridesBloodRecord(ClinicalMeasurementRecord):
    """
    Concentration of triglycerides in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTriglyceridesBloodRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanTriglyceridesBloodRecord"
    class_name: ClassVar[str] = "HumanTriglyceridesBloodRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTriglyceridesBloodRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanTriglyceridesBloodQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanTriglyceridesBloodQuantity):
            self.measurement_value = HumanTriglyceridesBloodQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTriglyceridesBloodRecord001(HumanTriglyceridesBloodRecord):
    """
    Concentration of triglycerides in blood in mg/dL, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTriglyceridesBloodRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanTriglyceridesBloodRecord001"
    class_name: ClassVar[str] = "HumanTriglyceridesBloodRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTriglyceridesBloodRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanTriglyceridesBloodQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTriglyceridesBloodRecord002(HumanTriglyceridesBloodRecord):
    """
    Concentration of triglycerides in blood in mmol/L, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTriglyceridesBloodRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanTriglyceridesBloodRecord002"
    class_name: ClassVar[str] = "HumanTriglyceridesBloodRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTriglyceridesBloodRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanTriglyceridesBloodQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTroponinRecord(ClinicalMeasurementRecord):
    """
    Concentration of all types of troponin in blood, typically measured in serum or plasma
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTroponinRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanTroponinRecord"
    class_name: ClassVar[str] = "HumanTroponinRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTroponinRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanTroponinQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanTroponinQuantity):
            self.measurement_value = HumanTroponinQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VegetableConsumptionRecord(ClinicalMeasurementRecord):
    """
    Servings of vegetables consumed per week
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["VegetableConsumptionRecord"]
    class_class_curie: ClassVar[str] = "cms:VegetableConsumptionRecord"
    class_name: ClassVar[str] = "VegetableConsumptionRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.VegetableConsumptionRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "VegetableConsumptionQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, VegetableConsumptionQuantity):
            self.measurement_value = VegetableConsumptionQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanVonWillebrandFactorRecord(ClinicalMeasurementRecord):
    """
    Von Willebrand factor (VWF) antigen or activity in blood, expressed as percent of normal
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanVonWillebrandFactorRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanVonWillebrandFactorRecord"
    class_name: ClassVar[str] = "HumanVonWillebrandFactorRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanVonWillebrandFactorRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanVonWillebrandFactorQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanVonWillebrandFactorQuantity):
            self.measurement_value = HumanVonWillebrandFactorQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanWaistCircumferenceRecord(ClinicalMeasurementRecord):
    """
    Distance measurement taken around the waist, just above the hip bone
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanWaistCircumferenceRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanWaistCircumferenceRecord"
    class_name: ClassVar[str] = "HumanWaistCircumferenceRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanWaistCircumferenceQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanWaistCircumferenceQuantity):
            self.measurement_value = HumanWaistCircumferenceQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanWaistCircumferenceRecord001(HumanWaistCircumferenceRecord):
    """
    Distance measurement taken around the waist, just above the hip bone, in cm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanWaistCircumferenceRecord001"]
    class_class_curie: ClassVar[str] = "cms:HumanWaistCircumferenceRecord001"
    class_name: ClassVar[str] = "HumanWaistCircumferenceRecord001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceRecord001

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanWaistCircumferenceQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanWaistCircumferenceRecord002(HumanWaistCircumferenceRecord):
    """
    Distance measurement taken around the waist, just above the hip bone, in mm
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanWaistCircumferenceRecord002"]
    class_class_curie: ClassVar[str] = "cms:HumanWaistCircumferenceRecord002"
    class_name: ClassVar[str] = "HumanWaistCircumferenceRecord002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceRecord002

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanWaistCircumferenceQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanWaistCircumferenceRecord003(HumanWaistCircumferenceRecord):
    """
    Distance measurement taken around the waist, just above the hip bone, in inches
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanWaistCircumferenceRecord003"]
    class_class_curie: ClassVar[str] = "cms:HumanWaistCircumferenceRecord003"
    class_name: ClassVar[str] = "HumanWaistCircumferenceRecord003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceRecord003

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanWaistCircumferenceQuantity"] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanWaistHipRatioRecord(ClinicalMeasurementRecord):
    """
    Ratio of the circumference of the waist to the circumference of the hips
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanWaistHipRatioRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanWaistHipRatioRecord"
    class_name: ClassVar[str] = "HumanWaistHipRatioRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanWaistHipRatioRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanWaistHipRatioQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanWaistHipRatioQuantity):
            self.measurement_value = HumanWaistHipRatioQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanWhiteBloodCellCountRecord(ClinicalMeasurementRecord):
    """
    Concentration of white blood cells in whole blood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanWhiteBloodCellCountRecord"]
    class_class_curie: ClassVar[str] = "cms:HumanWhiteBloodCellCountRecord"
    class_name: ClassVar[str] = "HumanWhiteBloodCellCountRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanWhiteBloodCellCountRecord

    subject_identifier: Union[str, URIorCURIE] = None
    measurement_type: Union[str, URIorCURIE] = None
    age_at_measurement: Union[dict, Quantity] = None
    measurement_value: Union[dict, "HumanWBCCountQuantity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, HumanWBCCountQuantity):
            self.measurement_value = HumanWBCCountQuantity(**as_dict(self.measurement_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AsthmaStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of asthma in the patient/participant or their
    blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AsthmaStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:AsthmaStatusRecord"
    class_name: ClassVar[str] = "AsthmaStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AsthmaStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HeartFailureStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of heart failure in the patient/participant or
    their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HeartFailureStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:HeartFailureStatusRecord"
    class_name: ClassVar[str] = "HeartFailureStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HeartFailureStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObesityStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of obesity in the patient/participant or their
    blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ObesityStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:ObesityStatusRecord"
    class_name: ClassVar[str] = "ObesityStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ObesityStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtrialFibrillationStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of atrial fibrillation in the patient/participant
    or their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AtrialFibrillationStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:AtrialFibrillationStatusRecord"
    class_name: ClassVar[str] = "AtrialFibrillationStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AtrialFibrillationStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnginaStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of angina in the patient/participant or their
    blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AnginaStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:AnginaStatusRecord"
    class_name: ClassVar[str] = "AnginaStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AnginaStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CardiovascularDiseaseStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of cardiovascular disease in the
    patient/participant or their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CardiovascularDiseaseStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:CardiovascularDiseaseStatusRecord"
    class_name: ClassVar[str] = "CardiovascularDiseaseStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CardiovascularDiseaseStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CarotidPlaqueStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of carotid plaque in the patient/participant or
    their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CarotidPlaqueStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:CarotidPlaqueStatusRecord"
    class_name: ClassVar[str] = "CarotidPlaqueStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CarotidPlaqueStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class COPDStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of COPD in the patient/participant or their blood
    relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["COPDStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:COPDStatusRecord"
    class_name: ClassVar[str] = "COPDStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.COPDStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiabetesStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of diabetes in the patient/participant or their
    blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["DiabetesStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:DiabetesStatusRecord"
    class_name: ClassVar[str] = "DiabetesStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.DiabetesStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StrokeStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of atrial fibrillation in the patient/participant
    or their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["StrokeStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:StrokeStatusRecord"
    class_name: ClassVar[str] = "StrokeStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.StrokeStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HeartDiseaseStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of heart disease in the patient/participant or
    their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HeartDiseaseStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:HeartDiseaseStatusRecord"
    class_name: ClassVar[str] = "HeartDiseaseStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HeartDiseaseStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MyocardialInfarctionStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of myocardial infarction in the
    patient/participant or their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["MyocardialInfarctionStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:MyocardialInfarctionStatusRecord"
    class_name: ClassVar[str] = "MyocardialInfarctionStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.MyocardialInfarctionStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HypertensionStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of hypertension in the patient/participant or
    their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HypertensionStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:HypertensionStatusRecord"
    class_name: ClassVar[str] = "HypertensionStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HypertensionStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LeftVentricularHypertrophyStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of left ventricular hypertrophy in the
    patient/participant or their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["LeftVentricularHypertrophyStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:LeftVentricularHypertrophyStatusRecord"
    class_name: ClassVar[str] = "LeftVentricularHypertrophyStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.LeftVentricularHypertrophyStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PeripheralArterialDiseaseStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of peripheral arterial disease in the
    patient/participant or their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["PeripheralArterialDiseaseStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:PeripheralArterialDiseaseStatusRecord"
    class_name: ClassVar[str] = "PeripheralArterialDiseaseStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.PeripheralArterialDiseaseStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SleepApneaStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of sleep apnea in the patient/participant or their
    blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["SleepApneaStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:SleepApneaStatusRecord"
    class_name: ClassVar[str] = "SleepApneaStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.SleepApneaStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValvularHeartDiseaseStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of valvular heart disease in the
    patient/participant or their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ValvularHeartDiseaseStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:ValvularHeartDiseaseStatusRecord"
    class_name: ClassVar[str] = "ValvularHeartDiseaseStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ValvularHeartDiseaseStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VenousThromboembolismStatusRecord(ConditionStatusRecord):
    """
    Record suggesting the current or historical presence or absence of venous thromboembolism in the
    patient/participant or their blood relatives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["VenousThromboembolismStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:VenousThromboembolismStatusRecord"
    class_name: ClassVar[str] = "VenousThromboembolismStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.VenousThromboembolismStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_condition_record: Union[dict, Quantity] = None
    condition_status: Union[str, "HistoricalStatusEnum"] = None
    relationship_to_participant: Union[str, "FamilyRelationshipEnum"] = None
    condition_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, URIorCURIE):
            self.condition_type = URIorCURIE(self.condition_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AspirinStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to aspirin
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AspirinStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:AspirinStatusRecord"
    class_name: ClassVar[str] = "AspirinStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AspirinStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BetaBlockerStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to beta blockers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["BetaBlockerStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:BetaBlockerStatusRecord"
    class_name: ClassVar[str] = "BetaBlockerStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.BetaBlockerStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiabetesMedicationStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to diabetes medication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["DiabetesMedicationStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:DiabetesMedicationStatusRecord"
    class_name: ClassVar[str] = "DiabetesMedicationStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.DiabetesMedicationStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HypertensionMedicationStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to hypertension medication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HypertensionMedicationStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:HypertensionMedicationStatusRecord"
    class_name: ClassVar[str] = "HypertensionMedicationStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HypertensionMedicationStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AceInhibitorStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to ACE inhibitors
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AceInhibitorStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:AceInhibitorStatusRecord"
    class_name: ClassVar[str] = "AceInhibitorStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AceInhibitorStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AldosteroneReceptorBlockerStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to Aldosterone receptor blockers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AldosteroneReceptorBlockerStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:AldosteroneReceptorBlockerStatusRecord"
    class_name: ClassVar[str] = "AldosteroneReceptorBlockerStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AldosteroneReceptorBlockerStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlphaBlockerStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to Alpha blockers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AlphaBlockerStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:AlphaBlockerStatusRecord"
    class_name: ClassVar[str] = "AlphaBlockerStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AlphaBlockerStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AngiotensinReceptorBlockerStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to Angiotensin receptor blockers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AngiotensinReceptorBlockerStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:AngiotensinReceptorBlockerStatusRecord"
    class_name: ClassVar[str] = "AngiotensinReceptorBlockerStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AngiotensinReceptorBlockerStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalciumChannelBlockerStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to Calcium channel blockers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CalciumChannelBlockerStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:CalciumChannelBlockerStatusRecord"
    class_name: ClassVar[str] = "CalciumChannelBlockerStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CalciumChannelBlockerStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CentrallyActingAgentsStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to centrally acting agents
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CentrallyActingAgentsStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:CentrallyActingAgentsStatusRecord"
    class_name: ClassVar[str] = "CentrallyActingAgentsStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CentrallyActingAgentsStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiureticsStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to diuretics
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["DiureticsStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:DiureticsStatusRecord"
    class_name: ClassVar[str] = "DiureticsStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.DiureticsStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InsulinStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to insulin
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["InsulinStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:InsulinStatusRecord"
    class_name: ClassVar[str] = "InsulinStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.InsulinStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NiacinMedicationStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to Niacin as a medication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["NiacinMedicationStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:NiacinMedicationStatusRecord"
    class_name: ClassVar[str] = "NiacinMedicationStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.NiacinMedicationStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LipidLoweringMedicationStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to lipid-lowering medications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["LipidLoweringMedicationStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:LipidLoweringMedicationStatusRecord"
    class_name: ClassVar[str] = "LipidLoweringMedicationStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.LipidLoweringMedicationStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FibratesStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to Fibrates
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["FibratesStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:FibratesStatusRecord"
    class_name: ClassVar[str] = "FibratesStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.FibratesStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BileAcidSequestrantStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to bile acid sequestrants
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["BileAcidSequestrantStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:BileAcidSequestrantStatusRecord"
    class_name: ClassVar[str] = "BileAcidSequestrantStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.BileAcidSequestrantStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OralHypoglycemicAgentStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to oral hypoglycemic agents
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["OralHypoglycemicAgentStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:OralHypoglycemicAgentStatusRecord"
    class_name: ClassVar[str] = "OralHypoglycemicAgentStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.OralHypoglycemicAgentStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StatinStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to statins
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["StatinStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:StatinStatusRecord"
    class_name: ClassVar[str] = "StatinStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.StatinStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemicSteroidStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to systemic steroids
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["SystemicSteroidStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:SystemicSteroidStatusRecord"
    class_name: ClassVar[str] = "SystemicSteroidStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.SystemicSteroidStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VasodilatorStatusRecord(DrugStatusRecord):
    """
    Record suggesting exposure to vasodilators
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["VasodilatorStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:VasodilatorStatusRecord"
    class_name: ClassVar[str] = "VasodilatorStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.VasodilatorStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_drug_record: Union[dict, Quantity] = None
    drug_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drug_type):
            self.MissingRequiredField("drug_type")
        if not isinstance(self.drug_type, URIorCURIE):
            self.drug_type = URIorCURIE(self.drug_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PacemakerStatusRecord(ProcedureStatusRecord):
    """
    Record of having a pacemaker implanted
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["PacemakerStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:PacemakerStatusRecord"
    class_name: ClassVar[str] = "PacemakerStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.PacemakerStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_procedure_record: Union[dict, Quantity] = None
    procedure_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.procedure_type):
            self.MissingRequiredField("procedure_type")
        if not isinstance(self.procedure_type, URIorCURIE):
            self.procedure_type = URIorCURIE(self.procedure_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoronaryAngioplastyStatusRecord(ProcedureStatusRecord):
    """
    Record of having a coronary angioplasty
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CoronaryAngioplastyStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:CoronaryAngioplastyStatusRecord"
    class_name: ClassVar[str] = "CoronaryAngioplastyStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CoronaryAngioplastyStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_procedure_record: Union[dict, Quantity] = None
    procedure_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.procedure_type):
            self.MissingRequiredField("procedure_type")
        if not isinstance(self.procedure_type, URIorCURIE):
            self.procedure_type = URIorCURIE(self.procedure_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoronaryBypassStatusRecord(ProcedureStatusRecord):
    """
    Record of having a coronary artery bypass graft
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CoronaryBypassStatusRecord"]
    class_class_curie: ClassVar[str] = "cms:CoronaryBypassStatusRecord"
    class_name: ClassVar[str] = "CoronaryBypassStatusRecord"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CoronaryBypassStatusRecord

    subject_identifier: Union[str, URIorCURIE] = None
    age_at_procedure_record: Union[dict, Quantity] = None
    procedure_type: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.procedure_type):
            self.MissingRequiredField("procedure_type")
        if not isinstance(self.procedure_type, URIorCURIE):
            self.procedure_type = URIorCURIE(self.procedure_type)

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
class AdultHumanBodyWeightQuantity(HumanBodyWeightQuantity):
    """
    Human body weight for adults. Bounds reflect biological limits for adult humans.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AdultHumanBodyWeightQuantity"]
    class_class_curie: ClassVar[str] = "cms:AdultHumanBodyWeightQuantity"
    class_name: ClassVar[str] = "AdultHumanBodyWeightQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AdultHumanBodyWeightQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

@dataclass(repr=False)
class ChildHumanBodyWeightQuantity(HumanBodyWeightQuantity):
    """
    Human body weight for children. Bounds reflect biological limits for children.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ChildHumanBodyWeightQuantity"]
    class_class_curie: ClassVar[str] = "cms:ChildHumanBodyWeightQuantity"
    class_name: ClassVar[str] = "ChildHumanBodyWeightQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

@dataclass(repr=False)
class BodyMassIndexQuantity(Quantity):
    """
    Body mass index value in kg/m², bounded 5–200. Limits based on observed limits of human body size.
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
    FVC measurement, negative values are impossible.
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
    FEV1 measurement, negative values are impossible
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
class HumanPredictedFev1Quantity(Quantity):
    """
    Predicted FEV1 in L, bounded 0–12.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPredictedFev1Quantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPredictedFev1Quantity"
    class_name: ClassVar[str] = "HumanPredictedFev1Quantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPredictedFev1Quantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPercentPredictedFev1Quantity(Quantity):
    """
    Percent-predicted FEV1, bounded 0–150.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPercentPredictedFev1Quantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPercentPredictedFev1Quantity"
    class_name: ClassVar[str] = "HumanPercentPredictedFev1Quantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPercentPredictedFev1Quantity

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
class Human8epiPGF2aUrineQuantity(Quantity):
    """
    Meaasurement of 8-epi-prostaglandin F2 alpha in urine. Negative values are impossible
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["Human8epiPGF2aUrineQuantity"]
    class_class_curie: ClassVar[str] = "cms:Human8epiPGF2aUrineQuantity"
    class_name: ClassVar[str] = "Human8epiPGF2aUrineQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.Human8epiPGF2aUrineQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLPPLA2ActivityBloodQuantity(Quantity):
    """
    Measurement of the activity of the Lp-PLA2 enzyme in blood. Negative values are impossible. Maximum values are
    unknown.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLPPLA2ActivityBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanLPPLA2ActivityBloodQuantity"
    class_name: ClassVar[str] = "HumanLPPLA2ActivityBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLPPLA2ActivityBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCreatinineUrineQuantity(Quantity):
    """
    Meaasurement of creatinine in urine. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCreatinineUrineQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanCreatinineUrineQuantity"
    class_name: ClassVar[str] = "HumanCreatinineUrineQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCreatinineUrineQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineQuantity(Quantity):
    """
    Measurement of albumin in urine. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineQuantity"
    class_name: ClassVar[str] = "HumanAlbuminUrineQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineQuantity001(HumanAlbuminUrineQuantity):
    """
    Measurement of albumin in urine, bounded to mg/dL using immunoturbidometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineQuantity001"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineQuantity001"
    class_name: ClassVar[str] = "HumanAlbuminUrineQuantity001"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity001

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineQuantity002(HumanAlbuminUrineQuantity):
    """
    Measurement of albumin in urine, bounded to mg/L using an albumin dipstick
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineQuantity002"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineQuantity002"
    class_name: ClassVar[str] = "HumanAlbuminUrineQuantity002"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity002

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineQuantity003(HumanAlbuminUrineQuantity):
    """
    Measurement of albumin in urine, bounded to mg/L using HPLC
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineQuantity003"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineQuantity003"
    class_name: ClassVar[str] = "HumanAlbuminUrineQuantity003"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity003

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineQuantity004(HumanAlbuminUrineQuantity):
    """
    Measurement of albumin in urine, bounded to mg/L using immunonephelometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineQuantity004"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineQuantity004"
    class_name: ClassVar[str] = "HumanAlbuminUrineQuantity004"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity004

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminUrineQuantity005(HumanAlbuminUrineQuantity):
    """
    Measurement of albumin in urine, bounded to mg/L using immunoturbidometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminUrineQuantity005"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminUrineQuantity005"
    class_name: ClassVar[str] = "HumanAlbuminUrineQuantity005"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity005

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminCreatinineRatioUrineQuantity(Quantity):
    """
    Calculation of the ratio of albumin to creatinine in urine, bounded to mg/g{creat}
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminCreatinineRatioUrineQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminCreatinineRatioUrineQuantity"
    class_name: ClassVar[str] = "HumanAlbuminCreatinineRatioUrineQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminCreatinineRatioUrineQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ApneaHypopneaIndexQuantity(Quantity):
    """
    Apnea-hypopnea index (AHI) in events per hour. Bounded 0–150 based on biologically plausible limits.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["ApneaHypopneaIndexQuantity"]
    class_class_curie: ClassVar[str] = "cms:ApneaHypopneaIndexQuantity"
    class_name: ClassVar[str] = "ApneaHypopneaIndexQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.ApneaHypopneaIndexQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAlbuminBloodQuantity(Quantity):
    """
    Albumin concentration in blood, bounded 1.0–6.0 g/dL.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAlbuminBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanAlbuminBloodQuantity"
    class_name: ClassVar[str] = "HumanAlbuminBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAlbuminBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlcoholConsumptionQuantity(Quantity):
    """
    Alcohol servings per week. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["AlcoholConsumptionQuantity"]
    class_class_curie: ClassVar[str] = "cms:AlcoholConsumptionQuantity"
    class_name: ClassVar[str] = "AlcoholConsumptionQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.AlcoholConsumptionQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAltSgptQuantity(Quantity):
    """
    ALT/SGPT activity in blood in IU/L. Bounded 0–2000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAltSgptQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanAltSgptQuantity"
    class_name: ClassVar[str] = "HumanAltSgptQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAltSgptQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAstSgotQuantity(Quantity):
    """
    AST/SGOT activity in blood in IU/L. Bounded 0–2000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanAstSgotQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanAstSgotQuantity"
    class_name: ClassVar[str] = "HumanAstSgotQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanAstSgotQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBilirubinConjugatedQuantity(Quantity):
    """
    Conjugated (direct) bilirubin concentration in blood in mg/dL. Bounded 0–30.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBilirubinConjugatedQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanBilirubinConjugatedQuantity"
    class_name: ClassVar[str] = "HumanBilirubinConjugatedQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBilirubinConjugatedQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBilirubinTotalQuantity(Quantity):
    """
    Total bilirubin concentration in blood in mg/dL. Bounded 0–40.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBilirubinTotalQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanBilirubinTotalQuantity"
    class_name: ClassVar[str] = "HumanBilirubinTotalQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBilirubinTotalQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBNPQuantity(Quantity):
    """
    BNP concentration in blood in pg/mL. Bounded 0–5000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBNPQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanBNPQuantity"
    class_name: ClassVar[str] = "HumanBNPQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBNPQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBloodUreaNitrogenQuantity(Quantity):
    """
    Blood urea nitrogen (BUN) concentration in mg/dL. Bounded 1–200.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBloodUreaNitrogenQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanBloodUreaNitrogenQuantity"
    class_name: ClassVar[str] = "HumanBloodUreaNitrogenQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBloodUreaNitrogenQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBUNCreatinineRatioQuantity(Quantity):
    """
    Ratio of blood urea nitrogen to creatinine. Bounded 1–50.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBUNCreatinineRatioQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanBUNCreatinineRatioQuantity"
    class_name: ClassVar[str] = "HumanBUNCreatinineRatioQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBUNCreatinineRatioQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCReactiveProteinQuantity(Quantity):
    """
    C-reactive protein (CRP) concentration in blood. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCReactiveProteinQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanCReactiveProteinQuantity"
    class_name: ClassVar[str] = "HumanCReactiveProteinQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCReactiveProteinQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoronaryArteryCalciumScoreQuantity(Quantity):
    """
    Coronary artery calcium (CAC) Agatston score. Bounded 0–5000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CoronaryArteryCalciumScoreQuantity"]
    class_class_curie: ClassVar[str] = "cms:CoronaryArteryCalciumScoreQuantity"
    class_name: ClassVar[str] = "CoronaryArteryCalciumScoreQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CoronaryArteryCalciumScoreQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoronaryArteryCalciumVolumeQuantity(Quantity):
    """
    Volume of coronary artery calcium in mm³. Bounded 0–3000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CoronaryArteryCalciumVolumeQuantity"]
    class_class_curie: ClassVar[str] = "cms:CoronaryArteryCalciumVolumeQuantity"
    class_name: ClassVar[str] = "CoronaryArteryCalciumVolumeQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CoronaryArteryCalciumVolumeQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CarotidIntimamediaThicknessQuantity(Quantity):
    """
    Carotid intima-media thickness in mm. Bounded 0.3–2.0.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CarotidIntimamediaThicknessQuantity"]
    class_class_curie: ClassVar[str] = "cms:CarotidIntimamediaThicknessQuantity"
    class_name: ClassVar[str] = "CarotidIntimamediaThicknessQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CarotidIntimamediaThicknessQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CarotidStenosisQuantity(Quantity):
    """
    Carotid artery stenosis as a percentage. Bounded 0–100.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CarotidStenosisQuantity"]
    class_class_curie: ClassVar[str] = "cms:CarotidStenosisQuantity"
    class_name: ClassVar[str] = "CarotidStenosisQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CarotidStenosisQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCD40BloodQuantity(Quantity):
    """
    CD40 concentration in blood in pg/mL. Bounded 0–2000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCD40BloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanCD40BloodQuantity"
    class_name: ClassVar[str] = "HumanCD40BloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCD40BloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CESDScoreQuantity(Quantity):
    """
    CES-D depression scale score. Bounded 0–60.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["CESDScoreQuantity"]
    class_class_curie: ClassVar[str] = "cms:CESDScoreQuantity"
    class_name: ClassVar[str] = "CESDScoreQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.CESDScoreQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanChlorideBloodQuantity(Quantity):
    """
    Chloride concentration in blood. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanChlorideBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanChlorideBloodQuantity"
    class_name: ClassVar[str] = "HumanChlorideBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanChlorideBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCreatinineBloodQuantity(Quantity):
    """
    Creatinine concentration in blood in mg/dL. Bounded 0.1–20.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCreatinineBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanCreatinineBloodQuantity"
    class_name: ClassVar[str] = "HumanCreatinineBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCreatinineBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanCystatinCBloodQuantity(Quantity):
    """
    Cystatin C concentration in blood in mg/L. Bounded 0.3–10.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanCystatinCBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanCystatinCBloodQuantity"
    class_name: ClassVar[str] = "HumanCystatinCBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanCystatinCBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanDDimerQuantity(Quantity):
    """
    D-dimer concentration in blood. Negative values are impossible
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanDDimerQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanDDimerQuantity"
    class_name: ClassVar[str] = "HumanDDimerQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanDDimerQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanDiastolicBloodPressureQuantity(Quantity):
    """
    Diastolic blood pressure in mm[Hg]. Bounded 20–180.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanDiastolicBloodPressureQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanDiastolicBloodPressureQuantity"
    class_name: ClassVar[str] = "HumanDiastolicBloodPressureQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanDiastolicBloodPressureQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanESelectinBloodQuantity(Quantity):
    """
    E-selectin concentration in blood in ng/mL. Bounded 5–200.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanESelectinBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanESelectinBloodQuantity"
    class_name: ClassVar[str] = "HumanESelectinBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanESelectinBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanEstimatedGFRQuantity(Quantity):
    """
    Estimated glomerular filtration rate (eGFR) in mL/min/1.73m². Bounded 0–150.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanEstimatedGFRQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanEstimatedGFRQuantity"
    class_name: ClassVar[str] = "HumanEstimatedGFRQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanEstimatedGFRQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanEosinophilCountQuantity(Quantity):
    """
    Eosinophil count in whole blood in 10*3/uL. Bounded 0–20.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanEosinophilCountQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanEosinophilCountQuantity"
    class_name: ClassVar[str] = "HumanEosinophilCountQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanEosinophilCountQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFactorVIIQuantity(Quantity):
    """
    Factor VII activity in plasma as % of normal. Bounded 0–200.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFactorVIIQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanFactorVIIQuantity"
    class_name: ClassVar[str] = "HumanFactorVIIQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFactorVIIQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFactorVIIIQuantity(Quantity):
    """
    Factor VIII activity in plasma in IU/mL. Bounded 0–3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFactorVIIIQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanFactorVIIIQuantity"
    class_name: ClassVar[str] = "HumanFactorVIIIQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFactorVIIIQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFastingGlucoseQuantity(Quantity):
    """
    Fasting blood glucose concentration. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFastingGlucoseQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanFastingGlucoseQuantity"
    class_name: ClassVar[str] = "HumanFastingGlucoseQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFastingGlucoseQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFerritinQuantity(Quantity):
    """
    Ferritin concentration in blood in ng/mL. Bounded 1–5000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFerritinQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanFerritinQuantity"
    class_name: ClassVar[str] = "HumanFerritinQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFerritinQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFEV1FVCRatioQuantity(Quantity):
    """
    FEV1/FVC ratio. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFEV1FVCRatioQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanFEV1FVCRatioQuantity"
    class_name: ClassVar[str] = "HumanFEV1FVCRatioQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFEV1FVCRatioQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPredictedFEV1FVCRatioQuantity(Quantity):
    """
    Predicted FEV1/FVC given as a ratio
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPredictedFEV1FVCRatioQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPredictedFEV1FVCRatioQuantity"
    class_name: ClassVar[str] = "HumanPredictedFEV1FVCRatioQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPredictedFEV1FVCRatioQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPercentPredictedFEV1FVCRatioQuantity(Quantity):
    """
    Percent of predicted FEV1/FVC that the patient achieves given as a percent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPercentPredictedFEV1FVCRatioQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPercentPredictedFEV1FVCRatioQuantity"
    class_name: ClassVar[str] = "HumanPercentPredictedFEV1FVCRatioQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPercentPredictedFEV1FVCRatioQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanFibrinogenQuantity(Quantity):
    """
    Fibrinogen concentration in plasma in mg/dL. Bounded 100–1000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanFibrinogenQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanFibrinogenQuantity"
    class_name: ClassVar[str] = "HumanFibrinogenQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanFibrinogenQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FruitConsumptionQuantity(Quantity):
    """
    Fruit servings per week. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["FruitConsumptionQuantity"]
    class_class_curie: ClassVar[str] = "cms:FruitConsumptionQuantity"
    class_name: ClassVar[str] = "FruitConsumptionQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.FruitConsumptionQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanGFRQuantity(Quantity):
    """
    Glomerular filtration rate (GFR) in mL/min/1.73m². Bounded 0–150.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanGFRQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanGFRQuantity"
    class_name: ClassVar[str] = "HumanGFRQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanGFRQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanGlucoseBloodQuantity(Quantity):
    """
    Glucose concentration in blood in mg/dL. Bounded 20–800.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanGlucoseBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanGlucoseBloodQuantity"
    class_name: ClassVar[str] = "HumanGlucoseBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanGlucoseBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHDLQuantity(Quantity):
    """
    HDL cholesterol concentration in blood. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHDLQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanHDLQuantity"
    class_name: ClassVar[str] = "HumanHDLQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHDLQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHeartRateQuantity(Quantity):
    """
    Heart rate in beats per minute. Bounded 20–300.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHeartRateQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanHeartRateQuantity"
    class_name: ClassVar[str] = "HumanHeartRateQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHeartRateQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHematocritQuantity(Quantity):
    """
    Hematocrit (packed cell volume) as a percentage. Bounded 10–70.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHematocritQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanHematocritQuantity"
    class_name: ClassVar[str] = "HumanHematocritQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHematocritQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHemoglobinQuantity(Quantity):
    """
    Hemoglobin concentration in whole blood in g/dL. Bounded 2–24.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHemoglobinQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanHemoglobinQuantity"
    class_name: ClassVar[str] = "HumanHemoglobinQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHemoglobinQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHemoglobinA1cQuantity(Quantity):
    """
    Hemoglobin A1c (HbA1c) as a percentage of total hemoglobin. Bounded 3–20.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHemoglobinA1cQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanHemoglobinA1cQuantity"
    class_name: ClassVar[str] = "HumanHemoglobinA1cQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHemoglobinA1cQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanHipCircumferenceQuantity(Quantity):
    """
    Hip circumference. Negative values are impossible
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanHipCircumferenceQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanHipCircumferenceQuantity"
    class_name: ClassVar[str] = "HumanHipCircumferenceQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanHipCircumferenceQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanICAM1BloodQuantity(Quantity):
    """
    ICAM-1 concentration in blood in ng/mL. Bounded 50–1500.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanICAM1BloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanICAM1BloodQuantity"
    class_name: ClassVar[str] = "HumanICAM1BloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanICAM1BloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInsulinBloodQuantity(Quantity):
    """
    Insulin concentration in blood. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInsulinBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanInsulinBloodQuantity"
    class_name: ClassVar[str] = "HumanInsulinBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInsulinBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInterleukin18BloodQuantity(Quantity):
    """
    IL-18 concentration in blood in pg/mL. Bounded 10–2000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInterleukin18BloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanInterleukin18BloodQuantity"
    class_name: ClassVar[str] = "HumanInterleukin18BloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInterleukin18BloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInterleukin1BetaBloodQuantity(Quantity):
    """
    IL-1β concentration in blood in pg/mL. Bounded 0–50.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInterleukin1BetaBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanInterleukin1BetaBloodQuantity"
    class_name: ClassVar[str] = "HumanInterleukin1BetaBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInterleukin1BetaBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInterleukin10BloodQuantity(Quantity):
    """
    IL-10 concentration in blood in pg/mL. Bounded 0–100.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInterleukin10BloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanInterleukin10BloodQuantity"
    class_name: ClassVar[str] = "HumanInterleukin10BloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInterleukin10BloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInterleukin6BloodQuantity(Quantity):
    """
    IL-6 concentration in blood in pg/mL. Bounded 0–1000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanInterleukin6BloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanInterleukin6BloodQuantity"
    class_name: ClassVar[str] = "HumanInterleukin6BloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanInterleukin6BloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLactateDehydrogenaseQuantity(Quantity):
    """
    Lactate dehydrogenase (LDH) activity in blood in IU/L. Bounded 50–3000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLactateDehydrogenaseQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanLactateDehydrogenaseQuantity"
    class_name: ClassVar[str] = "HumanLactateDehydrogenaseQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLactateDehydrogenaseQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLactateBloodQuantity(Quantity):
    """
    Lactate concentration in blood in mmol/L. Bounded 0.3–30.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLactateBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanLactateBloodQuantity"
    class_name: ClassVar[str] = "HumanLactateBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLactateBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLDLQuantity(Quantity):
    """
    LDL cholesterol concentration in blood in mg/dL. Bounded 10–400.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLDLQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanLDLQuantity"
    class_name: ClassVar[str] = "HumanLDLQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLDLQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLymphocyteCountQuantity(Quantity):
    """
    Lymphocyte count in whole blood in 10*3/uL. Bounded 0.1–20.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLymphocyteCountQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanLymphocyteCountQuantity"
    class_name: ClassVar[str] = "HumanLymphocyteCountQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLymphocyteCountQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLymphocytePercentQuantity(Quantity):
    """
    Lymphocyte percent of total leukocytes. Bounded 5–90.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLymphocytePercentQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanLymphocytePercentQuantity"
    class_name: ClassVar[str] = "HumanLymphocytePercentQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLymphocytePercentQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanLPPLA2MassBloodQuantity(Quantity):
    """
    Lp-PLA2 mass concentration in blood in ng/mL. Bounded 50–700.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanLPPLA2MassBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanLPPLA2MassBloodQuantity"
    class_name: ClassVar[str] = "HumanLPPLA2MassBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanLPPLA2MassBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMCP1BloodQuantity(Quantity):
    """
    MCP-1/CCL2 concentration in blood in pg/mL. Bounded 20–1000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCP1BloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMCP1BloodQuantity"
    class_name: ClassVar[str] = "HumanMCP1BloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCP1BloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMeanArterialPressureQuantity(Quantity):
    """
    Mean arterial pressure (MAP) in mm[Hg]. Bounded 30–180.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMeanArterialPressureQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMeanArterialPressureQuantity"
    class_name: ClassVar[str] = "HumanMeanArterialPressureQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMeanArterialPressureQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMCHQuantity(Quantity):
    """
    Mean corpuscular hemoglobin (MCH) in pg/cell. Bounded 15–40.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCHQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMCHQuantity"
    class_name: ClassVar[str] = "HumanMCHQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCHQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMCHCQuantity(Quantity):
    """
    Mean corpuscular hemoglobin concentration (MCHC) in g/dL. Bounded 25–40.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCHCQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMCHCQuantity"
    class_name: ClassVar[str] = "HumanMCHCQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCHCQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMCVQuantity(Quantity):
    """
    Mean corpuscular volume (MCV) in fL. Bounded 50–130.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMCVQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMCVQuantity"
    class_name: ClassVar[str] = "HumanMCVQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMCVQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMPVQuantity(Quantity):
    """
    Mean platelet volume (MPV) in fL. Bounded 5–15.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMPVQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMPVQuantity"
    class_name: ClassVar[str] = "HumanMPVQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMPVQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMMP9BloodQuantity(Quantity):
    """
    MMP-9 concentration in blood in ng/mL. Bounded 10–1000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMMP9BloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMMP9BloodQuantity"
    class_name: ClassVar[str] = "HumanMMP9BloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMMP9BloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMonocyteCountQuantity(Quantity):
    """
    Monocyte count in whole blood in 10*3/uL. Bounded 0–3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMonocyteCountQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMonocyteCountQuantity"
    class_name: ClassVar[str] = "HumanMonocyteCountQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMonocyteCountQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMyeloperoxidaseBloodQuantity(Quantity):
    """
    Myeloperoxidase (MPO) concentration in blood in ng/mL. Bounded 0–1000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanMyeloperoxidaseBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanMyeloperoxidaseBloodQuantity"
    class_name: ClassVar[str] = "HumanMyeloperoxidaseBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanMyeloperoxidaseBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanNeutrophilCountQuantity(Quantity):
    """
    Neutrophil count in whole blood in 10*3/uL. Bounded 0–30.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanNeutrophilCountQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanNeutrophilCountQuantity"
    class_name: ClassVar[str] = "HumanNeutrophilCountQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanNeutrophilCountQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanNeutrophilPercentQuantity(Quantity):
    """
    Neutrophil percent of total leukocytes. Bounded 10–95.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanNeutrophilPercentQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanNeutrophilPercentQuantity"
    class_name: ClassVar[str] = "HumanNeutrophilPercentQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanNeutrophilPercentQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanNTproBNPQuantity(Quantity):
    """
    NT-proBNP concentration in blood in pg/mL. Bounded 0–35000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanNTproBNPQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanNTproBNPQuantity"
    class_name: ClassVar[str] = "HumanNTproBNPQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanNTproBNPQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanOsteoprotegerinBloodQuantity(Quantity):
    """
    Osteoprotegerin (OPG) concentration in blood in ng/mL. Bounded 1–20.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanOsteoprotegerinBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanOsteoprotegerinBloodQuantity"
    class_name: ClassVar[str] = "HumanOsteoprotegerinBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanOsteoprotegerinBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPSelectinBloodQuantity(Quantity):
    """
    P-selectin concentration in blood in ng/mL. Bounded 10–300.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPSelectinBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPSelectinBloodQuantity"
    class_name: ClassVar[str] = "HumanPSelectinBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPSelectinBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPlateletCountQuantity(Quantity):
    """
    Platelet count in whole blood in 10*3/uL. Bounded 5–1500.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPlateletCountQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPlateletCountQuantity"
    class_name: ClassVar[str] = "HumanPlateletCountQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPlateletCountQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPotassiumBloodQuantity(Quantity):
    """
    Potassium concentration in blood in mmol/L. Bounded 1.5–9.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPotassiumBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPotassiumBloodQuantity"
    class_name: ClassVar[str] = "HumanPotassiumBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPotassiumBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPRIntervalQuantity(Quantity):
    """
    PR interval duration in ms. Bounded 80–400.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanPRIntervalQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanPRIntervalQuantity"
    class_name: ClassVar[str] = "HumanPRIntervalQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanPRIntervalQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanQRSIntervalQuantity(Quantity):
    """
    QRS interval duration in ms. Bounded 40–200.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanQRSIntervalQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanQRSIntervalQuantity"
    class_name: ClassVar[str] = "HumanQRSIntervalQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanQRSIntervalQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanQTIntervalQuantity(Quantity):
    """
    QT interval duration in ms. Bounded 200–700.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanQTIntervalQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanQTIntervalQuantity"
    class_name: ClassVar[str] = "HumanQTIntervalQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanQTIntervalQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanRBCCountQuantity(Quantity):
    """
    Red blood cell count in whole blood in 10*6/uL. Bounded 1–8.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanRBCCountQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanRBCCountQuantity"
    class_name: ClassVar[str] = "HumanRBCCountQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanRBCCountQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanRDWQuantity(Quantity):
    """
    Red cell distribution width (RDW) as a percentage. Bounded 10–30.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanRDWQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanRDWQuantity"
    class_name: ClassVar[str] = "HumanRDWQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanRDWQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanSleepDurationQuantity(Quantity):
    """
    Sleep duration in hours per night. Bounded 0–16.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanSleepDurationQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanSleepDurationQuantity"
    class_name: ClassVar[str] = "HumanSleepDurationQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanSleepDurationQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanSodiumBloodQuantity(Quantity):
    """
    Sodium concentration in blood in mmol/L. Bounded 100–180.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanSodiumBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanSodiumBloodQuantity"
    class_name: ClassVar[str] = "HumanSodiumBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanSodiumBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SodiumIntakeQuantity(Quantity):
    """
    Dietary sodium intake in mg/day. Bounded 200–15000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["SodiumIntakeQuantity"]
    class_class_curie: ClassVar[str] = "cms:SodiumIntakeQuantity"
    class_name: ClassVar[str] = "SodiumIntakeQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.SodiumIntakeQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanSpO2Quantity(Quantity):
    """
    Arterial oxygen saturation (SpO2) as a percentage. Bounded 50–100.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanSpO2Quantity"]
    class_class_curie: ClassVar[str] = "cms:HumanSpO2Quantity"
    class_name: ClassVar[str] = "HumanSpO2Quantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanSpO2Quantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanSystolicBloodPressureQuantity(Quantity):
    """
    Systolic blood pressure in mm[Hg]. Bounded 40–300.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanSystolicBloodPressureQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanSystolicBloodPressureQuantity"
    class_name: ClassVar[str] = "HumanSystolicBloodPressureQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanSystolicBloodPressureQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanBodyTemperatureQuantity(Quantity):
    """
    Body temperature in degrees Celsius. Bounded 25–43.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanBodyTemperatureQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanBodyTemperatureQuantity"
    class_name: ClassVar[str] = "HumanBodyTemperatureQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanBodyTemperatureQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTNFAlphaBloodQuantity(Quantity):
    """
    TNF-alpha concentration in blood in pg/mL. Bounded 0–100.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTNFAlphaBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanTNFAlphaBloodQuantity"
    class_name: ClassVar[str] = "HumanTNFAlphaBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTNFAlphaBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTNFAlphaR1BloodQuantity(Quantity):
    """
    TNF receptor 1 (TNFR1) concentration in blood in pg/mL. Bounded 200–5000.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTNFAlphaR1BloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanTNFAlphaR1BloodQuantity"
    class_name: ClassVar[str] = "HumanTNFAlphaR1BloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTNFAlphaR1BloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTotalCholesterolQuantity(Quantity):
    """
    Total cholesterol concentration in blood. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTotalCholesterolQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanTotalCholesterolQuantity"
    class_name: ClassVar[str] = "HumanTotalCholesterolQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTotalCholesterolQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTriglyceridesBloodQuantity(Quantity):
    """
    Triglycerides concentration in blood. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTriglyceridesBloodQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanTriglyceridesBloodQuantity"
    class_name: ClassVar[str] = "HumanTriglyceridesBloodQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTriglyceridesBloodQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanTroponinQuantity(Quantity):
    """
    Troponin concentration in blood in ng/mL. Bounded 0–50.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanTroponinQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanTroponinQuantity"
    class_name: ClassVar[str] = "HumanTroponinQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanTroponinQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VegetableConsumptionQuantity(Quantity):
    """
    Vegetable servings per week. Bounded 0–70.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["VegetableConsumptionQuantity"]
    class_class_curie: ClassVar[str] = "cms:VegetableConsumptionQuantity"
    class_name: ClassVar[str] = "VegetableConsumptionQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.VegetableConsumptionQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanVonWillebrandFactorQuantity(Quantity):
    """
    Von Willebrand factor (VWF) activity or antigen as % of normal. Bounded 0–300.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanVonWillebrandFactorQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanVonWillebrandFactorQuantity"
    class_name: ClassVar[str] = "HumanVonWillebrandFactorQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanVonWillebrandFactorQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanWaistCircumferenceQuantity(Quantity):
    """
    Waist circumference. Negative values are impossible.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanWaistCircumferenceQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanWaistCircumferenceQuantity"
    class_name: ClassVar[str] = "HumanWaistCircumferenceQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanWaistHipRatioQuantity(Quantity):
    """
    Waist-to-hip ratio. Bounded 0.5–1.5.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanWaistHipRatioQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanWaistHipRatioQuantity"
    class_name: ClassVar[str] = "HumanWaistHipRatioQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanWaistHipRatioQuantity

    quantity_unit: Union[str, URIorCURIE] = None
    quantity_value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.quantity_value):
            self.MissingRequiredField("quantity_value")
        if not isinstance(self.quantity_value, Decimal):
            self.quantity_value = Decimal(self.quantity_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanWBCCountQuantity(Quantity):
    """
    White blood cell (WBC) count in whole blood in 10*3/uL. Bounded 0.1–100.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CMS["HumanWBCCountQuantity"]
    class_class_curie: ClassVar[str] = "cms:HumanWBCCountQuantity"
    class_name: ClassVar[str] = "HumanWBCCountQuantity"
    class_model_uri: ClassVar[URIRef] = BDC_VARIABLE_LIBRARY.HumanWBCCountQuantity

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
    drugexposure = PermissibleValue(
        text="drugexposure",
        meaning=BDCHM["DrugExposure"])

    _defn = EnumDefinition(
        name="BdchmTypeEnum",
        description="A list of BDCHM entities used to describe variables",
    )

class ClinicalMicroschemaEnum(EnumDefinitionImpl):
    """
    A list of slots describing clinical data in microschema
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
    predicted_value = PermissibleValue(text="predicted_value")
    lower_limit_normal = PermissibleValue(text="lower_limit_normal")
    upper_limit_normal = PermissibleValue(text="upper_limit_normal")
    percent_predicted_value = PermissibleValue(text="percent_predicted_value")
    activity_type = PermissibleValue(text="activity_type")
    relative_timing = PermissibleValue(text="relative_timing")
    condition_type = PermissibleValue(text="condition_type")
    associated_evidence = PermissibleValue(text="associated_evidence")
    age_at_condition_start = PermissibleValue(text="age_at_condition_start")
    age_at_condition_end = PermissibleValue(text="age_at_condition_end")
    age_at_condition_record = PermissibleValue(text="age_at_condition_record")
    condition_status = PermissibleValue(text="condition_status")
    condition_provenance = PermissibleValue(text="condition_provenance")
    condition_severity = PermissibleValue(text="condition_severity")
    relationship_to_participant = PermissibleValue(text="relationship_to_participant")
    drug_type = PermissibleValue(text="drug_type")
    age_at_drug_start = PermissibleValue(text="age_at_drug_start")
    age_at_drug_end = PermissibleValue(text="age_at_drug_end")
    age_at_drug_record = PermissibleValue(text="age_at_drug_record")
    route_of_administration = PermissibleValue(text="route_of_administration")
    dose = PermissibleValue(text="dose")
    frequency = PermissibleValue(text="frequency")
    indication = PermissibleValue(text="indication")
    procedure_type = PermissibleValue(text="procedure_type")
    age_at_procedure_start = PermissibleValue(text="age_at_procedure_start")
    age_at_procedure_end = PermissibleValue(text="age_at_procedure_end")
    age_at_procedure_record = PermissibleValue(text="age_at_procedure_record")
    procedure_status = PermissibleValue(text="procedure_status")
    procedure_provenance = PermissibleValue(text="procedure_provenance")
    exposure_status = PermissibleValue(text="exposure_status")
    exposure_provenance = PermissibleValue(text="exposure_provenance")

    _defn = EnumDefinition(
        name="ClinicalMicroschemaEnum",
        description="A list of slots describing clinical data in microschema",
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

class UCUMEnum(EnumDefinitionImpl):
    """
    Unified Code for Units of Measure (UCUM) codes used in this schema
    """
    Cel = PermissibleValue(
        text="Cel",
        description="Degrees Celsius")
    L = PermissibleValue(
        text="L",
        description="Liters")
    cm = PermissibleValue(
        text="cm",
        description="Centimeters")
    fL = PermissibleValue(
        text="fL",
        description="Femtoliters")
    g = PermissibleValue(
        text="g",
        description="Grams")
    h = PermissibleValue(
        text="h",
        description="Hours")
    kg = PermissibleValue(
        text="kg",
        description="Kilograms")
    m = PermissibleValue(
        text="m",
        description="Meters")
    mL = PermissibleValue(
        text="mL",
        description="Milliliters")
    mm = PermissibleValue(
        text="mm",
        description="Millimeters")
    mm3 = PermissibleValue(
        text="mm3",
        description="Cubic millimeters")
    ms = PermissibleValue(
        text="ms",
        description="Milliseconds")

    _defn = EnumDefinition(
        name="UCUMEnum",
        description="Unified Code for Units of Measure (UCUM) codes used in this schema",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "%",
            PermissibleValue(
                text="%",
                description="Percent"))
        setattr(cls, "%{Normal}",
            PermissibleValue(
                text="%{Normal}",
                description="Percent of normal"))
        setattr(cls, "%{WBCs}",
            PermissibleValue(
                text="%{WBCs}",
                description="Percent of white blood cells"))
        setattr(cls, "/h",
            PermissibleValue(
                text="/h",
                description="Per hour"))
        setattr(cls, "10*3/uL",
            PermissibleValue(
                text="10*3/uL",
                description="Thousands per microliter"))
        setattr(cls, "10*6/uL",
            PermissibleValue(
                text="10*6/uL",
                description="Millions per microliter"))
        setattr(cls, "[IU]/L",
            PermissibleValue(
                text="[IU]/L",
                description="International units per liter"))
        setattr(cls, "[IU]/mL",
            PermissibleValue(
                text="[IU]/mL",
                description="International units per milliliter"))
        setattr(cls, "[ft_i]",
            PermissibleValue(
                text="[ft_i]",
                description="Feet (international)"))
        setattr(cls, "[in_i]",
            PermissibleValue(
                text="[in_i]",
                description="Inches (international)"))
        setattr(cls, "[lb_av]",
            PermissibleValue(
                text="[lb_av]",
                description="Pounds (avoirdupois)"))
        setattr(cls, "[oz_av]",
            PermissibleValue(
                text="[oz_av]",
                description="Ounces (avoirdupois)"))
        setattr(cls, "g/L",
            PermissibleValue(
                text="g/L",
                description="Grams per liter"))
        setattr(cls, "g/dL",
            PermissibleValue(
                text="g/dL",
                description="Grams per deciliter"))
        setattr(cls, "kg/m2",
            PermissibleValue(
                text="kg/m2",
                description="Kilograms per square meter (body mass index)"))
        setattr(cls, "mL/min/{1.73_m2}",
            PermissibleValue(
                text="mL/min/{1.73_m2}",
                description="Milliliters per minute per 1.73 square meters (eGFR)"))
        setattr(cls, "mg/L",
            PermissibleValue(
                text="mg/L",
                description="Milligrams per liter"))
        setattr(cls, "mg/d",
            PermissibleValue(
                text="mg/d",
                description="Milligrams per day"))
        setattr(cls, "mg/dL",
            PermissibleValue(
                text="mg/dL",
                description="Milligrams per deciliter"))
        setattr(cls, "mg/g{creat}",
            PermissibleValue(
                text="mg/g{creat}",
                description="Milligrams per gram of creatinine"))
        setattr(cls, "mm[Hg]",
            PermissibleValue(
                text="mm[Hg]",
                description="Millimeters of mercury"))
        setattr(cls, "mmol/L",
            PermissibleValue(
                text="mmol/L",
                description="Millimoles per liter"))
        setattr(cls, "mmol/dL",
            PermissibleValue(
                text="mmol/dL",
                description="Millimoles per deciliter"))
        setattr(cls, "ng/mL",
            PermissibleValue(
                text="ng/mL",
                description="Nanograms per milliliter"))
        setattr(cls, "nmol/min/mL",
            PermissibleValue(
                text="nmol/min/mL",
                description="Nanomoles per minute per milliliter"))
        setattr(cls, "pg/mL",
            PermissibleValue(
                text="pg/mL",
                description="Picograms per milliliter"))
        setattr(cls, "pg/{cell}",
            PermissibleValue(
                text="pg/{cell}",
                description="Picograms per cell"))
        setattr(cls, "pmol/L",
            PermissibleValue(
                text="pmol/L",
                description="Picomoles per liter"))
        setattr(cls, "u[iU]/mL",
            PermissibleValue(
                text="u[iU]/mL",
                description="Micro international units per milliliter"))
        setattr(cls, "ug/mL",
            PermissibleValue(
                text="ug/mL",
                description="Micrograms per milliliter"))
        setattr(cls, "{#}/uL",
            PermissibleValue(
                text="{#}/uL",
                description="Number per microliter"))
        setattr(cls, "{#}/wk",
            PermissibleValue(
                text="{#}/wk",
                description="Number per week"))
        setattr(cls, "{beats}/min",
            PermissibleValue(
                text="{beats}/min",
                description="Beats per minute"))
        setattr(cls, "{ratio}",
            PermissibleValue(
                text="{ratio}",
                description="Ratio (dimensionless)"))
        setattr(cls, "{score}",
            PermissibleValue(
                text="{score}",
                description="Score (dimensionless)"))

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
    identifier = PermissibleValue(
        text="identifier",
        description="a string used as an identifier by an external data source")

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
    jaffe_reaction = PermissibleValue(
        text="jaffe_reaction",
        description="""colorimetric method for measuring creatinine based on the Jaffe reaction, in which creatinine reacts with picric acid in alkaline solution""")
    cbc = PermissibleValue(
        text="cbc",
        description="""complete blood count; a common blood test that measures the cellular components of blood including red cells, white cells, and platelets""")
    plac_test = PermissibleValue(
        text="plac_test",
        description="""Lipoprotein-Associated Phospholipase A2 (Lp-PLA2) test; a blood test used to assess cardiovascular and stroke risk""")
    enzymatic_creatinine_assay = PermissibleValue(
        text="enzymatic_creatinine_assay",
        description="""enzymatic method for measuring creatinine using creatininase, offering greater specificity than the Jaffe reaction with fewer interferences""")
    lc_ms_ms = PermissibleValue(
        text="lc_ms_ms",
        description="""liquid chromatography-tandem mass spectrometry; a reference method for quantifying analytes with high specificity and sensitivity""")
    immunoturbidometry = PermissibleValue(
        text="immunoturbidometry",
        description="photometric method measuring the turbidity caused by antigen-antibody complexes in suspension")
    immunonephelometry = PermissibleValue(
        text="immunonephelometry",
        description="""optical method measuring light scatter from antigen-antibody complexes to quantify proteins such as albumin""")
    chemiluminescence_immunoassay = PermissibleValue(
        text="chemiluminescence_immunoassay",
        description="""immunoassay that uses a chemiluminescent label to detect and quantify an analyte via light emission""")
    elisa = PermissibleValue(
        text="elisa",
        description="""enzyme-linked immunosorbent assay; a plate-based immunoassay for detecting and quantifying proteins or antibodies""")
    albumin_dipstick = PermissibleValue(
        text="albumin_dipstick",
        description="semi-quantitative colorimetric urine test strip method for detecting albumin")
    hplc = PermissibleValue(
        text="hplc",
        description="""high-performance liquid chromatography; a chromatographic technique used to separate, identify, and quantify analytes in a mixture""")
    polysomnography = PermissibleValue(
        text="polysomnography",
        description="""in-laboratory polysomnography; comprehensive multi-channel sleep study recording brain activity, eye movements, muscle activity, and cardiorespiratory signals""")
    home_sleep_apnea_test = PermissibleValue(
        text="home_sleep_apnea_test",
        description="portable, simplified sleep monitoring performed at home to detect obstructive sleep apnea")
    bcg_bcp_colorimetric = PermissibleValue(
        text="bcg_bcp_colorimetric",
        description="""bromocresol green (BCG) or bromocresol purple (BCP) dye-binding colorimetric assay for measuring albumin concentration""")
    questionnaire = PermissibleValue(
        text="questionnaire",
        description="""self-report questionnaire or structured interview instrument used to collect behavioral, dietary, or symptom data""")
    enzymatic_kinetic_assay = PermissibleValue(
        text="enzymatic_kinetic_assay",
        description="""enzymatic kinetic (rate) assay standardized by the IFCC; measures the rate of an enzymatic reaction to quantify substrate or enzyme concentration""")
    diazo_colorimetric = PermissibleValue(
        text="diazo_colorimetric",
        description="diazo (van den Bergh) colorimetric method for measuring bilirubin fractions in serum or plasma")
    urease_gldh = PermissibleValue(
        text="urease_gldh",
        description="""enzymatic urease/glutamate dehydrogenase (GLDH) coupled assay for measuring blood urea nitrogen (BUN) or urea""")
    ion_selective_electrode = PermissibleValue(
        text="ion_selective_electrode",
        description="""potentiometric method using ion-selective electrodes to measure electrolyte concentrations such as sodium, potassium, and chloride""")
    agatston_scoring = PermissibleValue(
        text="agatston_scoring",
        description="""Agatston scoring algorithm applied to non-contrast cardiac CT images to quantify coronary artery calcium""")
    volume_scoring = PermissibleValue(
        text="volume_scoring",
        description="volume-based calcium scoring from non-contrast cardiac CT; reports total calcium volume in mm³")
    carotid_ultrasound = PermissibleValue(
        text="carotid_ultrasound",
        description="""B-mode (2-D) carotid ultrasound imaging used to measure intima-media thickness and detect plaques""")
    duplex_ultrasound = PermissibleValue(
        text="duplex_ultrasound",
        description="""duplex ultrasound combining B-mode imaging with Doppler velocity measurements to grade arterial stenosis""")
    ct_angiography = PermissibleValue(
        text="ct_angiography",
        description="computed tomography angiography; contrast-enhanced CT imaging of blood vessels")
    automated_hematology = PermissibleValue(
        text="automated_hematology",
        description="""automated hematology analysis using impedance, electrical resistance, or light-scatter technologies to count and characterize blood cells""")
    manual_differential = PermissibleValue(
        text="manual_differential",
        description="""manual microscopic differential cell count performed by a trained laboratory technician or pathologist on a stained blood smear""")
    one_stage_clotting = PermissibleValue(
        text="one_stage_clotting",
        description="""one-stage clotting assay (PT-based for Factor VII or aPTT-based for Factor VIII) measuring coagulation factor activity""")
    chromogenic_assay = PermissibleValue(
        text="chromogenic_assay",
        description="""chromogenic substrate assay measuring coagulation factor activity via colorimetric detection of a chromogenic substrate cleavage product""")
    hexokinase_glucose_oxidase = PermissibleValue(
        text="hexokinase_glucose_oxidase",
        description="""enzymatic assay using hexokinase or glucose oxidase to measure glucose concentration; the reference method for glucose measurement""")
    clauss_assay = PermissibleValue(
        text="clauss_assay",
        description="""Clauss functional clotting assay for fibrinogen; measures the time to clot formation after adding thrombin to diluted plasma""")
    electrocardiography = PermissibleValue(
        text="electrocardiography",
        description="""electrocardiography; recording of the heart's electrical activity over time to measure intervals and waveforms""")
    pulse_oximetry = PermissibleValue(
        text="pulse_oximetry",
        description="non-invasive photoplethysmographic method for measuring blood oxygen saturation and pulse rate")
    auscultatory = PermissibleValue(
        text="auscultatory",
        description="""auscultatory method for blood pressure measurement using a stethoscope and sphygmomanometer (Korotkoff sounds)""")
    oscillometric = PermissibleValue(
        text="oscillometric",
        description="""oscillometric method for blood pressure measurement detecting arterial wall oscillations via an automated cuff""")
    actigraphy = PermissibleValue(
        text="actigraphy",
        description="""actigraphy; continuous monitoring of movement and rest-activity cycles using a wrist-worn accelerometer to estimate sleep duration and quality""")
    thermometry = PermissibleValue(
        text="thermometry",
        description="""thermometry; measurement of body temperature using a thermometer placed at an oral, rectal, tympanic, temporal, or axillary site""")
    multiplex_bead_immunoassay = PermissibleValue(
        text="multiplex_bead_immunoassay",
        description="""multiplex bead-based immunoassay (e.g., Luminex xMAP) simultaneously quantifying multiple cytokines or proteins in a single sample""")
    microhematocrit_centrifugation = PermissibleValue(
        text="microhematocrit_centrifugation",
        description="""microhematocrit centrifugation method; capillary blood tubes are centrifuged and the packed cell volume fraction read directly""")
    cyanmethemoglobin = PermissibleValue(
        text="cyanmethemoglobin",
        description="""cyanmethemoglobin (Drabkin) spectrophotometric method for measuring whole-blood hemoglobin concentration""")
    precipitation_method = PermissibleValue(
        text="precipitation_method",
        description="""precipitation method for HDL cholesterol; LDL and VLDL are precipitated with a chemical agent and HDL is measured in the supernatant""")
    direct_homogeneous_enzymatic = PermissibleValue(
        text="direct_homogeneous_enzymatic",
        description="""direct homogeneous enzymatic assay for HDL or LDL cholesterol; uses selective detergents and enzymatic reactions without prior precipitation""")
    friedewald_calculation = PermissibleValue(
        text="friedewald_calculation",
        description="""Friedewald equation calculation of LDL cholesterol from total cholesterol, HDL cholesterol, and triglycerides""")
    manual_pulse_palpation = PermissibleValue(
        text="manual_pulse_palpation",
        description="""manual palpation or auscultation of the pulse at a peripheral artery or cardiac apex to count heart rate""")
    latex_agglutination = PermissibleValue(
        text="latex_agglutination",
        description="""latex particle agglutination immunoassay for detecting and semi-quantifying analytes such as D-dimer""")
    ristocetin_cofactor_assay = PermissibleValue(
        text="ristocetin_cofactor_assay",
        description="""ristocetin cofactor activity assay (VWF:RCo) measuring the ability of von Willebrand factor to agglutinate platelets in the presence of ristocetin""")
    boronate_affinity_chromatography = PermissibleValue(
        text="boronate_affinity_chromatography",
        description="""boronate affinity chromatography for HbA1c measurement; glycated hemoglobin binds selectively to boronate-coupled resin""")
    direct_measurement = PermissibleValue(
        text="direct_measurement",
        description="""direct physical measurement using a measuring tape, ruler, or caliper applied to the body surface""")
    gc_ms = PermissibleValue(
        text="gc_ms",
        description="""gas chromatography-mass spectrometry; a combined technique for separating and identifying volatile compounds with high specificity""")
    arterial_catheter = PermissibleValue(
        text="arterial_catheter",
        description="""invasive intra-arterial catheter measurement using a pressure transducer placed directly in an artery to continuously measure blood pressure""")
    clearance_test = PermissibleValue(
        text="clearance_test",
        description="""renal clearance test measuring the rate at which the kidneys filter a marker substance (e.g., iothalamate, inulin) from plasma""")

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
    flow_cytometer = PermissibleValue(
        text="flow_cytometer",
        description="""instrument that measures physical and chemical characteristics of cells or particles as they flow through a laser beam""")
    microscope = PermissibleValue(
        text="microscope",
        description="""optical instrument used to magnify and visualize cells, microorganisms, or other small structures""")
    particle_counter = PermissibleValue(
        text="particle_counter",
        description="instrument that counts and sizes particles suspended in a fluid, used in hematology analyzers")
    mechanical_baby_scale = PermissibleValue(
        text="mechanical_baby_scale",
        description="mechanical scale designed to weigh infants and young children")
    unknown = PermissibleValue(
        text="unknown",
        description="the instrument used for the measurement is not known or was not recorded")
    polysomnograph = PermissibleValue(
        text="polysomnograph",
        description="""multi-channel laboratory instrument for polysomnography recording EEG, EOG, EMG, ECG, airflow, respiratory effort, and oxygen saturation""")
    portable_home_sleep_apnea_monitor = PermissibleValue(
        text="portable_home_sleep_apnea_monitor",
        description="""portable simplified device used for home sleep apnea testing, recording airflow, respiratory effort, and oximetry""")
    automated_clinical_chemistry_analyzer = PermissibleValue(
        text="automated_clinical_chemistry_analyzer",
        description="""automated benchtop or modular analyzer performing photometric, potentiometric, and immunological assays on serum, plasma, or urine""")
    microplate_reader = PermissibleValue(
        text="microplate_reader",
        description="""spectrophotometric instrument that reads absorbance, fluorescence, or luminescence in microwell plates for immunoassays such as ELISA""")
    automated_immunoassay_analyzer = PermissibleValue(
        text="automated_immunoassay_analyzer",
        description="""dedicated automated platform for chemiluminescent, fluorescent, or electrochemiluminescent immunoassays""")
    automated_hematology_analyzer = PermissibleValue(
        text="automated_hematology_analyzer",
        description="""automated instrument using impedance, light scatter, or flow cytometry to count and characterize blood cell populations in a complete blood count""")
    automated_coagulation_analyzer = PermissibleValue(
        text="automated_coagulation_analyzer",
        description="""automated instrument measuring clot formation times and coagulation factor activities via optical or mechanical detection""")
    carotid_ultrasound_system = PermissibleValue(
        text="carotid_ultrasound_system",
        description="""duplex ultrasound system with a high-frequency linear transducer for B-mode carotid artery imaging and Doppler flow measurement""")
    ct_scanner = PermissibleValue(
        text="ct_scanner",
        description="""computed tomography scanner; cardiac-gated CT used for coronary artery calcium scoring and CT angiography""")
    electrocardiograph = PermissibleValue(
        text="electrocardiograph",
        description="""electrocardiograph (ECG/EKG machine) recording the heart's electrical activity via surface electrodes for interval and waveform measurements""")
    pulse_oximeter = PermissibleValue(
        text="pulse_oximeter",
        description="""non-invasive photoplethysmographic device placed on a finger or earlobe to measure arterial oxygen saturation (SpO2) and pulse rate""")
    sphygmomanometer = PermissibleValue(
        text="sphygmomanometer",
        description="""manual aneroid or mercury sphygmomanometer with an inflatable cuff and stethoscope for auscultatory blood pressure measurement""")
    automated_bp_monitor = PermissibleValue(
        text="automated_bp_monitor",
        description="""automated oscillometric blood pressure monitor measuring systolic and diastolic pressure with an inflatable upper-arm or wrist cuff""")
    glucometer = PermissibleValue(
        text="glucometer",
        description="""point-of-care electrochemical glucometer for rapid whole-blood glucose measurement using a glucose oxidase or glucose dehydrogenase test strip""")
    actigraph = PermissibleValue(
        text="actigraph",
        description="""wrist-worn or hip-worn accelerometer device recording continuous movement data to estimate sleep and physical activity patterns""")
    thermometer = PermissibleValue(
        text="thermometer",
        description="digital electronic thermometer for oral, rectal, or axillary body temperature measurement")
    infrared_thermometer = PermissibleValue(
        text="infrared_thermometer",
        description="""non-contact infrared or tympanic thermometer measuring body temperature from emitted thermal radiation at the ear canal or skin surface""")
    multiplex_analyzer = PermissibleValue(
        text="multiplex_analyzer",
        description="""bead-based multiplex immunoassay platform (e.g., Luminex xMAP) capable of simultaneously quantifying multiple analytes in a single sample""")
    blood_gas_analyzer = PermissibleValue(
        text="blood_gas_analyzer",
        description="""point-of-care or laboratory instrument measuring pH, blood gases (pO2, pCO2), electrolytes, and metabolites in whole blood""")
    hemocytometer = PermissibleValue(
        text="hemocytometer",
        description="""ruled counting chamber used with a light microscope for manual cell counting of blood or other cell suspensions""")
    hematocrit_centrifuge = PermissibleValue(
        text="hematocrit_centrifuge",
        description="""microhematocrit centrifuge spinning capillary blood tubes at high speed to pack red blood cells for packed cell volume (hematocrit) measurement""")
    point_of_care_cardiac_analyzer = PermissibleValue(
        text="point_of_care_cardiac_analyzer",
        description="""bedside or point-of-care immunoassay device for rapid quantitative measurement of cardiac biomarkers such as BNP, NT-proBNP, or troponin""")
    hba1c_analyzer = PermissibleValue(
        text="hba1c_analyzer",
        description="""dedicated ion-exchange HPLC or immunoassay analyzer for HbA1c measurement, reporting the percentage of glycated hemoglobin""")
    lactate_meter = PermissibleValue(
        text="lactate_meter",
        description="""handheld electrochemical point-of-care device for rapid whole-blood or plasma lactate measurement""")
    stethoscope = PermissibleValue(
        text="stethoscope",
        description="""acoustic medical device used for auscultation of heart sounds and Korotkoff sounds during manual blood pressure measurement""")
    infantometer = PermissibleValue(
        text="infantometer",
        description="""flat-surface board with a fixed headpiece and sliding footpiece used to measure recumbent length in infants""")
    bariatric_scale = PermissibleValue(
        text="bariatric_scale",
        description="""heavy-duty scale with an extended weight capacity designed to measure body weight in bariatric patients""")
    body_composition_analyzer = PermissibleValue(
        text="body_composition_analyzer",
        description="""device using bioelectrical impedance analysis (BIA) or dual-energy X-ray absorptiometry (DXA) to measure body weight and body composition""")
    digital_baby_scale = PermissibleValue(
        text="digital_baby_scale",
        description="""digital electronic scale designed to accurately measure the weight of infants and young children""")
    gli = PermissibleValue(
        text="gli",
        description="""Global Lung Function Initiative 2012 reference equations for spirometry; used to derive predicted lung function values""")
    gli_global = PermissibleValue(
        text="gli_global",
        description="""Global Lung Function Initiative 2022 multi-ethnic global reference equations for spirometry; an update of the 2012 GLI equations""")
    nhanesiii = PermissibleValue(
        text="nhanesiii",
        description="""NHANES III (1999) reference equations for spirometry derived from the Third National Health and Nutrition Examination Survey""")

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
    no_lipid_lowering_medications = PermissibleValue(
        text="no_lipid_lowering_medications",
        description="No lipid-lowering medications taken at that time")
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

class DynamicAsthmaEnum(EnumDefinitionImpl):
    """
    Asthma and asthma-related terms from Mondo and HPO
    """
    _defn = EnumDefinition(
        name="DynamicAsthmaEnum",
        description="Asthma and asthma-related terms from Mondo and HPO",
    )

class DynamicHeartFailureEnum(EnumDefinitionImpl):
    """
    Heart failure and related terms from Mondo and HPO
    """
    _defn = EnumDefinition(
        name="DynamicHeartFailureEnum",
        description="Heart failure and related terms from Mondo and HPO",
    )

class DynamicObesityEnum(EnumDefinitionImpl):
    """
    Obesity and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicObesityEnum",
        description="Obesity and related terms from HPO and Mondo",
    )

class DynamicAfibEnum(EnumDefinitionImpl):
    """
    Atrial fibrillation and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicAfibEnum",
        description="Atrial fibrillation and related terms from HPO and Mondo",
    )

class DynamicAnginaEnum(EnumDefinitionImpl):
    """
    Angina and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicAnginaEnum",
        description="Angina and related terms from HPO and Mondo",
    )

class DynamicCvdEnum(EnumDefinitionImpl):
    """
    Cardiovascular disease and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicCvdEnum",
        description="Cardiovascular disease and related terms from HPO and Mondo",
    )

class DynamicCopdEnum(EnumDefinitionImpl):
    """
    COPD and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicCopdEnum",
        description="COPD and related terms from HPO and Mondo",
    )

class DynamicDiabetesEnum(EnumDefinitionImpl):
    """
    Diabetes and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicDiabetesEnum",
        description="Diabetes and related terms from HPO and Mondo",
    )

class DynamicStrokeEnum(EnumDefinitionImpl):
    """
    Stroke and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicStrokeEnum",
        description="Stroke and related terms from HPO and Mondo",
    )

class DynamicHeartDiseaseEnum(EnumDefinitionImpl):
    """
    Heart disease and related terms from Mondo
    """
    _defn = EnumDefinition(
        name="DynamicHeartDiseaseEnum",
        description="Heart disease and related terms from Mondo",
    )

class DynamicMyocardialInfarctionEnum(EnumDefinitionImpl):
    """
    Myocardial infarction and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicMyocardialInfarctionEnum",
        description="Myocardial infarction and related terms from HPO and Mondo",
    )

class DynamicHypertensionEnum(EnumDefinitionImpl):
    """
    Hypertension and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicHypertensionEnum",
        description="Hypertension and related terms from HPO and Mondo",
    )

class DynamicLvhEnum(EnumDefinitionImpl):
    """
    Left ventricular hypertrophy and related terms from HPO
    """
    _defn = EnumDefinition(
        name="DynamicLvhEnum",
        description="Left ventricular hypertrophy and related terms from HPO",
    )

class DynamicPadEnum(EnumDefinitionImpl):
    """
    Peripheral arterial disease and related terms from Mondo
    """
    _defn = EnumDefinition(
        name="DynamicPadEnum",
        description="Peripheral arterial disease and related terms from Mondo",
    )

class DynamicSleepApneaEnum(EnumDefinitionImpl):
    """
    Sleep apnea and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicSleepApneaEnum",
        description="Sleep apnea and related terms from HPO and Mondo",
    )

class DynamicVhdEnum(EnumDefinitionImpl):
    """
    Valvular heart disease and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicVhdEnum",
        description="Valvular heart disease and related terms from HPO and Mondo",
    )

class DynamicVenThromEnum(EnumDefinitionImpl):
    """
    Venous thromboembolism and related terms from HPO and Mondo
    """
    _defn = EnumDefinition(
        name="DynamicVenThromEnum",
        description="Venous thromboembolism and related terms from HPO and Mondo",
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

slots.missing_value = Slot(uri=BDC_VARIABLE_LIBRARY.missing_value, name="missing_value", curie=BDC_VARIABLE_LIBRARY.curie('missing_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.missing_value, domain=None, range=Optional[Union[Union[dict, MissingValue], list[Union[dict, MissingValue]]]])

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

slots.row_metadata = Slot(uri=BDC_VARIABLE_LIBRARY.row_metadata, name="row_metadata", curie=BDC_VARIABLE_LIBRARY.curie('row_metadata'),
                   model_uri=BDC_VARIABLE_LIBRARY.row_metadata, domain=None, range=Optional[Union[dict[Union[str, MetadataVariableId], Union[dict, MetadataVariable]], list[Union[dict, MetadataVariable]]]])

slots.documentation_metadata = Slot(uri=BDC_VARIABLE_LIBRARY.documentation_metadata, name="documentation_metadata", curie=BDC_VARIABLE_LIBRARY.curie('documentation_metadata'),
                   model_uri=BDC_VARIABLE_LIBRARY.documentation_metadata, domain=None, range=Optional[Union[Union[dict, DocumentationVariable], list[Union[dict, DocumentationVariable]]]])

slots.alert_value = Slot(uri=BDC_VARIABLE_LIBRARY.alert_value, name="alert_value", curie=BDC_VARIABLE_LIBRARY.curie('alert_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.alert_value, domain=None, range=Optional[Union[Union[dict, AlertValue], list[Union[dict, AlertValue]]]])

slots.alert_values = Slot(uri=BDC_VARIABLE_LIBRARY.alert_values, name="alert_values", curie=BDC_VARIABLE_LIBRARY.curie('alert_values'),
                   model_uri=BDC_VARIABLE_LIBRARY.alert_values, domain=None, range=Optional[Union[Union[dict, AlertValue], list[Union[dict, AlertValue]]]])

slots.indicator_char = Slot(uri=BDC_VARIABLE_LIBRARY.indicator_char, name="indicator_char", curie=BDC_VARIABLE_LIBRARY.curie('indicator_char'),
                   model_uri=BDC_VARIABLE_LIBRARY.indicator_char, domain=None, range=Optional[str])

slots.indicator_meaning = Slot(uri=BDC_VARIABLE_LIBRARY.indicator_meaning, name="indicator_meaning", curie=BDC_VARIABLE_LIBRARY.curie('indicator_meaning'),
                   model_uri=BDC_VARIABLE_LIBRARY.indicator_meaning, domain=None, range=Optional[str])

slots.indicator_type = Slot(uri=BDC_VARIABLE_LIBRARY.indicator_type, name="indicator_type", curie=BDC_VARIABLE_LIBRARY.curie('indicator_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.indicator_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.microschema_slot = Slot(uri=BDC_VARIABLE_LIBRARY.microschema_slot, name="microschema_slot", curie=BDC_VARIABLE_LIBRARY.curie('microschema_slot'),
                   model_uri=BDC_VARIABLE_LIBRARY.microschema_slot, domain=None, range=Optional[Union[Union[str, "ClinicalMicroschemaEnum"], list[Union[str, "ClinicalMicroschemaEnum"]]]])

slots.integrates = Slot(uri=BDC_VARIABLE_LIBRARY.integrates, name="integrates", curie=BDC_VARIABLE_LIBRARY.curie('integrates'),
                   model_uri=BDC_VARIABLE_LIBRARY.integrates, domain=None, range=Optional[Union[Union[str, CompoundVariableId], list[Union[str, CompoundVariableId]]]])

slots.coded_values = Slot(uri=BDC_VARIABLE_LIBRARY.coded_values, name="coded_values", curie=BDC_VARIABLE_LIBRARY.curie('coded_values'),
                   model_uri=BDC_VARIABLE_LIBRARY.coded_values, domain=None, range=Optional[Union[Union[dict, EnumValue], list[Union[dict, EnumValue]]]])

slots.contr_vocab = Slot(uri=BDC_VARIABLE_LIBRARY.contr_vocab, name="contr_vocab", curie=BDC_VARIABLE_LIBRARY.curie('contr_vocab'),
                   model_uri=BDC_VARIABLE_LIBRARY.contr_vocab, domain=None, range=Optional[str])

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
                   model_uri=BDC_VARIABLE_LIBRARY.unit, domain=None, range=Optional[str])

slots.method = Slot(uri=BDCHM.method_type, name="method", curie=BDCHM.curie('method_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.method, domain=None, range=Optional[Union[str, "MethodEnum"]])

slots.instrument = Slot(uri=CMS.instrument, name="instrument", curie=CMS.curie('instrument'),
                   model_uri=BDC_VARIABLE_LIBRARY.instrument, domain=None, range=Optional[str])

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

slots.exposure_status = Slot(uri=CMS.exposure_status, name="exposure_status", curie=CMS.curie('exposure_status'),
                   model_uri=BDC_VARIABLE_LIBRARY.exposure_status, domain=None, range=Optional[Union[str, "HistoricalStatusEnum"]])

slots.exposure_provenance = Slot(uri=CMS.exposure_provenance, name="exposure_provenance", curie=CMS.curie('exposure_provenance'),
                   model_uri=BDC_VARIABLE_LIBRARY.exposure_provenance, domain=None, range=Optional[Union[str, "ProvenanceEnum"]])

slots.procedure_status = Slot(uri=CMS.procedure_status, name="procedure_status", curie=CMS.curie('procedure_status'),
                   model_uri=BDC_VARIABLE_LIBRARY.procedure_status, domain=None, range=Optional[Union[str, "HistoricalStatusEnum"]])

slots.procedure_provenance = Slot(uri=CMS.procedure_provenance, name="procedure_provenance", curie=CMS.curie('procedure_provenance'),
                   model_uri=BDC_VARIABLE_LIBRARY.procedure_provenance, domain=None, range=Optional[Union[str, "ProvenanceEnum"]])

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

slots.HumanBodyHeightRecord001_unit = Slot(uri=BDCHM.unit, name="HumanBodyHeightRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord001_unit, domain=HumanBodyHeightRecord001, range=Optional[str])

slots.HumanBodyHeightRecord001_age_at_measurement = Slot(uri=CMS.age_at_measurement, name="HumanBodyHeightRecord001_age_at_measurement", curie=CMS.curie('age_at_measurement'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord001_age_at_measurement, domain=HumanBodyHeightRecord001, range=Union[dict, Quantity])

slots.HumanBodyHeightRecord002_unit = Slot(uri=BDCHM.unit, name="HumanBodyHeightRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord002_unit, domain=HumanBodyHeightRecord002, range=Optional[str])

slots.HumanBodyHeightRecord002_age_at_measurement = Slot(uri=CMS.age_at_measurement, name="HumanBodyHeightRecord002_age_at_measurement", curie=CMS.curie('age_at_measurement'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord002_age_at_measurement, domain=HumanBodyHeightRecord002, range=Union[dict, Quantity])

slots.HumanBodyHeightRecord003_unit = Slot(uri=BDCHM.unit, name="HumanBodyHeightRecord003_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord003_unit, domain=HumanBodyHeightRecord003, range=Optional[str])

slots.HumanBodyHeightRecord003_age_at_measurement = Slot(uri=CMS.age_at_measurement, name="HumanBodyHeightRecord003_age_at_measurement", curie=CMS.curie('age_at_measurement'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord003_age_at_measurement, domain=HumanBodyHeightRecord003, range=Union[dict, Quantity])

slots.HumanBodyHeightRecord004_unit = Slot(uri=BDCHM.unit, name="HumanBodyHeightRecord004_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord004_unit, domain=HumanBodyHeightRecord004, range=Optional[str])

slots.HumanBodyHeightRecord004_age_at_measurement = Slot(uri=CMS.age_at_measurement, name="HumanBodyHeightRecord004_age_at_measurement", curie=CMS.curie('age_at_measurement'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightRecord004_age_at_measurement, domain=HumanBodyHeightRecord004, range=Union[dict, Quantity])

slots.HumanBodyWeightRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyWeightRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightRecord_measurement_value, domain=HumanBodyWeightRecord, range=Union[dict, "HumanBodyWeightQuantity"])

slots.AdultHumanBodyWeightRecord_measurement_value = Slot(uri=CMS.measurement_value, name="AdultHumanBodyWeightRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.AdultHumanBodyWeightRecord_measurement_value, domain=AdultHumanBodyWeightRecord, range=Union[dict, "AdultHumanBodyWeightQuantity"])

slots.AdultHumanBodyWeightRecord001_unit = Slot(uri=BDCHM.unit, name="AdultHumanBodyWeightRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.AdultHumanBodyWeightRecord001_unit, domain=AdultHumanBodyWeightRecord001, range=Optional[str])

slots.AdultHumanBodyWeightRecord002_unit = Slot(uri=BDCHM.unit, name="AdultHumanBodyWeightRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.AdultHumanBodyWeightRecord002_unit, domain=AdultHumanBodyWeightRecord002, range=Optional[str])

slots.ChildHumanBodyWeightRecord_measurement_value = Slot(uri=CMS.measurement_value, name="ChildHumanBodyWeightRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord_measurement_value, domain=ChildHumanBodyWeightRecord, range=Union[dict, "ChildHumanBodyWeightQuantity"])

slots.ChildHumanBodyWeightRecord_age_at_measurement = Slot(uri=CMS.age_at_measurement, name="ChildHumanBodyWeightRecord_age_at_measurement", curie=CMS.curie('age_at_measurement'),
                   model_uri=BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord_age_at_measurement, domain=ChildHumanBodyWeightRecord, range=Union[dict, Quantity])

slots.ChildHumanBodyWeightRecord001_unit = Slot(uri=BDCHM.unit, name="ChildHumanBodyWeightRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord001_unit, domain=ChildHumanBodyWeightRecord001, range=Optional[str])

slots.ChildHumanBodyWeightRecord002_unit = Slot(uri=BDCHM.unit, name="ChildHumanBodyWeightRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord002_unit, domain=ChildHumanBodyWeightRecord002, range=Optional[str])

slots.ChildHumanBodyWeightRecord003_unit = Slot(uri=BDCHM.unit, name="ChildHumanBodyWeightRecord003_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord003_unit, domain=ChildHumanBodyWeightRecord003, range=Optional[str])

slots.ChildHumanBodyWeightRecord004_unit = Slot(uri=BDCHM.unit, name="ChildHumanBodyWeightRecord004_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.ChildHumanBodyWeightRecord004_unit, domain=ChildHumanBodyWeightRecord004, range=Optional[str])

slots.BodyMassIndexRecord_measurement_value = Slot(uri=CMS.measurement_value, name="BodyMassIndexRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.BodyMassIndexRecord_measurement_value, domain=BodyMassIndexRecord, range=Union[dict, "BodyMassIndexQuantity"])

slots.HumanFvcRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFvcRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFvcRecord_measurement_value, domain=HumanFvcRecord, range=Union[dict, "HumanFvcQuantity"])

slots.HumanFvcRecord001_unit = Slot(uri=BDCHM.unit, name="HumanFvcRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFvcRecord001_unit, domain=HumanFvcRecord001, range=Optional[str])

slots.HumanFvcRecord002_unit = Slot(uri=BDCHM.unit, name="HumanFvcRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFvcRecord002_unit, domain=HumanFvcRecord002, range=Optional[str])

slots.HumanPredictedFvcRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPredictedFvcRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPredictedFvcRecord_measurement_value, domain=HumanPredictedFvcRecord, range=Union[dict, "HumanPredictedFvcQuantity"])

slots.HumanPercentPredictedFvcRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPercentPredictedFvcRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPercentPredictedFvcRecord_measurement_value, domain=HumanPercentPredictedFvcRecord, range=Union[dict, "HumanPercentPredictedFvcQuantity"])

slots.HumanFev1Record_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFev1Record_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFev1Record_measurement_value, domain=HumanFev1Record, range=Union[dict, "HumanFev1Quantity"])

slots.HumanFev1Record001_unit = Slot(uri=BDCHM.unit, name="HumanFev1Record001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFev1Record001_unit, domain=HumanFev1Record001, range=Optional[str])

slots.HumanFev1Record002_unit = Slot(uri=BDCHM.unit, name="HumanFev1Record002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFev1Record002_unit, domain=HumanFev1Record002, range=Optional[str])

slots.HumanPredictedFev1Record_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPredictedFev1Record_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPredictedFev1Record_measurement_value, domain=HumanPredictedFev1Record, range=Union[dict, "HumanPredictedFev1Quantity"])

slots.HumanPercentPredictedFev1Record_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPercentPredictedFev1Record_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPercentPredictedFev1Record_measurement_value, domain=HumanPercentPredictedFev1Record, range=Union[dict, "HumanPercentPredictedFev1Quantity"])

slots.HumanBasophilCountRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBasophilCountRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord_measurement_value, domain=HumanBasophilCountRecord, range=Union[dict, "HumanBasophilCountQuantity"])

slots.HumanBasophilCountRecord001_unit = Slot(uri=BDCHM.unit, name="HumanBasophilCountRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord001_unit, domain=HumanBasophilCountRecord001, range=Optional[str])

slots.HumanBasophilCountRecord002_unit = Slot(uri=BDCHM.unit, name="HumanBasophilCountRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountRecord002_unit, domain=HumanBasophilCountRecord002, range=Optional[str])

slots.Human8epiPGF2aUrineRecord_measurement_value = Slot(uri=CMS.measurement_value, name="Human8epiPGF2aUrineRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.Human8epiPGF2aUrineRecord_measurement_value, domain=Human8epiPGF2aUrineRecord, range=Union[dict, "Human8epiPGF2aUrineQuantity"])

slots.Human8epiPGF2aUrineRecord001_unit = Slot(uri=BDCHM.unit, name="Human8epiPGF2aUrineRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.Human8epiPGF2aUrineRecord001_unit, domain=Human8epiPGF2aUrineRecord001, range=Optional[str])

slots.HumanLPPLA2ActivityBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanLPPLA2ActivityBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLPPLA2ActivityBloodRecord_measurement_value, domain=HumanLPPLA2ActivityBloodRecord, range=Union[dict, "HumanLPPLA2ActivityBloodQuantity"])

slots.HumanCreatinineUrineRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanCreatinineUrineRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCreatinineUrineRecord_measurement_value, domain=HumanCreatinineUrineRecord, range=Union[dict, "HumanCreatinineUrineQuantity"])

slots.HumanCreatinineUrineRecord001_unit = Slot(uri=BDCHM.unit, name="HumanCreatinineUrineRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCreatinineUrineRecord001_unit, domain=HumanCreatinineUrineRecord001, range=Optional[str])

slots.HumanCreatinineUrineRecord002_unit = Slot(uri=BDCHM.unit, name="HumanCreatinineUrineRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCreatinineUrineRecord002_unit, domain=HumanCreatinineUrineRecord002, range=Optional[str])

slots.HumanAlbuminUrineRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAlbuminUrineRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord_measurement_value, domain=HumanAlbuminUrineRecord, range=Union[dict, "HumanAlbuminUrineQuantity"])

slots.HumanAlbuminUrineRecord001_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAlbuminUrineRecord001_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord001_measurement_value, domain=HumanAlbuminUrineRecord001, range=Union[dict, "HumanAlbuminUrineQuantity001"])

slots.HumanAlbuminUrineRecord001_unit = Slot(uri=BDCHM.unit, name="HumanAlbuminUrineRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord001_unit, domain=HumanAlbuminUrineRecord001, range=Optional[str])

slots.HumanAlbuminUrineRecord001_method = Slot(uri=BDCHM.method_type, name="HumanAlbuminUrineRecord001_method", curie=BDCHM.curie('method_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord001_method, domain=HumanAlbuminUrineRecord001, range=Optional[Union[str, "MethodEnum"]])

slots.HumanAlbuminUrineRecord002_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAlbuminUrineRecord002_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord002_measurement_value, domain=HumanAlbuminUrineRecord002, range=Union[dict, "HumanAlbuminUrineQuantity002"])

slots.HumanAlbuminUrineRecord002_unit = Slot(uri=BDCHM.unit, name="HumanAlbuminUrineRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord002_unit, domain=HumanAlbuminUrineRecord002, range=Optional[str])

slots.HumanAlbuminUrineRecord002_method = Slot(uri=BDCHM.method_type, name="HumanAlbuminUrineRecord002_method", curie=BDCHM.curie('method_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord002_method, domain=HumanAlbuminUrineRecord002, range=Optional[Union[str, "MethodEnum"]])

slots.HumanAlbuminUrineRecord003_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAlbuminUrineRecord003_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord003_measurement_value, domain=HumanAlbuminUrineRecord003, range=Union[dict, "HumanAlbuminUrineQuantity003"])

slots.HumanAlbuminUrineRecord003_unit = Slot(uri=BDCHM.unit, name="HumanAlbuminUrineRecord003_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord003_unit, domain=HumanAlbuminUrineRecord003, range=Optional[str])

slots.HumanAlbuminUrineRecord003_method = Slot(uri=BDCHM.method_type, name="HumanAlbuminUrineRecord003_method", curie=BDCHM.curie('method_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord003_method, domain=HumanAlbuminUrineRecord003, range=Optional[Union[str, "MethodEnum"]])

slots.HumanAlbuminUrineRecord004_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAlbuminUrineRecord004_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord004_measurement_value, domain=HumanAlbuminUrineRecord004, range=Union[dict, "HumanAlbuminUrineQuantity004"])

slots.HumanAlbuminUrineRecord004_unit = Slot(uri=BDCHM.unit, name="HumanAlbuminUrineRecord004_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord004_unit, domain=HumanAlbuminUrineRecord004, range=Optional[str])

slots.HumanAlbuminUrineRecord004_method = Slot(uri=BDCHM.method_type, name="HumanAlbuminUrineRecord004_method", curie=BDCHM.curie('method_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord004_method, domain=HumanAlbuminUrineRecord004, range=Optional[Union[str, "MethodEnum"]])

slots.HumanAlbuminUrineRecord005_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAlbuminUrineRecord005_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord005_measurement_value, domain=HumanAlbuminUrineRecord005, range=Union[dict, "HumanAlbuminUrineQuantity005"])

slots.HumanAlbuminUrineRecord005_unit = Slot(uri=BDCHM.unit, name="HumanAlbuminUrineRecord005_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord005_unit, domain=HumanAlbuminUrineRecord005, range=Optional[str])

slots.HumanAlbuminUrineRecord005_method = Slot(uri=BDCHM.method_type, name="HumanAlbuminUrineRecord005_method", curie=BDCHM.curie('method_type'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineRecord005_method, domain=HumanAlbuminUrineRecord005, range=Optional[Union[str, "MethodEnum"]])

slots.HumanAlbuminCreatinineRatioUrineRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAlbuminCreatinineRatioUrineRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminCreatinineRatioUrineRecord_measurement_value, domain=HumanAlbuminCreatinineRatioUrineRecord, range=Union[dict, "HumanAlbuminCreatinineRatioUrineQuantity"])

slots.ApneaHypopneaIndexRecord_measurement_value = Slot(uri=CMS.measurement_value, name="ApneaHypopneaIndexRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.ApneaHypopneaIndexRecord_measurement_value, domain=ApneaHypopneaIndexRecord, range=Union[dict, "ApneaHypopneaIndexQuantity"])

slots.HumanAlbuminBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAlbuminBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminBloodRecord_measurement_value, domain=HumanAlbuminBloodRecord, range=Union[dict, "HumanAlbuminBloodQuantity"])

slots.AlcoholConsumptionRecord_measurement_value = Slot(uri=CMS.measurement_value, name="AlcoholConsumptionRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.AlcoholConsumptionRecord_measurement_value, domain=AlcoholConsumptionRecord, range=Union[dict, "AlcoholConsumptionQuantity"])

slots.HumanAltSgptRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAltSgptRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAltSgptRecord_measurement_value, domain=HumanAltSgptRecord, range=Union[dict, "HumanAltSgptQuantity"])

slots.HumanAstSgotRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanAstSgotRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAstSgotRecord_measurement_value, domain=HumanAstSgotRecord, range=Union[dict, "HumanAstSgotQuantity"])

slots.HumanBilirubinConjugatedRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBilirubinConjugatedRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBilirubinConjugatedRecord_measurement_value, domain=HumanBilirubinConjugatedRecord, range=Union[dict, "HumanBilirubinConjugatedQuantity"])

slots.HumanBilirubinTotalRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBilirubinTotalRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBilirubinTotalRecord_measurement_value, domain=HumanBilirubinTotalRecord, range=Union[dict, "HumanBilirubinTotalQuantity"])

slots.HumanBNPRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBNPRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBNPRecord_measurement_value, domain=HumanBNPRecord, range=Union[dict, "HumanBNPQuantity"])

slots.HumanBloodUreaNitrogenRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBloodUreaNitrogenRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBloodUreaNitrogenRecord_measurement_value, domain=HumanBloodUreaNitrogenRecord, range=Union[dict, "HumanBloodUreaNitrogenQuantity"])

slots.HumanBUNCreatinineRatioRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBUNCreatinineRatioRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBUNCreatinineRatioRecord_measurement_value, domain=HumanBUNCreatinineRatioRecord, range=Union[dict, "HumanBUNCreatinineRatioQuantity"])

slots.HumanCReactiveProteinRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanCReactiveProteinRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCReactiveProteinRecord_measurement_value, domain=HumanCReactiveProteinRecord, range=Union[dict, "HumanCReactiveProteinQuantity"])

slots.HumanCReactiveProteinRecord001_unit = Slot(uri=BDCHM.unit, name="HumanCReactiveProteinRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCReactiveProteinRecord001_unit, domain=HumanCReactiveProteinRecord001, range=Optional[str])

slots.HumanCReactiveProteinRecord002_unit = Slot(uri=BDCHM.unit, name="HumanCReactiveProteinRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCReactiveProteinRecord002_unit, domain=HumanCReactiveProteinRecord002, range=Optional[str])

slots.HumanCReactiveProteinRecord003_unit = Slot(uri=BDCHM.unit, name="HumanCReactiveProteinRecord003_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCReactiveProteinRecord003_unit, domain=HumanCReactiveProteinRecord003, range=Optional[str])

slots.CoronaryArteryCalciumScoreRecord_measurement_value = Slot(uri=CMS.measurement_value, name="CoronaryArteryCalciumScoreRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CoronaryArteryCalciumScoreRecord_measurement_value, domain=CoronaryArteryCalciumScoreRecord, range=Union[dict, "CoronaryArteryCalciumScoreQuantity"])

slots.CoronaryArteryCalciumVolumeRecord_measurement_value = Slot(uri=CMS.measurement_value, name="CoronaryArteryCalciumVolumeRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CoronaryArteryCalciumVolumeRecord_measurement_value, domain=CoronaryArteryCalciumVolumeRecord, range=Union[dict, "CoronaryArteryCalciumVolumeQuantity"])

slots.CarotidIntimamediaThicknessRecord_measurement_value = Slot(uri=CMS.measurement_value, name="CarotidIntimamediaThicknessRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CarotidIntimamediaThicknessRecord_measurement_value, domain=CarotidIntimamediaThicknessRecord, range=Union[dict, "CarotidIntimamediaThicknessQuantity"])

slots.CarotidStenosisLeftRecord_measurement_value = Slot(uri=CMS.measurement_value, name="CarotidStenosisLeftRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CarotidStenosisLeftRecord_measurement_value, domain=CarotidStenosisLeftRecord, range=Union[dict, "CarotidStenosisQuantity"])

slots.CarotidStenosisRightRecord_measurement_value = Slot(uri=CMS.measurement_value, name="CarotidStenosisRightRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CarotidStenosisRightRecord_measurement_value, domain=CarotidStenosisRightRecord, range=Union[dict, "CarotidStenosisQuantity"])

slots.HumanCD40BloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanCD40BloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCD40BloodRecord_measurement_value, domain=HumanCD40BloodRecord, range=Union[dict, "HumanCD40BloodQuantity"])

slots.CESDScoreRecord_measurement_value = Slot(uri=CMS.measurement_value, name="CESDScoreRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CESDScoreRecord_measurement_value, domain=CESDScoreRecord, range=Union[dict, "CESDScoreQuantity"])

slots.HumanChlorideBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanChlorideBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanChlorideBloodRecord_measurement_value, domain=HumanChlorideBloodRecord, range=Union[dict, "HumanChlorideBloodQuantity"])

slots.HumanChlorideBloodRecord001_unit = Slot(uri=BDCHM.unit, name="HumanChlorideBloodRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanChlorideBloodRecord001_unit, domain=HumanChlorideBloodRecord001, range=Optional[str])

slots.HumanChlorideBloodRecord002_unit = Slot(uri=BDCHM.unit, name="HumanChlorideBloodRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanChlorideBloodRecord002_unit, domain=HumanChlorideBloodRecord002, range=Optional[str])

slots.HumanCreatinineBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanCreatinineBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCreatinineBloodRecord_measurement_value, domain=HumanCreatinineBloodRecord, range=Union[dict, "HumanCreatinineBloodQuantity"])

slots.HumanCystatinCBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanCystatinCBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCystatinCBloodRecord_measurement_value, domain=HumanCystatinCBloodRecord, range=Union[dict, "HumanCystatinCBloodQuantity"])

slots.HumanDDimerRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanDDimerRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanDDimerRecord_measurement_value, domain=HumanDDimerRecord, range=Union[dict, "HumanDDimerQuantity"])

slots.HumanDDimerRecord001_unit = Slot(uri=BDCHM.unit, name="HumanDDimerRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanDDimerRecord001_unit, domain=HumanDDimerRecord001, range=Optional[str])

slots.HumanDDimerRecord002_unit = Slot(uri=BDCHM.unit, name="HumanDDimerRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanDDimerRecord002_unit, domain=HumanDDimerRecord002, range=Optional[str])

slots.HumanDiastolicBloodPressureRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanDiastolicBloodPressureRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanDiastolicBloodPressureRecord_measurement_value, domain=HumanDiastolicBloodPressureRecord, range=Union[dict, "HumanDiastolicBloodPressureQuantity"])

slots.HumanESelectinBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanESelectinBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanESelectinBloodRecord_measurement_value, domain=HumanESelectinBloodRecord, range=Union[dict, "HumanESelectinBloodQuantity"])

slots.HumanEstimatedGFRRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanEstimatedGFRRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanEstimatedGFRRecord_measurement_value, domain=HumanEstimatedGFRRecord, range=Union[dict, "HumanEstimatedGFRQuantity"])

slots.HumanEosinophilCountRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanEosinophilCountRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanEosinophilCountRecord_measurement_value, domain=HumanEosinophilCountRecord, range=Union[dict, "HumanEosinophilCountQuantity"])

slots.HumanFactorVIIRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFactorVIIRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFactorVIIRecord_measurement_value, domain=HumanFactorVIIRecord, range=Union[dict, "HumanFactorVIIQuantity"])

slots.HumanFactorVIIIRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFactorVIIIRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFactorVIIIRecord_measurement_value, domain=HumanFactorVIIIRecord, range=Union[dict, "HumanFactorVIIIQuantity"])

slots.HumanFastingGlucoseRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFastingGlucoseRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFastingGlucoseRecord_measurement_value, domain=HumanFastingGlucoseRecord, range=Union[dict, "HumanFastingGlucoseQuantity"])

slots.HumanFastingGlucoseRecord001_unit = Slot(uri=BDCHM.unit, name="HumanFastingGlucoseRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFastingGlucoseRecord001_unit, domain=HumanFastingGlucoseRecord001, range=Optional[str])

slots.HumanFastingGlucoseRecord002_unit = Slot(uri=BDCHM.unit, name="HumanFastingGlucoseRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFastingGlucoseRecord002_unit, domain=HumanFastingGlucoseRecord002, range=Optional[str])

slots.HumanFerritinRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFerritinRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFerritinRecord_measurement_value, domain=HumanFerritinRecord, range=Union[dict, "HumanFerritinQuantity"])

slots.HumanFEV1FVCRatioRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFEV1FVCRatioRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFEV1FVCRatioRecord_measurement_value, domain=HumanFEV1FVCRatioRecord, range=Union[dict, "HumanFEV1FVCRatioQuantity"])

slots.HumanFEV1FVCRatioRecord001_unit = Slot(uri=BDCHM.unit, name="HumanFEV1FVCRatioRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFEV1FVCRatioRecord001_unit, domain=HumanFEV1FVCRatioRecord001, range=Optional[str])

slots.HumanFEV1FVCRatioRecord002_unit = Slot(uri=BDCHM.unit, name="HumanFEV1FVCRatioRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFEV1FVCRatioRecord002_unit, domain=HumanFEV1FVCRatioRecord002, range=Optional[str])

slots.HumanPredictedFEV1FVCRatioRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPredictedFEV1FVCRatioRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPredictedFEV1FVCRatioRecord_measurement_value, domain=HumanPredictedFEV1FVCRatioRecord, range=Union[dict, "HumanPredictedFEV1FVCRatioQuantity"])

slots.HumanPercentPredictedFEV1FVCRatioRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPercentPredictedFEV1FVCRatioRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPercentPredictedFEV1FVCRatioRecord_measurement_value, domain=HumanPercentPredictedFEV1FVCRatioRecord, range=Union[dict, "HumanPercentPredictedFEV1FVCRatioQuantity"])

slots.HumanFibrinogenRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanFibrinogenRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFibrinogenRecord_measurement_value, domain=HumanFibrinogenRecord, range=Union[dict, "HumanFibrinogenQuantity"])

slots.FruitConsumptionRecord_measurement_value = Slot(uri=CMS.measurement_value, name="FruitConsumptionRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.FruitConsumptionRecord_measurement_value, domain=FruitConsumptionRecord, range=Union[dict, "FruitConsumptionQuantity"])

slots.HumanGFRRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanGFRRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanGFRRecord_measurement_value, domain=HumanGFRRecord, range=Union[dict, "HumanGFRQuantity"])

slots.HumanGlucoseBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanGlucoseBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanGlucoseBloodRecord_measurement_value, domain=HumanGlucoseBloodRecord, range=Union[dict, "HumanGlucoseBloodQuantity"])

slots.HumanHDLRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanHDLRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHDLRecord_measurement_value, domain=HumanHDLRecord, range=Union[dict, "HumanHDLQuantity"])

slots.HumanHDLRecord001_unit = Slot(uri=BDCHM.unit, name="HumanHDLRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHDLRecord001_unit, domain=HumanHDLRecord001, range=Optional[str])

slots.HumanHDLRecord002_unit = Slot(uri=BDCHM.unit, name="HumanHDLRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHDLRecord002_unit, domain=HumanHDLRecord002, range=Optional[str])

slots.HumanHeartRateRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanHeartRateRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHeartRateRecord_measurement_value, domain=HumanHeartRateRecord, range=Union[dict, "HumanHeartRateQuantity"])

slots.HumanHematocritRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanHematocritRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHematocritRecord_measurement_value, domain=HumanHematocritRecord, range=Union[dict, "HumanHematocritQuantity"])

slots.HumanHemoglobinRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanHemoglobinRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHemoglobinRecord_measurement_value, domain=HumanHemoglobinRecord, range=Union[dict, "HumanHemoglobinQuantity"])

slots.HumanHemoglobinA1cRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanHemoglobinA1cRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHemoglobinA1cRecord_measurement_value, domain=HumanHemoglobinA1cRecord, range=Union[dict, "HumanHemoglobinA1cQuantity"])

slots.HumanHipCircumferenceRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanHipCircumferenceRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHipCircumferenceRecord_measurement_value, domain=HumanHipCircumferenceRecord, range=Union[dict, "HumanHipCircumferenceQuantity"])

slots.HumanHipCircumferenceRecord001_unit = Slot(uri=BDCHM.unit, name="HumanHipCircumferenceRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHipCircumferenceRecord001_unit, domain=HumanHipCircumferenceRecord001, range=Optional[str])

slots.HumanHipCircumferenceRecord002_unit = Slot(uri=BDCHM.unit, name="HumanHipCircumferenceRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHipCircumferenceRecord002_unit, domain=HumanHipCircumferenceRecord002, range=Optional[str])

slots.HumanICAM1BloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanICAM1BloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanICAM1BloodRecord_measurement_value, domain=HumanICAM1BloodRecord, range=Union[dict, "HumanICAM1BloodQuantity"])

slots.HumanInsulinBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanInsulinBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInsulinBloodRecord_measurement_value, domain=HumanInsulinBloodRecord, range=Union[dict, "HumanInsulinBloodQuantity"])

slots.HumanInsulinBloodRecord001_unit = Slot(uri=BDCHM.unit, name="HumanInsulinBloodRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInsulinBloodRecord001_unit, domain=HumanInsulinBloodRecord001, range=Optional[str])

slots.HumanInsulinBloodRecord002_unit = Slot(uri=BDCHM.unit, name="HumanInsulinBloodRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInsulinBloodRecord002_unit, domain=HumanInsulinBloodRecord002, range=Optional[str])

slots.HumanInterleukin18BloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanInterleukin18BloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInterleukin18BloodRecord_measurement_value, domain=HumanInterleukin18BloodRecord, range=Union[dict, "HumanInterleukin18BloodQuantity"])

slots.HumanInterleukin1BetaBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanInterleukin1BetaBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInterleukin1BetaBloodRecord_measurement_value, domain=HumanInterleukin1BetaBloodRecord, range=Union[dict, "HumanInterleukin1BetaBloodQuantity"])

slots.HumanInterleukin10BloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanInterleukin10BloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInterleukin10BloodRecord_measurement_value, domain=HumanInterleukin10BloodRecord, range=Union[dict, "HumanInterleukin10BloodQuantity"])

slots.HumanInterleukin6BloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanInterleukin6BloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInterleukin6BloodRecord_measurement_value, domain=HumanInterleukin6BloodRecord, range=Union[dict, "HumanInterleukin6BloodQuantity"])

slots.HumanLactateDehydrogenaseRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanLactateDehydrogenaseRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLactateDehydrogenaseRecord_measurement_value, domain=HumanLactateDehydrogenaseRecord, range=Union[dict, "HumanLactateDehydrogenaseQuantity"])

slots.HumanLactateBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanLactateBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLactateBloodRecord_measurement_value, domain=HumanLactateBloodRecord, range=Union[dict, "HumanLactateBloodQuantity"])

slots.HumanLDLRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanLDLRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLDLRecord_measurement_value, domain=HumanLDLRecord, range=Union[dict, "HumanLDLQuantity"])

slots.HumanLymphocyteCountRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanLymphocyteCountRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLymphocyteCountRecord_measurement_value, domain=HumanLymphocyteCountRecord, range=Union[dict, "HumanLymphocyteCountQuantity"])

slots.HumanLymphocytePercentRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanLymphocytePercentRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLymphocytePercentRecord_measurement_value, domain=HumanLymphocytePercentRecord, range=Union[dict, "HumanLymphocytePercentQuantity"])

slots.HumanLPPLA2MassBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanLPPLA2MassBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLPPLA2MassBloodRecord_measurement_value, domain=HumanLPPLA2MassBloodRecord, range=Union[dict, "HumanLPPLA2MassBloodQuantity"])

slots.HumanMCP1BloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMCP1BloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMCP1BloodRecord_measurement_value, domain=HumanMCP1BloodRecord, range=Union[dict, "HumanMCP1BloodQuantity"])

slots.HumanMeanArterialPressureRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMeanArterialPressureRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMeanArterialPressureRecord_measurement_value, domain=HumanMeanArterialPressureRecord, range=Union[dict, "HumanMeanArterialPressureQuantity"])

slots.HumanMCHRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMCHRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMCHRecord_measurement_value, domain=HumanMCHRecord, range=Union[dict, "HumanMCHQuantity"])

slots.HumanMCHCRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMCHCRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMCHCRecord_measurement_value, domain=HumanMCHCRecord, range=Union[dict, "HumanMCHCQuantity"])

slots.HumanMCVRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMCVRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMCVRecord_measurement_value, domain=HumanMCVRecord, range=Union[dict, "HumanMCVQuantity"])

slots.HumanMPVRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMPVRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMPVRecord_measurement_value, domain=HumanMPVRecord, range=Union[dict, "HumanMPVQuantity"])

slots.HumanMMP9BloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMMP9BloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMMP9BloodRecord_measurement_value, domain=HumanMMP9BloodRecord, range=Union[dict, "HumanMMP9BloodQuantity"])

slots.HumanMonocyteCountRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMonocyteCountRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMonocyteCountRecord_measurement_value, domain=HumanMonocyteCountRecord, range=Union[dict, "HumanMonocyteCountQuantity"])

slots.HumanMyeloperoxidaseBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanMyeloperoxidaseBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMyeloperoxidaseBloodRecord_measurement_value, domain=HumanMyeloperoxidaseBloodRecord, range=Union[dict, "HumanMyeloperoxidaseBloodQuantity"])

slots.HumanNeutrophilCountRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanNeutrophilCountRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanNeutrophilCountRecord_measurement_value, domain=HumanNeutrophilCountRecord, range=Union[dict, "HumanNeutrophilCountQuantity"])

slots.HumanNeutrophilPercentRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanNeutrophilPercentRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanNeutrophilPercentRecord_measurement_value, domain=HumanNeutrophilPercentRecord, range=Union[dict, "HumanNeutrophilPercentQuantity"])

slots.HumanNTproBNPRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanNTproBNPRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanNTproBNPRecord_measurement_value, domain=HumanNTproBNPRecord, range=Union[dict, "HumanNTproBNPQuantity"])

slots.HumanOsteoprotegerinBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanOsteoprotegerinBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanOsteoprotegerinBloodRecord_measurement_value, domain=HumanOsteoprotegerinBloodRecord, range=Union[dict, "HumanOsteoprotegerinBloodQuantity"])

slots.HumanPSelectinBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPSelectinBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPSelectinBloodRecord_measurement_value, domain=HumanPSelectinBloodRecord, range=Union[dict, "HumanPSelectinBloodQuantity"])

slots.HumanPlateletCountRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPlateletCountRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPlateletCountRecord_measurement_value, domain=HumanPlateletCountRecord, range=Union[dict, "HumanPlateletCountQuantity"])

slots.HumanPotassiumBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPotassiumBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPotassiumBloodRecord_measurement_value, domain=HumanPotassiumBloodRecord, range=Union[dict, "HumanPotassiumBloodQuantity"])

slots.HumanPRIntervalRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanPRIntervalRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPRIntervalRecord_measurement_value, domain=HumanPRIntervalRecord, range=Union[dict, "HumanPRIntervalQuantity"])

slots.HumanQRSIntervalRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanQRSIntervalRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanQRSIntervalRecord_measurement_value, domain=HumanQRSIntervalRecord, range=Union[dict, "HumanQRSIntervalQuantity"])

slots.HumanQTIntervalRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanQTIntervalRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanQTIntervalRecord_measurement_value, domain=HumanQTIntervalRecord, range=Union[dict, "HumanQTIntervalQuantity"])

slots.HumanRBCCountRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanRBCCountRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanRBCCountRecord_measurement_value, domain=HumanRBCCountRecord, range=Union[dict, "HumanRBCCountQuantity"])

slots.HumanRDWRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanRDWRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanRDWRecord_measurement_value, domain=HumanRDWRecord, range=Union[dict, "HumanRDWQuantity"])

slots.HumanSleepDurationRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanSleepDurationRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanSleepDurationRecord_measurement_value, domain=HumanSleepDurationRecord, range=Union[dict, "HumanSleepDurationQuantity"])

slots.HumanSodiumBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanSodiumBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanSodiumBloodRecord_measurement_value, domain=HumanSodiumBloodRecord, range=Union[dict, "HumanSodiumBloodQuantity"])

slots.SodiumIntakeRecord_measurement_value = Slot(uri=CMS.measurement_value, name="SodiumIntakeRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.SodiumIntakeRecord_measurement_value, domain=SodiumIntakeRecord, range=Union[dict, "SodiumIntakeQuantity"])

slots.HumanSpO2Record_measurement_value = Slot(uri=CMS.measurement_value, name="HumanSpO2Record_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanSpO2Record_measurement_value, domain=HumanSpO2Record, range=Union[dict, "HumanSpO2Quantity"])

slots.HumanSystolicBloodPressureRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanSystolicBloodPressureRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanSystolicBloodPressureRecord_measurement_value, domain=HumanSystolicBloodPressureRecord, range=Union[dict, "HumanSystolicBloodPressureQuantity"])

slots.HumanBodyTemperatureRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanBodyTemperatureRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyTemperatureRecord_measurement_value, domain=HumanBodyTemperatureRecord, range=Union[dict, "HumanBodyTemperatureQuantity"])

slots.HumanTNFAlphaBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanTNFAlphaBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTNFAlphaBloodRecord_measurement_value, domain=HumanTNFAlphaBloodRecord, range=Union[dict, "HumanTNFAlphaBloodQuantity"])

slots.HumanTNFAlphaR1BloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanTNFAlphaR1BloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTNFAlphaR1BloodRecord_measurement_value, domain=HumanTNFAlphaR1BloodRecord, range=Union[dict, "HumanTNFAlphaR1BloodQuantity"])

slots.HumanTotalCholesterolRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanTotalCholesterolRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTotalCholesterolRecord_measurement_value, domain=HumanTotalCholesterolRecord, range=Union[dict, "HumanTotalCholesterolQuantity"])

slots.HumanTotalCholesterolRecord001_unit = Slot(uri=BDCHM.unit, name="HumanTotalCholesterolRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTotalCholesterolRecord001_unit, domain=HumanTotalCholesterolRecord001, range=Optional[str])

slots.HumanTotalCholesterolRecord002_unit = Slot(uri=BDCHM.unit, name="HumanTotalCholesterolRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTotalCholesterolRecord002_unit, domain=HumanTotalCholesterolRecord002, range=Optional[str])

slots.HumanTriglyceridesBloodRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanTriglyceridesBloodRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTriglyceridesBloodRecord_measurement_value, domain=HumanTriglyceridesBloodRecord, range=Union[dict, "HumanTriglyceridesBloodQuantity"])

slots.HumanTriglyceridesBloodRecord001_unit = Slot(uri=BDCHM.unit, name="HumanTriglyceridesBloodRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTriglyceridesBloodRecord001_unit, domain=HumanTriglyceridesBloodRecord001, range=Optional[str])

slots.HumanTriglyceridesBloodRecord002_unit = Slot(uri=BDCHM.unit, name="HumanTriglyceridesBloodRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTriglyceridesBloodRecord002_unit, domain=HumanTriglyceridesBloodRecord002, range=Optional[str])

slots.HumanTroponinRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanTroponinRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTroponinRecord_measurement_value, domain=HumanTroponinRecord, range=Union[dict, "HumanTroponinQuantity"])

slots.VegetableConsumptionRecord_measurement_value = Slot(uri=CMS.measurement_value, name="VegetableConsumptionRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.VegetableConsumptionRecord_measurement_value, domain=VegetableConsumptionRecord, range=Union[dict, "VegetableConsumptionQuantity"])

slots.HumanVonWillebrandFactorRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanVonWillebrandFactorRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanVonWillebrandFactorRecord_measurement_value, domain=HumanVonWillebrandFactorRecord, range=Union[dict, "HumanVonWillebrandFactorQuantity"])

slots.HumanWaistCircumferenceRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanWaistCircumferenceRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceRecord_measurement_value, domain=HumanWaistCircumferenceRecord, range=Union[dict, "HumanWaistCircumferenceQuantity"])

slots.HumanWaistCircumferenceRecord001_unit = Slot(uri=BDCHM.unit, name="HumanWaistCircumferenceRecord001_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceRecord001_unit, domain=HumanWaistCircumferenceRecord001, range=Optional[str])

slots.HumanWaistCircumferenceRecord002_unit = Slot(uri=BDCHM.unit, name="HumanWaistCircumferenceRecord002_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceRecord002_unit, domain=HumanWaistCircumferenceRecord002, range=Optional[str])

slots.HumanWaistCircumferenceRecord003_unit = Slot(uri=BDCHM.unit, name="HumanWaistCircumferenceRecord003_unit", curie=BDCHM.curie('unit'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceRecord003_unit, domain=HumanWaistCircumferenceRecord003, range=Optional[str])

slots.HumanWaistHipRatioRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanWaistHipRatioRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanWaistHipRatioRecord_measurement_value, domain=HumanWaistHipRatioRecord, range=Union[dict, "HumanWaistHipRatioQuantity"])

slots.HumanWhiteBloodCellCountRecord_measurement_value = Slot(uri=CMS.measurement_value, name="HumanWhiteBloodCellCountRecord_measurement_value", curie=CMS.curie('measurement_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanWhiteBloodCellCountRecord_measurement_value, domain=HumanWhiteBloodCellCountRecord, range=Union[dict, "HumanWBCCountQuantity"])

slots.AsthmaStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="AsthmaStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.AsthmaStatusRecord_condition_type, domain=AsthmaStatusRecord, range=Union[str, URIorCURIE])

slots.HeartFailureStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="HeartFailureStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.HeartFailureStatusRecord_condition_type, domain=HeartFailureStatusRecord, range=Union[str, URIorCURIE])

slots.ObesityStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="ObesityStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.ObesityStatusRecord_condition_type, domain=ObesityStatusRecord, range=Union[str, URIorCURIE])

slots.AtrialFibrillationStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="AtrialFibrillationStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.AtrialFibrillationStatusRecord_condition_type, domain=AtrialFibrillationStatusRecord, range=Union[str, URIorCURIE])

slots.AnginaStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="AnginaStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.AnginaStatusRecord_condition_type, domain=AnginaStatusRecord, range=Union[str, URIorCURIE])

slots.CardiovascularDiseaseStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="CardiovascularDiseaseStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.CardiovascularDiseaseStatusRecord_condition_type, domain=CardiovascularDiseaseStatusRecord, range=Union[str, URIorCURIE])

slots.CarotidPlaqueStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="CarotidPlaqueStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.CarotidPlaqueStatusRecord_condition_type, domain=CarotidPlaqueStatusRecord, range=Union[str, URIorCURIE])

slots.COPDStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="COPDStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.COPDStatusRecord_condition_type, domain=COPDStatusRecord, range=Union[str, URIorCURIE])

slots.DiabetesStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="DiabetesStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.DiabetesStatusRecord_condition_type, domain=DiabetesStatusRecord, range=Union[str, URIorCURIE])

slots.StrokeStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="StrokeStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.StrokeStatusRecord_condition_type, domain=StrokeStatusRecord, range=Union[str, URIorCURIE])

slots.HeartDiseaseStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="HeartDiseaseStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.HeartDiseaseStatusRecord_condition_type, domain=HeartDiseaseStatusRecord, range=Union[str, URIorCURIE])

slots.MyocardialInfarctionStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="MyocardialInfarctionStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.MyocardialInfarctionStatusRecord_condition_type, domain=MyocardialInfarctionStatusRecord, range=Union[str, URIorCURIE])

slots.HypertensionStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="HypertensionStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.HypertensionStatusRecord_condition_type, domain=HypertensionStatusRecord, range=Union[str, URIorCURIE])

slots.LeftVentricularHypertrophyStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="LeftVentricularHypertrophyStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.LeftVentricularHypertrophyStatusRecord_condition_type, domain=LeftVentricularHypertrophyStatusRecord, range=Union[str, URIorCURIE])

slots.PeripheralArterialDiseaseStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="PeripheralArterialDiseaseStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.PeripheralArterialDiseaseStatusRecord_condition_type, domain=PeripheralArterialDiseaseStatusRecord, range=Union[str, URIorCURIE])

slots.SleepApneaStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="SleepApneaStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.SleepApneaStatusRecord_condition_type, domain=SleepApneaStatusRecord, range=Union[str, URIorCURIE])

slots.ValvularHeartDiseaseStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="ValvularHeartDiseaseStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.ValvularHeartDiseaseStatusRecord_condition_type, domain=ValvularHeartDiseaseStatusRecord, range=Union[str, URIorCURIE])

slots.VenousThromboembolismStatusRecord_condition_type = Slot(uri=BDCHM.condition_concept, name="VenousThromboembolismStatusRecord_condition_type", curie=BDCHM.curie('condition_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.VenousThromboembolismStatusRecord_condition_type, domain=VenousThromboembolismStatusRecord, range=Union[str, URIorCURIE])

slots.AspirinStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="AspirinStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.AspirinStatusRecord_drug_type, domain=AspirinStatusRecord, range=Union[str, URIorCURIE])

slots.BetaBlockerStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="BetaBlockerStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.BetaBlockerStatusRecord_drug_type, domain=BetaBlockerStatusRecord, range=Union[str, URIorCURIE])

slots.DiabetesMedicationStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="DiabetesMedicationStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.DiabetesMedicationStatusRecord_drug_type, domain=DiabetesMedicationStatusRecord, range=Union[str, URIorCURIE])

slots.HypertensionMedicationStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="HypertensionMedicationStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.HypertensionMedicationStatusRecord_drug_type, domain=HypertensionMedicationStatusRecord, range=Union[str, URIorCURIE])

slots.AceInhibitorStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="AceInhibitorStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.AceInhibitorStatusRecord_drug_type, domain=AceInhibitorStatusRecord, range=Union[str, URIorCURIE])

slots.AldosteroneReceptorBlockerStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="AldosteroneReceptorBlockerStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.AldosteroneReceptorBlockerStatusRecord_drug_type, domain=AldosteroneReceptorBlockerStatusRecord, range=Union[str, URIorCURIE])

slots.AlphaBlockerStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="AlphaBlockerStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.AlphaBlockerStatusRecord_drug_type, domain=AlphaBlockerStatusRecord, range=Union[str, URIorCURIE])

slots.AngiotensinReceptorBlockerStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="AngiotensinReceptorBlockerStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.AngiotensinReceptorBlockerStatusRecord_drug_type, domain=AngiotensinReceptorBlockerStatusRecord, range=Union[str, URIorCURIE])

slots.CalciumChannelBlockerStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="CalciumChannelBlockerStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.CalciumChannelBlockerStatusRecord_drug_type, domain=CalciumChannelBlockerStatusRecord, range=Union[str, URIorCURIE])

slots.CentrallyActingAgentsStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="CentrallyActingAgentsStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.CentrallyActingAgentsStatusRecord_drug_type, domain=CentrallyActingAgentsStatusRecord, range=Union[str, URIorCURIE])

slots.DiureticsStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="DiureticsStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.DiureticsStatusRecord_drug_type, domain=DiureticsStatusRecord, range=Union[str, URIorCURIE])

slots.InsulinStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="InsulinStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.InsulinStatusRecord_drug_type, domain=InsulinStatusRecord, range=Union[str, URIorCURIE])

slots.NiacinMedicationStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="NiacinMedicationStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.NiacinMedicationStatusRecord_drug_type, domain=NiacinMedicationStatusRecord, range=Union[str, URIorCURIE])

slots.LipidLoweringMedicationStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="LipidLoweringMedicationStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.LipidLoweringMedicationStatusRecord_drug_type, domain=LipidLoweringMedicationStatusRecord, range=Union[str, URIorCURIE])

slots.FibratesStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="FibratesStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.FibratesStatusRecord_drug_type, domain=FibratesStatusRecord, range=Union[str, URIorCURIE])

slots.BileAcidSequestrantStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="BileAcidSequestrantStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.BileAcidSequestrantStatusRecord_drug_type, domain=BileAcidSequestrantStatusRecord, range=Union[str, URIorCURIE])

slots.OralHypoglycemicAgentStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="OralHypoglycemicAgentStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.OralHypoglycemicAgentStatusRecord_drug_type, domain=OralHypoglycemicAgentStatusRecord, range=Union[str, URIorCURIE])

slots.StatinStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="StatinStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.StatinStatusRecord_drug_type, domain=StatinStatusRecord, range=Union[str, URIorCURIE])

slots.SystemicSteroidStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="SystemicSteroidStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.SystemicSteroidStatusRecord_drug_type, domain=SystemicSteroidStatusRecord, range=Union[str, URIorCURIE])

slots.VasodilatorStatusRecord_drug_type = Slot(uri=BDCHM.drug_concept, name="VasodilatorStatusRecord_drug_type", curie=BDCHM.curie('drug_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.VasodilatorStatusRecord_drug_type, domain=VasodilatorStatusRecord, range=Union[str, URIorCURIE])

slots.PacemakerStatusRecord_procedure_type = Slot(uri=BDCHM.procedure_concept, name="PacemakerStatusRecord_procedure_type", curie=BDCHM.curie('procedure_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.PacemakerStatusRecord_procedure_type, domain=PacemakerStatusRecord, range=Union[str, URIorCURIE])

slots.CoronaryAngioplastyStatusRecord_procedure_type = Slot(uri=BDCHM.procedure_concept, name="CoronaryAngioplastyStatusRecord_procedure_type", curie=BDCHM.curie('procedure_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.CoronaryAngioplastyStatusRecord_procedure_type, domain=CoronaryAngioplastyStatusRecord, range=Union[str, URIorCURIE])

slots.CoronaryBypassStatusRecord_procedure_type = Slot(uri=BDCHM.procedure_concept, name="CoronaryBypassStatusRecord_procedure_type", curie=BDCHM.curie('procedure_concept'),
                   model_uri=BDC_VARIABLE_LIBRARY.CoronaryBypassStatusRecord_procedure_type, domain=CoronaryBypassStatusRecord, range=Union[str, URIorCURIE])

slots.HumanBodyHeightQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyHeightQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyHeightQuantity_quantity_value, domain=HumanBodyHeightQuantity, range=Decimal)

slots.HumanBodyWeightQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyWeightQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyWeightQuantity_quantity_value, domain=HumanBodyWeightQuantity, range=Decimal)

slots.BodyMassIndexQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="BodyMassIndexQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.BodyMassIndexQuantity_quantity_value, domain=BodyMassIndexQuantity, range=Decimal)

slots.HumanFvcQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFvcQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFvcQuantity_quantity_value, domain=HumanFvcQuantity, range=Decimal)

slots.HumanPredictedFvcQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPredictedFvcQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPredictedFvcQuantity_quantity_value, domain=HumanPredictedFvcQuantity, range=Decimal)

slots.HumanPercentPredictedFvcQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPercentPredictedFvcQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPercentPredictedFvcQuantity_quantity_value, domain=HumanPercentPredictedFvcQuantity, range=Decimal)

slots.HumanFev1Quantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFev1Quantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFev1Quantity_quantity_value, domain=HumanFev1Quantity, range=Decimal)

slots.HumanPredictedFev1Quantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPredictedFev1Quantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPredictedFev1Quantity_quantity_value, domain=HumanPredictedFev1Quantity, range=Decimal)

slots.HumanPercentPredictedFev1Quantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPercentPredictedFev1Quantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPercentPredictedFev1Quantity_quantity_value, domain=HumanPercentPredictedFev1Quantity, range=Decimal)

slots.HumanBasophilCountQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBasophilCountQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBasophilCountQuantity_quantity_value, domain=HumanBasophilCountQuantity, range=Decimal)

slots.Human8epiPGF2aUrineQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="Human8epiPGF2aUrineQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.Human8epiPGF2aUrineQuantity_quantity_value, domain=Human8epiPGF2aUrineQuantity, range=Decimal)

slots.HumanLPPLA2ActivityBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanLPPLA2ActivityBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLPPLA2ActivityBloodQuantity_quantity_value, domain=HumanLPPLA2ActivityBloodQuantity, range=Decimal)

slots.HumanCreatinineUrineQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanCreatinineUrineQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCreatinineUrineQuantity_quantity_value, domain=HumanCreatinineUrineQuantity, range=Decimal)

slots.HumanAlbuminUrineQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAlbuminUrineQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity_quantity_value, domain=HumanAlbuminUrineQuantity, range=Decimal)

slots.HumanAlbuminUrineQuantity001_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAlbuminUrineQuantity001_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity001_quantity_value, domain=HumanAlbuminUrineQuantity001, range=Decimal)

slots.HumanAlbuminUrineQuantity002_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAlbuminUrineQuantity002_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity002_quantity_value, domain=HumanAlbuminUrineQuantity002, range=Decimal)

slots.HumanAlbuminUrineQuantity003_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAlbuminUrineQuantity003_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity003_quantity_value, domain=HumanAlbuminUrineQuantity003, range=Decimal)

slots.HumanAlbuminUrineQuantity004_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAlbuminUrineQuantity004_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity004_quantity_value, domain=HumanAlbuminUrineQuantity004, range=Decimal)

slots.HumanAlbuminUrineQuantity005_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAlbuminUrineQuantity005_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminUrineQuantity005_quantity_value, domain=HumanAlbuminUrineQuantity005, range=Decimal)

slots.HumanAlbuminCreatinineRatioUrineQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAlbuminCreatinineRatioUrineQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminCreatinineRatioUrineQuantity_quantity_value, domain=HumanAlbuminCreatinineRatioUrineQuantity, range=Decimal)

slots.ApneaHypopneaIndexQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="ApneaHypopneaIndexQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.ApneaHypopneaIndexQuantity_quantity_value, domain=ApneaHypopneaIndexQuantity, range=Decimal)

slots.HumanAlbuminBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAlbuminBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAlbuminBloodQuantity_quantity_value, domain=HumanAlbuminBloodQuantity, range=Decimal)

slots.AlcoholConsumptionQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="AlcoholConsumptionQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.AlcoholConsumptionQuantity_quantity_value, domain=AlcoholConsumptionQuantity, range=Decimal)

slots.HumanAltSgptQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAltSgptQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAltSgptQuantity_quantity_value, domain=HumanAltSgptQuantity, range=Decimal)

slots.HumanAstSgotQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanAstSgotQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanAstSgotQuantity_quantity_value, domain=HumanAstSgotQuantity, range=Decimal)

slots.HumanBilirubinConjugatedQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBilirubinConjugatedQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBilirubinConjugatedQuantity_quantity_value, domain=HumanBilirubinConjugatedQuantity, range=Decimal)

slots.HumanBilirubinTotalQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBilirubinTotalQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBilirubinTotalQuantity_quantity_value, domain=HumanBilirubinTotalQuantity, range=Decimal)

slots.HumanBNPQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBNPQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBNPQuantity_quantity_value, domain=HumanBNPQuantity, range=Decimal)

slots.HumanBloodUreaNitrogenQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBloodUreaNitrogenQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBloodUreaNitrogenQuantity_quantity_value, domain=HumanBloodUreaNitrogenQuantity, range=Decimal)

slots.HumanBUNCreatinineRatioQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBUNCreatinineRatioQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBUNCreatinineRatioQuantity_quantity_value, domain=HumanBUNCreatinineRatioQuantity, range=Decimal)

slots.HumanCReactiveProteinQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanCReactiveProteinQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCReactiveProteinQuantity_quantity_value, domain=HumanCReactiveProteinQuantity, range=Decimal)

slots.CoronaryArteryCalciumScoreQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="CoronaryArteryCalciumScoreQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CoronaryArteryCalciumScoreQuantity_quantity_value, domain=CoronaryArteryCalciumScoreQuantity, range=Decimal)

slots.CoronaryArteryCalciumVolumeQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="CoronaryArteryCalciumVolumeQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CoronaryArteryCalciumVolumeQuantity_quantity_value, domain=CoronaryArteryCalciumVolumeQuantity, range=Decimal)

slots.CarotidIntimamediaThicknessQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="CarotidIntimamediaThicknessQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CarotidIntimamediaThicknessQuantity_quantity_value, domain=CarotidIntimamediaThicknessQuantity, range=Decimal)

slots.CarotidStenosisQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="CarotidStenosisQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CarotidStenosisQuantity_quantity_value, domain=CarotidStenosisQuantity, range=Decimal)

slots.HumanCD40BloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanCD40BloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCD40BloodQuantity_quantity_value, domain=HumanCD40BloodQuantity, range=Decimal)

slots.CESDScoreQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="CESDScoreQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.CESDScoreQuantity_quantity_value, domain=CESDScoreQuantity, range=Decimal)

slots.HumanChlorideBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanChlorideBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanChlorideBloodQuantity_quantity_value, domain=HumanChlorideBloodQuantity, range=Decimal)

slots.HumanCreatinineBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanCreatinineBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCreatinineBloodQuantity_quantity_value, domain=HumanCreatinineBloodQuantity, range=Decimal)

slots.HumanCystatinCBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanCystatinCBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanCystatinCBloodQuantity_quantity_value, domain=HumanCystatinCBloodQuantity, range=Decimal)

slots.HumanDDimerQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanDDimerQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanDDimerQuantity_quantity_value, domain=HumanDDimerQuantity, range=Decimal)

slots.HumanDiastolicBloodPressureQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanDiastolicBloodPressureQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanDiastolicBloodPressureQuantity_quantity_value, domain=HumanDiastolicBloodPressureQuantity, range=Decimal)

slots.HumanESelectinBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanESelectinBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanESelectinBloodQuantity_quantity_value, domain=HumanESelectinBloodQuantity, range=Decimal)

slots.HumanEstimatedGFRQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanEstimatedGFRQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanEstimatedGFRQuantity_quantity_value, domain=HumanEstimatedGFRQuantity, range=Decimal)

slots.HumanEosinophilCountQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanEosinophilCountQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanEosinophilCountQuantity_quantity_value, domain=HumanEosinophilCountQuantity, range=Decimal)

slots.HumanFactorVIIQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFactorVIIQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFactorVIIQuantity_quantity_value, domain=HumanFactorVIIQuantity, range=Decimal)

slots.HumanFactorVIIIQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFactorVIIIQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFactorVIIIQuantity_quantity_value, domain=HumanFactorVIIIQuantity, range=Decimal)

slots.HumanFastingGlucoseQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFastingGlucoseQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFastingGlucoseQuantity_quantity_value, domain=HumanFastingGlucoseQuantity, range=Decimal)

slots.HumanFerritinQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFerritinQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFerritinQuantity_quantity_value, domain=HumanFerritinQuantity, range=Decimal)

slots.HumanFEV1FVCRatioQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFEV1FVCRatioQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFEV1FVCRatioQuantity_quantity_value, domain=HumanFEV1FVCRatioQuantity, range=Decimal)

slots.HumanPredictedFEV1FVCRatioQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPredictedFEV1FVCRatioQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPredictedFEV1FVCRatioQuantity_quantity_value, domain=HumanPredictedFEV1FVCRatioQuantity, range=Decimal)

slots.HumanPercentPredictedFEV1FVCRatioQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPercentPredictedFEV1FVCRatioQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPercentPredictedFEV1FVCRatioQuantity_quantity_value, domain=HumanPercentPredictedFEV1FVCRatioQuantity, range=Decimal)

slots.HumanFibrinogenQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanFibrinogenQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanFibrinogenQuantity_quantity_value, domain=HumanFibrinogenQuantity, range=Decimal)

slots.FruitConsumptionQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="FruitConsumptionQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.FruitConsumptionQuantity_quantity_value, domain=FruitConsumptionQuantity, range=Decimal)

slots.HumanGFRQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanGFRQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanGFRQuantity_quantity_value, domain=HumanGFRQuantity, range=Decimal)

slots.HumanGlucoseBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanGlucoseBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanGlucoseBloodQuantity_quantity_value, domain=HumanGlucoseBloodQuantity, range=Decimal)

slots.HumanHDLQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanHDLQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHDLQuantity_quantity_value, domain=HumanHDLQuantity, range=Decimal)

slots.HumanHeartRateQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanHeartRateQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHeartRateQuantity_quantity_value, domain=HumanHeartRateQuantity, range=Decimal)

slots.HumanHematocritQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanHematocritQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHematocritQuantity_quantity_value, domain=HumanHematocritQuantity, range=Decimal)

slots.HumanHemoglobinQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanHemoglobinQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHemoglobinQuantity_quantity_value, domain=HumanHemoglobinQuantity, range=Decimal)

slots.HumanHemoglobinA1cQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanHemoglobinA1cQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHemoglobinA1cQuantity_quantity_value, domain=HumanHemoglobinA1cQuantity, range=Decimal)

slots.HumanHipCircumferenceQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanHipCircumferenceQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanHipCircumferenceQuantity_quantity_value, domain=HumanHipCircumferenceQuantity, range=Decimal)

slots.HumanICAM1BloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanICAM1BloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanICAM1BloodQuantity_quantity_value, domain=HumanICAM1BloodQuantity, range=Decimal)

slots.HumanInsulinBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanInsulinBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInsulinBloodQuantity_quantity_value, domain=HumanInsulinBloodQuantity, range=Decimal)

slots.HumanInterleukin18BloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanInterleukin18BloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInterleukin18BloodQuantity_quantity_value, domain=HumanInterleukin18BloodQuantity, range=Decimal)

slots.HumanInterleukin1BetaBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanInterleukin1BetaBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInterleukin1BetaBloodQuantity_quantity_value, domain=HumanInterleukin1BetaBloodQuantity, range=Decimal)

slots.HumanInterleukin10BloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanInterleukin10BloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInterleukin10BloodQuantity_quantity_value, domain=HumanInterleukin10BloodQuantity, range=Decimal)

slots.HumanInterleukin6BloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanInterleukin6BloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanInterleukin6BloodQuantity_quantity_value, domain=HumanInterleukin6BloodQuantity, range=Decimal)

slots.HumanLactateDehydrogenaseQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanLactateDehydrogenaseQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLactateDehydrogenaseQuantity_quantity_value, domain=HumanLactateDehydrogenaseQuantity, range=Decimal)

slots.HumanLactateBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanLactateBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLactateBloodQuantity_quantity_value, domain=HumanLactateBloodQuantity, range=Decimal)

slots.HumanLDLQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanLDLQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLDLQuantity_quantity_value, domain=HumanLDLQuantity, range=Decimal)

slots.HumanLymphocyteCountQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanLymphocyteCountQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLymphocyteCountQuantity_quantity_value, domain=HumanLymphocyteCountQuantity, range=Decimal)

slots.HumanLymphocytePercentQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanLymphocytePercentQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLymphocytePercentQuantity_quantity_value, domain=HumanLymphocytePercentQuantity, range=Decimal)

slots.HumanLPPLA2MassBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanLPPLA2MassBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanLPPLA2MassBloodQuantity_quantity_value, domain=HumanLPPLA2MassBloodQuantity, range=Decimal)

slots.HumanMCP1BloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMCP1BloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMCP1BloodQuantity_quantity_value, domain=HumanMCP1BloodQuantity, range=Decimal)

slots.HumanMeanArterialPressureQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMeanArterialPressureQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMeanArterialPressureQuantity_quantity_value, domain=HumanMeanArterialPressureQuantity, range=Decimal)

slots.HumanMCHQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMCHQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMCHQuantity_quantity_value, domain=HumanMCHQuantity, range=Decimal)

slots.HumanMCHCQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMCHCQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMCHCQuantity_quantity_value, domain=HumanMCHCQuantity, range=Decimal)

slots.HumanMCVQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMCVQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMCVQuantity_quantity_value, domain=HumanMCVQuantity, range=Decimal)

slots.HumanMPVQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMPVQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMPVQuantity_quantity_value, domain=HumanMPVQuantity, range=Decimal)

slots.HumanMMP9BloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMMP9BloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMMP9BloodQuantity_quantity_value, domain=HumanMMP9BloodQuantity, range=Decimal)

slots.HumanMonocyteCountQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMonocyteCountQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMonocyteCountQuantity_quantity_value, domain=HumanMonocyteCountQuantity, range=Decimal)

slots.HumanMyeloperoxidaseBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanMyeloperoxidaseBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanMyeloperoxidaseBloodQuantity_quantity_value, domain=HumanMyeloperoxidaseBloodQuantity, range=Decimal)

slots.HumanNeutrophilCountQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanNeutrophilCountQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanNeutrophilCountQuantity_quantity_value, domain=HumanNeutrophilCountQuantity, range=Decimal)

slots.HumanNeutrophilPercentQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanNeutrophilPercentQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanNeutrophilPercentQuantity_quantity_value, domain=HumanNeutrophilPercentQuantity, range=Decimal)

slots.HumanNTproBNPQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanNTproBNPQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanNTproBNPQuantity_quantity_value, domain=HumanNTproBNPQuantity, range=Decimal)

slots.HumanOsteoprotegerinBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanOsteoprotegerinBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanOsteoprotegerinBloodQuantity_quantity_value, domain=HumanOsteoprotegerinBloodQuantity, range=Decimal)

slots.HumanPSelectinBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPSelectinBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPSelectinBloodQuantity_quantity_value, domain=HumanPSelectinBloodQuantity, range=Decimal)

slots.HumanPlateletCountQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPlateletCountQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPlateletCountQuantity_quantity_value, domain=HumanPlateletCountQuantity, range=Decimal)

slots.HumanPotassiumBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPotassiumBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPotassiumBloodQuantity_quantity_value, domain=HumanPotassiumBloodQuantity, range=Decimal)

slots.HumanPRIntervalQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanPRIntervalQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanPRIntervalQuantity_quantity_value, domain=HumanPRIntervalQuantity, range=Decimal)

slots.HumanQRSIntervalQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanQRSIntervalQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanQRSIntervalQuantity_quantity_value, domain=HumanQRSIntervalQuantity, range=Decimal)

slots.HumanQTIntervalQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanQTIntervalQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanQTIntervalQuantity_quantity_value, domain=HumanQTIntervalQuantity, range=Decimal)

slots.HumanRBCCountQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanRBCCountQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanRBCCountQuantity_quantity_value, domain=HumanRBCCountQuantity, range=Decimal)

slots.HumanRDWQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanRDWQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanRDWQuantity_quantity_value, domain=HumanRDWQuantity, range=Decimal)

slots.HumanSleepDurationQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanSleepDurationQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanSleepDurationQuantity_quantity_value, domain=HumanSleepDurationQuantity, range=Decimal)

slots.HumanSodiumBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanSodiumBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanSodiumBloodQuantity_quantity_value, domain=HumanSodiumBloodQuantity, range=Decimal)

slots.SodiumIntakeQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="SodiumIntakeQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.SodiumIntakeQuantity_quantity_value, domain=SodiumIntakeQuantity, range=Decimal)

slots.HumanSpO2Quantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanSpO2Quantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanSpO2Quantity_quantity_value, domain=HumanSpO2Quantity, range=Decimal)

slots.HumanSystolicBloodPressureQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanSystolicBloodPressureQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanSystolicBloodPressureQuantity_quantity_value, domain=HumanSystolicBloodPressureQuantity, range=Decimal)

slots.HumanBodyTemperatureQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanBodyTemperatureQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanBodyTemperatureQuantity_quantity_value, domain=HumanBodyTemperatureQuantity, range=Decimal)

slots.HumanTNFAlphaBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanTNFAlphaBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTNFAlphaBloodQuantity_quantity_value, domain=HumanTNFAlphaBloodQuantity, range=Decimal)

slots.HumanTNFAlphaR1BloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanTNFAlphaR1BloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTNFAlphaR1BloodQuantity_quantity_value, domain=HumanTNFAlphaR1BloodQuantity, range=Decimal)

slots.HumanTotalCholesterolQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanTotalCholesterolQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTotalCholesterolQuantity_quantity_value, domain=HumanTotalCholesterolQuantity, range=Decimal)

slots.HumanTriglyceridesBloodQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanTriglyceridesBloodQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTriglyceridesBloodQuantity_quantity_value, domain=HumanTriglyceridesBloodQuantity, range=Decimal)

slots.HumanTroponinQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanTroponinQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanTroponinQuantity_quantity_value, domain=HumanTroponinQuantity, range=Decimal)

slots.VegetableConsumptionQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="VegetableConsumptionQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.VegetableConsumptionQuantity_quantity_value, domain=VegetableConsumptionQuantity, range=Decimal)

slots.HumanVonWillebrandFactorQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanVonWillebrandFactorQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanVonWillebrandFactorQuantity_quantity_value, domain=HumanVonWillebrandFactorQuantity, range=Decimal)

slots.HumanWaistCircumferenceQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanWaistCircumferenceQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanWaistCircumferenceQuantity_quantity_value, domain=HumanWaistCircumferenceQuantity, range=Decimal)

slots.HumanWaistHipRatioQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanWaistHipRatioQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanWaistHipRatioQuantity_quantity_value, domain=HumanWaistHipRatioQuantity, range=Decimal)

slots.HumanWBCCountQuantity_quantity_value = Slot(uri=LINKML['linkml-microschema-profile/quantity_value'], name="HumanWBCCountQuantity_quantity_value", curie=LINKML.curie('linkml-microschema-profile/quantity_value'),
                   model_uri=BDC_VARIABLE_LIBRARY.HumanWBCCountQuantity_quantity_value, domain=HumanWBCCountQuantity, range=Decimal)

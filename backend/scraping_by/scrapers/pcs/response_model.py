# generated by datamodel-codegen:
#   filename:  release_packages.json
#   timestamp: 2021-09-18T12:41:19+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Identifier(BaseModel):
    legalName: str


class Address(BaseModel):
    streetAddress: Optional[str] = None
    locality: str
    region: Optional[str] = None
    postalCode: Optional[str] = None


class ContactPoint(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    url: Optional[str] = None
    telephone: Optional[str] = None
    faxNumber: Optional[str] = None


class Classification(BaseModel):
    id: str
    scheme: str


class Details(BaseModel):
    classifications: List[Classification]
    url: str


class Party(BaseModel):
    name: str
    id: str
    identifier: Optional[Identifier] = None
    address: Address
    contactPoint: ContactPoint
    roles: List[str]
    details: Optional[Details] = None


class Buyer(BaseModel):
    name: str
    id: str


class DeliveryAddress(BaseModel):
    region: str


class AdditionalClassification(BaseModel):
    id: str
    scheme: str


class DeliveryLocation(BaseModel):
    description: str


class Item(BaseModel):
    id: str
    deliveryAddresses: List[DeliveryAddress]
    relatedLot: str
    additionalClassifications: Optional[List[AdditionalClassification]] = None
    deliveryLocation: Optional[DeliveryLocation] = None


class Value(BaseModel):
    amount: float
    currency: str


class TenderPeriod(BaseModel):
    endDate: str


class AwardPeriod(BaseModel):
    startDate: str


class Document(BaseModel):
    id: str
    documentType: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    format: Optional[str] = None
    datePublished: Optional[str] = None
    dateModified: Optional[str] = None


class Criterion(BaseModel):
    type: str
    name: Optional[str] = None
    description: str


class AwardCriteria(BaseModel):
    criteria: List[Criterion]


class Options(BaseModel):
    description: str


class SubmissionTerms(BaseModel):
    variantPolicy: str
    electronicCataloguePolicy: Optional[str] = None


class ContractPeriod(BaseModel):
    durationInDays: Optional[int] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None


class Renewal(BaseModel):
    description: str


class Value1(BaseModel):
    amount: float
    currency: str


class SecondStage(BaseModel):
    minimumCandidates: Optional[int] = None
    maximumCandidates: Optional[int] = None


class SelectionCriteria(BaseModel):
    description: str


class Lot(BaseModel):
    id: str
    description: str
    status: str
    awardCriteria: Optional[AwardCriteria] = None
    options: Optional[Options] = None
    hasOptions: bool
    submissionTerms: SubmissionTerms
    contractPeriod: ContractPeriod
    hasRenewal: bool
    renewal: Optional[Renewal] = None
    value: Optional[Value1] = None
    title: Optional[str] = None
    secondStage: Optional[SecondStage] = None
    selectionCriteria: Optional[SelectionCriteria] = None


class Address1(BaseModel):
    streetAddress: str


class BidOpening(BaseModel):
    date: str
    address: Optional[Address1] = None
    description: Optional[str] = None


class Communication(BaseModel):
    atypicalToolUrl: str


class ContractTerms(BaseModel):
    hasElectronicPayment: Optional[bool] = None
    hasElectronicOrdering: Optional[bool] = None
    electronicInvoicingPolicy: Optional[str] = None
    performanceTerms: Optional[str] = None
    reservedExecution: Optional[bool] = None


class Criterion1(BaseModel):
    type: str
    description: str
    minimum: Optional[str] = None


class SelectionCriteria1(BaseModel):
    criteria: Optional[List[Criterion1]] = None


class BidValidityPeriod(BaseModel):
    durationInDays: Optional[int] = None
    endDate: Optional[str] = None


class SubmissionTerms1(BaseModel):
    languages: List[str]
    bidValidityPeriod: Optional[BidValidityPeriod] = None


class Classification1(BaseModel):
    id: str
    scheme: str


class LegalBasis(BaseModel):
    id: str
    scheme: str


class Recurrence(BaseModel):
    description: str


class OtherRequirements(BaseModel):
    requiresStaffNamesAndQualifications: bool


class FrameworkAgreement(BaseModel):
    maximumParticipants: float
    periodRationale: Optional[str] = None


class DynamicPurchasingSystem(BaseModel):
    type: str


class ElectronicAuction(BaseModel):
    description: str


class Techniques(BaseModel):
    hasFrameworkAgreement: Optional[bool] = None
    frameworkAgreement: Optional[FrameworkAgreement] = None
    hasDynamicPurchasingSystem: Optional[bool] = None
    dynamicPurchasingSystem: Optional[DynamicPurchasingSystem] = None
    hasElectronicAuction: Optional[bool] = None
    electronicAuction: Optional[ElectronicAuction] = None


class LotDetails(BaseModel):
    maximumLotsBidPerSupplier: int
    awardCriteriaDetails: Optional[str] = None
    maximumLotsAwardedPerSupplier: Optional[int] = None


class ParticipationFee(BaseModel):
    id: str
    type: List[str]


class SecondStage1(BaseModel):
    invitationDate: str
    successiveReduction: Optional[bool] = None
    noNegotiationNecessary: Optional[bool] = None


class Tender(BaseModel):
    id: str
    title: str
    description: str
    status: str
    items: List[Item]
    value: Optional[Value] = None
    procurementMethod: str
    procurementMethodDetails: str
    mainProcurementCategory: str
    submissionMethod: List[str]
    submissionMethodDetails: str
    tenderPeriod: TenderPeriod
    awardPeriod: Optional[AwardPeriod] = None
    documents: List[Document]
    lots: List[Lot]
    bidOpening: Optional[BidOpening] = None
    communication: Optional[Communication] = None
    contractTerms: Optional[ContractTerms] = None
    coveredBy: Optional[List[str]] = None
    selectionCriteria: Optional[SelectionCriteria1] = None
    submissionTerms: SubmissionTerms1
    classification: Classification1
    reviewDetails: Optional[str] = None
    hasRecurrence: bool
    legalBasis: LegalBasis
    recurrence: Optional[Recurrence] = None
    otherRequirements: Optional[OtherRequirements] = None
    techniques: Optional[Techniques] = None
    lotDetails: Optional[LotDetails] = None
    participationFees: Optional[List[ParticipationFee]] = None
    secondStage: Optional[SecondStage1] = None


class RelatedProcess(BaseModel):
    id: str
    relationship: List[str]
    scheme: str
    identifier: str


class Release(BaseModel):
    id: str
    ocid: str
    date: str
    tag: List[str]
    initiationType: str
    parties: List[Party]
    buyer: Buyer
    tender: Tender
    language: str
    description: str
    relatedProcesses: Optional[List[RelatedProcess]] = None


class Publisher(BaseModel):
    name: str


class Model(BaseModel):
    uri: str
    version: str
    publishedDate: str
    releases: List[Release]
    publisher: Publisher
    extensions: List[str]
    license: str
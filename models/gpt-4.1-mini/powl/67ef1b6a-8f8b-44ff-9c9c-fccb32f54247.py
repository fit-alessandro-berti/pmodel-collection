# Generated from: 67ef1b6a-8f8b-44ff-9c9c-fccb32f54247.json
# Description: This process outlines the comprehensive steps required to authenticate ancient artifacts for museum acquisition. It begins with preliminary provenance verification, followed by multi-disciplinary scientific analysis including radiocarbon dating and material composition assessment. Next, expert consultations and stylistic comparisons are conducted to validate cultural origin. The process also involves condition reporting, risk assessment for transportation, and legal compliance checks related to export/import regulations. Finally, a formal authentication report is compiled and submitted for board approval before acquisition decision and artifact cataloging occur, ensuring a thorough and legally compliant authentication workflow for rare historical items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Provenance_Check = Transition(label='Provenance Check')

Radiocarbon_Test = Transition(label='Radiocarbon Test')
Material_Analysis = Transition(label='Material Analysis')
# Scientific analysis partial order with Radiocarbon Test and Material Analysis concurrent
Scientific_Analysis = StrictPartialOrder(nodes=[Radiocarbon_Test, Material_Analysis])

Stylistic_Review = Transition(label='Stylistic Review')
Expert_Consultation = Transition(label='Expert Consultation')
# Stylistic Review and Expert Consultation concurrent
Validation = StrictPartialOrder(nodes=[Stylistic_Review, Expert_Consultation])

Condition_Report = Transition(label='Condition Report')
Risk_Assessment = Transition(label='Risk Assessment')

Legal_Compliance = Transition(label='Legal Compliance')
Export_Verification = Transition(label='Export Verification')
Import_Clearance = Transition(label='Import Clearance')
# Legal compliance partial order: Legal Compliance --> Export Verification, Import Clearance in parallel
Legal_Process = StrictPartialOrder(
    nodes=[Legal_Compliance, Export_Verification, Import_Clearance]
)
Legal_Process.order.add_edge(Legal_Compliance, Export_Verification)
Legal_Process.order.add_edge(Legal_Compliance, Import_Clearance)

Authentication_Draft = Transition(label='Authentication Draft')
Board_Approval = Transition(label='Board Approval')
Acquisition_Decision = Transition(label='Acquisition Decision')
Catalog_Entry = Transition(label='Catalog Entry')
Transport_Planning = Transition(label='Transport Planning')

# Build the main partial order

root = StrictPartialOrder(nodes=[
    Provenance_Check,
    Scientific_Analysis,
    Validation,
    Condition_Report,
    Risk_Assessment,
    Legal_Process,
    Authentication_Draft,
    Board_Approval,
    Acquisition_Decision,
    Catalog_Entry,
    Transport_Planning
])

### Define edges for the order according to the description:

# Provenance Check --> Scientific Analysis
root.order.add_edge(Provenance_Check, Scientific_Analysis)
# Scientific Analysis --> Validation (Stylistic Review + Expert Consultation)
root.order.add_edge(Scientific_Analysis, Validation)
# Validation --> Condition Report and Risk Assessment in parallel
root.order.add_edge(Validation, Condition_Report)
root.order.add_edge(Validation, Risk_Assessment)
# Condition Report and Risk Assessment --> Legal Process
root.order.add_edge(Condition_Report, Legal_Process)
root.order.add_edge(Risk_Assessment, Legal_Process)
# Legal Process --> Authentication Draft
root.order.add_edge(Legal_Process, Authentication_Draft)
# Authentication Draft --> Board Approval
root.order.add_edge(Authentication_Draft, Board_Approval)
# Board Approval --> Acquisition Decision
root.order.add_edge(Board_Approval, Acquisition_Decision)
# Acquisition Decision --> Catalog Entry and Transport Planning in parallel
root.order.add_edge(Acquisition_Decision, Catalog_Entry)
root.order.add_edge(Acquisition_Decision, Transport_Planning)
# Generated from: 6d291212-6c4d-4a5a-ac78-b56d3538f529.json
# Description: This process details the intricate creation of artisanal perfumes, combining rare botanical extractions with traditional blending techniques. It begins with sourcing exotic raw materials from multiple continents, followed by delicate extraction methods like enfleurage and steam distillation. Next, master perfumers experiment with scent profiles in controlled environments, adjusting ratios to achieve a harmonious fragrance. Quality control includes olfactory testing and chemical analysis to ensure consistency and safety. The final phase involves aging the perfume in specialized containers, bottling, and bespoke packaging, while maintaining traceability and sustainability throughout the workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
RawSourcing        = Transition(label='Raw Sourcing')
BotanicalSorting   = Transition(label='Botanical Sorting')
ExtractionPrep     = Transition(label='Extraction Prep')
EnfleurageProcess  = Transition(label='Enfleurage Process')
SteamDistill       = Transition(label='Steam Distill')
ScentBlending      = Transition(label='Scent Blending')
ProfileTesting     = Transition(label='Profile Testing')
RatioAdjust        = Transition(label='Ratio Adjust')
OlfactoryCheck     = Transition(label='Olfactory Check')
ChemicalScan       = Transition(label='Chemical Scan')
QualityApproval    = Transition(label='Quality Approval')
AgingStorage       = Transition(label='Aging Storage')
BottleFilling      = Transition(label='Bottle Filling')
LabelPrinting      = Transition(label='Label Printing')
CustomPackaging    = Transition(label='Custom Packaging')
SustainabilityAudit= Transition(label='Sustainability Audit')
TraceabilityLog    = Transition(label='Traceability Log')

# Loop for iterative testing and ratio adjustment:
#   execute ProfileTesting, then repeat (RatioAdjust -> ProfileTesting) until exit
loop_testing = OperatorPOWL(operator=Operator.LOOP, children=[ProfileTesting, RatioAdjust])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    RawSourcing,
    BotanicalSorting,
    ExtractionPrep,
    EnfleurageProcess,
    SteamDistill,
    ScentBlending,
    loop_testing,
    OlfactoryCheck,
    ChemicalScan,
    QualityApproval,
    AgingStorage,
    BottleFilling,
    LabelPrinting,
    CustomPackaging,
    SustainabilityAudit,
    TraceabilityLog
])

# Establish the control‐flow dependencies
root.order.add_edge(RawSourcing,        BotanicalSorting)
root.order.add_edge(BotanicalSorting,   ExtractionPrep)
root.order.add_edge(ExtractionPrep,     EnfleurageProcess)
root.order.add_edge(ExtractionPrep,     SteamDistill)
root.order.add_edge(EnfleurageProcess,  ScentBlending)
root.order.add_edge(SteamDistill,       ScentBlending)
root.order.add_edge(ScentBlending,      loop_testing)
root.order.add_edge(loop_testing,       OlfactoryCheck)
root.order.add_edge(loop_testing,       ChemicalScan)
root.order.add_edge(OlfactoryCheck,     QualityApproval)
root.order.add_edge(ChemicalScan,       QualityApproval)
root.order.add_edge(QualityApproval,    AgingStorage)
root.order.add_edge(AgingStorage,       BottleFilling)
root.order.add_edge(BottleFilling,      LabelPrinting)
root.order.add_edge(LabelPrinting,      CustomPackaging)

# Traceability and sustainability run in parallel throughout
root.order.add_edge(RawSourcing,         SustainabilityAudit)
root.order.add_edge(RawSourcing,         TraceabilityLog)
root.order.add_edge(SustainabilityAudit, CustomPackaging)
root.order.add_edge(TraceabilityLog,     CustomPackaging)
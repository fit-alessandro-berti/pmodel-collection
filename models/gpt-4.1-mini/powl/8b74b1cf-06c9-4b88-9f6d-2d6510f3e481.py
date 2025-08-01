# Generated from: 8b74b1cf-06c9-4b88-9f6d-2d6510f3e481.json
# Description: This process outlines the complex and atypical supply chain of artisan cheese production and distribution. It begins with raw milk sourcing from niche farms focusing on unique breeds, followed by milk quality testing and specialized fermentation. The aging environment is carefully controlled, requiring regular monitoring and adjustments based on sensory evaluations. Packaging involves customized biodegradable materials to preserve flavor and texture. The distribution network integrates small-scale retailers and direct-to-consumer subscriptions, necessitating dynamic logistics planning to maintain freshness. Marketing leverages storytelling around origin and craft, supported by seasonal event coordination and customer feedback loops to refine product offerings and ensure sustainable practices throughout the chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
MilkSourcing = Transition(label='Milk Sourcing')
QualityCheck = Transition(label='Quality Check')
MilkPasteurize = Transition(label='Milk Pasteurize')
CultureAdd = Transition(label='Culture Add')
CoagulateMilk = Transition(label='Coagulate Milk')
CutCurds = Transition(label='Cut Curds')
DrainWhey = Transition(label='Drain Whey')
MoldPress = Transition(label='Mold Press')
SaltingStep = Transition(label='Salting Step')
CaveAging = Transition(label='Cave Aging')
SensoryTest = Transition(label='Sensory Test')
PackageCheese = Transition(label='Package Cheese')
LabelDesign = Transition(label='Label Design')
OrderFulfill = Transition(label='Order Fulfill')
RoutePlanning = Transition(label='Route Planning')
CustomerSurvey = Transition(label='Customer Survey')
EventManage = Transition(label='Event Manage')
SupplyAudit = Transition(label='Supply Audit')

# Define partial orders for milk processing stages
milk_processing = StrictPartialOrder(nodes=[
    MilkSourcing, QualityCheck, MilkPasteurize, CultureAdd, CoagulateMilk,
    CutCurds, DrainWhey, MoldPress, SaltingStep
])
milk_processing.order.add_edge(MilkSourcing, QualityCheck)
milk_processing.order.add_edge(QualityCheck, MilkPasteurize)
milk_processing.order.add_edge(MilkPasteurize, CultureAdd)
milk_processing.order.add_edge(CultureAdd, CoagulateMilk)
milk_processing.order.add_edge(CoagulateMilk, CutCurds)
milk_processing.order.add_edge(CutCurds, DrainWhey)
milk_processing.order.add_edge(DrainWhey, MoldPress)
milk_processing.order.add_edge(MoldPress, SaltingStep)

# Aging and testing partial order
aging_and_test = StrictPartialOrder(nodes=[CaveAging, SensoryTest])
aging_and_test.order.add_edge(CaveAging, SensoryTest)

# Packaging partial order
packaging = StrictPartialOrder(nodes=[PackageCheese, LabelDesign])
packaging.order.add_edge(PackageCheese, LabelDesign)

# Distribution and logistics partial order
distribution = StrictPartialOrder(nodes=[OrderFulfill, RoutePlanning])
distribution.order.add_edge(RoutePlanning, OrderFulfill)  # Route planning before order fulfill

# Marketing and feedback partial order
marketing = StrictPartialOrder(nodes=[CustomerSurvey, EventManage])
marketing.order.add_edge(EventManage, CustomerSurvey)  # Events before surveys (logical ordering)

# Loop for sensory evaluation and aging adjustments (Aging -> Sensory -> may loop back to Aging)
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[CaveAging, SensoryTest])

# Full production partial order combining milk processing, aging loop, packaging, distribution, marketing, and audit
root = StrictPartialOrder(nodes=[
    milk_processing,
    aging_loop,
    packaging,
    distribution,
    marketing,
    SupplyAudit
])

# Define partial order edges between major phases
root.order.add_edge(milk_processing, aging_loop)
root.order.add_edge(aging_loop, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(distribution, marketing)
root.order.add_edge(marketing, SupplyAudit)
# Generated from: 8afbc869-7383-4713-83a8-478c9e286a24.json
# Description: This process outlines the complex journey of artisanal cheese from small-scale farms to niche gourmet retailers. It involves milk sourcing with strict quality criteria, traditional curdling and aging techniques, rigorous sensory testing, custom packaging, and coordinating temperature-controlled logistics. Additionally, the process integrates direct farmer feedback loops, seasonal production adjustments, and targeted marketing strategies to maintain product authenticity and meet fluctuating demand in specialty markets. It also includes compliance with regional food safety regulations and proactive risk management to handle spoilage or supply disruptions, ensuring a consistent supply of high-quality artisan cheese to discerning consumers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
BatchMixing = Transition(label='Batch Mixing')
CurdFormation = Transition(label='Curd Formation')
WheySeparation = Transition(label='Whey Separation')
MoldInoculation = Transition(label='Mold Inoculation')
PressingCheese = Transition(label='Pressing Cheese')
CaveAging = Transition(label='Cave Aging')
SensoryCheck = Transition(label='Sensory Check')
PackagingDesign = Transition(label='Packaging Design')
LabelPrinting = Transition(label='Label Printing')
ColdStorage = Transition(label='Cold Storage')
OrderProcessing = Transition(label='Order Processing')
ShipmentScheduling = Transition(label='Shipment Scheduling')
RetailDelivery = Transition(label='Retail Delivery')
FarmerFeedback = Transition(label='Farmer Feedback')
DemandForecast = Transition(label='Demand Forecast')

# Silent transition for controlling loops
tau = SilentTransition()

# Loop 1: Farmer feedback loop integrated after SensoryCheck to adjust demand forecast and packaging
# Structure: LOOP(children=[SensoryCheck, OperatorPOWL(XOR, [FarmerFeedback, tau])])
feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[FarmerFeedback, tau])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[SensoryCheck, feedback_choice])

# Loop 2: Seasonal production adjustment and demand forecast loop after FarmerFeedback and before MilkSourcing restart
seasonal_choice = OperatorPOWL(operator=Operator.XOR, children=[DemandForecast, tau])
seasonal_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, seasonal_choice])

# Partial order of the main production process before feedback loop

# Initial steps: Milk sourcing and quality testing must happen in order
initial_po = StrictPartialOrder(nodes=[
    MilkSourcing, QualityTesting
])
initial_po.order.add_edge(MilkSourcing, QualityTesting)

# Cheese production steps in sequence
production_steps = StrictPartialOrder(nodes=[
    BatchMixing,
    CurdFormation,
    WheySeparation,
    MoldInoculation,
    PressingCheese,
    CaveAging
])
production_steps.order.add_edge(BatchMixing, CurdFormation)
production_steps.order.add_edge(CurdFormation, WheySeparation)
production_steps.order.add_edge(WheySeparation, MoldInoculation)
production_steps.order.add_edge(MoldInoculation, PressingCheese)
production_steps.order.add_edge(PressingCheese, CaveAging)

# Packaging steps in sequence
packaging_steps = StrictPartialOrder(nodes=[
    PackagingDesign,
    LabelPrinting,
    ColdStorage
])
packaging_steps.order.add_edge(PackagingDesign, LabelPrinting)
packaging_steps.order.add_edge(LabelPrinting, ColdStorage)

# Distribution steps in sequence
distribution_steps = StrictPartialOrder(nodes=[
    OrderProcessing,
    ShipmentScheduling,
    RetailDelivery
])
distribution_steps.order.add_edge(OrderProcessing, ShipmentScheduling)
distribution_steps.order.add_edge(ShipmentScheduling, RetailDelivery)

# Sensory check must be after aging and before packaging
# Also, feedback_loop embeds SensoryCheck, so integrate here carefully:
# We'll build an overall partial order connecting the components:

# Create a top-level PO with nodes:
# [initial_po, production_steps, seasonal_loop, packaging_steps, distribution_steps]

# To do so, we use a partial order with these as nodes.
# But POWL nodes are either Transitions, SilentTransitions or OperatorPOWL or StrictPartialOrder
# The instructions say StrictPartialOrder nodes can be nodes and XO or LOOP operators can be children

root = StrictPartialOrder(nodes=[
    initial_po,
    production_steps,
    seasonal_loop,
    packaging_steps,
    distribution_steps
])

# Define order between these subcomponents:
# initial_po --> production_steps (quality testing before batch mixing)
root.order.add_edge(initial_po, production_steps)
# production_steps --> seasonal_loop (after aging, do sensory check + feedback loops)
root.order.add_edge(production_steps, seasonal_loop)
# seasonal_loop contains SensoryCheck and FarmerFeedback and DemandForecast loops

# seasonal_loop --> packaging_steps (after exiting the loop, packaging)
root.order.add_edge(seasonal_loop, packaging_steps)
# packaging_steps --> distribution_steps
root.order.add_edge(packaging_steps, distribution_steps)
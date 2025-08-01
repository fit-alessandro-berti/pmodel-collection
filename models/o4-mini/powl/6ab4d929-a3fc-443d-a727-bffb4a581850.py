# Generated from: 6ab4d929-a3fc-443d-a727-bffb4a581850.json
# Description: This process outlines the detailed steps involved in producing and distributing artisanal cheese from small-scale farms to gourmet retail outlets. It includes raw milk collection from diverse breeds, precise temperature-controlled fermentation, multiple rounds of quality assessment, packaging with eco-friendly materials, specialized cold-chain logistics, and targeted marketing to niche consumers. The process also incorporates feedback loops with cheesemakers and retailers to continually refine taste profiles and shelf life, ensuring product consistency and brand reputation in a highly competitive specialty food market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
MilkCollection   = Transition(label='Milk Collection')
QualityTesting   = Transition(label='Quality Testing')
MilkPasteurize   = Transition(label='Milk Pasteurize')
StarterCulture   = Transition(label='Starter Culture')
CurdFormation    = Transition(label='Curd Formation')
CutCurd          = Transition(label='Cut Curd')
DrainWhey        = Transition(label='Drain Whey')
PressCheese      = Transition(label='Press Cheese')
SaltApplication  = Transition(label='Salt Application')
Fermentation     = Transition(label='Fermentation')
RindTreatment    = Transition(label='Rind Treatment')
AgingMonitor     = Transition(label='Aging Monitor')
QualityCheck     = Transition(label='Quality Check')
EcoPackaging     = Transition(label='Eco Packaging')
ColdStorage      = Transition(label='Cold Storage')
OrderProcessing  = Transition(label='Order Processing')
LogisticsPlan    = Transition(label='Logistics Plan')
RetailDelivery   = Transition(label='Retail Delivery')
CustomerFeedback = Transition(label='Customer Feedback')

# Inner loop: multiple rounds of aging + quality check
loop_aging = OperatorPOWL(
    operator=Operator.LOOP,
    children=[AgingMonitor, QualityCheck]
)

# Main partial order of cheese production & distribution
main = StrictPartialOrder(nodes=[
    MilkCollection, QualityTesting, MilkPasteurize, StarterCulture,
    CurdFormation, CutCurd, DrainWhey, PressCheese, SaltApplication,
    Fermentation, RindTreatment, loop_aging, EcoPackaging, ColdStorage,
    OrderProcessing, LogisticsPlan, RetailDelivery
])
# Define control‐flow edges
main.order.add_edge(MilkCollection,  QualityTesting)
main.order.add_edge(QualityTesting,  MilkPasteurize)
main.order.add_edge(MilkPasteurize,  StarterCulture)
main.order.add_edge(StarterCulture,  CurdFormation)
main.order.add_edge(CurdFormation,   CutCurd)
main.order.add_edge(CutCurd,         DrainWhey)
main.order.add_edge(DrainWhey,       PressCheese)
main.order.add_edge(PressCheese,     SaltApplication)
main.order.add_edge(SaltApplication, Fermentation)
main.order.add_edge(Fermentation,    RindTreatment)
main.order.add_edge(RindTreatment,   loop_aging)
main.order.add_edge(loop_aging,      EcoPackaging)
main.order.add_edge(EcoPackaging,    ColdStorage)
main.order.add_edge(ColdStorage,     OrderProcessing)
main.order.add_edge(OrderProcessing, LogisticsPlan)
main.order.add_edge(LogisticsPlan,   RetailDelivery)

# Outer loop: feedback from customers to refine taste/shelf life
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main, CustomerFeedback]
)
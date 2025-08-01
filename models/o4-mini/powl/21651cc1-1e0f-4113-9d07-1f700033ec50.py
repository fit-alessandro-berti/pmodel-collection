# Generated from: 21651cc1-1e0f-4113-9d07-1f700033ec50.json
# Description: This process outlines the intricate supply chain of artisan cheese production, starting from raw milk sourcing from select farms with specific breed cows to quality testing and aging in controlled environments. It includes steps like microbial culture preparation, curd cutting, whey drainage, pressing, salting, and maturation under precise humidity and temperature settings. The process also involves packaging with eco-friendly materials, batch traceability tagging, and coordinating delivery logistics to specialty retailers, ensuring freshness and compliance with food safety standards. Customer feedback is integrated for continuous improvement, and seasonal variations in milk quality are accounted for by adjusting fermentation parameters accordingly.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
MilkPasteurize = Transition(label='Milk Pasteurize')
CulturePrep = Transition(label='Culture Prep')
ParameterAdjust = Transition(label='Parameter Adjust')
CurdCutting = Transition(label='Curd Cutting')
WheyDrainage = Transition(label='Whey Drainage')
CurdPressing = Transition(label='Curd Pressing')
SaltApplication = Transition(label='Salt Application')
CheeseAging = Transition(label='Cheese Aging')
HumidityControl = Transition(label='Humidity Control')
TempMonitoring = Transition(label='Temp Monitoring')
PackagingEco = Transition(label='Packaging Eco')
BatchTagging = Transition(label='Batch Tagging')
DeliveryPlan = Transition(label='Delivery Plan')
RetailCoordination = Transition(label='Retail Coordination')
FeedbackReview = Transition(label='Feedback Review')

# Loop for seasonal fermentation adjustments around culture preparation
loop_culture = OperatorPOWL(
    operator=Operator.LOOP,
    children=[CulturePrep, ParameterAdjust]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    MilkSourcing,
    QualityTesting,
    MilkPasteurize,
    loop_culture,
    CurdCutting,
    WheyDrainage,
    CurdPressing,
    SaltApplication,
    CheeseAging,
    HumidityControl,
    TempMonitoring,
    PackagingEco,
    BatchTagging,
    DeliveryPlan,
    RetailCoordination,
    FeedbackReview
])

# Define the control-flow (ordering) relations
root.order.add_edge(MilkSourcing, QualityTesting)
root.order.add_edge(QualityTesting, MilkPasteurize)
root.order.add_edge(MilkPasteurize, loop_culture)
root.order.add_edge(loop_culture, CurdCutting)
root.order.add_edge(CurdCutting, WheyDrainage)
root.order.add_edge(WheyDrainage, CurdPressing)
root.order.add_edge(CurdPressing, SaltApplication)
root.order.add_edge(SaltApplication, CheeseAging)
root.order.add_edge(CheeseAging, HumidityControl)
root.order.add_edge(CheeseAging, TempMonitoring)
root.order.add_edge(HumidityControl, PackagingEco)
root.order.add_edge(TempMonitoring, PackagingEco)
root.order.add_edge(PackagingEco, BatchTagging)
root.order.add_edge(BatchTagging, DeliveryPlan)
root.order.add_edge(DeliveryPlan, RetailCoordination)
root.order.add_edge(RetailCoordination, FeedbackReview)
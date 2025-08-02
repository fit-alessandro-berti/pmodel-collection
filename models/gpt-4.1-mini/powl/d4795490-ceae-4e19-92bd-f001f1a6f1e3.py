# Generated from: d4795490-ceae-4e19-92bd-f001f1a6f1e3.json
# Description: This process involves sourcing rare coffee beans from remote, eco-sensitive farms, ensuring sustainable harvesting practices. Beans undergo micro-lot selection, followed by specialized fermentation and drying techniques tailored to each batch's unique profile. Quality control includes chemical and sensory analysis. The beans are then roasted using variable profiles depending on target markets. Packaging incorporates biodegradable materials with embedded QR codes for traceability. Distribution logistics optimize cold-chain transport to preserve freshness, integrating real-time environmental monitoring. Customer feedback loops inform continuous process refinement and personalized subscription adjustments, blending artisanal craftsmanship with advanced technology to deliver premium coffee experiences globally.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Farm_Sourcing = Transition(label='Farm Sourcing')
Lot_Selection = Transition(label='Lot Selection')
Bean_Sorting = Transition(label='Bean Sorting')
Fermentation = Transition(label='Fermentation')
Drying_Process = Transition(label='Drying Process')
Quality_Control = Transition(label='Quality Control')
Chemical_Testing = Transition(label='Chemical Testing')
Sensory_Analysis = Transition(label='Sensory Analysis')
Roast_Profiling = Transition(label='Roast Profiling')
Eco_Packaging = Transition(label='Eco Packaging')
Traceability_QR = Transition(label='Traceability QR')
Cold_Transport = Transition(label='Cold Transport')
Env_Monitoring = Transition(label='Env Monitoring')
Customer_Feedback = Transition(label='Customer Feedback')
Subscription_Adjust = Transition(label='Subscription Adjust')

# Quality control partial order:
# Chemical Testing and Sensory Analysis are parallel but both after Quality Control
quality_control_po = StrictPartialOrder(nodes=[Quality_Control, Chemical_Testing, Sensory_Analysis])
quality_control_po.order.add_edge(Quality_Control, Chemical_Testing)
quality_control_po.order.add_edge(Quality_Control, Sensory_Analysis)

# Packaging partial order: Eco Packaging then Traceability QR
packaging_po = StrictPartialOrder(nodes=[Eco_Packaging, Traceability_QR])
packaging_po.order.add_edge(Eco_Packaging, Traceability_QR)

# Distribution partial order: Cold Transport then Env Monitoring
distribution_po = StrictPartialOrder(nodes=[Cold_Transport, Env_Monitoring])
distribution_po.order.add_edge(Cold_Transport, Env_Monitoring)

# Customer feedback loop: loop with Customer Feedback and Subscription Adjust
# Loop executes Customer Feedback then choose between exit or do Subscription Adjust then repeat
customer_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Feedback, Subscription_Adjust])

# Main partial order breaking down the process:
# Farm Sourcing --> Lot Selection --> Bean Sorting --> Fermentation --> Drying Process --> quality_control_po --> Roast Profiling --> packaging_po --> distribution_po --> customer_feedback_loop
nodes_main = [
    Farm_Sourcing,
    Lot_Selection,
    Bean_Sorting,
    Fermentation,
    Drying_Process,
    quality_control_po,
    Roast_Profiling,
    packaging_po,
    distribution_po,
    customer_feedback_loop
]

root = StrictPartialOrder(nodes=nodes_main)

root.order.add_edge(Farm_Sourcing, Lot_Selection)
root.order.add_edge(Lot_Selection, Bean_Sorting)
root.order.add_edge(Bean_Sorting, Fermentation)
root.order.add_edge(Fermentation, Drying_Process)
root.order.add_edge(Drying_Process, quality_control_po)
root.order.add_edge(quality_control_po, Roast_Profiling)
root.order.add_edge(Roast_Profiling, packaging_po)
root.order.add_edge(packaging_po, distribution_po)
root.order.add_edge(distribution_po, customer_feedback_loop)
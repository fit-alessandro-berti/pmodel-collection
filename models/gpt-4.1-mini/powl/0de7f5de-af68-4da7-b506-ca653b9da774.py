# Generated from: 0de7f5de-af68-4da7-b506-ca653b9da774.json
# Description: This process outlines the intricate and atypical supply chain of artisanal cheese production, involving unique steps such as milk sourcing from rare breeds, controlled fermentation environments, and a multi-level quality authentication system. The process integrates traditional craftsmanship with modern traceability technology, ensuring each batch maintains distinct regional characteristics while complying with stringent food safety standards. It also includes bespoke packaging design tailored to seasonal markets, customized logistics coordination for temperature-sensitive deliveries, and direct consumer engagement through curated tasting events. The complexity arises from managing small-scale producers, variable raw material quality, and fluctuating demand cycles, requiring adaptive scheduling, real-time quality feedback loops, and collaborative innovation with local farmers and artisans to sustain authenticity and profitability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Breed_Selection = Transition(label='Breed Selection')
Milk_Harvest = Transition(label='Milk Harvest')
Initial_Testing = Transition(label='Initial Testing')
Batch_Allocation = Transition(label='Batch Allocation')
Fermentation_Start = Transition(label='Fermentation Start')
Humidity_Control = Transition(label='Humidity Control')
Flavor_Sampling = Transition(label='Flavor Sampling')
Rind_Treatment = Transition(label='Rind Treatment')
Aging_Monitor = Transition(label='Aging Monitor')
Quality_Audit = Transition(label='Quality Audit')
Trace_Logging = Transition(label='Trace Logging')
Packaging_Design = Transition(label='Packaging Design')
Market_Forecast = Transition(label='Market Forecast')
Logistics_Plan = Transition(label='Logistics Plan')
Event_Setup = Transition(label='Event Setup')
Customer_Feedback = Transition(label='Customer Feedback')

# Partial orders for fermentation steps (concurrent)
Fermentation_PO = StrictPartialOrder(
    nodes=[Fermentation_Start, Humidity_Control, Flavor_Sampling]
)
Fermentation_PO.order.add_edge(Fermentation_Start, Humidity_Control)
Fermentation_PO.order.add_edge(Fermentation_Start, Flavor_Sampling)

# Partial order for aging steps (concurrent)
Aging_PO = StrictPartialOrder(
    nodes=[Rind_Treatment, Aging_Monitor]
)
# No order, concurrent

# Partial order for packaging and market prep (concurrent)
Packaging_Market_PO = StrictPartialOrder(
    nodes=[Packaging_Design, Market_Forecast]
)
# No order, concurrent

# Partial order for logistics and event
Logistics_Event_PO = StrictPartialOrder(
    nodes=[Logistics_Plan, Event_Setup]
)
# No order, concurrent

# Loop: adaptive scheduling with real-time quality feedback loops
# loop node: execute Quality_Audit, then either exit or do Trace_Logging + Quality_Audit again
loop_quality_feedback = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Quality_Audit, Trace_Logging]
)

# Customer feedback comes after event setup
Event_Feedback_PO = StrictPartialOrder(
    nodes=[Event_Setup, Customer_Feedback]
)
Event_Feedback_PO.order.add_edge(Event_Setup, Customer_Feedback)

# Initial sequence with concurrency in fermentation and aging after Batch Allocation
Init_Seq_PO = StrictPartialOrder(
    nodes=[Breed_Selection, Milk_Harvest, Initial_Testing, Batch_Allocation]
)
Init_Seq_PO.order.add_edge(Breed_Selection, Milk_Harvest)
Init_Seq_PO.order.add_edge(Milk_Harvest, Initial_Testing)
Init_Seq_PO.order.add_edge(Initial_Testing, Batch_Allocation)

# From Batch Allocation, fermentation and aging PO run concurrently
Batch_to_Fermentation_Aging_PO = StrictPartialOrder(
    nodes=[Batch_Allocation, Fermentation_PO, Aging_PO]
)
Batch_to_Fermentation_Aging_PO.order.add_edge(Batch_Allocation, Fermentation_PO)
Batch_to_Fermentation_Aging_PO.order.add_edge(Batch_Allocation, Aging_PO)

# After fermentation and aging we do quality loop and trace logging loop
QA_and_Trace_PO = StrictPartialOrder(
    nodes=[Fermentation_PO, Aging_PO, loop_quality_feedback]
)
QA_and_Trace_PO.order.add_edge(Fermentation_PO, loop_quality_feedback)
QA_and_Trace_PO.order.add_edge(Aging_PO, loop_quality_feedback)

# Parallel packaging and market forecasting alongside Quality loop node
# Packaging and market forecasting after or concurrent with quality audit loop ?
# Let's put packaging and market forecast concurrent with logistics and events, all after QA loop finishes

After_Quality_PO = StrictPartialOrder(
    nodes=[loop_quality_feedback, Packaging_Market_PO, Logistics_Event_PO]
)
After_Quality_PO.order.add_edge(loop_quality_feedback, Packaging_Market_PO)
After_Quality_PO.order.add_edge(loop_quality_feedback, Logistics_Event_PO)

# Add customer feedback after event setup (part of Logistics_Event_PO)
# So integrate Event_Feedback_PO into Logistics_Event_PO nodes: remove Event_Setup and add Event_Feedback_PO nodes combination

# We'll flatten Event_Feedback_PO by replacing Event_Setup with the PO Event_Feedback_PO in Logistics_Event_PO nodes

Logistics_Event_with_Feedback_PO = StrictPartialOrder(
    nodes=[Logistics_Plan, Event_Feedback_PO]
)
# Order from Market_Forecast and Packaging_Design to Logistics_Plan and Event_Feedback_PO is managed in After_Quality_PO

# So update After_Quality_PO nodes accordingly
After_Quality_PO = StrictPartialOrder(
    nodes=[loop_quality_feedback, Packaging_Market_PO, Logistics_Event_with_Feedback_PO]
)
After_Quality_PO.order.add_edge(loop_quality_feedback, Packaging_Market_PO)
After_Quality_PO.order.add_edge(loop_quality_feedback, Logistics_Event_with_Feedback_PO)

# Final overall process order combining all parts
root = StrictPartialOrder(
    nodes=[Init_Seq_PO, Batch_to_Fermentation_Aging_PO, QA_and_Trace_PO, After_Quality_PO]
)
root.order.add_edge(Init_Seq_PO, Batch_to_Fermentation_Aging_PO)
root.order.add_edge(Batch_to_Fermentation_Aging_PO, QA_and_Trace_PO)
root.order.add_edge(QA_and_Trace_PO, After_Quality_PO)
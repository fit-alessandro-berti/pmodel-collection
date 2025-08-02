# Generated from: c90423c6-8c34-4503-a4d0-e0c1a2ad7214.json
# Description: This process describes the complex journey of sourcing, roasting, packaging, and distributing artisan coffee beans from remote farms to specialty cafes. It includes unique steps such as micro-lot selection, sensory profiling, fermentation control, and direct trade negotiations. The process also involves sustainability audits, custom blend creation, and dynamic pricing models based on seasonal crop yields and market demand fluctuations, ensuring premium quality and traceability throughout the supply chain. Additionally, it incorporates digital inventory synchronization and barista training programs to maintain brand consistency and customer satisfaction across multiple geographic regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Farm_Selection = Transition(label='Farm Selection')
Sample_Testing = Transition(label='Sample Testing')
Trade_Negotiation = Transition(label='Trade Negotiation')
Micro_Lot_Sorting = Transition(label='Micro-Lot Sorting')
Fermentation_Control = Transition(label='Fermentation Control')
Sensory_Profiling = Transition(label='Sensory Profiling')
Roast_Calibration = Transition(label='Roast Calibration')
Blend_Creation = Transition(label='Blend Creation')
Sustainability_Audit = Transition(label='Sustainability Audit')
Packaging_Design = Transition(label='Packaging Design')
Quality_Inspection = Transition(label='Quality Inspection')
Inventory_Sync = Transition(label='Inventory Sync')
Logistics_Planning = Transition(label='Logistics Planning')
Cafe_Training = Transition(label='Cafe Training')
Dynamic_Pricing = Transition(label='Dynamic Pricing')
Customer_Feedback = Transition(label='Customer Feedback')
Traceability_Logging = Transition(label='Traceability Logging')

# Model key subprocesses partially ordered and combined with choices and loops where appropriate.

# 1. Sourcing & initial quality assessment
sourcing = StrictPartialOrder(nodes=[
    Farm_Selection,
    Sample_Testing,
    Trade_Negotiation,
    Micro_Lot_Sorting,
])
sourcing.order.add_edge(Farm_Selection, Sample_Testing)
sourcing.order.add_edge(Sample_Testing, Trade_Negotiation)
sourcing.order.add_edge(Trade_Negotiation, Micro_Lot_Sorting)

# 2. Controlled fermentation and sensory profiling done concurrently after sorting
fermentation_and_profiling = StrictPartialOrder(nodes=[
    Fermentation_Control,
    Sensory_Profiling,
])
# No order edge - concurrent

# 3. Roasting and blend creation partially ordered (roast calibration before blend)
roast_and_blend = StrictPartialOrder(nodes=[
    Roast_Calibration,
    Blend_Creation,
])
roast_and_blend.order.add_edge(Roast_Calibration, Blend_Creation)

# 4. Sustainability audit and packaging design can happen after roasting/blending, order: audit then packaging
audit_and_packaging = StrictPartialOrder(nodes=[
    Sustainability_Audit,
    Packaging_Design,
])
audit_and_packaging.order.add_edge(Sustainability_Audit, Packaging_Design)

# 5. Quality inspection after packaging design
# Just one node for now
quality = Quality_Inspection

# 6. Inventory sync and logistics planning can occur concurrently after quality inspection
inventory_and_logistics = StrictPartialOrder(nodes=[
    Inventory_Sync,
    Logistics_Planning,
])
# concurrent - no order edge

# 7. Cafe training and customer feedback can be done in parallel after logistics
training_and_feedback = StrictPartialOrder(nodes=[
    Cafe_Training,
    Customer_Feedback,
])
# concurrent - no order edge

# 8. Traceability logging and dynamic pricing are continuous supporting activities
# We will put them in parallel with training/feedback as final steps
dynamic_and_trace = StrictPartialOrder(nodes=[
    Dynamic_Pricing,
    Traceability_Logging,
])
# concurrent - no order edge

# Now combine parts according to the process flow with partial orders:
# Overall flow:

# 1 -> 2 concurrent fermentation and profiling after Micro-Lot Sorting
# fermentation_and_profiling depends on Micro-Lot Sorting

# 2 -> 3 roast_and_blend after fermentation_and_profiling complete
# 3 ->4 audit_and_packaging 
# 4 ->5 quality inspection
# 5 ->6 inventory_and_logistics
# 6 ->7 training_and_feedback
# 7->8 dynamic_and_trace

root = StrictPartialOrder(nodes=[
    sourcing,
    fermentation_and_profiling,
    roast_and_blend,
    audit_and_packaging,
    quality,
    inventory_and_logistics,
    training_and_feedback,
    dynamic_and_trace
])

root.order.add_edge(sourcing, fermentation_and_profiling)
root.order.add_edge(fermentation_and_profiling, roast_and_blend)
root.order.add_edge(roast_and_blend, audit_and_packaging)
root.order.add_edge(audit_and_packaging, quality)
root.order.add_edge(quality, inventory_and_logistics)
root.order.add_edge(inventory_and_logistics, training_and_feedback)
root.order.add_edge(training_and_feedback, dynamic_and_trace)
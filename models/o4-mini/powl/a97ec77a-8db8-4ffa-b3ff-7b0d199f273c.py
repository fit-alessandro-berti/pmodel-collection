# Generated from: a97ec77a-8db8-4ffa-b3ff-7b0d199f273c.json
# Description: This process involves sourcing rare artisan cheeses from multiple small-scale farms, ensuring compliance with diverse international food safety standards, coordinating cold-chain logistics for perishable goods, handling customs documentation unique to dairy products, conducting quality assurance tests at multiple checkpoints, and managing niche market distribution channels to premium retailers and specialty stores worldwide. The process demands meticulous tracking of batch provenance, temperature-controlled packaging innovations, and adaptive scheduling to accommodate variable production cycles and fluctuating demand in global luxury markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
farm_sourcing      = Transition(label='Farm Sourcing')
batch_testing      = Transition(label='Batch Testing')
safety_audit       = Transition(label='Safety Audit')
compliance_review  = Transition(label='Compliance Review')
order_processing   = Transition(label='Order Processing')
label_design       = Transition(label='Label Design')
cold_packing       = Transition(label='Cold Packing')
quality_control    = Transition(label='Quality Control')
temperature_check  = Transition(label='Temperature Check')
customs_filing     = Transition(label='Customs Filing')
logistics_booking  = Transition(label='Logistics Booking')
retail_coordination= Transition(label='Retail Coordination')
delivery_tracking  = Transition(label='Delivery Tracking')

# Define sub-loops
# 1) Adaptive scheduling: analyze market & sync inventory in a loop
market_analysis    = Transition(label='Market Analysis')
inventory_sync     = Transition(label='Inventory Sync')
loop_adaptive = OperatorPOWL(
    operator=Operator.LOOP,
    children=[market_analysis, inventory_sync]
)

# 2) Rework loop for packing & QC
loop_rework = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cold_packing, quality_control]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    farm_sourcing,
    batch_testing,
    safety_audit,
    compliance_review,
    order_processing,
    loop_adaptive,
    label_design,
    loop_rework,
    temperature_check,
    customs_filing,
    logistics_booking,
    retail_coordination,
    delivery_tracking
])

# Define the control-flow / dependencies
root.order.add_edge(farm_sourcing,     batch_testing)
root.order.add_edge(batch_testing,     safety_audit)
root.order.add_edge(safety_audit,      compliance_review)
root.order.add_edge(compliance_review, order_processing)
root.order.add_edge(order_processing,  loop_adaptive)
root.order.add_edge(loop_adaptive,     label_design)
root.order.add_edge(label_design,      loop_rework)
root.order.add_edge(loop_rework,       temperature_check)
root.order.add_edge(temperature_check, customs_filing)
root.order.add_edge(temperature_check, logistics_booking)
root.order.add_edge(customs_filing,    retail_coordination)
root.order.add_edge(logistics_booking, retail_coordination)
root.order.add_edge(retail_coordination, delivery_tracking)
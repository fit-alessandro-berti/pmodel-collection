# Generated from: f686e87e-1a19-446f-9051-7f70149a6474.json
# Description: This process involves the intricate coordination of sourcing raw milk from multiple small-scale farms, ensuring quality through microbial testing, and managing seasonal variations. It includes curdling, aging under controlled humidity and temperature, and packaging with detailed provenance labels. The distribution phase requires temperature-controlled logistics to specialty retailers and direct-to-consumer channels. Additionally, the process entails continuous feedback collection from customers to refine aging profiles and innovate new cheese varieties, while complying with stringent food safety and organic certification standards throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
batch_curdling = Transition(label='Batch Curdling')
whey_removal = Transition(label='Whey Removal')
mold_inoculation = Transition(label='Mold Inoculation')
humidity_control = Transition(label='Humidity Control')
temperature_aging = Transition(label='Temperature Aging')
rind_brushing = Transition(label='Rind Brushing')
flavor_sampling = Transition(label='Flavor Sampling')
label_printing = Transition(label='Label Printing')
packaging_prep = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
order_consolidation = Transition(label='Order Consolidation')
logistics_scheduling = Transition(label='Logistics Scheduling')
customer_feedback = Transition(label='Customer Feedback')
certification_audit = Transition(label='Certification Audit')
recipe_adjustment = Transition(label='Recipe Adjustment')

#
# Structure outline:
# 1) Milk Sourcing --> Quality Testing
# 2) After Quality Testing success, batch curdling with whey removal in sequence
# 3) Aging, involving mold inoculation, humidity control, temperature aging; some activities concurrent
# 4) Rind brushing and flavor sampling after aging (partially ordered: brushing --> flavor sampling)
# 5) Packaging phase: label printing and packaging prep in parallel, then cold storage
# 6) Distribution: order consolidation --> logistics scheduling (dependent)
# 7) Continuous feedback loop: customer feedback --> recipe adjustment
# 8) Certification audits run concurrently all along, synchronize after logistics scheduling before loop back or end
# 
# The loop models continuous improvement cycle:
#   Loop body:
#       - Customer feedback
#       - Certification audit
#       - Recipe adjustment
#   Loop condition: user/external decides to exit or continue improvement

# Steps 1 and 2: sourcing, testing, curdling, whey removal in strict order
initial_seq = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, batch_curdling, whey_removal])
initial_seq.order.add_edge(milk_sourcing, quality_testing)
initial_seq.order.add_edge(quality_testing, batch_curdling)
initial_seq.order.add_edge(batch_curdling, whey_removal)

# Aging phase:
# Mold inoculation, humidity control, temperature aging
# Mold inoculation must be before humidity and temperature,
# humidity and temperature can be concurrent
aging = StrictPartialOrder(nodes=[mold_inoculation, humidity_control, temperature_aging])
aging.order.add_edge(mold_inoculation, humidity_control)
aging.order.add_edge(mold_inoculation, temperature_aging)

# Rind brushing --> flavor sampling (strict order, after aging)
post_aging = StrictPartialOrder(nodes=[rind_brushing, flavor_sampling])
post_aging.order.add_edge(rind_brushing, flavor_sampling)

# Packaging phase:
# label printing and packaging prep can be concurrent, then cold storage
packaging_parallel = StrictPartialOrder(nodes=[label_printing, packaging_prep])
# no order edges between these two: concurrent
packaging_sequence = StrictPartialOrder(nodes=[packaging_parallel, cold_storage])
packaging_sequence.order.add_edge(packaging_parallel, cold_storage)

# Because packaging_parallel is a StrictPartialOrder itself, it can be nested
# But POWL nodes should be atomic or Operators or StrictPartialOrders; 
# We'll integrate packaging_parallel as nodes inside packaging_sequence

# So redefine packaging_sequence nodes fully expanded
packaging_sequence = StrictPartialOrder(
    nodes=[label_printing, packaging_prep, cold_storage]
)
# label printing and packaging prep concurrent => no edges
# both must precede cold_storage
packaging_sequence.order.add_edge(label_printing, cold_storage)
packaging_sequence.order.add_edge(packaging_prep, cold_storage)

# Distribution phase: order consolidation before logistics scheduling
distribution = StrictPartialOrder(nodes=[order_consolidation, logistics_scheduling])
distribution.order.add_edge(order_consolidation, logistics_scheduling)

# Certification audit runs concurrently throughout but synchronizes after logistics scheduling
# So we will place certification audit parallel to distribution, joined afterwards

# Combine packaging_sequence and distribution and certification audit in a StrictPartialOrder:
# Packaging -> distribution -> certification audit (concurrent with distribution but requires it to end)
# We'll do packaging --> distribution --> certification audit
packaging_to_distribution = StrictPartialOrder(
    nodes=[packaging_sequence, distribution, certification_audit]
)
packaging_to_distribution.order.add_edge(packaging_sequence, distribution)
packaging_to_distribution.order.add_edge(distribution, certification_audit)

# Assemble main production partial order:

# initial_seq (milk sourcing to whey removal) -->
# aging -->
# post_aging -->
# packaging_to_distribution

main_production = StrictPartialOrder(
    nodes=[initial_seq, aging, post_aging, packaging_to_distribution]
)
main_production.order.add_edge(initial_seq, aging)
main_production.order.add_edge(aging, post_aging)
main_production.order.add_edge(post_aging, packaging_to_distribution)

# Continuous improvement loop:
# Loop body:
# customer_feedback --> certification_audit --> recipe_adjustment
# Modeled as a strict partial order
improvement_body = StrictPartialOrder(
    nodes=[customer_feedback, certification_audit, recipe_adjustment]
)
improvement_body.order.add_edge(customer_feedback, certification_audit)
improvement_body.order.add_edge(certification_audit, recipe_adjustment)

# Loop node: execute main_production, then 0 or more iterations of improvement_body + main production again
# As the POWL loop nodes are * (A,B):
# execute A, then either exit or execute B and then A again

root = OperatorPOWL(operator=Operator.LOOP, children=[main_production, improvement_body])
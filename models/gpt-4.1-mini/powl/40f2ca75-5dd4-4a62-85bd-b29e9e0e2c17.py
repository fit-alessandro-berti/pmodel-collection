# Generated from: 40f2ca75-5dd4-4a62-85bd-b29e9e0e2c17.json
# Description: This process outlines the intricate steps involved in producing, certifying, and exporting artisanal cheese from rural farms to international gourmet markets. It begins with milk sourcing from select heritage breeds, followed by traditional curdling and aging methods. Quality inspections and microbial testing ensure compliance with stringent health standards. Packaging is customized for optimal preservation during long transit times. The export phase includes complex documentation, customs clearance, and coordination with specialized logistics partners. Finally, market entry involves targeted distribution to niche retailers and promotional events to build brand recognition overseas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
milk_sourcing = Transition(label='Milk Sourcing')
curd_preparation = Transition(label='Curd Preparation')
coagulation_check = Transition(label='Coagulation Check')
whey_removal = Transition(label='Whey Removal')
pressing_cheese = Transition(label='Pressing Cheese')
salting_process = Transition(label='Salting Process')
aging_control = Transition(label='Aging Control')
microbial_test = Transition(label='Microbial Test')
quality_audit = Transition(label='Quality Audit')
packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
export_licensing = Transition(label='Export Licensing')
customs_filing = Transition(label='Customs Filing')
logistics_setup = Transition(label='Logistics Setup')
market_launch = Transition(label='Market Launch')

# Create partial orders for each phase

# Phase 1: Milk Sourcing -> Curd Preparation -> Coagulation Check -> Whey Removal -> Pressing Cheese -> Salting Process -> Aging Control 
phase1_nodes = [
    milk_sourcing, curd_preparation, coagulation_check, whey_removal,
    pressing_cheese, salting_process, aging_control
]
phase1 = StrictPartialOrder(nodes=phase1_nodes)
phase1.order.add_edge(milk_sourcing, curd_preparation)
phase1.order.add_edge(curd_preparation, coagulation_check)
phase1.order.add_edge(coagulation_check, whey_removal)
phase1.order.add_edge(whey_removal, pressing_cheese)
phase1.order.add_edge(pressing_cheese, salting_process)
phase1.order.add_edge(salting_process, aging_control)

# Phase 2: Quality Inspection and Microbial Testing
# Microbial Test and Quality Audit are concurrent after Aging Control, but both must precede Packaging Design
quality_nodes = [microbial_test, quality_audit]
quality = StrictPartialOrder(nodes=quality_nodes)  # no order between these two, concurrent

# Packaging Design and Label Printing after quality checks (both depend on microbial_test & quality_audit)
packaging_phase = StrictPartialOrder(nodes=[packaging_design, label_printing])
packaging_phase.order.add_edge(packaging_design, label_printing)  # packaging -> label printing

# Phase 3: Exporting
export_nodes = [export_licensing, customs_filing, logistics_setup]
export = StrictPartialOrder(nodes=export_nodes)
export.order.add_edge(export_licensing, customs_filing)
export.order.add_edge(customs_filing, logistics_setup)

# Phase 4: Market Launch after export logistics setup
market = StrictPartialOrder(nodes=[market_launch])

# Combine quality and packaging phases
quality_packaging = StrictPartialOrder(
    nodes=[quality, packaging_phase]
)
# We need all four activities as nodes, flatten them for edges
# Flatten the nodes of quality and packaging_phase
# Instead of nesting StrictPartialOrders inside nodes (which is not allowed), we join all nodes under a single PO
q_p_nodes = quality_nodes + [packaging_design, label_printing]
quality_packaging = StrictPartialOrder(nodes=q_p_nodes)
# Both microbial_test and quality_audit precede packaging_design
quality_packaging.order.add_edge(microbial_test, packaging_design)
quality_packaging.order.add_edge(quality_audit, packaging_design)
# Packaging design precedes label printing
quality_packaging.order.add_edge(packaging_design, label_printing)

# Combine phases 1 -> quality_packaging -> export -> market

root_nodes = [phase1, quality_packaging, export, market]

root = StrictPartialOrder(nodes=root_nodes)

# phase1 precedes quality_packaging
root.order.add_edge(phase1, quality_packaging)

# quality_packaging precedes export
root.order.add_edge(quality_packaging, export)

# export precedes market launch
root.order.add_edge(export, market)
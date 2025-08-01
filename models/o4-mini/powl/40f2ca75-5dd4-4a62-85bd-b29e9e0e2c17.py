# Generated from: 40f2ca75-5dd4-4a62-85bd-b29e9e0e2c17.json
# Description: This process outlines the intricate steps involved in producing, certifying, and exporting artisanal cheese from rural farms to international gourmet markets. It begins with milk sourcing from select heritage breeds, followed by traditional curdling and aging methods. Quality inspections and microbial testing ensure compliance with stringent health standards. Packaging is customized for optimal preservation during long transit times. The export phase includes complex documentation, customs clearance, and coordination with specialized logistics partners. Finally, market entry involves targeted distribution to niche retailers and promotional events to build brand recognition overseas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
milk_sourcing     = Transition(label='Milk Sourcing')
curd_preparation  = Transition(label='Curd Preparation')
coagulation_check = Transition(label='Coagulation Check')
whey_removal      = Transition(label='Whey Removal')
pressing_cheese   = Transition(label='Pressing Cheese')
salting_process   = Transition(label='Salting Process')
aging_control     = Transition(label='Aging Control')
microbial_test    = Transition(label='Microbial Test')
quality_audit     = Transition(label='Quality Audit')
packaging_design  = Transition(label='Packaging Design')
label_printing    = Transition(label='Label Printing')
export_licensing  = Transition(label='Export Licensing')
customs_filing    = Transition(label='Customs Filing')
logistics_setup   = Transition(label='Logistics Setup')
market_launch     = Transition(label='Market Launch')

# Build the partial order model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    curd_preparation,
    coagulation_check,
    whey_removal,
    pressing_cheese,
    salting_process,
    aging_control,
    microbial_test,
    quality_audit,
    packaging_design,
    label_printing,
    export_licensing,
    customs_filing,
    logistics_setup,
    market_launch
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, curd_preparation)
root.order.add_edge(curd_preparation, coagulation_check)
root.order.add_edge(coagulation_check, whey_removal)
root.order.add_edge(whey_removal, pressing_cheese)
root.order.add_edge(pressing_cheese, salting_process)
root.order.add_edge(salting_process, aging_control)
# After aging, both tests can run (concurrent)
root.order.add_edge(aging_control, microbial_test)
root.order.add_edge(aging_control, quality_audit)
# Both tests must complete before packaging
root.order.add_edge(microbial_test, packaging_design)
root.order.add_edge(quality_audit, packaging_design)
root.order.add_edge(packaging_design, label_printing)
# Export documentation and logistics
root.order.add_edge(label_printing, export_licensing)
root.order.add_edge(export_licensing, customs_filing)
root.order.add_edge(customs_filing, logistics_setup)
# Final market launch
root.order.add_edge(logistics_setup, market_launch)
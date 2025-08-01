# Generated from: c76e808d-69af-4f46-a81b-151f08211ef3.json
# Description: This process details the intricate and atypical supply chain for producing and distributing artisanal cheeses from small-scale farms to niche gourmet retailers. It involves unique steps like microbial culture selection, seasonal milk sourcing based on animal diet, controlled aging with environmental monitoring, and bespoke packaging tailored to cheese type. The process also integrates direct farmer collaboration, traceability through blockchain, and adaptive logistics that account for cheese maturation stages and fragile transport conditions, ensuring product quality and authenticity while balancing traditional methods with modern technology.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing    = Transition(label="Milk Sourcing")
culture_selection = Transition(label="Culture Selection")
milk_testing     = Transition(label="Milk Testing")
curd_formation   = Transition(label="Curd Formation")
whey_separation  = Transition(label="Whey Separation")
molding_cheese   = Transition(label="Molding Cheese")
salting_process  = Transition(label="Salting Process")
aging_setup      = Transition(label="Aging Setup")
env_monitoring   = Transition(label="Env Monitoring")
flavor_profiling = Transition(label="Flavor Profiling")
packaging_design = Transition(label="Packaging Design")
blockchain_entry = Transition(label="Blockchain Entry")
quality_audit    = Transition(label="Quality Audit")
retail_sync      = Transition(label="Retail Sync")
transport_prep   = Transition(label="Transport Prep")
delivery_tracking= Transition(label="Delivery Tracking")
customer_feedback= Transition(label="Customer Feedback")

# Silent transition for loop exit
skip = SilentTransition()

# Loop for environmental monitoring during aging:
# Execute Env Monitoring, then either exit (skip) or repeat monitoring.
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[env_monitoring, skip]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_selection,
    milk_testing,
    curd_formation,
    whey_separation,
    molding_cheese,
    salting_process,
    aging_setup,
    aging_loop,
    flavor_profiling,
    packaging_design,
    blockchain_entry,
    quality_audit,
    retail_sync,
    transport_prep,
    delivery_tracking,
    customer_feedback
])

# Define the control-flow (partial order) edges

# 1) Milk preparation: sourcing & culture → testing
root.order.add_edge(milk_sourcing, milk_testing)
root.order.add_edge(culture_selection, milk_testing)

# 2) Testing → curd → whey separation
root.order.add_edge(milk_testing, curd_formation)
root.order.add_edge(curd_formation, whey_separation)

# 3) Whey separation → mold → salt → aging setup
root.order.add_edge(whey_separation, molding_cheese)
root.order.add_edge(molding_cheese, salting_process)
root.order.add_edge(salting_process, aging_setup)

# 4) Aging setup → enter monitoring loop → flavor profiling
root.order.add_edge(aging_setup, aging_loop)
root.order.add_edge(aging_loop, flavor_profiling)

# 5) After flavor profiling, design packaging and enter blockchain in parallel
root.order.add_edge(flavor_profiling, packaging_design)
root.order.add_edge(flavor_profiling, blockchain_entry)

# 6) Packaging & blockchain → quality audit
root.order.add_edge(packaging_design, quality_audit)
root.order.add_edge(blockchain_entry, quality_audit)

# 7) Quality audit → retail sync & transport prep in parallel
root.order.add_edge(quality_audit, retail_sync)
root.order.add_edge(quality_audit, transport_prep)

# 8) Retail sync & transport prep → delivery tracking → customer feedback
root.order.add_edge(retail_sync, delivery_tracking)
root.order.add_edge(transport_prep, delivery_tracking)
root.order.add_edge(delivery_tracking, customer_feedback)
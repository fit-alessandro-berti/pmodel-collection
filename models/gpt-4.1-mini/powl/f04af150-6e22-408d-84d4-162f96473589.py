# Generated from: f04af150-6e22-408d-84d4-162f96473589.json
# Description: This process describes a complex supply chain tailored for artisan goods involving multiple small-scale producers, quality verification steps, custom packaging, and niche distribution channels. It integrates bespoke material sourcing, handcrafted production timelines, and direct consumer engagement through curated marketplaces. The process also incorporates sustainability audits, adaptive inventory management based on seasonal demand, and collaborative marketing strategies among stakeholders to maintain brand authenticity and exclusivity while scaling operations within limited production capacities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Material_Sourcing = Transition(label='Material Sourcing')
Supplier_Vetting = Transition(label='Supplier Vetting')
Design_Review = Transition(label='Design Review')
Prototype_Build = Transition(label='Prototype Build')
Quality_Audit = Transition(label='Quality Audit')
Batch_Scheduling = Transition(label='Batch Scheduling')
Handcrafting = Transition(label='Handcrafting')
Packaging_Design = Transition(label='Packaging Design')
Custom_Labeling = Transition(label='Custom Labeling')
Sustainability_Check = Transition(label='Sustainability Check')
Inventory_Sync = Transition(label='Inventory Sync')
Market_Analysis = Transition(label='Market Analysis')
Order_Aggregation = Transition(label='Order Aggregation')
Distribution_Plan = Transition(label='Distribution Plan')
Customer_Feedback = Transition(label='Customer Feedback')

# Partial order for sourcing and vetting (Material Sourcing -> Supplier Vetting)
sourcing_vetting = StrictPartialOrder(nodes=[Material_Sourcing, Supplier_Vetting])
sourcing_vetting.order.add_edge(Material_Sourcing, Supplier_Vetting)

# Partial order for design, prototype and quality audit
design_process = StrictPartialOrder(
    nodes=[Design_Review, Prototype_Build, Quality_Audit]
)
design_process.order.add_edge(Design_Review, Prototype_Build)
design_process.order.add_edge(Prototype_Build, Quality_Audit)

# Partial order for packaging and labeling (Packaging Design -> Custom Labeling)
packaging_process = StrictPartialOrder(nodes=[Packaging_Design, Custom_Labeling])
packaging_process.order.add_edge(Packaging_Design, Custom_Labeling)

# Loop to represent adaptive inventory management and sustainability check before batch scheduling
# Loop(* (Batch_Scheduling, Sustainability_Check and Inventory_Sync concurrent))
sustain_inv_sync = StrictPartialOrder(nodes=[Sustainability_Check, Inventory_Sync])  # concurrent sustainability + inventory
batch_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Batch_Scheduling,
        sustain_inv_sync
    ]
)

# Market analysis, order aggregation, distribution plan in sequence
market_to_distribution = StrictPartialOrder(
    nodes=[Market_Analysis, Order_Aggregation, Distribution_Plan]
)
market_to_distribution.order.add_edge(Market_Analysis, Order_Aggregation)
market_to_distribution.order.add_edge(Order_Aggregation, Distribution_Plan)

# Handcrafting depends on quality audit and supplier vetting
handcrafting_dep = StrictPartialOrder(
    nodes=[Handcrafting, Quality_Audit, Supplier_Vetting]
)
handcrafting_dep.order.add_edge(Quality_Audit, Handcrafting)
handcrafting_dep.order.add_edge(Supplier_Vetting, Handcrafting)

# Customer feedback after distribution plan
feedback_order = StrictPartialOrder(
    nodes=[Distribution_Plan, Customer_Feedback]
)
feedback_order.order.add_edge(Distribution_Plan, Customer_Feedback)

# Marketing strategy involves Market Analysis and Customer Feedback concurrent
marketing = StrictPartialOrder(
    nodes=[Market_Analysis, Customer_Feedback]
)  # no order - concurrent, but both included in partial order for completeness

# Build full sourcing and production phase
sourcing_and_design = StrictPartialOrder(
    nodes=[sourcing_vetting, design_process]
)
sourcing_and_design.order.add_edge(sourcing_vetting, design_process)

# Full pre-packaging phase: sourcing_and_design then handcrafting then packaging_process
pre_packaging = StrictPartialOrder(
    nodes=[sourcing_and_design, handcrafting_dep, packaging_process]
)
pre_packaging.order.add_edge(sourcing_and_design, handcrafting_dep)
pre_packaging.order.add_edge(handcrafting_dep, packaging_process)

# Combine packaging with batch loop
packaging_batch = StrictPartialOrder(
    nodes=[packaging_process, batch_loop]
)
packaging_batch.order.add_edge(packaging_process, batch_loop)

# Combine everything before market to distribution
production_to_distribution = StrictPartialOrder(
    nodes=[pre_packaging, packaging_batch, market_to_distribution]
)
production_to_distribution.order.add_edge(pre_packaging, packaging_batch)
production_to_distribution.order.add_edge(packaging_batch, market_to_distribution)

# Root combines production_to_distribution and customer feedback after distribution plan
root = StrictPartialOrder(
    nodes=[production_to_distribution, feedback_order]
)
root.order.add_edge(production_to_distribution, feedback_order)
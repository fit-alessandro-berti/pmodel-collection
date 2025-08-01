# Generated from: 5de8837f-7d09-4b94-8344-9af78eca43f6.json
# Description: This process involves the end-to-end management of artisan cheese production and distribution, starting from sourcing rare milk varieties from niche farms, monitoring fermentation stages with microbial analysis, and custom aging in controlled environments. It includes quality inspections, bespoke packaging design tailored for each cheese type, coordinating limited batch shipments to specialty retailers, and managing customer feedback loops for continuous product refinement. The process also integrates seasonal variations in milk supply, compliance with food safety regulations, and marketing efforts highlighting artisanal craftsmanship and provenance stories to attract connoisseurs and maintain brand exclusivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Microbial_Test = Transition(label='Microbial Test')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Whey_Drain = Transition(label='Whey Drain')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Cheese = Transition(label='Press Cheese')
Custom_Aging = Transition(label='Custom Aging')
Quality_Inspect = Transition(label='Quality Inspect')
Flavor_Profiling = Transition(label='Flavor Profiling')
Package_Design = Transition(label='Package Design')
Batch_Labeling = Transition(label='Batch Labeling')
Shipment_Plan = Transition(label='Shipment Plan')
Retail_Notify = Transition(label='Retail Notify')
Feedback_Review = Transition(label='Feedback Review')
Regulation_Check = Transition(label='Regulation Check')
Marketing_Draft = Transition(label='Marketing Draft')
Inventory_Audit = Transition(label='Inventory Audit')

skip = SilentTransition()

# Loop for seasonal variations and continuous improvement
# Loop body:
#  - Milk sourcing to fermentation (Milk Sourcing -> Microbial Test -> Milk Pasteurize -> Curd Formation -> Whey Drain -> Mold Inoculate -> Press Cheese)
#  - Then Custom Aging and Quality Inspect (in parallel)
#  - Flavor Profiling and Package Design (Package Design depending on Flavor Profiling)
#  - Shipment plan phases and Retail notify
#  - Feedback review loop (Feedback Review <-> Quality Inspect)
#  - Regulation Check must be done timely (concurrent with packaging)
#  - Marketing and Inventory (concurrent with shipment planning)
#  - Inventory audit likely at the end of a loop iteration before next milk sourcing

# Build sub-partial orders for the inner loop parts

# 1) Fermentation & Production steps sequentially
fermentation_PO = StrictPartialOrder(
    nodes=[Milk_Sourcing, Microbial_Test, Milk_Pasteurize, Curd_Formation, Whey_Drain, Mold_Inoculate, Press_Cheese]
)
fermentation_PO.order.add_edge(Milk_Sourcing, Microbial_Test)
fermentation_PO.order.add_edge(Microbial_Test, Milk_Pasteurize)
fermentation_PO.order.add_edge(Milk_Pasteurize, Curd_Formation)
fermentation_PO.order.add_edge(Curd_Formation, Whey_Drain)
fermentation_PO.order.add_edge(Whey_Drain, Mold_Inoculate)
fermentation_PO.order.add_edge(Mold_Inoculate, Press_Cheese)

# 2) Aging and Quality Inspect concurrent after Press Cheese
aging_and_quality_PO = StrictPartialOrder(
    nodes=[Custom_Aging, Quality_Inspect]
)
# No edges inside - concurrent

# 3) Flavor profiling before packaging design
flavor_package_PO = StrictPartialOrder(
    nodes=[Flavor_Profiling, Package_Design]
)
flavor_package_PO.order.add_edge(Flavor_Profiling, Package_Design)

# 4) Batch Labeling after packaging design
batch_labeling_PO = StrictPartialOrder(
    nodes=[Package_Design, Batch_Labeling]
)
batch_labeling_PO.order.add_edge(Package_Design, Batch_Labeling)

# 5) Shipment planning after batch labeling
shipment_PO = StrictPartialOrder(
    nodes=[Batch_Labeling, Shipment_Plan, Retail_Notify]
)
shipment_PO.order.add_edge(Batch_Labeling, Shipment_Plan)
shipment_PO.order.add_edge(Shipment_Plan, Retail_Notify)

# 6) Feedback Review loops with Quality Inspect using a loop operator:
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Inspect, Feedback_Review])

# 7) Regulation Check concurrent with packaging and shipment phases
regulation_and_marketing_PO = StrictPartialOrder(
    nodes=[Regulation_Check, Marketing_Draft]
)

# 8) Inventory audit concurrent with marketing and shipment
marketing_inventory_PO = StrictPartialOrder(
    nodes=[Marketing_Draft, Inventory_Audit]
)
marketing_inventory_PO.order.add_edge(Marketing_Draft, Inventory_Audit)

# Merge regulation_and_marketing_PO and marketing_inventory_PO for concurrency of Regulation, Marketing, Inventory
reg_mark_inv_PO = StrictPartialOrder(
    nodes=[Regulation_Check, Marketing_Draft, Inventory_Audit]
)
reg_mark_inv_PO.order.add_edge(Marketing_Draft, Inventory_Audit)
# Regulation_Check concurrent, so no edges from or to it

# Now combine all partial orders reflecting the process flow

# Top level partial order nodes:
# fermentation_PO --> aging_and_quality_PO, flavor_package_PO, reg_mark_inv_PO, shipment_PO, feedback_loop
# Place them and organize ordering:

root = StrictPartialOrder(
    nodes=[fermentation_PO, aging_and_quality_PO, flavor_package_PO, batch_labeling_PO, shipment_PO, feedback_loop, reg_mark_inv_PO]
)

# Edges:
# fermentation proceed to aging_and_quality and flavor_package_PO (aging and flavor start after fermentation)
root.order.add_edge(fermentation_PO, aging_and_quality_PO)
root.order.add_edge(fermentation_PO, flavor_package_PO)
root.order.add_edge(flavor_package_PO, batch_labeling_PO)
root.order.add_edge(batch_labeling_PO, shipment_PO)

# shipment_PO, feedback_loop, reg_mark_inv_PO start after aging and quality (concurrent)
root.order.add_edge(aging_and_quality_PO, shipment_PO)
root.order.add_edge(aging_and_quality_PO, feedback_loop)
root.order.add_edge(aging_and_quality_PO, reg_mark_inv_PO)

# feedback_loop feeds back to fermentation_PO for continuous improvement cycle
root.order.add_edge(feedback_loop, fermentation_PO)

# This creates a loop in the model representing the feedback-driven refinement and seasonal recurrences

# The Inventory_Audit is within reg_mark_inv_PO and scheduled after Marketing_Draft already

# This model captures:
# - linear start with fermentation
# - concurrent aging and quality inspect
# - sequential flavor profiling, packaging, labeling, shipping
# - concurrent regulatory check, marketing and inventory management
# - feedback loop feeding back to start

# Done
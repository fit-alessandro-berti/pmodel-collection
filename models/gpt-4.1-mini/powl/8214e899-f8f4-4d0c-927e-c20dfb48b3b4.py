# Generated from: 8214e899-f8f4-4d0c-927e-c20dfb48b3b4.json
# Description: This process manages the end-to-end workflow for sourcing rare, handcrafted materials from remote artisan communities and integrating them into a luxury goods manufacturing pipeline. It involves delicate coordination between local cooperatives, quality verification through sensory and historical validation, sustainable logistics planning, custom tariff negotiations, and adaptive production scheduling to accommodate fluctuating artisan output while ensuring ethical sourcing standards and minimizing environmental impact throughout the supply chain lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Source_Artisans = Transition(label='Source Artisans')
Validate_Origins = Transition(label='Validate Origins')
Quality_Inspect = Transition(label='Quality Inspect')
Negotiate_Tariffs = Transition(label='Negotiate Tariffs')
Schedule_Pickup = Transition(label='Schedule Pickup')
Custom_Clearance = Transition(label='Custom Clearance')
Transport_Goods = Transition(label='Transport Goods')
Inventory_Check = Transition(label='Inventory Check')
Material_Testing = Transition(label='Material Testing')
Sustainability_Audit = Transition(label='Sustainability Audit')
Adjust_Production = Transition(label='Adjust Production')
Packaging_Design = Transition(label='Packaging Design')
Finalize_Orders = Transition(label='Finalize Orders')
Distribute_Stock = Transition(label='Distribute Stock')
Feedback_Collect = Transition(label='Feedback Collect')
Supplier_Review = Transition(label='Supplier Review')

# Define loops for adaptive production scheduling:
# Loop node: (* (Adjust Production, Validate Origins))
# Here, after Adjust Production, we either exit or do Validate Origins + continue loop (re-check and re-adjust)
loop_adapt = OperatorPOWL(operator=Operator.LOOP, children=[Adjust_Production, Validate_Origins])

# Choice after Quality Inspection: either proceed to tariff negotiation or go back to source artisans for re-check (loop)
# This models possible re-sourcing or re-validation step
loop_resourcing = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Quality_Inspect, Source_Artisans]
)

# Choice after Sustainability Audit: either accept and proceed or do Supplier Review as a corrective measure
choice_sustainability = OperatorPOWL(operator=Operator.XOR, children=[SilentTransition(), Supplier_Review])

# Partial order nodes sets representing logical sections:
# 1. Sourcing & Validation
# Source Artisans -> Validate Origins -> Quality Inspect
po_src = StrictPartialOrder(nodes=[Source_Artisans, Validate_Origins, Quality_Inspect, loop_resourcing])
po_src.order.add_edge(Source_Artisans, Validate_Origins)
po_src.order.add_edge(Validate_Origins, Quality_Inspect)
po_src.order.add_edge(Quality_Inspect, loop_resourcing)

# 2. Logistics & Customs
# Negotiate Tariffs -> Schedule Pickup -> Custom Clearance -> Transport Goods
po_logistics = StrictPartialOrder(nodes=[Negotiate_Tariffs, Schedule_Pickup, Custom_Clearance, Transport_Goods])
po_logistics.order.add_edge(Negotiate_Tariffs, Schedule_Pickup)
po_logistics.order.add_edge(Schedule_Pickup, Custom_Clearance)
po_logistics.order.add_edge(Custom_Clearance, Transport_Goods)

# 3. Inventory & Testing
# Inventory Check in parallel with Sustainability Audit and Material Testing
po_test = StrictPartialOrder(nodes=[Inventory_Check, Sustainability_Audit, Material_Testing, choice_sustainability])
# Sustainability Audit leads to choice of Supplier Review
po_test.order.add_edge(Sustainability_Audit, choice_sustainability)

# 4. Production adjustment loop including loop_adapt from above
# Material Testing -> Adjust Production loop
po_prod_adj = StrictPartialOrder(nodes=[Material_Testing, loop_adapt])
po_prod_adj.order.add_edge(Material_Testing, loop_adapt)

# 5. Finalization and distribution
# Packaging Design -> Finalize Orders -> Distribute Stock -> Feedback Collect
po_finalize = StrictPartialOrder(nodes=[Packaging_Design, Finalize_Orders, Distribute_Stock, Feedback_Collect])
po_finalize.order.add_edge(Packaging_Design, Finalize_Orders)
po_finalize.order.add_edge(Finalize_Orders, Distribute_Stock)
po_finalize.order.add_edge(Distribute_Stock, Feedback_Collect)

# Compose the main process partial order:
# Start from sourcing chain then logistic, then inventory/testing + production adjustment, then final steps
# Negotiate Tariffs can only start after Quality Inspect completes
# Inventory Check, Sustainability Audit, Material Testing happen after Transport Goods
# Packaging Design can start after loop_adapt completes (adjust production)
root = StrictPartialOrder(nodes=[po_src, po_logistics, po_test, po_prod_adj, po_finalize])

# Add cross-component order edges reflecting control flow dependencies

# After Quality Inspect / loop_resourcing finish, Negotiate Tariffs starts
root.order.add_edge(po_src, po_logistics)

# Transport Goods before Inventory Check, Sustainability Audit, Material Testing start
root.order.add_edge(po_logistics, po_test)

# Sustainability audit flow controls Supplier Review within po_test (already linked inside po_test)

# po_test dependencies flow into production adjustment
root.order.add_edge(po_test, po_prod_adj)

# Production adjustment loop leads to packaging design (/ finalization)
root.order.add_edge(po_prod_adj, po_finalize)
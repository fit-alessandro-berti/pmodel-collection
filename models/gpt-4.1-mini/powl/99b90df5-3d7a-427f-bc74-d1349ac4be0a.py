# Generated from: 99b90df5-3d7a-427f-bc74-d1349ac4be0a.json
# Description: This process involves sourcing rare, handcrafted materials from remote artisans across multiple continents, verifying authenticity through blockchain certification, coordinating bespoke production schedules, managing fluctuating artisan availability, and ensuring timely delivery to niche luxury boutiques. The workflow integrates cultural considerations, sustainable practices, dynamic pricing negotiation, quality assurance audits, and custom packaging design to maintain exclusivity and traceability throughout the supply chain. Customer feedback loops and artisan development programs further enhance product uniqueness and community impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Material_Sourcing = Transition(label='Material Sourcing')
Authenticity_Check = Transition(label='Authenticity Check')
Blockchain_Audit = Transition(label='Blockchain Audit')
Schedule_Sync = Transition(label='Schedule Sync')
Artisan_Liaison = Transition(label='Artisan Liaison')
Price_Negotiation = Transition(label='Price Negotiation')
Quality_Review = Transition(label='Quality Review')
Production_Setup = Transition(label='Production Setup')
Custom_Packaging = Transition(label='Custom Packaging')
Sustainability_Check = Transition(label='Sustainability Check')
Logistics_Plan = Transition(label='Logistics Plan')
Boutique_Delivery = Transition(label='Boutique Delivery')
Feedback_Analysis = Transition(label='Feedback Analysis')
Community_Support = Transition(label='Community Support')
Inventory_Update = Transition(label='Inventory Update')

# Define loops for customer feedback loop: Feedback_Analysis and Community_Support loop
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Analysis, Community_Support])

# Define a loop for managing fluctuating artisan availability and schedule sync:
artisan_availability_loop = OperatorPOWL(operator=Operator.LOOP, children=[Schedule_Sync, Artisan_Liaison])

# Define a loop for price negotiation and quality review - these two may depend on each other iteratively
price_quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[Price_Negotiation, Quality_Review])

# Define a choice for blockchain verification: Authenticity_Check or Blockchain_Audit (as alternative ways to verify)
verification_choice = OperatorPOWL(operator=Operator.XOR, children=[Authenticity_Check, Blockchain_Audit])

# Partial order representing main flow and integration of subprocesses
root = StrictPartialOrder(nodes=[
    Material_Sourcing,
    verification_choice,
    artisan_availability_loop,
    price_quality_loop,
    Production_Setup,
    Sustainability_Check,
    Custom_Packaging,
    Logistics_Plan,
    Boutique_Delivery,
    feedback_loop,
    Inventory_Update
])

# Add edges to express control flow dependencies and partial orders
root.order.add_edge(Material_Sourcing, verification_choice)
root.order.add_edge(verification_choice, artisan_availability_loop)
root.order.add_edge(artisan_availability_loop, price_quality_loop)
root.order.add_edge(price_quality_loop, Production_Setup)
root.order.add_edge(Production_Setup, Sustainability_Check)
root.order.add_edge(Sustainability_Check, Custom_Packaging)
root.order.add_edge(Custom_Packaging, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Boutique_Delivery)
root.order.add_edge(Boutique_Delivery, feedback_loop)
root.order.add_edge(feedback_loop, Inventory_Update)
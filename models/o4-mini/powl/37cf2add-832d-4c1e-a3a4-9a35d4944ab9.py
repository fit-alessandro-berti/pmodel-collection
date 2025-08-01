# Generated from: 37cf2add-832d-4c1e-a3a4-9a35d4944ab9.json
# Description: This process outlines the dynamic leasing of fine art pieces to corporate clients, combining inventory management, client preference analysis, and rotational logistics to ensure artworks remain fresh and relevant within office environments. The process begins with artwork acquisition and categorization, followed by personalized client profiling to match art styles with corporate branding. Contracts are negotiated with flexible duration terms, incorporating insurance and maintenance clauses. Logistics teams coordinate artwork delivery, installation, and periodic rotation based on client feedback and seasonal trends. Maintenance crews perform condition checks and restoration as needed. Billing cycles adapt to contract changes, while data analytics monitor client satisfaction and market trends to optimize the art portfolio. The process concludes with contract renewal discussions or artwork return, ensuring a seamless, evolving art leasing experience that balances client needs, artist exposure, and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
art_sourcing       = Transition(label='Art Sourcing')
style_analysis     = Transition(label='Style Analysis')
client_profiling   = Transition(label='Client Profiling')
contract_drafting  = Transition(label='Contract Drafting')
insurance_setup    = Transition(label='Insurance Setup')
inventory_tagging  = Transition(label='Inventory Tagging')
logistics_planning = Transition(label='Logistics Planning')
artwork_delivery   = Transition(label='Artwork Delivery')
installation_setup = Transition(label='Installation Setup')
rotation           = Transition(label='Rotation Scheduling')
condition_check    = Transition(label='Condition Check')
restoration_work   = Transition(label='Restoration Work')
billing            = Transition(label='Billing Process')
feedback           = Transition(label='Feedback Collection')
portfolio_review   = Transition(label='Portfolio Review')
contract_renewal   = Transition(label='Contract Renewal')
return_handling    = Transition(label='Return Handling')
skip               = SilentTransition()

# Restoration is optional
restoration_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[restoration_work, skip]
)

# Maintenance partial order: condition check before possible restoration
maintenance_po = StrictPartialOrder(nodes=[condition_check, restoration_choice])
maintenance_po.order.add_edge(condition_check, restoration_choice)

# Loop of rotation and maintenance
rotation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[rotation, maintenance_po]
)

# Final choice: contract renewal or return handling
final_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[contract_renewal, return_handling]
)

# Initial setup sequence
initial_po = StrictPartialOrder(nodes=[
    art_sourcing, style_analysis, client_profiling,
    contract_drafting, insurance_setup, inventory_tagging,
    logistics_planning, artwork_delivery, installation_setup
])
initial_edges = [
    (art_sourcing, style_analysis),
    (style_analysis, client_profiling),
    (client_profiling, contract_drafting),
    (contract_drafting, insurance_setup),
    (insurance_setup, inventory_tagging),
    (inventory_tagging, logistics_planning),
    (logistics_planning, artwork_delivery),
    (artwork_delivery, installation_setup)
]
for src, tgt in initial_edges:
    initial_po.order.add_edge(src, tgt)

# Assemble the whole process
root = StrictPartialOrder(nodes=[
    initial_po,
    rotation_loop,
    billing,
    feedback,
    portfolio_review,
    final_choice
])
root.order.add_edge(initial_po,     rotation_loop)
root.order.add_edge(rotation_loop,  billing)
root.order.add_edge(billing,        feedback)
root.order.add_edge(feedback,       portfolio_review)
root.order.add_edge(portfolio_review, final_choice)
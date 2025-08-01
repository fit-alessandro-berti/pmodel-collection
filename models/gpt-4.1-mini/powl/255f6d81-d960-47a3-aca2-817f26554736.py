# Generated from: 255f6d81-d960-47a3-aca2-817f26554736.json
# Description: This process governs the acquisition, evaluation, and rotation of artwork leased to corporate offices for aesthetic enhancement and brand alignment. It involves curating pieces based on corporate culture, negotiating lease terms with artists or galleries, scheduling installation and maintenance, and periodically rotating collections to refresh environments. Feedback from employees is collected to assess impact on workplace ambiance and productivity. Additionally, the process includes managing insurance, provenance verification, and coordinating art events to engage stakeholders. The goal is to maintain a dynamic, inspiring visual environment while optimizing budget and compliance with corporate policies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Art_Sourcing = Transition(label='Art Sourcing')
Budget_Approval = Transition(label='Budget Approval')
Artist_Liaison = Transition(label='Artist Liaison')
Lease_Negotiation = Transition(label='Lease Negotiation')
Workplace_Survey = Transition(label='Workplace Survey')
Collection_Selection = Transition(label='Collection Selection')
Contract_Drafting = Transition(label='Contract Drafting')
Insurance_Setup = Transition(label='Insurance Setup')
Installation_Plan = Transition(label='Installation Plan')
Artwork_Delivery = Transition(label='Artwork Delivery')
Display_Setup = Transition(label='Display Setup')
Maintenance_Check = Transition(label='Maintenance Check')
Employee_Feedback = Transition(label='Employee Feedback')
Collection_Rotation = Transition(label='Collection Rotation')
Event_Coordination = Transition(label='Event Coordination')
Provenance_Check = Transition(label='Provenance Check')
Policy_Compliance = Transition(label='Policy Compliance')

# Phase 1: Sourcing & Budget
# Art Sourcing -> Budget Approval
po_sourcing_budget = StrictPartialOrder(
    nodes=[Art_Sourcing, Budget_Approval]
)
po_sourcing_budget.order.add_edge(Art_Sourcing, Budget_Approval)

# Phase 2: Artist & Lease negotiation + Contract + Insurance + Provenance + Policy
# These are sequential with Policy Compliance last
po_negotiation = StrictPartialOrder(
    nodes=[Artist_Liaison, Lease_Negotiation, Contract_Drafting, Insurance_Setup, Provenance_Check, Policy_Compliance]
)
po_negotiation.order.add_edge(Artist_Liaison, Lease_Negotiation)
po_negotiation.order.add_edge(Lease_Negotiation, Contract_Drafting)
po_negotiation.order.add_edge(Contract_Drafting, Insurance_Setup)
po_negotiation.order.add_edge(Insurance_Setup, Provenance_Check)
po_negotiation.order.add_edge(Provenance_Check, Policy_Compliance)

# Phase 3: Installation & Display Setup with Artwork Delivery
po_installation = StrictPartialOrder(
    nodes=[Installation_Plan, Artwork_Delivery, Display_Setup]
)
po_installation.order.add_edge(Installation_Plan, Artwork_Delivery)
po_installation.order.add_edge(Artwork_Delivery, Display_Setup)

# Phase 4: Collection Selection (depends on budget approval and provenance & policy)
# For better clarity, model Collection Selection separately to be ordered after budget and policy
# We'll combine below at root level with dependencies.

# Phase 5: Maintenance and Workplace Survey and Employee Feedback
# Maintenance_Check in loop with Collection_Rotation
# Loop body: Maintenance_Check then choose (exit or Collection_Rotation then Maintenance_Check again)
maintenance_rotation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Maintenance_Check, Collection_Rotation]
)

# Concurrently with maintenance_rotation_loop, collect Workplace_Survey and Employee_Feedback, and Event Coordination
# Workplace_Survey and Employee_Feedback are related feedback activities; Event Coordination related but can run concurrently
po_feedback_events = StrictPartialOrder(
    nodes=[Workplace_Survey, Employee_Feedback, Event_Coordination]
)
# no order edges between them → concurrent

# Now putting together final partial order:

# Root nodes:
# - po_sourcing_budget
# - po_negotiation
# - Collection_Selection
# - po_installation
# - maintenance_rotation_loop
# - po_feedback_events

Collection_Selection_node = Collection_Selection  # single node transition

# Define root partial order with all nodes
root_nodes = [
    po_sourcing_budget,
    po_negotiation,
    Collection_Selection_node,
    po_installation,
    maintenance_rotation_loop,
    po_feedback_events
]

root = StrictPartialOrder(nodes=root_nodes)

# Add ordering edges reflecting dependencies:

# po_sourcing_budget --> po_negotiation (because negotiation requires budget approval and sourcing)
root.order.add_edge(po_sourcing_budget, po_negotiation)

# po_negotiation --> Collection_Selection (collection chosen after negotiation complete)
root.order.add_edge(po_negotiation, Collection_Selection_node)

# Collection_Selection --> po_installation (installation after collection selected)
root.order.add_edge(Collection_Selection_node, po_installation)

# Installation and setup completed before maintenance/rotation and feedback/events start
root.order.add_edge(po_installation, maintenance_rotation_loop)
root.order.add_edge(po_installation, po_feedback_events)

# No order assumed between maintenance_rotation_loop and po_feedback_events (concurrent)

# Final model is root
# Generated from: 8b3fb9b3-cf6c-47a0-8200-0bef5474b07e.json
# Description: This process governs the rapid mobilization and coordination of resources during a sudden multi-regional crisis, such as a natural disaster combined with infrastructure failure. It involves initial threat assessment, stakeholder communication, resource allocation under uncertainty, dynamic route planning for aid delivery, contingency management for supply chain disruption, and real-time feedback incorporation from field teams. The process demands flexible decision-making frameworks, integration of multiple data sources including satellite and social media feeds, and simultaneous coordination with governmental agencies, NGOs, and private sector partners to minimize response time and maximize impact. Post-crisis evaluation and knowledge transfer to improve future responses are also key components.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Threat_Assess = Transition(label='Threat Assess')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Resource_Map = Transition(label='Resource Map')
Priority_Set = Transition(label='Priority Set')
Route_Plan = Transition(label='Route Plan')
Asset_Deploy = Transition(label='Asset Deploy')
Field_Brief = Transition(label='Field Brief')
Supply_Check = Transition(label='Supply Check')
Transport_Track = Transition(label='Transport Track')
Data_Integrate = Transition(label='Data Integrate')
Risk_Manage = Transition(label='Risk Manage')
Partner_Align = Transition(label='Partner Align')
Feedback_Loop = Transition(label='Feedback Loop')
Crisis_Review = Transition(label='Crisis Review')
Lessons_Share = Transition(label='Lessons Share')
Contingency_Set = Transition(label='Contingency Set')

# Model dynamic route planning and asset deployment loop with contingency
# Loop node: 
# A = Route Plan -> Asset Deploy -> Field Brief -> Feedback Loop (partial order)
# B = Contingency Set -> Supply Check -> Transport Track
route_asset_po = StrictPartialOrder(
    nodes=[Route_Plan, Asset_Deploy, Field_Brief, Feedback_Loop]
)
route_asset_po.order.add_edge(Route_Plan, Asset_Deploy)
route_asset_po.order.add_edge(Asset_Deploy, Field_Brief)
route_asset_po.order.add_edge(Field_Brief, Feedback_Loop)

contingency_po = StrictPartialOrder(
    nodes=[Contingency_Set, Supply_Check, Transport_Track]
)
contingency_po.order.add_edge(Contingency_Set, Supply_Check)
contingency_po.order.add_edge(Supply_Check, Transport_Track)

loop_route_contingency = OperatorPOWL(
    operator=Operator.LOOP,
    children=[route_asset_po, contingency_po]
)

# Initial sequence
initial_po = StrictPartialOrder(
    nodes=[
        Threat_Assess,
        Stakeholder_Sync,
        Resource_Map,
        Priority_Set
    ]
)
initial_po.order.add_edge(Threat_Assess, Stakeholder_Sync)
initial_po.order.add_edge(Stakeholder_Sync, Resource_Map)
initial_po.order.add_edge(Resource_Map, Priority_Set)

# Data integration and risk management concurrent with partner align
data_risk_po = StrictPartialOrder(
    nodes=[Data_Integrate, Risk_Manage]
)  # concurrent, no edges between them

partner_align = Partner_Align

# Combine these three (data_risk_po, partner_align, and loop_route_contingency) concurrently
middle_po = StrictPartialOrder(
    nodes=[data_risk_po, partner_align, loop_route_contingency]
)
# Since data_risk_po is itself a POWL, to place it as a node, treat as is
# In pm4py POWL you can nest POWL models as nodes in a StrictPartialOrder
# But StrictPartialOrder's nodes expects Transition or OperatorPOWL or StrictPartialOrder instances

# Post crisis evaluation and lessons share (sequence)
post_crisis_po = StrictPartialOrder(
    nodes=[Crisis_Review, Lessons_Share]
)
post_crisis_po.order.add_edge(Crisis_Review, Lessons_Share)

# Build the full model as a partial order:
# initial_po --> middle_po --> post_crisis_po
root = StrictPartialOrder(
    nodes=[initial_po, middle_po, post_crisis_po]
)
root.order.add_edge(initial_po, middle_po)
root.order.add_edge(middle_po, post_crisis_po)
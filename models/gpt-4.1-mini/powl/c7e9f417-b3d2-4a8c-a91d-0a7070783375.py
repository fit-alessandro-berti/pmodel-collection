# Generated from: c7e9f417-b3d2-4a8c-a91d-0a7070783375.json
# Description: This process involves the strategic alignment and operational consolidation of two distinct corporate brands following a merger. It includes analyzing brand equity, harmonizing marketing strategies, integrating customer databases, redesigning product portfolios, and realigning internal communications to ensure a unified market presence. Key steps include legal trademark reviews, cultural assimilation workshops, and synchronized launch campaigns. The goal is to minimize customer confusion, optimize resource allocation, and leverage combined strengths to enhance competitive advantage while maintaining stakeholder trust throughout the transition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Brand_Audit = Transition(label='Brand Audit')
Equity_Review = Transition(label='Equity Review')
Market_Analysis = Transition(label='Market Analysis')
Legal_Clearance = Transition(label='Legal Clearance')
Trademark_Check = Transition(label='Trademark Check')
Portfolio_Merge = Transition(label='Portfolio Merge')
Customer_Sync = Transition(label='Customer Sync')
Cultural_Align = Transition(label='Cultural Align')
Internal_Brief = Transition(label='Internal Brief')
Campaign_Design = Transition(label='Campaign Design')
Resource_Plan = Transition(label='Resource Plan')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Launch_Prep = Transition(label='Launch Prep')
Feedback_Loop = Transition(label='Feedback Loop')
Performance_Track = Transition(label='Performance Track')

# Build substructures:

# Legal subflow: Legal Clearance --> Trademark Check
legal_po = StrictPartialOrder(nodes=[Legal_Clearance, Trademark_Check])
legal_po.order.add_edge(Legal_Clearance, Trademark_Check)

# Brand Audit subflow: Brand Audit --> Equity Review
brand_audit_po = StrictPartialOrder(nodes=[Brand_Audit, Equity_Review])
brand_audit_po.order.add_edge(Brand_Audit, Equity_Review)

# Market Analysis is independent after brand audit and equity review
# We'll connect brand audit flow to market analysis

# Phase 1: Brand Audit & Equity Review --> Market Analysis --> Legal flow
phase1 = StrictPartialOrder(nodes=[brand_audit_po, Market_Analysis, legal_po])
phase1.order.add_edge(brand_audit_po, Market_Analysis)
phase1.order.add_edge(Market_Analysis, legal_po)

# Phase 2: Portfolio Merge and Customer Sync happen concurrently after Phase 1
phase2 = StrictPartialOrder(nodes=[Portfolio_Merge, Customer_Sync])

# Phase 3: Cultural Align and Internal Brief after phase2 concurrently
phase3 = StrictPartialOrder(nodes=[Cultural_Align, Internal_Brief])

# Phase 2 and Phase 3 are sequential: phase2 --> phase3
phase2_3 = StrictPartialOrder(nodes=[phase2, phase3])
phase2_3.order.add_edge(phase2, phase3)

# Phase 4: Campaign Design, Resource Plan, Stakeholder Meet run in partial order (campaign depends on resource and stakeholder meet)
campaign_planning = StrictPartialOrder(nodes=[Campaign_Design, Resource_Plan, Stakeholder_Meet])
campaign_planning.order.add_edge(Resource_Plan, Campaign_Design)
campaign_planning.order.add_edge(Stakeholder_Meet, Campaign_Design)

# Phase 5: Launch Prep after campaign planning
phase5 = StrictPartialOrder(nodes=[campaign_planning, Launch_Prep])
phase5.order.add_edge(campaign_planning, Launch_Prep)

# Loop for Feedback and Performance tracking after launch prep
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Performance_Track])

# Connect Phase 5 to loop
phase5_loop = StrictPartialOrder(nodes=[phase5, loop_node])
phase5_loop.order.add_edge(phase5, loop_node)

# Compose the full flow:
# phase1 --> phase2_3 --> phase5_loop

root = StrictPartialOrder(
    nodes=[phase1, phase2_3, phase5_loop]
)
root.order.add_edge(phase1, phase2_3)
root.order.add_edge(phase2_3, phase5_loop)
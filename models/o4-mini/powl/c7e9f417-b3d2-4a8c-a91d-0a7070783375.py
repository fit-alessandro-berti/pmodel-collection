# Generated from: c7e9f417-b3d2-4a8c-a91d-0a7070783375.json
# Description: This process involves the strategic alignment and operational consolidation of two distinct corporate brands following a merger. It includes analyzing brand equity, harmonizing marketing strategies, integrating customer databases, redesigning product portfolios, and realigning internal communications to ensure a unified market presence. Key steps include legal trademark reviews, cultural assimilation workshops, and synchronized launch campaigns. The goal is to minimize customer confusion, optimize resource allocation, and leverage combined strengths to enhance competitive advantage while maintaining stakeholder trust throughout the transition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
BA = Transition(label='Brand Audit')
ER = Transition(label='Equity Review')
MA = Transition(label='Market Analysis')
LC = Transition(label='Legal Clearance')
TC = Transition(label='Trademark Check')
PS = Transition(label='Portfolio Merge')
CS = Transition(label='Customer Sync')
CA = Transition(label='Cultural Align')
IB = Transition(label='Internal Brief')
RP = Transition(label='Resource Plan')
SM = Transition(label='Stakeholder Meet')
CD = Transition(label='Campaign Design')
LP = Transition(label='Launch Prep')
FL = Transition(label='Feedback Loop')
PT = Transition(label='Performance Track')

# Define the feedback loop: after a campaign launch, gather feedback and measure performance,
# then optionally repeat campaign design & launch.
seq_campaign = StrictPartialOrder(nodes=[CD, LP])
seq_campaign.order.add_edge(CD, LP)

seq_feedback = StrictPartialOrder(nodes=[FL, PT])
seq_feedback.order.add_edge(FL, PT)

campaign_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[seq_campaign, seq_feedback]
)

# Assemble the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    BA, ER, MA,
    LC, TC,
    PS, CS, CA, IB,
    RP, SM,
    campaign_loop
])

# Control-flow dependencies
root.order.add_edge(BA, ER)
root.order.add_edge(ER, MA)

# After market analysis, run legal reviews, portfolio merge, and customer sync in parallel
root.order.add_edge(MA, LC)
root.order.add_edge(LC, TC)
root.order.add_edge(MA, PS)
root.order.add_edge(MA, CS)

# Sequence product & people alignment
root.order.add_edge(PS, CA)
root.order.add_edge(CS, IB)
root.order.add_edge(CA, IB)

# Merge into internal briefing then resource planning
root.order.add_edge(IB, RP)
root.order.add_edge(TC, RP)  # ensure trademark clearance before planning

# Stakeholder engagement, then campaign loop
root.order.add_edge(RP, SM)
root.order.add_edge(SM, campaign_loop)
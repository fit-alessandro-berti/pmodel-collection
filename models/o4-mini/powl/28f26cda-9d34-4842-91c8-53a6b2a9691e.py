# Generated from: 28f26cda-9d34-4842-91c8-53a6b2a9691e.json
# Description: This process describes a cross-industry innovation cycle where ideas originating in one sector are systematically adapted and integrated into a different industry to create novel products or services. It involves identifying transferable concepts, conducting feasibility analyses, securing multi-sector partnerships, prototyping with hybrid teams, and navigating complex regulatory environments unique to each industry. Continuous feedback loops from diverse market segments are incorporated to refine solutions. The cycle culminates in scalable deployment plans that leverage combined supply chains and shared intellectual property management to maximize impact and sustainability across sectors.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
idea_sourcing    = Transition(label="Idea Sourcing")
concept_mapping  = Transition(label="Concept Mapping")
feasibility      = Transition(label="Feasibility Study")
partner_outreach = Transition(label="Partner Outreach")
joint_workshops  = Transition(label="Joint Workshops")
prototype_build  = Transition(label="Prototype Build")
cross_test       = Transition(label="Cross-Test")
regulatory_rev   = Transition(label="Regulatory Review")
market_feedback  = Transition(label="Market Feedback")
design_iterate   = Transition(label="Design Iterate")
ip_negotiation   = Transition(label="IP Negotiation")
pilot_launch     = Transition(label="Pilot Launch")
supply_sync      = Transition(label="Supply Sync")
scale_planning   = Transition(label="Scale Planning")
impact_audit     = Transition(label="Impact Audit")

# Construct the feedback‐loop as a LOOP operator:
# A = cross-test → regulatory review → market feedback
loop_body_A = StrictPartialOrder(
    nodes=[cross_test, regulatory_rev, market_feedback]
)
loop_body_A.order.add_edge(cross_test, regulatory_rev)
loop_body_A.order.add_edge(regulatory_rev, market_feedback)

# B = design iterate → prototype build (redo part)
loop_body_B = StrictPartialOrder(
    nodes=[design_iterate, prototype_build]
)
loop_body_B.order.add_edge(design_iterate, prototype_build)

feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[loop_body_A, loop_body_B]
)

# Assemble the entire process as a single partial order
root = StrictPartialOrder(
    nodes=[
        idea_sourcing,
        concept_mapping,
        feasibility,
        partner_outreach,
        joint_workshops,
        prototype_build,
        feedback_loop,
        ip_negotiation,
        pilot_launch,
        supply_sync,
        scale_planning,
        impact_audit
    ]
)

# Add the sequencing constraints
root.order.add_edge(idea_sourcing,    concept_mapping)
root.order.add_edge(concept_mapping,  feasibility)
root.order.add_edge(feasibility,      partner_outreach)
root.order.add_edge(partner_outreach, joint_workshops)
root.order.add_edge(joint_workshops,  prototype_build)
root.order.add_edge(prototype_build,  feedback_loop)
root.order.add_edge(feedback_loop,     ip_negotiation)
root.order.add_edge(ip_negotiation,    pilot_launch)
root.order.add_edge(pilot_launch,      supply_sync)
root.order.add_edge(supply_sync,       scale_planning)
root.order.add_edge(scale_planning,    impact_audit)
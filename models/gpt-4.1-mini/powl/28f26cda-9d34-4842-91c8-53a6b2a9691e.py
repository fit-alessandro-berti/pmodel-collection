# Generated from: 28f26cda-9d34-4842-91c8-53a6b2a9691e.json
# Description: This process describes a cross-industry innovation cycle where ideas originating in one sector are systematically adapted and integrated into a different industry to create novel products or services. It involves identifying transferable concepts, conducting feasibility analyses, securing multi-sector partnerships, prototyping with hybrid teams, and navigating complex regulatory environments unique to each industry. Continuous feedback loops from diverse market segments are incorporated to refine solutions. The cycle culminates in scalable deployment plans that leverage combined supply chains and shared intellectual property management to maximize impact and sustainability across sectors.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Idea_Sourcing = Transition(label='Idea Sourcing')
Concept_Mapping = Transition(label='Concept Mapping')
Feasibility_Study = Transition(label='Feasibility Study')
Partner_Outreach = Transition(label='Partner Outreach')
Joint_Workshops = Transition(label='Joint Workshops')
Prototype_Build = Transition(label='Prototype Build')
Cross_Test = Transition(label='Cross-Test')
Regulatory_Review = Transition(label='Regulatory Review')
Market_Feedback = Transition(label='Market Feedback')
Design_Iterate = Transition(label='Design Iterate')
IP_Negotiation = Transition(label='IP Negotiation')
Pilot_Launch = Transition(label='Pilot Launch')
Supply_Sync = Transition(label='Supply Sync')
Scale_Planning = Transition(label='Scale Planning')
Impact_Audit = Transition(label='Impact Audit')

# Construct loops and choices according to the description

# Loop 1: iterate over Design Iterate and Market Feedback (continuous feedback loops)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Design_Iterate, Market_Feedback])

# After Prototype Build and Cross-Test, Regulatory Review occurs before feedback loop
partial_after_prototype = StrictPartialOrder(
    nodes=[Prototype_Build, Cross_Test, Regulatory_Review, feedback_loop]
)
partial_after_prototype.order.add_edge(Prototype_Build, Cross_Test)
partial_after_prototype.order.add_edge(Cross_Test, Regulatory_Review)
partial_after_prototype.order.add_edge(Regulatory_Review, feedback_loop)

# After Feasibility Study, partner outreach and joint workshops must happen before prototype build
partnering = StrictPartialOrder(
    nodes=[Partner_Outreach, Joint_Workshops]
)
partnering.order.add_edge(Partner_Outreach, Joint_Workshops)

# Sequence from Idea Sourcing to Feasibility Study to partnering
pre_prototype_seq = StrictPartialOrder(
    nodes=[Idea_Sourcing, Concept_Mapping, Feasibility_Study, partnering]
)
pre_prototype_seq.order.add_edge(Idea_Sourcing, Concept_Mapping)
pre_prototype_seq.order.add_edge(Concept_Mapping, Feasibility_Study)
pre_prototype_seq.order.add_edge(Feasibility_Study, partnering)

# Combine pre-prototype sequence and prototype-related partial order
proto_and_after = StrictPartialOrder(
    nodes=[pre_prototype_seq, partial_after_prototype]
)
proto_and_after.order.add_edge(pre_prototype_seq, partial_after_prototype)

# After feedback loop, IP Negotiation and Pilot Launch follow in parallel (partial order with no order edges)
post_feedback = StrictPartialOrder(
    nodes=[IP_Negotiation, Pilot_Launch]
)

# After post feedback, Supply Sync and Scale Planning happen before Impact Audit
final_sequence = StrictPartialOrder(
    nodes=[post_feedback, Supply_Sync, Scale_Planning, Impact_Audit]
)
final_sequence.order.add_edge(post_feedback, Supply_Sync)
final_sequence.order.add_edge(Supply_Sync, Scale_Planning)
final_sequence.order.add_edge(Scale_Planning, Impact_Audit)

# Root PO combines all major phases in order:
# proto_and_after -> post_feedback (inside final_sequence already linked) -> Impact Audit included above
root = StrictPartialOrder(
    nodes=[proto_and_after, final_sequence]
)
root.order.add_edge(proto_and_after, final_sequence)
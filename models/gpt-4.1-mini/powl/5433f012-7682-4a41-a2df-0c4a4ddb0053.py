# Generated from: 5433f012-7682-4a41-a2df-0c4a4ddb0053.json
# Description: This process outlines a complex cycle where a company leverages cross-industry insights to drive innovation. Starting with trend scanning across unrelated sectors, it incorporates collaborative ideation sessions with external experts, rapid prototyping using agile methods, and iterative testing in real-world environments. The cycle further includes strategic IP mapping to avoid conflicts, market simulation to predict adoption, and adaptive scaling plans that integrate continuous feedback loops from multiple stakeholder groups. The process emphasizes dynamic resource allocation, legal compliance checks across jurisdictions, and post-launch ecosystem integration, ensuring sustained competitive advantage through unconventional knowledge transfer and multi-disciplinary collaboration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Transitions for each activity
trend_scan = Transition(label='Trend Scan')
expert_invite = Transition(label='Expert Invite')
idea_sprint = Transition(label='Idea Sprint')
prototype_build = Transition(label='Prototype Build')
field_test = Transition(label='Field Test')
ip_mapping = Transition(label='IP Mapping')
market_model = Transition(label='Market Model')
scale_plan = Transition(label='Scale Plan')
feedback_loop = Transition(label='Feedback Loop')
resource_shift = Transition(label='Resource Shift')
legal_check = Transition(label='Legal Check')
partner_sync = Transition(label='Partner Sync')
data_review = Transition(label='Data Review')
launch_prep = Transition(label='Launch Prep')
eco_integrate = Transition(label='Eco Integrate')

# Build the iterative innovation cycle loop: 
# This is the core where after Trend Scan, through Expert Invite, Idea Sprint, Prototype Build, Field Test,
# the loop repeats via Feedback Loop.
# Loop(A=Trend Scan, B= StrictPartialOrder of expert_invite->idea_sprint->prototype_build->field_test->feedback_loop)

# Define sequence inside the loop body B:
loop_body_nodes = [expert_invite, idea_sprint, prototype_build, field_test, feedback_loop]
loop_body = StrictPartialOrder(nodes=loop_body_nodes)
loop_body.order.add_edge(expert_invite, idea_sprint)
loop_body.order.add_edge(idea_sprint, prototype_build)
loop_body.order.add_edge(prototype_build, field_test)
loop_body.order.add_edge(field_test, feedback_loop)

# Loop node: execute trend_scan, then repeated execution of loop_body and back
loop = OperatorPOWL(operator=Operator.LOOP, children=[trend_scan, loop_body])

# Post iteration strategic steps and concurrent activities:
# IP Mapping and Market Modeling are sequential after loop:
strategic_seq = StrictPartialOrder(nodes=[ip_mapping, market_model])
strategic_seq.order.add_edge(ip_mapping, market_model)

# Scale plan incorporates Feedback Loop results and resource shift + legal check + partner sync
# Consider resource_shift, legal_check, partner_sync as concurrent before data_review
# Data Review then Launch prep then Eco integrate sequentially.

post_scale_nodes = [scale_plan, feedback_loop]  # feedback_loop is reused, accepting it as a shared node for concurrency
post_scale = StrictPartialOrder(nodes=post_scale_nodes)
post_scale.order.add_edge(scale_plan, feedback_loop)  # ensure scale_plan before feedback_loop

resource_legal_partner = StrictPartialOrder(nodes=[resource_shift, legal_check, partner_sync])
# concurrent, no edges added

# Data review and launch prep and eco integrate sequentially
final_seq = StrictPartialOrder(nodes=[data_review, launch_prep, eco_integrate])
final_seq.order.add_edge(data_review, launch_prep)
final_seq.order.add_edge(launch_prep, eco_integrate)

# Compose all after strategic steps in partial order with edges to maintain control-flow
# We'll make a big PO with nodes:
# loop, strategic_seq, post_scale, resource_legal_partner, final_seq
root_nodes = [loop, strategic_seq, post_scale, resource_legal_partner, final_seq]
root = StrictPartialOrder(nodes=root_nodes)

# Define ordering among these big blocks:
root.order.add_edge(loop, strategic_seq)           # loop before strategic_seq
root.order.add_edge(strategic_seq, post_scale)     # strategic_seq before post_scale
root.order.add_edge(post_scale, resource_legal_partner)  # post_scale before concurrent resource/legal/partner
root.order.add_edge(resource_legal_partner, final_seq)   # after these concurrent activities, final_seq

# Note concurrent nodes inside resource_legal_partner (resource_shift, legal_check, partner_sync) have no internal edges - concurrent

# The feedback_loop is reused inside loop and post_scale for continuous feedback integration.
# This reuse is acceptable as POWL nodes can be multi-referenced for modeling feedback integration.

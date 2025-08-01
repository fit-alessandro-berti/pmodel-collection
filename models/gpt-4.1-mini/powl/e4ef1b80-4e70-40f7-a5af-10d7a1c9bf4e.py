# Generated from: e4ef1b80-4e70-40f7-a5af-10d7a1c9bf4e.json
# Description: This process enables companies from disparate industries to collaboratively generate and implement breakthrough innovations by leveraging diverse expertise, iterative knowledge exchange, and synchronized development phases. It begins with opportunity scouting across sectors, followed by rapid ideation workshops that blend unique perspectives. Subsequent feasibility testing incorporates shared resources and joint prototyping. The cycle continues with cross-validation through pilot deployments in varied markets, collecting multi-dimensional feedback. Adaptation and scaling efforts require coordinated regulatory navigation and resource allocation among partners. The process concludes with collective intellectual property management and market launch strategies that maximize cross-industry synergies while maintaining agility and confidentiality throughout the collaboration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
op_scan = Transition(label='Opportunity Scan')
idea_ws = Transition(label='Idea Workshop')
concept_merge = Transition(label='Concept Merge')
resource_align = Transition(label='Resource Align')
prototype_build = Transition(label='Prototype Build')
feasibility_test = Transition(label='Feasibility Test')
pilot_launch = Transition(label='Pilot Launch')
feedback_gather = Transition(label='Feedback Gather')
design_adapt = Transition(label='Design Adapt')
compliance_check = Transition(label='Compliance Check')
scaling_plan = Transition(label='Scaling Plan')
ip_management = Transition(label='IP Management')
market_sync = Transition(label='Market Sync')
partner_review = Transition(label='Partner Review')
exit_strategy = Transition(label='Exit Strategy')

# We model the cycle involving feasibility test, pilot launch, feedback, adaptation, compliance, scaling, resource alignment, and prototyping as a loop:
# Loop body (B): resource_align -> prototype_build -> feasibility_test -> pilot_launch -> feedback_gather -> design_adapt -> compliance_check -> scaling_plan -> partner_review
loop_body_nodes = [
    resource_align,
    prototype_build,
    feasibility_test,
    pilot_launch,
    feedback_gather,
    design_adapt,
    compliance_check,
    scaling_plan,
    partner_review
]
loop_body = StrictPartialOrder(nodes=loop_body_nodes)
# Add order edges inside loop body according to the process logical sequence:
loop_body.order.add_edge(resource_align, prototype_build)
loop_body.order.add_edge(prototype_build, feasibility_test)
loop_body.order.add_edge(feasibility_test, pilot_launch)
loop_body.order.add_edge(pilot_launch, feedback_gather)
loop_body.order.add_edge(feedback_gather, design_adapt)
loop_body.order.add_edge(design_adapt, compliance_check)
loop_body.order.add_edge(compliance_check, scaling_plan)
loop_body.order.add_edge(scaling_plan, partner_review)

# Loop initial activity (A): concept_merge (merging concepts after idea workshop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[concept_merge, loop_body])

# After loop exit, final activities: IP Management, Market Sync, Exit Strategy
final_nodes = [ip_management, market_sync, exit_strategy]
final_po = StrictPartialOrder(nodes=final_nodes)
final_po.order.add_edge(ip_management, market_sync)
final_po.order.add_edge(market_sync, exit_strategy)

# First two activities connected sequentially: opportunity scan -> idea workshop -> concept merge (which appears as loop initial activity)
start_po = StrictPartialOrder(nodes=[op_scan, idea_ws])
start_po.order.add_edge(op_scan, idea_ws)

# Combine start_po and loop and final_po in a partial order
root = StrictPartialOrder(nodes=[start_po, loop, final_po])

# Add order edges to connect these components
root.order.add_edge(start_po, loop)
root.order.add_edge(loop, final_po)
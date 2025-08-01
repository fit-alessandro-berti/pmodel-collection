# Generated from: 8a7df71f-a28d-4a1d-a7b5-269e26562a33.json
# Description: This process involves the systematic identification, acquisition, and transformation of obsolete corporate artifacts such as outdated technology hardware, legacy software modules, and discontinued branded materials. The objective is to creatively repurpose these assets into new, value-generating products or services that align with current market demands. The process encompasses cross-departmental collaboration, including asset auditing, feasibility analysis, design prototyping, regulatory compliance checks, and stakeholder approvals. It further integrates sustainability assessments to ensure environmental impact is minimized. The final phase involves pilot testing, market feedback incorporation, and scaled production rollout, thereby extending the lifecycle of corporate assets while fostering innovation and reducing waste.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
asset_audit       = Transition(label='Asset Audit')
market_scan       = Transition(label='Market Scan')
feasibility       = Transition(label='Feasibility Study')
design_concept    = Transition(label='Design Concept')
prototype_build   = Transition(label='Prototype Build')
feedback_design   = Transition(label='Feedback Review')
iterate_design    = Transition(label='Iterate Design')
compliance_check  = Transition(label='Compliance Check')
stakeholder_meet  = Transition(label='Stakeholder Meet')
sustainability_ev = Transition(label='Sustainability Eval')
risk_assess       = Transition(label='Risk Assess')
pilot_launch      = Transition(label='Pilot Launch')
feedback_final    = Transition(label='Feedback Review')
scale_plan        = Transition(label='Scale Plan')
production_setup  = Transition(label='Production Setup')
launch_campaign   = Transition(label='Launch Campaign')
post_launch       = Transition(label='Post Launch')

# Loop for prototype iterations: build -> (feedback -> iterate) -> build -> ...
iteration_po = StrictPartialOrder(nodes=[feedback_design, iterate_design])
iteration_po.order.add_edge(feedback_design, iterate_design)
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, iteration_po])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    asset_audit, market_scan, feasibility,
    design_concept, design_loop,
    compliance_check, stakeholder_meet, sustainability_ev, risk_assess,
    pilot_launch, feedback_final, scale_plan,
    production_setup, launch_campaign, post_launch
])

# Initial analysis phase
root.order.add_edge(asset_audit, feasibility)
root.order.add_edge(market_scan, feasibility)
root.order.add_edge(feasibility, design_concept)

# Concept to prototyping loop
root.order.add_edge(design_concept, design_loop)

# Post-loop compliance, approvals, sustainability, risk (concurrent)
root.order.add_edge(design_loop, compliance_check)
root.order.add_edge(design_loop, stakeholder_meet)
root.order.add_edge(design_loop, sustainability_ev)
root.order.add_edge(design_loop, risk_assess)

# Synchronize before pilot launch
root.order.add_edge(compliance_check, pilot_launch)
root.order.add_edge(stakeholder_meet, pilot_launch)
root.order.add_edge(sustainability_ev, pilot_launch)
root.order.add_edge(risk_assess, pilot_launch)

# Final phase: pilot -> feedback -> scale -> production -> launch -> post-launch
root.order.add_edge(pilot_launch, feedback_final)
root.order.add_edge(feedback_final, scale_plan)
root.order.add_edge(scale_plan, production_setup)
root.order.add_edge(production_setup, launch_campaign)
root.order.add_edge(launch_campaign, post_launch)
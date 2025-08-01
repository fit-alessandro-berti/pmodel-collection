# Generated from: 54a77740-09cb-44f1-a62b-81c4ec6a9a51.json
# Description: This process involves the complex verification and authentication of rare historical artifacts for museum acquisition. It integrates multidisciplinary expert evaluations including provenance research, material composition analysis, and digital imaging. The workflow handles conflicting data by iterative cross-validation and incorporates legal clearance checks. Coordination between legal, scientific, and curatorial teams ensures authenticity before final acquisition decisions. Special attention is given to ethical sourcing, risk assessment of forgeries, and long-term conservation planning, making this an intricate and atypical business process requiring high collaboration and precision.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
initial_audit = Transition(label='Initial Audit')
provenance = Transition(label='Provenance Check')
material = Transition(label='Material Scan')
imaging = Transition(label='Imaging Capture')
expert1 = Transition(label='Expert Review')
crosscheck = Transition(label='Data Crosscheck')
forg_analysis = Transition(label='Forgery Analysis')
expert2 = Transition(label='Expert Review')
legal_clearance = Transition(label='Legal Clearance')
ethics_review = Transition(label='Ethics Review')
risk_assessment = Transition(label='Risk Assessment')
curator_meeting = Transition(label='Curator Meeting')
conservation_plan = Transition(label='Conservation Plan')
acquisition_vote = Transition(label='Acquisition Vote')
documentation = Transition(label='Documentation')
final_approval = Transition(label='Final Approval')

# Build the loop body for iterative cross-validation
loop_body = StrictPartialOrder(nodes=[forg_analysis, expert2])
loop_body.order.add_edge(forg_analysis, expert2)

# Loop: crosscheck then either exit or do forgery analysis + expert review and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[crosscheck, loop_body])

# Build the overall partial order workflow
root = StrictPartialOrder(nodes=[
    initial_audit,
    provenance, material, imaging,
    expert1,
    loop,
    legal_clearance, ethics_review, risk_assessment,
    curator_meeting,
    conservation_plan,
    acquisition_vote,
    documentation,
    final_approval
])

# Define ordering constraints
root.order.add_edge(initial_audit, provenance)
root.order.add_edge(initial_audit, material)
root.order.add_edge(initial_audit, imaging)

root.order.add_edge(provenance, expert1)
root.order.add_edge(material, expert1)
root.order.add_edge(imaging, expert1)

root.order.add_edge(expert1, loop)

root.order.add_edge(loop, legal_clearance)
root.order.add_edge(loop, ethics_review)
root.order.add_edge(loop, risk_assessment)

root.order.add_edge(legal_clearance, curator_meeting)
root.order.add_edge(ethics_review, curator_meeting)
root.order.add_edge(risk_assessment, curator_meeting)

root.order.add_edge(curator_meeting, conservation_plan)
root.order.add_edge(conservation_plan, acquisition_vote)
root.order.add_edge(acquisition_vote, documentation)
root.order.add_edge(documentation, final_approval)
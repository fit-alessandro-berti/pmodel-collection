# Generated from: 54a77740-09cb-44f1-a62b-81c4ec6a9a51.json
# Description: This process involves the complex verification and authentication of rare historical artifacts for museum acquisition. It integrates multidisciplinary expert evaluations including provenance research, material composition analysis, and digital imaging. The workflow handles conflicting data by iterative cross-validation and incorporates legal clearance checks. Coordination between legal, scientific, and curatorial teams ensures authenticity before final acquisition decisions. Special attention is given to ethical sourcing, risk assessment of forgeries, and long-term conservation planning, making this an intricate and atypical business process requiring high collaboration and precision.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Initial_Audit = Transition(label='Initial Audit')
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Imaging_Capture = Transition(label='Imaging Capture')
Expert_Review = Transition(label='Expert Review')
Data_Crosscheck = Transition(label='Data Crosscheck')
Forgery_Analysis = Transition(label='Forgery Analysis')
Legal_Clearance = Transition(label='Legal Clearance')
Ethics_Review = Transition(label='Ethics Review')
Risk_Assessment = Transition(label='Risk Assessment')
Curator_Meeting = Transition(label='Curator Meeting')
Conservation_Plan = Transition(label='Conservation Plan')
Acquisition_Vote = Transition(label='Acquisition Vote')
Documentation = Transition(label='Documentation')
Final_Approval = Transition(label='Final Approval')

# Partial order for multidisciplinary expert evaluation after Initial Audit
# The three expert checks: Provenance Check, Material Scan, Imaging Capture run concurrently
expert_checks = StrictPartialOrder(nodes=[Provenance_Check, Material_Scan, Imaging_Capture])

# After expert checks, Expert Review
# Build the overall partial order for initial audit --> expert_checks --> expert review
eval_po = StrictPartialOrder(nodes=[Initial_Audit, expert_checks, Expert_Review])
eval_po.order.add_edge(Initial_Audit, expert_checks)
eval_po.order.add_edge(expert_checks, Expert_Review)

# Data crosscheck with possible iterative cross-validation loop incorporating Forgery Analysis
# Loop: execute Data Crosscheck, then choose exit or Forgery Analysis + Data Crosscheck again
loop_crosscheck = OperatorPOWL(operator=Operator.LOOP, children=[Data_Crosscheck, Forgery_Analysis])

# After Expert Review, do the loop for data crosscheck and forgery analysis
post_review_po = StrictPartialOrder(nodes=[Expert_Review, loop_crosscheck])
post_review_po.order.add_edge(Expert_Review, loop_crosscheck)

# Legal clearance and ethics review in parallel after loop_crosscheck
legal_ethics_po = StrictPartialOrder(nodes=[Legal_Clearance, Ethics_Review])

# Next Risk Assessment after legal clearance and ethics review (both must complete first)
risk_assessment_po = StrictPartialOrder(nodes=[legal_ethics_po, Risk_Assessment])
risk_assessment_po.order.add_edge(legal_ethics_po, Risk_Assessment)

# Curator Meeting after Risk Assessment
curator_meeting_po = StrictPartialOrder(nodes=[Risk_Assessment, Curator_Meeting])
curator_meeting_po.order.add_edge(Risk_Assessment, Curator_Meeting)

# Conservation Plan concurrent with documentation, both after curator meeting
conservation_doc_po = StrictPartialOrder(nodes=[Conservation_Plan, Documentation])
# Both depend on curator meeting
conservation_doc_total = StrictPartialOrder(nodes=[curator_meeting_po, conservation_doc_po])
conservation_doc_total.order.add_edge(curator_meeting_po, conservation_doc_po)

# Acquisition Vote after conservation plan and documentation
vote_po = StrictPartialOrder(nodes=[conservation_doc_po, Acquisition_Vote])
vote_po.order.add_edge(conservation_doc_po, Acquisition_Vote)

# Final Approval after Acquisition Vote
final_po = StrictPartialOrder(nodes=[vote_po, Final_Approval])
final_po.order.add_edge(vote_po, Final_Approval)

# Compose all parts in one big partial order root:
root = StrictPartialOrder(nodes=[
    eval_po,
    post_review_po,
    risk_assessment_po,
    curator_meeting_po,
    conservation_doc_total,
    vote_po,
    final_po
])

# Add edges to connect the high level sequence of the process:
root.order.add_edge(eval_po, post_review_po)
root.order.add_edge(post_review_po, risk_assessment_po)
root.order.add_edge(risk_assessment_po, curator_meeting_po)
root.order.add_edge(curator_meeting_po, conservation_doc_total)
root.order.add_edge(conservation_doc_total, vote_po)
root.order.add_edge(vote_po, final_po)
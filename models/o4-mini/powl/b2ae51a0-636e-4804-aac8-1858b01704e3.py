# Generated from: b2ae51a0-636e-4804-aac8-1858b01704e3.json
# Description: This process outlines the multi-disciplinary approach to authenticate historical artifacts before acquisition by a museum. It involves scientific analysis, provenance verification, expert consultation, and legal clearance. The workflow ensures that artifacts are genuine, legally acquired, and suitable for display or research, minimizing risks related to forgery, theft, or cultural misappropriation. The process integrates physical testing, digital imaging, archival research, and stakeholder negotiation to establish authenticity and compliance with international regulations. Final approval requires consensus from scientific experts and legal advisors to proceed with acquisition or rejection.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
initial_review        = Transition(label='Initial Review')
provenance_check      = Transition(label='Provenance Check')
material_sampling     = Transition(label='Material Sampling')
spectral_analysis     = Transition(label='Spectral Analysis')
digital_imaging       = Transition(label='Digital Imaging')
historical_research   = Transition(label='Historical Research')
cultural_assessment   = Transition(label='Cultural Assessment')
condition_report      = Transition(label='Condition Report')
risk_evaluation       = Transition(label='Risk Evaluation')
stakeholder_meeting   = Transition(label='Stakeholder Meeting')
expert_panel          = Transition(label='Expert Panel')
legal_review          = Transition(label='Legal Review')
authentication_vote   = Transition(label='Authentication Vote')
acquisition_approval  = Transition(label='Acquisition Approval')
documentation         = Transition(label='Documentation')
storage_planning      = Transition(label='Storage Planning')
public_disclosure     = Transition(label='Public Disclosure')

# Silent transition for rejection branch
skip = SilentTransition()

# Build the approval branch: sequential activities after a positive vote
approval_branch = StrictPartialOrder(nodes=[
    acquisition_approval,
    documentation,
    storage_planning,
    public_disclosure
])
approval_branch.order.add_edge(acquisition_approval, documentation)
approval_branch.order.add_edge(documentation, storage_planning)
approval_branch.order.add_edge(storage_planning, public_disclosure)

# XOR between approval branch and rejection (skip)
decision = OperatorPOWL(operator=Operator.XOR, children=[approval_branch, skip])

# Assemble the main process
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    material_sampling,
    spectral_analysis,
    digital_imaging,
    historical_research,
    cultural_assessment,
    condition_report,
    risk_evaluation,
    stakeholder_meeting,
    expert_panel,
    legal_review,
    authentication_vote,
    decision
])

# Define partial order (dependencies)
# 1. Initial review precedes all parallel analyses and checks
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(initial_review, material_sampling)
root.order.add_edge(initial_review, digital_imaging)
root.order.add_edge(initial_review, historical_research)
root.order.add_edge(initial_review, cultural_assessment)

# 2. Material sampling → spectral analysis
root.order.add_edge(material_sampling, spectral_analysis)

# 3. Spectral analysis & digital imaging → condition report
root.order.add_edge(spectral_analysis, condition_report)
root.order.add_edge(digital_imaging, condition_report)

# 4. Condition report, provenance check, historical research, cultural assessment → risk evaluation
root.order.add_edge(condition_report, risk_evaluation)
root.order.add_edge(provenance_check, risk_evaluation)
root.order.add_edge(historical_research, risk_evaluation)
root.order.add_edge(cultural_assessment, risk_evaluation)

# 5. Risk evaluation → stakeholder meeting
root.order.add_edge(risk_evaluation, stakeholder_meeting)

# 6. Stakeholder meeting → expert panel & legal review (parallel)
root.order.add_edge(stakeholder_meeting, expert_panel)
root.order.add_edge(stakeholder_meeting, legal_review)

# 7. Expert panel & legal review → authentication vote
root.order.add_edge(expert_panel, authentication_vote)
root.order.add_edge(legal_review, authentication_vote)

# 8. After vote → decision (approve or reject)
root.order.add_edge(authentication_vote, decision)
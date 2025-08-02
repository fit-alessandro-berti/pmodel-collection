# Generated from: b2ae51a0-636e-4804-aac8-1858b01704e3.json
# Description: This process outlines the multi-disciplinary approach to authenticate historical artifacts before acquisition by a museum. It involves scientific analysis, provenance verification, expert consultation, and legal clearance. The workflow ensures that artifacts are genuine, legally acquired, and suitable for display or research, minimizing risks related to forgery, theft, or cultural misappropriation. The process integrates physical testing, digital imaging, archival research, and stakeholder negotiation to establish authenticity and compliance with international regulations. Final approval requires consensus from scientific experts and legal advisors to proceed with acquisition or rejection.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
Initial_Review = Transition(label='Initial Review')

# Provenance verification branch
Provenance_Check = Transition(label='Provenance Check')
Historical_Research = Transition(label='Historical Research')
Cultural_Assessment = Transition(label='Cultural Assessment')

# Scientific analysis branch
Material_Sampling = Transition(label='Material Sampling')
Spectral_Analysis = Transition(label='Spectral Analysis')
Digital_Imaging = Transition(label='Digital Imaging')
Condition_Report = Transition(label='Condition Report')
Risk_Evaluation = Transition(label='Risk Evaluation')

# Expert consultation branch
Expert_Panel = Transition(label='Expert Panel')
Stakeholder_Meeting = Transition(label='Stakeholder Meeting')
Authentication_Vote = Transition(label='Authentication Vote')

# Legal clearance branch
Legal_Review = Transition(label='Legal Review')
Acquisition_Approval = Transition(label='Acquisition Approval')

# Final steps
Documentation = Transition(label='Documentation')
Storage_Planning = Transition(label='Storage Planning')
Public_Disclosure = Transition(label='Public Disclosure')

# Silent transition for conditions (like consensus yes/no)
skip = SilentTransition()

# Build provenance verification partial order:
# Provenance_Check --> Historical_Research --> Cultural_Assessment
provenance_PO = StrictPartialOrder(nodes=[Provenance_Check, Historical_Research, Cultural_Assessment])
provenance_PO.order.add_edge(Provenance_Check, Historical_Research)
provenance_PO.order.add_edge(Historical_Research, Cultural_Assessment)

# Build scientific analysis partial order:
# Material_Sampling --> {Spectral_Analysis, Digital_Imaging} concurrent
# Then both --> Condition_Report --> Risk_Evaluation
scientific_PO = StrictPartialOrder(
    nodes=[
        Material_Sampling,
        Spectral_Analysis,
        Digital_Imaging,
        Condition_Report,
        Risk_Evaluation
    ]
)
scientific_PO.order.add_edge(Material_Sampling, Spectral_Analysis)
scientific_PO.order.add_edge(Material_Sampling, Digital_Imaging)
scientific_PO.order.add_edge(Spectral_Analysis, Condition_Report)
scientific_PO.order.add_edge(Digital_Imaging, Condition_Report)
scientific_PO.order.add_edge(Condition_Report, Risk_Evaluation)

# Expert consultation partial order:
# Expert_Panel --> Stakeholder_Meeting --> Authentication_Vote
expert_PO = StrictPartialOrder(nodes=[Expert_Panel, Stakeholder_Meeting, Authentication_Vote])
expert_PO.order.add_edge(Expert_Panel, Stakeholder_Meeting)
expert_PO.order.add_edge(Stakeholder_Meeting, Authentication_Vote)

# Legal clearance partial order:
# Legal_Review --> Acquisition_Approval
legal_PO = StrictPartialOrder(nodes=[Legal_Review, Acquisition_Approval])
legal_PO.order.add_edge(Legal_Review, Acquisition_Approval)

# Approval vote decision modeled as a loop:
# loop = * (Authentication_Vote, Stakeholder_Meeting)
# Repeated rounds of Stakeholder Meeting and Authentication Vote until consensus (modeled as loop)
approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[Authentication_Vote, Stakeholder_Meeting])

# Combine Expert consultation with loop (replace linear expert_PO last two nodes with loop)
# So Expert_Panel --> approval_loop
expert_consultation = StrictPartialOrder(nodes=[Expert_Panel, approval_loop])
expert_consultation.order.add_edge(Expert_Panel, approval_loop)

# Finally, consensus from expert consultation AND legal approval before acquisition
# Both must finish before Acquisition_Approval
# Since Acquisition_Approval is in legal_PO, we will create a node that merges expert_consultation and legal_PO 
# Then after Acquisition_Approval, Documentation, Storage_Planning, Public_Disclosure sequentially.

# Merge expert_consultation and legal_PO concurrency
consensus_PO = StrictPartialOrder(nodes=[expert_consultation, legal_PO])
# no order edges, meaning concurrent execution of expert_consultation and legal_PO

# Acquisition_Approval depends on legal_PO (Legal_Review->Acquisition_Approval)
# We add a silent transition "Consensus_Reached" that depends on both expert_consultation finish and Acquisition_Approval
Consensus_Reached = SilentTransition()

consensus_merge_PO = StrictPartialOrder(nodes=[consensus_PO, Acquisition_Approval, Consensus_Reached])
# expert_consultation and legal_PO concurrent in consensus_PO
# Acquisition_Approval is in legal_PO so it is node there, but to express that consensus requires both expert_consultation done and Acquisition_Approval done,
# we add edges consensus_PO --> Consensus_Reached and Acquisition_Approval --> Consensus_Reached
consensus_merge_PO.order.add_edge(consensus_PO, Consensus_Reached)
consensus_merge_PO.order.add_edge(Acquisition_Approval, Consensus_Reached)

# After consensus, sequentially: Documentation --> Storage_Planning --> Public_Disclosure
final_PO = StrictPartialOrder(nodes=[Documentation, Storage_Planning, Public_Disclosure])
final_PO.order.add_edge(Documentation, Storage_Planning)
final_PO.order.add_edge(Storage_Planning, Public_Disclosure)

# Combine all parts in a final PO:
# Initial_Review --> provenance_PO & scientific_PO (concurrent)
# provenance_PO and scientific_PO must finish before expert_consultation and legal_PO start (concurrent)
# expert_consultation & legal_PO produce consensus_merge_PO
# consensus_merge_PO --> final_PO

# First combine provenance_PO and scientific_PO concurrency after Initial_Review
first_PO = StrictPartialOrder(nodes=[Initial_Review, provenance_PO, scientific_PO])
first_PO.order.add_edge(Initial_Review, provenance_PO)
first_PO.order.add_edge(Initial_Review, scientific_PO)

# Then expert_consultation and legal_PO concurrent after provenance_PO and scientific_PO finished
# So provenance_PO and scientific_PO --> expert_consultation and legal_PO

second_PO = StrictPartialOrder(nodes=[first_PO, expert_consultation, legal_PO])
second_PO.order.add_edge(first_PO, expert_consultation)
second_PO.order.add_edge(first_PO, legal_PO)

# But expert_consultation and legal_PO already included in consensus_PO (combined)
# We use consensus_merge_PO to model join of consensus with acquisition approval, so instead of legal_PO here, use consensus_merge_PO minus duplicated legal_PO nodes.

# To keep it consistent, replace expert_consultation & legal_PO with consensus_merge_PO in second_PO nodes
second_PO = StrictPartialOrder(nodes=[first_PO, consensus_merge_PO])
second_PO.order.add_edge(first_PO, consensus_merge_PO)

# Finally, consensus_merge_PO --> final_PO
root = StrictPartialOrder(nodes=[second_PO, final_PO])
root.order.add_edge(second_PO, final_PO)
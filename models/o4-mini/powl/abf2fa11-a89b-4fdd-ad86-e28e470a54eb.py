# Generated from: abf2fa11-a89b-4fdd-ad86-e28e470a54eb.json
# Description: This process involves verifying the authenticity of ancient artifacts through a series of interdisciplinary activities combining scientific analysis, provenance research, and expert validation. The workflow starts with artifact intake and initial physical assessment, followed by multi-modal imaging techniques to detect hidden markings and material composition. Next, chemical dating and isotopic analysis help establish temporal origins. Concurrently, archival research cross-references historical records to confirm provenance chains. Expert panels review combined findings and assess cultural significance. Digital replication and blockchain registration ensure traceability. Finally, the artifact is either certified authentic or flagged for further investigation, with detailed reports generated for stakeholders and regulatory compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
t_in = Transition(label='Artifact Intake')
t_pc = Transition(label='Physical Check')
t_img = Transition(label='Imaging Scan')
t_mat = Transition(label='Material Test')
t_cd = Transition(label='Chemical Dating')
t_iso = Transition(label='Isotopic Analysis')
t_ar = Transition(label='Archive Review')
t_pr = Transition(label='Provenance Check')
t_ep = Transition(label='Expert Panel')
t_ca = Transition(label='Cultural Assess')
t_dr = Transition(label='Digital Replica')
t_br = Transition(label='Blockchain Reg')
t_rd = Transition(label='Report Draft')
t_cr = Transition(label='Compliance Review')
t_fc = Transition(label='Final Certification')

# Define concurrent/partial‐order branches
imaging_branch = StrictPartialOrder(nodes=[t_img, t_mat])
# imaging_branch.order.add_edge(t_img, t_mat)  # if sequential, uncomment

chem_branch = StrictPartialOrder(nodes=[t_cd, t_iso])
# chem_branch.order.add_edge(t_cd, t_iso)  # if sequential, uncomment

archive_branch = StrictPartialOrder(nodes=[t_ar, t_pr])
archive_branch.order.add_edge(t_ar, t_pr)

# Define the flagged branch for further investigation
flag_branch = StrictPartialOrder(nodes=[t_rd, t_cr])
flag_branch.order.add_edge(t_rd, t_cr)

# Define exclusive choice between certification or flagging branch
final_choice = OperatorPOWL(operator=Operator.XOR, children=[t_fc, flag_branch])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    t_in, t_pc,
    imaging_branch, chem_branch, archive_branch,
    t_ep, t_ca, t_dr, t_br,
    final_choice
])

# Add control‐flow edges
root.order.add_edge(t_in, t_pc)
root.order.add_edge(t_pc, imaging_branch)
root.order.add_edge(t_pc, chem_branch)
root.order.add_edge(t_pc, archive_branch)

root.order.add_edge(imaging_branch, t_ep)
root.order.add_edge(chem_branch, t_ep)
root.order.add_edge(archive_branch, t_ep)

root.order.add_edge(t_ep, t_ca)
root.order.add_edge(t_ca, t_dr)
root.order.add_edge(t_dr, t_br)
root.order.add_edge(t_br, final_choice)
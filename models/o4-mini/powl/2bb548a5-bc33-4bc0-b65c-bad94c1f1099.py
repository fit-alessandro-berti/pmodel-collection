# Generated from: 2bb548a5-bc33-4bc0-b65c-bad94c1f1099.json
# Description: This process outlines the comprehensive workflow for authenticating rare historical artifacts prior to acquisition by a museum or collector. It involves multidisciplinary evaluation including provenance verification, scientific analysis, expert consultation, and legal clearance. The process begins with initial artifact intake, followed by detailed condition assessment and documentation. Next, provenance research is conducted through archival searches and ownership history tracing. Scientific analysis employs various techniques such as radiocarbon dating, spectroscopy, and material composition tests to confirm period authenticity. Parallel to these, expert appraisals are collected from historians, archaeologists, and cultural specialists to validate findings. Legal teams then perform due diligence to ensure no ownership disputes or export restrictions apply. The final phase includes consolidation of all findings into a comprehensive authentication report, review by senior curators, and decision-making regarding acquisition or rejection. This atypical process ensures rigorous validation to mitigate risks related to forgery, misattribution, and legal complications, preserving institutional integrity and cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
intake = Transition(label='Artifact Intake')
condition = Transition(label='Condition Check')
photo = Transition(label='Photo Documentation')

provenance_search = Transition(label='Provenance Search')
archive = Transition(label='Archive Review')
ownership = Transition(label='Ownership Trace')

radiocarbon = Transition(label='Radiocarbon Test')
spectroscopy = Transition(label='Spectroscopy Scan')
material = Transition(label='Material Analysis')

expert_consult = Transition(label='Expert Consult')
appraisal = Transition(label='Appraisal Collection')

legal_review = Transition(label='Legal Review')
export_check = Transition(label='Export Check')

report = Transition(label='Report Compilation')
curator = Transition(label='Curator Review')
decision = Transition(label='Final Decision')

# Sub‐workflow: provenance research → archive & ownership in parallel
prov_parallel = StrictPartialOrder(nodes=[archive, ownership])
prov_seq = StrictPartialOrder(nodes=[provenance_search, prov_parallel])
prov_seq.order.add_edge(provenance_search, prov_parallel)

# Sub‐workflow: scientific analyses in parallel
sci_parallel = StrictPartialOrder(nodes=[radiocarbon, spectroscopy, material])

# Sub‐workflow: expert appraisal sequence
expert_seq = StrictPartialOrder(nodes=[expert_consult, appraisal])
expert_seq.order.add_edge(expert_consult, appraisal)

# Sub‐workflow: legal due diligence sequence
legal_seq = StrictPartialOrder(nodes=[legal_review, export_check])
legal_seq.order.add_edge(legal_review, export_check)

# Sub‐workflow: final reporting and decision sequence
final_seq = StrictPartialOrder(nodes=[report, curator, decision])
final_seq.order.add_edge(report, curator)
final_seq.order.add_edge(curator, decision)

# Root workflow: stitch everything together
root = StrictPartialOrder(
    nodes=[
        intake,
        condition,
        photo,
        prov_seq,
        sci_parallel,
        expert_seq,
        legal_seq,
        final_seq
    ]
)

# Define the control‐flow order
root.order.add_edge(intake, condition)
root.order.add_edge(condition, photo)

# After documentation, run provenance, science and expert branches in parallel
root.order.add_edge(photo, prov_seq)
root.order.add_edge(photo, sci_parallel)
root.order.add_edge(photo, expert_seq)

# Once those finish, legal due diligence runs
root.order.add_edge(prov_seq, legal_seq)
root.order.add_edge(sci_parallel, legal_seq)
root.order.add_edge(expert_seq, legal_seq)

# Finally, reporting & decision
root.order.add_edge(legal_seq, final_seq)
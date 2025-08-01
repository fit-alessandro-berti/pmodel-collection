# Generated from: bd7f8495-2e3a-4edc-8a9e-dcb0de2bff48.json
# Description: This process involves the detailed verification and authentication of historical artifacts before acquisition or exhibition. It includes provenance research, scientific testing, expert consultations, and legal documentation to ensure artifact legitimacy and compliance with international heritage laws. The workflow begins with initial artifact intake and condition assessment, followed by advanced material analysis and carbon dating. Concurrently, provenance tracing is conducted through archival research and interviews with previous owners or custodians. After scientific validation, expert panels review findings to confirm authenticity. Legal teams then verify ownership rights and prepare acquisition contracts. Finally, the artifact undergoes conservation planning before being cataloged for display or storage. This atypical process requires coordination between historians, scientists, legal experts, and conservators to uphold ethical standards and cultural preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')

material_test = Transition(label='Material Test')
carbon_dating = Transition(label='Carbon Dating')

provenance_trace = Transition(label='Provenance Trace')
archive_research = Transition(label='Archive Research')
owner_interview = Transition(label='Owner Interview')

expert_review = Transition(label='Expert Review')

legal_verify = Transition(label='Legal Verify')
rights_review = Transition(label='Rights Review')
contract_draft = Transition(label='Contract Draft')
acquisition_approve = Transition(label='Acquisition Approve')

conservation_plan = Transition(label='Conservation Plan')
catalog_entry = Transition(label='Catalog Entry')
exhibit_prep = Transition(label='Exhibit Prep')

# Provenance Trace partial order: Provenance Trace -> {Archive Research, Owner Interview} concurrent
po_provenance = StrictPartialOrder(nodes=[provenance_trace, archive_research, owner_interview])
po_provenance.order.add_edge(provenance_trace, archive_research)
po_provenance.order.add_edge(provenance_trace, owner_interview)

# Scientific testing partial order: Material Test --> Carbon Dating
po_scientific = StrictPartialOrder(nodes=[material_test, carbon_dating])
po_scientific.order.add_edge(material_test, carbon_dating)

# Legal checks partial order: Legal Verify -> Rights Review -> Contract Draft -> Acquisition Approve
po_legal = StrictPartialOrder(
    nodes=[legal_verify, rights_review, contract_draft, acquisition_approve]
)
po_legal.order.add_edge(legal_verify, rights_review)
po_legal.order.add_edge(rights_review, contract_draft)
po_legal.order.add_edge(contract_draft, acquisition_approve)

# Scientific validation to expert review includes scientific tests and provenance trace concurrent, then expert review
po_validation = StrictPartialOrder(
    nodes=[po_scientific, po_provenance, expert_review]
)
po_validation.order.add_edge(po_scientific, expert_review)
po_validation.order.add_edge(po_provenance, expert_review)

# After expert review, legal team starts
po_after_expert = StrictPartialOrder(
    nodes=[expert_review, po_legal]
)
po_after_expert.order.add_edge(expert_review, po_legal)

# After legal, conservation plan then catalog for display/storage (catalog entry and exhibit prep concurrent)
po_catalog = StrictPartialOrder(
    nodes=[catalog_entry, exhibit_prep]
)  # concurrent

po_conservation_and_catalog = StrictPartialOrder(
    nodes=[conservation_plan, po_catalog]
)
po_conservation_and_catalog.order.add_edge(conservation_plan, po_catalog)

# Main process partial order building:
# Start: Artifact Intake --> Condition Check
# Then converge to scientific validation and provenance tracing concurrently (done above)
# Then expert review --> legal checks --> conservation plan --> catalog/exhibit prep
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        condition_check,
        po_validation,
        po_after_expert,
        po_conservation_and_catalog,
    ]
)

# Order edges:
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, po_validation)
root.order.add_edge(po_validation, po_after_expert)
root.order.add_edge(po_after_expert, po_conservation_and_catalog)
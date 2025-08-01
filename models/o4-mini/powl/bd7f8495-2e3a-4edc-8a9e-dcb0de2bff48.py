# Generated from: bd7f8495-2e3a-4edc-8a9e-dcb0de2bff48.json
# Description: This process involves the detailed verification and authentication of historical artifacts before acquisition or exhibition. It includes provenance research, scientific testing, expert consultations, and legal documentation to ensure artifact legitimacy and compliance with international heritage laws. The workflow begins with initial artifact intake and condition assessment, followed by advanced material analysis and carbon dating. Concurrently, provenance tracing is conducted through archival research and interviews with previous owners or custodians. After scientific validation, expert panels review findings to confirm authenticity. Legal teams then verify ownership rights and prepare acquisition contracts. Finally, the artifact undergoes conservation planning before being cataloged for display or storage. This atypical process requires coordination between historians, scientists, legal experts, and conservators to uphold ethical standards and cultural preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_intake     = Transition(label="Artifact Intake")
t_cond       = Transition(label="Condition Check")
t_mat        = Transition(label="Material Test")
t_carbon     = Transition(label="Carbon Dating")
t_archive    = Transition(label="Archive Research")
t_owner      = Transition(label="Owner Interview")
t_prov       = Transition(label="Provenance Trace")
t_expert     = Transition(label="Expert Review")
t_legal      = Transition(label="Legal Verify")
t_rights     = Transition(label="Rights Review")
t_contract   = Transition(label="Contract Draft")
t_approve    = Transition(label="Acquisition Approve")
t_conserve   = Transition(label="Conservation Plan")
t_catalog    = Transition(label="Catalog Entry")
t_exhibit    = Transition(label="Exhibit Prep")
skip         = SilentTransition()

# Model the choice: either Exhibit Prep or skip (storage path)
exhibit_choice = OperatorPOWL(operator=Operator.XOR, children=[t_exhibit, skip])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    t_intake, t_cond,
    t_mat, t_carbon,
    t_archive, t_owner, t_prov,
    t_expert,
    t_legal, t_rights, t_contract, t_approve,
    t_conserve,
    exhibit_choice, t_catalog
])

# 1) Intake → Condition Check
root.order.add_edge(t_intake, t_cond)

# 2) After Condition Check: scientific branch and provenance branch start
root.order.add_edge(t_cond, t_mat)
root.order.add_edge(t_cond, t_archive)
root.order.add_edge(t_cond, t_owner)

# 3) Scientific branch: Material Test → Carbon Dating
root.order.add_edge(t_mat, t_carbon)

# 4) Provenance branch: Archive Research & Owner Interview → Provenance Trace
root.order.add_edge(t_archive, t_prov)
root.order.add_edge(t_owner, t_prov)

# 5) Synchronize scientific & provenance → Expert Review
root.order.add_edge(t_carbon, t_expert)
root.order.add_edge(t_prov, t_expert)

# 6) Expert Review → Legal verification sequence
root.order.add_edge(t_expert, t_legal)
root.order.add_edge(t_legal, t_rights)
root.order.add_edge(t_rights, t_contract)
root.order.add_edge(t_contract, t_approve)

# 7) Approval → Conservation Plan
root.order.add_edge(t_approve, t_conserve)

# 8) Conservation Plan → choice (Exhibit Prep or skip) → Catalog Entry
root.order.add_edge(t_conserve, exhibit_choice)
root.order.add_edge(exhibit_choice, t_catalog)
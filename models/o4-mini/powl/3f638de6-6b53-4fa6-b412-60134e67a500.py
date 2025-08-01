# Generated from: 3f638de6-6b53-4fa6-b412-60134e67a500.json
# Description: This process outlines the detailed verification and authentication workflow for rare historical artifacts submitted to a museum. It involves initial intake and documentation, provenance research, scientific testing including isotopic and material analysis, expert consultation across multiple disciplines, condition reporting, legal compliance checks related to cultural property laws, digital cataloging with high-resolution imaging, temporary exhibition preparation, insurance valuation, and final certification issuance. The process ensures that each artifact is thoroughly vetted for authenticity, legal ownership, and preservation standards before public display or acquisition, maintaining institutional integrity and cultural heritage protection.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
intake        = Transition(label="Intake Review")
prov          = Transition(label="Provenance Check")
mat           = Transition(label="Material Analysis")
iso           = Transition(label="Isotope Testing")
ex_consult    = Transition(label="Expert Consult")
cond          = Transition(label="Condition Report")
legal         = Transition(label="Legal Review")
imaging       = Transition(label="Digital Imaging")
catalog       = Transition(label="Catalog Entry")
insure        = Transition(label="Insurance Valuation")
cert          = Transition(label="Certification")
final_app     = Transition(label="Final Approval")
ex_prep       = Transition(label="Exhibit Prep")
storage       = Transition(label="Storage Allocation")
public_disc   = Transition(label="Public Disclosure")

# Branch for public exhibition: Exhibit Prep -> Public Disclosure
branch_exhibit = StrictPartialOrder(nodes=[ex_prep, public_disc])
branch_exhibit.order.add_edge(ex_prep, public_disc)

# XOR choice: either prepare for exhibit OR allocate to storage
choice_post = OperatorPOWL(
    operator=Operator.XOR,
    children=[branch_exhibit, storage]
)

# Build the main partial order
root = StrictPartialOrder(
    nodes=[
        intake, prov,
        mat, iso, ex_consult,
        cond, legal,
        imaging, catalog,
        insure, cert, final_app,
        choice_post
    ]
)

# Define the flows / partial orders
root.order.add_edge(intake, prov)

# Provenance Check → parallel testing
root.order.add_edge(prov, mat)
root.order.add_edge(prov, iso)

# Join tests → expert consult
root.order.add_edge(mat, ex_consult)
root.order.add_edge(iso, ex_consult)

# Consultation → condition report → legal review
root.order.add_edge(ex_consult, cond)
root.order.add_edge(cond, legal)

# Legal review → parallel cataloging & imaging
root.order.add_edge(legal, imaging)
root.order.add_edge(legal, catalog)

# After both imaging & catalog, insurance valuation
root.order.add_edge(imaging, insure)
root.order.add_edge(catalog, insure)

# Insurance → certification → final approval
root.order.add_edge(insure, cert)
root.order.add_edge(cert, final_app)

# Final approval → choice between exhibit path or storage
root.order.add_edge(final_app, choice_post)
# Generated from: 3f638de6-6b53-4fa6-b412-60134e67a500.json
# Description: This process outlines the detailed verification and authentication workflow for rare historical artifacts submitted to a museum. It involves initial intake and documentation, provenance research, scientific testing including isotopic and material analysis, expert consultation across multiple disciplines, condition reporting, legal compliance checks related to cultural property laws, digital cataloging with high-resolution imaging, temporary exhibition preparation, insurance valuation, and final certification issuance. The process ensures that each artifact is thoroughly vetted for authenticity, legal ownership, and preservation standards before public display or acquisition, maintaining institutional integrity and cultural heritage protection.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Intake_Review = Transition(label='Intake Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Analysis = Transition(label='Material Analysis')
Isotope_Testing = Transition(label='Isotope Testing')
Expert_Consult = Transition(label='Expert Consult')
Condition_Report = Transition(label='Condition Report')
Legal_Review = Transition(label='Legal Review')
Digital_Imaging = Transition(label='Digital Imaging')
Catalog_Entry = Transition(label='Catalog Entry')
Exhibit_Prep = Transition(label='Exhibit Prep')
Insurance_Valuation = Transition(label='Insurance Valuation')
Certification = Transition(label='Certification')
Storage_Allocation = Transition(label='Storage Allocation')
Public_Disclosure = Transition(label='Public Disclosure')
Final_Approval = Transition(label='Final Approval')

# Scientific Testing partial order: Material Analysis and Isotope Testing in parallel
scientific_testing = StrictPartialOrder(
    nodes=[Material_Analysis, Isotope_Testing]
)
# No order edges between Material_Analysis and Isotope_Testing, so concurrent

# Expert Consultation after scientific testing
expert_block = StrictPartialOrder(
    nodes=[scientific_testing, Expert_Consult]
)
expert_block.order.add_edge(scientific_testing, Expert_Consult)

# Condition Report and Legal Review in parallel after Expert Consult
cond_legal = StrictPartialOrder(
    nodes=[Condition_Report, Legal_Review]
)
# no order dependencies, so concurrent

# Digital Imaging then Catalog Entry sequentially
digital_catalog = StrictPartialOrder(
    nodes=[Digital_Imaging, Catalog_Entry]
)
digital_catalog.order.add_edge(Digital_Imaging, Catalog_Entry)

# Exhibit Prep and Insurance Valuation in parallel after catalog
exhibit_insurance = StrictPartialOrder(
    nodes=[Exhibit_Prep, Insurance_Valuation]
)
# no order between them, so concurrent

# Certification after Exhibit Prep and Insurance Valuation
certification_block = StrictPartialOrder(
    nodes=[exhibit_insurance, Certification]
)
certification_block.order.add_edge(exhibit_insurance, Certification)

# Storage Allocation after Certification
# Public Disclosure & Final Approval after Storage Allocation, in parallel
post_cert = StrictPartialOrder(
    nodes=[Public_Disclosure, Final_Approval]
)
# no order between them, so concurrent

final_post = StrictPartialOrder(
    nodes=[Storage_Allocation, post_cert]
)
final_post.order.add_edge(Storage_Allocation, post_cert)

# Assemble the whole process flow partial order:
# Intake Review -> Provenance Check -> expert_block -> cond_legal -> digital_catalog -> certification_block -> final_post

# Start nodes
start_nodes = [Intake_Review, Provenance_Check, expert_block, cond_legal,
               digital_catalog, certification_block, final_post]

root = StrictPartialOrder(
    nodes=[
        Intake_Review,
        Provenance_Check,
        expert_block,
        cond_legal,
        digital_catalog,
        certification_block,
        final_post
    ]
)

# Add the edges for sequential dependencies between blocks
root.order.add_edge(Intake_Review, Provenance_Check)
root.order.add_edge(Provenance_Check, expert_block)
root.order.add_edge(expert_block, cond_legal)
root.order.add_edge(cond_legal, digital_catalog)
root.order.add_edge(digital_catalog, certification_block)
root.order.add_edge(certification_block, final_post)
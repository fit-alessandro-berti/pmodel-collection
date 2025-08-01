# Generated from: 15fb7753-c6cb-4882-82f5-ee00fd55b80d.json
# Description: This process outlines the detailed verification and authentication workflow for custom-made historical artifacts intended for museum acquisition. It involves multidisciplinary collaboration among historians, material scientists, forensic analysts, and legal advisors to ensure the artifact's origin, age, and ownership are accurately documented and verified. The steps include preliminary research, sample testing, chain-of-custody validation, provenance documentation, legal clearance, and final certification. The process ensures authenticity while adhering to international cultural property laws, minimizing risks of forgery and illicit trade. The workflow integrates both physical analysis and archival investigation, including interviews with previous owners and cross-referencing with historical databases, culminating in a comprehensive provenance report for museum curators and acquisition committees.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Initial_Research = Transition(label='Initial Research')
Sample_Testing = Transition(label='Sample Testing')
Material_Analysis = Transition(label='Material Analysis')
Forensic_Imaging = Transition(label='Forensic Imaging')
Historical_Check = Transition(label='Historical Check')
Ownership_Audit = Transition(label='Ownership Audit')
Chain_Validation = Transition(label='Chain Validation')
Legal_Review = Transition(label='Legal Review')
Interview_Owners = Transition(label='Interview Owners')
Database_Crossref = Transition(label='Database Crossref')
Condition_Report = Transition(label='Condition Report')
Forgery_Scan = Transition(label='Forgery Scan')
Provenance_Draft = Transition(label='Provenance Draft')
Compliance_Check = Transition(label='Compliance Check')
Final_Certification = Transition(label='Final Certification')
Report_Delivery = Transition(label='Report Delivery')

# Physical analysis partial order (Sample Testing must precede Material Analysis and Forensic Imaging)
physical_PO = StrictPartialOrder(nodes=[Sample_Testing, Material_Analysis, Forensic_Imaging])
physical_PO.order.add_edge(Sample_Testing, Material_Analysis)
physical_PO.order.add_edge(Sample_Testing, Forensic_Imaging)

# Archival investigation partial order (Historical Check, Ownership Audit, Interview Owners, Database Crossref)
# Historical Check precedes Interview Owners and Database Crossref
archival_PO = StrictPartialOrder(
    nodes=[Historical_Check, Ownership_Audit, Interview_Owners, Database_Crossref]
)
archival_PO.order.add_edge(Historical_Check, Interview_Owners)
archival_PO.order.add_edge(Historical_Check, Database_Crossref)
# Ownership Audit can happen concurrently here (no edges to others)

# Chain validation step after physical and archival investigations
chain_validation = Chain_Validation

# For legal clearance partial order: Legal Review and Compliance Check could be concurrent
legal_PO = StrictPartialOrder(nodes=[Legal_Review, Compliance_Check])
# no ordering between Legal Review and Compliance Check

# Verification partial order:
# After chain_validation, the following verification activities happen:
# Condition Report and Forgery Scan in parallel
# Then Provenance Draft which depends on these two
verification_PO = StrictPartialOrder(
    nodes=[Condition_Report, Forgery_Scan, Provenance_Draft]
)
verification_PO.order.add_edge(Condition_Report, Provenance_Draft)
verification_PO.order.add_edge(Forgery_Scan, Provenance_Draft)

# Compose physical_PO and archival_PO in parallel, both precede chain_validation
phy_arch_PO = StrictPartialOrder(
    nodes=[physical_PO, archival_PO, chain_validation]
)
phy_arch_PO.order.add_edge(physical_PO, chain_validation)
phy_arch_PO.order.add_edge(archival_PO, chain_validation)

# Verification after chain_validation
phy_arch_ver_PO = StrictPartialOrder(
    nodes=[phy_arch_PO, verification_PO]
)
phy_arch_ver_PO.order.add_edge(phy_arch_PO, verification_PO)

# Legal partial order after chain_validation (can be concurrent with verification)
# So legal_PO and verification_PO are concurrent, but both after chain_validation
legal_ver_PO = StrictPartialOrder(
    nodes=[chain_validation, legal_PO, verification_PO]
)
legal_ver_PO.order.add_edge(chain_validation, legal_PO)
legal_ver_PO.order.add_edge(chain_validation, verification_PO)

# Merge chain_validation's predecessors (physical_PO and archival_PO) into one PO with legal_PO and verification_PO:

# Actually better:
# Initial Research precedes physical_PO and archival_PO
# Then physical_PO and archival_PO in parallel
# Then chain_validation after both
# Then legal_PO and verification_PO in parallel after chain_validation
# Then Final Certification after legal_PO and verification_PO
# Then Report Delivery after Final Certification

# Build initial researcher node
initial = Initial_Research

# physical and archival investigations PO
investigation_PO = StrictPartialOrder(
    nodes=[physical_PO, archival_PO]
)
investigation_PO.order.add_edge(physical_PO, physical_PO) # no self edge, remove - was a mistake
investigation_PO.order.add_edge(physical_PO, archival_PO) # No order between physical/archival, remove

# actually physical_PO and archival_PO are parallel (no edges)
investigation_PO = StrictPartialOrder(
    nodes=[physical_PO, archival_PO]
)
# no edges = parallel

# After initial research, both physical and archival investigations start
start_PO = StrictPartialOrder(
    nodes=[initial, physical_PO, archival_PO]
)
start_PO.order.add_edge(initial, physical_PO)
start_PO.order.add_edge(initial, archival_PO)

# After physical and archival investigations, chain validation
after_invest_PO = StrictPartialOrder(
    nodes=[start_PO, chain_validation]
)
after_invest_PO.order.add_edge(start_PO, chain_validation)

# After chain validation, legal and verification in parallel
after_chain_PO = StrictPartialOrder(
    nodes=[after_invest_PO, legal_PO, verification_PO]
)
after_chain_PO.order.add_edge(after_invest_PO, legal_PO)
after_chain_PO.order.add_edge(after_invest_PO, verification_PO)

# Final certification after legal and verification
final_cert_PO = StrictPartialOrder(
    nodes=[after_chain_PO, Final_Certification]
)
final_cert_PO.order.add_edge(after_chain_PO, Final_Certification)

# Report delivery after final certification
root = StrictPartialOrder(
    nodes=[final_cert_PO, Report_Delivery]
)
root.order.add_edge(final_cert_PO, Report_Delivery)